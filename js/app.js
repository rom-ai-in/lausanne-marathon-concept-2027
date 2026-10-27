
const ANSWERS = {
  sac:{q:"Où déposer mon sac ?",a:`Il est possible de déposer des sacs de sport / habits personnels sur le site de l’arrivée de <strong>Bellerive-Plage</strong> (emplacement surveillé, accessible sur présentation du dossard). Autres options : casiers à la Piscine de Bellerive-Plage, ou vestiaires non-surveillés du complexe Auguste Piccard. Horaire tente sac : 08h00–17h00. <strong>Pas de transfert de sac du départ à l’arrivée</strong> (420 m entre les deux sites).`,src:"https://fr.lausanne-marathon.com/info-coureurs/sacs-coureurs-depot/"},
  semi:{q:"À quelle heure part le semi ?",a:`Départ du semi-marathon à <strong>08h40</strong> à la Place de Milan (édition 2026 ; à confirmer pour 2027). Départs par 9 blocs toutes les 4 minutes.`,src:"https://fr.lausanne-marathon.com/info-coureurs/departs-horaires/"},
  dossard:{q:"Où retirer mon dossard ?",a:`Distribution à la Salle de sport Auguste Piccard, Ch. de Bellerive 36, Lausanne, sur présentation du mail/SMS indiquant le n° de dossard. Horaires 2026 : ven. 15h–18h, sam. 11h–18h, dim. 07h–14h.`,src:"https://fr.lausanne-marathon.com/info-coureurs/retrait-des-dossards-sur-place-le-23-24-et-25-octobre/"},
  ravito:{q:"Quels ravitaillements sur le semi ?",a:`Semi 2026 : Km 0 Place de Milan (eau) · Km 5 Lutry (eau) · Km 11 Cully (eau, isotonique, fruits…) · Km 15 Lutry · Km 16 Paudex · Km 19 Musée Olympique · Km 21 arrivée Bellerive.`,src:"https://fr.lausanne-marathon.com/info-coureurs/ravitaillement/ravitaillements-semi-marathon/"},
  prix:{q:"Combien coûte le semi ?",a:`Finance d’inscription semi 2026 : <strong>CHF 63.–</strong> (médaille + t-shirt inclus, TVA incluse selon page Prix & Catégories). Tarifs 2027 à confirmer à l’ouverture des inscriptions.`,src:"https://fr.lausanne-marathon.com/inscription/prix-categories/"}
};
function showAnswer(key){
  const box=document.getElementById('ask-answer'); const item=ANSWERS[key]; if(!box||!item) return;
  box.classList.add('show');
  box.innerHTML=`<div class="tag">Réponse d’exemple (maquette)</div><strong>${item.q}</strong><p style="margin:8px 0">${item.a}</p><a href="${item.src}" target="_blank" rel="noopener">Source officielle →</a>`;
  const input=document.getElementById('ask-input'); if(input) input.value=item.q;
}
function askSubmit(e){
  e.preventDefault();
  const v=(document.getElementById('ask-input').value||'').toLowerCase();
  if(v.includes('sac')) return showAnswer('sac');
  if(v.includes('prix')||v.includes('coût')||v.includes('cout')||v.includes('CHF')||v.includes('combien')) return showAnswer('prix');
  if(v.includes('semi')||v.includes('heure')||v.includes('départ')||v.includes('depart')) return showAnswer('semi');
  if(v.includes('dossard')||v.includes('retrait')) return showAnswer('dossard');
  if(v.includes('ravit')||v.includes('ravito')) return showAnswer('ravito');
  const box=document.getElementById('ask-answer'); box.classList.add('show');
  box.innerHTML=`<div class="tag">Réponse d’exemple (maquette)</div><p>Dans la version réelle, l’assistant interrogerait uniquement les pages officielles et renverrait un extrait + lien source. Essayez une suggestion.</p>`;
}
function toggleMore(e){e.preventDefault(); document.getElementById('more-menu').classList.toggle('open');}
function tickCountdown(){
  const el=document.getElementById('cd'); if(!el) return;
  const target=new Date('2027-10-24T08:40:00+02:00').getTime();
  let d=Math.max(0,target-Date.now());
  const days=Math.floor(d/86400000); d-=days*86400000;
  const h=Math.floor(d/3600000); d-=h*3600000;
  const m=Math.floor(d/60000); d-=m*60000;
  const s=Math.floor(d/1000);
  const vals=[days,h,m,s];
  el.querySelectorAll('strong').forEach((n,i)=>n.textContent=String(vals[i]).padStart(2,'0'));
}
document.addEventListener('DOMContentLoaded',()=>{tickCountdown(); setInterval(tickCountdown,1000);});
