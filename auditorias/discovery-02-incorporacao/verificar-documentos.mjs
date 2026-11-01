import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
const root=path.resolve(process.argv[2]||'.');
const audit='auditorias/discovery-02-incorporacao/';
const sum=b=>crypto.createHash('sha256').update(b).digest('hex');
const blob=b=>crypto.createHash('sha1').update(Buffer.concat([Buffer.from('blob '+b.length+'\0'),b])).digest('hex');
async function safeTarget(relative){if(!validPath(relative))throw Error('PATH');let p=root;for(const part of relative.split('/')){p=path.join(p,part);const st=await fs.lstat(p);if(st.isSymbolicLink())throw Error('SYMLINK_ANCESTOR');}return p;}
const checks=[];
const check=(id,ok,detail)=>checks.push({id,status:ok?'PASS':'FAIL',detail});
const validPath=p=>typeof p==='string'&&!!p&&!p.includes('\\')&&!p.includes(':')&&!p.startsWith('/')&&!p.split('/').includes('..')&&!p.split('/').includes('.')&&!p.includes('//');
function inventory(entries){const seen=new Set();if(entries.some((e,i)=>i&&entries[i-1].path>e.path))throw Error('ORDER');for(const e of entries){if(!validPath(e.path))throw Error('PATH');const key=e.path.toLowerCase();if(seen.has(key))throw Error('DUPLICATE_OR_CASE_COLLISION');seen.add(key);if(e.mode!=='100644')throw Error('MODE');if(!Number.isInteger(e.bytes)||e.bytes<0||! /^[a-f0-9]{64}$/.test(e.sha256))throw Error('IDENTITY');}return true;}
const states=['PASS','FAIL','INCONCLUSIVO','BLOQUEADO','NOT_RUN'];
function aggregate(v){return ['FAIL','INCONCLUSIVO','BLOQUEADO','NOT_RUN'].find(s=>v.includes(s))||'PASS';}
function global(v){return {FAIL:'COM_FALHAS',INCONCLUSIVO:'EVIDENCIA_INSUFICIENTE',BLOQUEADO:'BLOQUEADO_PARCIAL',NOT_RUN:'PARCIAL_VERIFICADO',PASS:'INTEGRALMENTE_COMPROVADO'}[aggregate(v)];}
const baseline=JSON.parse(await fs.readFile(path.join(root,audit,'BASELINE-REMOTA.json')));
const allow=JSON.parse(await fs.readFile(path.join(root,'AUTORIA-ARQUIVOS.json')));
const allowPaths=Array.isArray(allow)?allow.map(x=>typeof x==='string'?x:x.path):allow.files.map(x=>typeof x==='string'?x:x.path);
const allowed=new Set(allowPaths);
let preserved=0;
for(const e of baseline.entries){if(!validPath(e.path))throw Error('BASELINE_PATH');const target=await safeTarget(e.path);const st=await fs.lstat(target);if(st.isSymbolicLink()||!st.isFile())throw Error('BASELINE_MODE');const b=await fs.readFile(target);if(!allowed.has(e.path)){check('protected:'+e.path,blob(b)===e.sha,{expected:e.sha,actual:blob(b)});preserved++;}}
check('baseline-authenticity',baseline.repository==='lazaruscarvalho-a11y/engenharia-agentica-plataforma-ide'&&baseline.commit==='e37af725a162c577cfa9ffde286d0fcf69294429',baseline.commit);
const freeze=JSON.parse(await fs.readFile(path.join(root,audit,'CANDIDATO-CONGELADO.json')));
try{inventory(freeze.files);check('freeze-paths-modes',true,freeze.files.length);}catch(e){check('freeze-paths-modes',false,e.message);throw Error('INVALID_FREEZE_ABORTED_BEFORE_PAYLOAD_READ:'+e.message);}
check('freeze-aggregate',sum(Buffer.from(JSON.stringify(freeze.files)))===freeze.freeze_digest,freeze.freeze_digest);
for(const e of freeze.files){const file=await safeTarget(e.path);const st=await fs.lstat(file);if(st.isSymbolicLink()||!st.isFile()){check('freeze:'+e.path,false,'SYMLINK_OR_NOT_FILE');continue;}const b=await fs.readFile(file);check('freeze:'+e.path,st.isFile()&&!st.isSymbolicLink()&&b.length===e.bytes&&sum(b)===e.sha256,e.sha256);}
const sample={path:'docs/a.md',mode:'100644',bytes:1,sha256:'a'.repeat(64)};
for(const [id,entries,expected]of [['escape',[{...sample,path:'../x'}],'PATH'],['absolute',[{...sample,path:'C:/x'}],'PATH'],['duplicate',[sample,sample],'DUPLICATE_OR_CASE_COLLISION'],['case',[{...sample,path:'DOCS/a.md'},sample],'DUPLICATE_OR_CASE_COLLISION'],['symlink',[{...sample,mode:'120000'}],'MODE'],['submodule',[{...sample,mode:'160000'}],'MODE'],['digest',[{...sample,sha256:'inventado'}],'IDENTITY']]){let got;try{inventory(entries);got='ACCEPTED';}catch(e){got=e.message;}check('negative:'+id,got===expected,{expected,observed:got});}
check('positive:inventory',inventory([sample]),'valid fixture');
let combinations=0;
for(const a of states)for(const b of states)for(const c of states)for(const d of states){const vector=[a,b,c,d];const expected=states.slice(1).find(s=>vector.includes(s))||'PASS';check('aggregate:'+ ++combinations,aggregate(vector)===expected,vector);}
const gateNames=['A','G','F','PS','PI','RG','RF','RN','Z'];
check('RN-required',global(gateNames.map(g=>g==='RN'?'NOT_RUN':'PASS'))==='PARCIAL_VERIFICADO','No simulated RN');
for(let i=0;i<gateNames.length;i++)for(const s of states){const v=gateNames.map((_,j)=>i===j?s:'PASS');const expected={PASS:'INTEGRALMENTE_COMPROVADO',FAIL:'COM_FALHAS',INCONCLUSIVO:'EVIDENCIA_INSUFICIENTE',BLOQUEADO:'BLOQUEADO_PARCIAL',NOT_RUN:'PARCIAL_VERIFICADO'}[s];check('global:'+gateNames[i]+':'+s,global(v)===expected,v);}
const pm=await fs.readFile(path.join(root,audit,'entradas/PROMPT-MASTER-DISCOVERY-02-R5.md'));
check('PM-identity',pm.length===75442&&sum(pm)==='ada7257fabb483c921ab3ead2eb6fe7db2d1ccb742502da28dfa9c33b7431da6',{bytes:pm.length,sha256:sum(pm)});
const ids=[...pm.toString().matchAll(/\*\*R4-(\d{3}) —/g)].map(m=>m[1]);
check('74-stable-clauses',ids.length===74&&new Set(ids).size===74,ids.length);
const slug=s=>s.replace(/<[^>]+>/g,'').replace(/\[([^\]]+)\]\([^)]+\)/g,'$1').replace(/[\x60*_~]/g,'').toLowerCase().replace(/[^\p{L}\p{N}_\-\s]/gu,'').trim().replace(/\s/g,'-');
function anchors(text){let seen=new Map(),a=new Set();for(const m of text.matchAll(/^#{1,6}\s+(.+)$/gm)){const base=slug(m[1]);const n=seen.get(base)||0;seen.set(base,n+1);a.add(base+(n?'-'+n:''));}for(const m of text.matchAll(/<(?:a|[^>]+)\s+(?:id|name)=["']([^"']+)["']/g))a.add(m[1]);return a;}
let links=0;
for(const file of allowPaths.filter(p=>/\.md$/i.test(p)&&!p.includes('/entradas/')&&!p.includes('/historico/'))){const text=(await fs.readFile(path.join(root,file),'utf8')).replace(/^\x60\x60\x60[^\n]*\n[\s\S]*?^\x60\x60\x60\s*$/gm,'');for(const m of text.matchAll(/\[[^\]]*\]\(([^)\n]+)\)/g)){let dest=m[1].replace(/^<|>$/g,'');if(/^[a-zA-Z][\w+.-]*:/.test(dest))continue;let [p,anchor]=dest.split('#');try{p=decodeURIComponent(p);if(anchor)anchor=decodeURIComponent(anchor);}catch{}const target=p?path.resolve(path.dirname(path.join(root,file)),p):path.join(root,file);if(!target.startsWith(root+path.sep)){check('link:'+file+'->'+dest,false,'ESCAPE');continue;}try{const t=await fs.readFile(target,'utf8');check('link:'+file+'->'+dest,!anchor||anchors(t).has(anchor),'file and heading/id');}catch(e){check('link:'+file+'->'+dest,false,e.code);}links++;}}
const result={schema_version:'d02-documentary-tests-1',scope:'DOCUMENTARY_STRUCTURE_AND_SYNTHETIC_GATE_CALCULATION_NOT_PRODUCT_TESTS',checks,summary:{total:checks.length,passed:checks.filter(c=>c.status==='PASS').length,failed:checks.filter(c=>c.status==='FAIL').length,protectedFiles:preserved,links,aggregateCombinations:combinations,semanticAudit:'SEPARATE_INDEPENDENT_AGENT',caOperacionais:'49 NOT_RUN'}};
await fs.writeFile(path.join(root,audit,'TESTES-DOCUMENTAIS.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({...result.summary,failures:checks.filter(c=>c.status==='FAIL')},null,2));
process.exitCode=result.summary.failed?1:0;
