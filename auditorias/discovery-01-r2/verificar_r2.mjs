import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
const root=path.resolve(process.argv[2]||'.');
const read=p=>fs.readFileSync(path.join(root,p),'utf8');
const audit='auditorias/discovery-01-r2/';
const reg=read('docs/01-discovery/discovery-01/REGISTRO.md');
const dossier=read(audit+'DOSSIE-REPRODUZIDO.md');
const index=JSON.parse(read(audit+'COBERTURA.json'));
const sourceAnchors=[...dossier.matchAll(/^### (E\d{2}) —/gm)].map(m=>m[1]);
const base=index.entries;
const ids=new Set([...reg.matchAll(/D01-(?:DEC|REL|PROP|HIP|INT|RST|CTX|NEC)-\d{3}/g)].map(m=>m[0]));
const checks=[];
function check(name,fn){fn();checks.push({name,pass:true});}
check('36 source anchors, unique and ordered',()=>assert.deepEqual(sourceAnchors,Array.from({length:36},(_,i)=>'E'+String(i+1).padStart(2,'0'))));
check('coverage exact to independently archived source headings',()=>assert.deepEqual(base.map(e=>e.anchor),sourceAnchors));
check('canonical IDs, explicit anchors and source references resolve',()=>{for(const e of base){assert(ids.has(e.id),e.id);assert(reg.includes('id="'+e.artifactAnchor+'"'),e.artifactAnchor);assert(reg.includes(e.source),e.source);assert(e.elements.length>0);}});
check('E12 does not fabricate unavailable antecedent',()=>{const e=base.find(x=>x.anchor==='E12');assert.equal(e.question,null);assert.equal(e.response,null);assert(!reg.includes('Incorporação majoritariamente automática ou revisão humana obrigatória por contribuição?'));});
check('inverse pending scope preserves review commitments',()=>{for(const e of base)assert(e.pending.includes('D01-PEN-001'));for(const a of ['E05','E23','E26','E30','E31','E32','E33','E34','E35'])assert(base.find(e=>e.anchor===a).pending.includes('D01-PEN-010'));for(const a of ['E13','E32','E33','E34'])assert(base.find(e=>e.anchor===a).pending.includes('D01-PEN-005'));});
check('all historical IDs retained',()=>{for(const [k,n]of [['DEC',4],['REL',9],['PROP',11],['HIP',3]])for(let i=1;i<=n;i++)assert(ids.has('D01-'+k+'-'+String(i).padStart(3,'0')));});
check('P-A..P-L retained in canonical proposal inventory',()=>{for(const x of 'ABCDEFGHIJKL')assert(reg.includes('P-'+x));});
const proposed=[...reg.matchAll(/D01-PROP-\d{3}|D01-HIP-\d{3}/g)].map(m=>m[0]);
const questions=base.filter(x=>x.response).map(x=>({anchor:x.anchor,questionAnchor:x.anchor,response:x.response}));
const fixture={
coverage:base.map(x=>({anchor:x.anchor,id:x.id})),
questions,
proposals:[...new Set(proposed)].map(id=>({id,state:'PROPOSTA_OU_HIPOTESE'})),
permissions:{consultationImpliesWrite:false,migrationImpliesDeletion:false,localRunByAgent:false},
versions:{mainImpliesProd:false,submoduleImpliesSynced:false},
external:{accessibleImpliesShareable:false},
corporate:{reportedImpliesPolicy:false},
migration:{nonCriticalPendingVisible:true},
evidence:{claimHasSource:true,sourceKind:'REPRODUZIDA'},
resume:{revision:2,base:index.base_commit,entry:'docs/01-discovery/discovery-02/RETOMADA.md'}
};
// These are documentary invariants derived from the dossier, not an IDE authorization engine.
function errors(s){
 const out=[];
 if(JSON.stringify(s.coverage)!==JSON.stringify(fixture.coverage))out.push('ANCHOR_OR_CANONICAL_OMISSION');
 if(JSON.stringify(s.questions)!==JSON.stringify(questions))out.push('SHORT_ANSWER_CONTEXT');
 if(s.proposals.some(p=>p.state!=='PROPOSTA_OU_HIPOTESE'))out.push('PROPOSAL_PROMOTION');
 if(s.permissions.consultationImpliesWrite)out.push('READ_NOT_WRITE');
 if(s.permissions.migrationImpliesDeletion)out.push('MIGRATION_NOT_DELETE');
 if(s.permissions.localRunByAgent)out.push('ENGINEER_LOCAL_RUN');
 if(s.versions.mainImpliesProd)out.push('MAIN_NOT_DEPLOYMENT');
 if(s.versions.submoduleImpliesSynced)out.push('SUBMODULE_NOT_SYNC');
 if(s.external.accessibleImpliesShareable)out.push('ACCESS_NOT_REDISTRIBUTION');
 if(s.corporate.reportedImpliesPolicy)out.push('REPORT_NOT_POLICY');
 if(!s.migration.nonCriticalPendingVisible)out.push('PENDING_NOT_HIDDEN');
 if(!s.evidence.claimHasSource||s.evidence.sourceKind==='DIRECT_ORIGINAL_FABRICATED')out.push('SOURCE_REQUIRED');
 if(JSON.stringify(s.resume)!==JSON.stringify(fixture.resume))out.push('RESUME_REVISION');
 return out;
}
check('positive documentary fixture admitted',()=>assert.deepEqual(errors(fixture),[]));
const cases=[
 ['N01','E34','Human determination omitted',s=>s.coverage.splice(33,1),'ANCHOR_OR_CANONICAL_OMISSION'],
 ['N02','E10/E22','Short answer attached to another question',s=>{const q=s.questions.find(x=>x.anchor==='E10');q.questionAnchor='E22';},'SHORT_ANSWER_CONTEXT'],
 ['N03','P-G','Proposal promoted to approved decision',s=>s.proposals[0].state='DECISAO_APROVADA','PROPOSAL_PROMOTION'],
 ['N04','E23/E31','Consultation authorization treated as writing',s=>s.permissions.consultationImpliesWrite=true,'READ_NOT_WRITE'],
 ['N05','E27','Migration approval used to delete originals',s=>s.permissions.migrationImpliesDeletion=true,'MIGRATION_NOT_DELETE'],
 ['N06','E17','Main treated as deployed PROD',s=>s.versions.mainImpliesProd=true,'MAIN_NOT_DEPLOYMENT'],
 ['N07','E09/E10','Submodule reference treated as synchronized',s=>s.versions.submoduleImpliesSynced=true,'SUBMODULE_NOT_SYNC'],
 ['N08','E22','Accessible external source treated as shareable',s=>s.external.accessibleImpliesShareable=true,'ACCESS_NOT_REDISTRIBUTION'],
 ['N09','E15/E16','Corporate report promoted to institutional policy',s=>s.corporate.reportedImpliesPolicy=true,'REPORT_NOT_POLICY'],
 ['N10','E32/E34','Noncritical pending hidden after completion',s=>s.migration.nonCriticalPendingVisible=false,'PENDING_NOT_HIDDEN'],
 ['N11','all','Unattributed claim presented as proven fact',s=>{s.evidence.claimHasSource=false;s.evidence.sourceKind='DIRECT_ORIGINAL_FABRICATED';},'SOURCE_REQUIRED'],
 ['N12','E36','D02 points to incompatible revision/base/path',s=>{s.resume.revision=1;s.resume.base='main';s.resume.entry='missing.md';},'RESUME_REVISION'],
 ['N13','E03','Documented startup treated as agent permission',s=>s.permissions.localRunByAgent=true,'ENGINEER_LOCAL_RUN']
];
const negative=[];
for(const[id,source,scenario,mutate,expected]of cases){
 const s=structuredClone(fixture);mutate(s);const found=errors(s);
 assert(found.includes(expected),id+': mutation escaped');
 negative.push({id,source,scenario,expected,observed:found,result:'REJECTED_AS_EXPECTED'});
}
const output={schema_version:'d01-r2-document-checks-1',kind:'DOCUMENTARY_ONLY',checks,negative,
 limits:['Synthetic structured documentary counterexamples; not a general natural-language semantic verifier.','Semantic coverage requires independent source-to-document audit.','No application or IDE functionality executed; PGC operational CA not run.']};
if(process.argv.includes('--write'))fs.writeFileSync(path.join(root,audit+'TESTES-DOCUMENTAIS.json'),JSON.stringify(output,null,2)+'\n');
console.log(JSON.stringify({checks:checks.length,negative:negative.length,allPassed:true}));
