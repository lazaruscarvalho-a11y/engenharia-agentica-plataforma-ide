import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
const root=path.resolve(process.argv[2]||'.');
const manifestPath='docs/01-discovery/discovery-01/MANIFESTO.json';
const manifest=JSON.parse(fs.readFileSync(path.join(root,manifestPath),'utf8'));
assert.equal(manifest.revision,2,'This checker applies to R2 only');
const base=manifest.inherited_index||[];
const known=new Set([...base.map(x=>x.path),...manifest.files.map(x=>x.path),manifestPath,...manifest.later_evidence_paths]);
const slug=s=>s.toLowerCase().replace(/<[^>]+>/g,'').replace(/[^\p{L}\p{N}_\-\s]/gu,'').replace(/\s/g,'-');
const broken=[],anchors=[],hashes=[];
let links=0;
for(const f of manifest.files){
 const bytes=fs.readFileSync(path.join(root,f.path));
 hashes.push({path:f.path,pass:bytes.length===f.bytes&&crypto.createHash('sha256').update(bytes).digest('hex')===f.sha256});
 if(!f.path.endsWith('.md'))continue;
 const text=bytes.toString('utf8');assert(!text.includes('\r')&&!text.includes('\uFFFD'),f.path+' UTF8/LF');
 for(const m of text.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)){
  const url=m[1];if(/^[a-z][a-z0-9+.-]*:/i.test(url)||url.startsWith('#'))continue;
  links++;
  const [raw,fragment]=url.split('#');
  const target=path.posix.normalize(path.posix.join(path.posix.dirname(f.path),decodeURIComponent(raw)));
  if(!known.has(target)){broken.push({source:f.path,target});continue;}
  if(fragment&&fs.existsSync(path.join(root,target))){
   const content=fs.readFileSync(path.join(root,target),'utf8');
   const ids=new Set([...content.matchAll(/<a id="([^"]+)"/g)].map(x=>x[1]));
   for(const h of content.matchAll(/^#{1,6} (.+)$/gm))ids.add(slug(h[1]));
   if(!ids.has(decodeURIComponent(fragment)))anchors.push({source:f.path,target,fragment});
  }
 }
}
assert(hashes.every(x=>x.pass),'File hash mismatch');
assert.deepEqual(broken,[],'Broken local path');
assert.deepEqual(anchors,[],'Broken local anchor');
const out={kind:'DOCUMENTARY_INTEGRITY_ONLY',files:hashes.length,hashes,local_links:links,broken_paths:broken,broken_anchors:anchors,pass:true,limits:['Links to explicitly declared later evidence files are planned until their separate commit is read back.','No remote URL reachability or corporate authorization inferred.']};
if(process.argv.includes('--write'))fs.writeFileSync(path.join(root,'auditorias/discovery-01-r2/INTEGRIDADE-LOCAL.json'),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({files:hashes.length,links,anchors:anchors.length,pass:true}));
