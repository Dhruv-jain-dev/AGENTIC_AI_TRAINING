const reports = window.REPORTS || [];
const $ = s => document.querySelector(s);
const cleanTitle = t => t.replace(/^Day\s*\d+\s*[–—-]\s*/i, '');
const getOverview = md => (md.match(/## Overview\s+([\s\S]*?)(?=\n##|\n---)/i)?.[1] || '').trim().replace(/\*\*/g,'').replace(/`/g,'');
const getTags = md => [...md.matchAll(/^### \d+\.\s+(.+)$/gm)].map(m=>m[1].replace(/\*\*|`/g,'')).slice(0,3);
const inline = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>').replace(/`(.+?)`/g,'<code>$1</code>');
function markdown(md){
  const lines=md.split('\n'); let html='',list=false,table=false;
  const end=()=>{if(list){html+='</ul>';list=false}if(table){html+='</tbody></table>';table=false}};
  lines.forEach((line,i)=>{if(/^\|/.test(line)){if(/^\|[\s|:-]+\|?$/.test(line))return;if(!table){end();html+='<table><tbody>';table=true}html+='<tr>'+line.split('|').slice(1,-1).map((c,j)=>`${i&&j===0?'<td>':'<td>'}${inline(c.trim())}</td>`).join('')+'</tr>';return}else if(table){html+='</tbody></table>';table=false}
    let m;if(m=line.match(/^(#{1,3})\s+(.+)/)){end();let n=m[1].length;html+=`<h${n}>${inline(m[2])}</h${n}>`}else if(/^[-*] /.test(line.trim())){if(!list){html+='<ul>';list=true}html+=`<li>${inline(line.trim().slice(2))}</li>`}else if(/^---+$/.test(line.trim())){end();html+='<hr>'}else if(line.trim()){if(list){html+='</ul>';list=false}html+=`<p>${inline(line)}</p>`}});end();return html;
}
function render(filter=''){
  const q=filter.toLowerCase(); const shown=reports.filter(r=>(r.title+' '+r.markdown).toLowerCase().includes(q));
  $('#report-list').innerHTML=shown.map(r=>`<article class="report-card" data-day="${r.day}" tabindex="0"><span class="day-number">DAY ${String(r.day).padStart(2,'0')}</span><div><h3>${cleanTitle(r.title)}</h3><p>${getOverview(r.markdown).slice(0,210)}${getOverview(r.markdown).length>210?'…':''}</p><div class="tags">${getTags(r.markdown).map(t=>`<span class="tag">${t}</span>`).join('')}</div></div><div class="card-meta">${r.date}<span class="arrow">↗</span></div></article>`).join('');
  $('#empty').hidden=shown.length>0;
  document.querySelectorAll('.report-card').forEach(c=>{const open=()=>showReport(+c.dataset.day);c.onclick=open;c.onkeydown=e=>{if(e.key==='Enter')open()}});
}
function showReport(day){const r=reports.find(x=>x.day===day);if(!r)return;$('#reader-content').innerHTML=markdown(r.markdown)+`<p><a class="button primary" target="_blank" href="https://github.com/Dhruv-jain-dev/AGENTIC_AI_TRAINING/tree/main/DAY-${day}">View files on GitHub ↗</a></p>`;$('#reader').showModal();}
$('#timeline').innerHTML=reports.map(r=>`<button class="timeline-btn" data-day="${r.day}">Day ${String(r.day).padStart(2,'0')} · ${r.date.split(' ')[0]}</button>`).join('');
document.querySelectorAll('.timeline-btn').forEach(b=>b.onclick=()=>showReport(+b.dataset.day));
$('#search').oninput=e=>render(e.target.value);$('.close').onclick=()=>$('#reader').close();$('#reader').onclick=e=>{if(e.target===$('#reader'))$('#reader').close()};
$('#day-count').textContent=String(reports.length).padStart(2,'0');render();
