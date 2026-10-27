(function(){
  const el=document.getElementById('route-map');
  if(!el || typeof L==='undefined') return;
  const map=L.map(el,{scrollWheelZoom:false});
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom:19
  }).addTo(map);
  let layer=null, markers=[];
  const colors={semi:'#1657d9',marathon:'#ff5a1f',dix:'#0f9d58'};
  const labelEl=document.getElementById('map-course-label');
  const noteEl=document.getElementById('map-note');
  const elevEl=document.getElementById('elev-svg');
  const aidEl=document.getElementById('aid-list');
  const metaDist=document.getElementById('meta-dist');
  const metaDeniv=document.getElementById('meta-deniv');
  const metaStart=document.getElementById('meta-start');

  function drawProfile(profile, color){
    if(!elevEl||!profile?.length) return;
    const w=320,h=70,pad=4;
    const ds=profile.map(p=>p.d), es=profile.map(p=>p.e);
    const minE=Math.min(...es), maxE=Math.max(...es);
    const minD=Math.min(...ds), maxD=Math.max(...ds)||1;
    const pts=profile.map(p=>{
      const x=pad+(p.d-minD)/(maxD-minD)*(w-pad*2);
      const y=h-pad-(p.e-minE)/Math.max(1,maxE-minE)*(h-pad*2);
      return `${x.toFixed(1)},${y.toFixed(1)}`;
    }).join(' ');
    elevEl.innerHTML=`<polyline fill="none" stroke="${color}" stroke-width="2.5" points="${pts}"/><polyline fill="${color}33" stroke="none" points="${pad},${h-pad} ${pts} ${w-pad},${h-pad}"/>`;
  }

  function load(key){
    fetch('../data/routes.json').then(r=>r.json()).then(data=>{
      const c=data.courses[key]; if(!c) return;
      if(layer) map.removeLayer(layer);
      markers.forEach(m=>map.removeLayer(m)); markers=[];
      layer=L.geoJSON(c.geojson,{style:{color:colors[key]||'#1657d9',weight:5,opacity:.92}}).addTo(map);
      map.fitBounds(layer.getBounds(),{padding:[30,30]});
      const start=L.circleMarker([c.start.lat,c.start.lon],{radius:8,color:'#fff',weight:2,fillColor:'#0f9d58',fillOpacity:1}).bindPopup(c.start.name).addTo(map);
      const finish=L.circleMarker([c.finish.lat,c.finish.lon],{radius:8,color:'#fff',weight:2,fillColor:'#ff5a1f',fillOpacity:1}).bindPopup(c.finish.name).addTo(map);
      markers.push(start,finish);
      (c.aid||[]).forEach(a=>{
        const m=L.circleMarker([a.lat,a.lon],{radius:5,color:'#fff',weight:1.5,fillColor:'#1aa7ff',fillOpacity:1}).bindPopup(`<strong>Km ${a.km} · ${a.name}</strong><br>${a.offer}`).addTo(map);
        markers.push(m);
      });
      if(labelEl) labelEl.textContent=c.name;
      if(noteEl) noteEl.textContent=data.note;
      if(metaDist) metaDist.textContent=String(c.official_km).replace('.',',')+' km';
      if(metaDeniv && c.official_deniv) metaDeniv.textContent=`${c.official_deniv.dplus} / ${c.official_deniv.dminus} m`;
      if(metaStart) metaStart.textContent=window.LM_STARTS?.[key]||'—';
      drawProfile(c.profile, colors[key]||'#1657d9');
      if(aidEl){
        aidEl.innerHTML=(c.aid||[]).map(a=>`<div class="aid"><div class="km">Km ${a.km}</div><div><strong>${a.name}</strong><div style="color:var(--muted);font-size:13px">${a.offer}</div></div></div>`).join('');
      }
    }).catch(console.error);
  }
  document.querySelectorAll('[data-course]').forEach(btn=>{
    btn.addEventListener('click',()=>{
      document.querySelectorAll('[data-course]').forEach(b=>b.classList.remove('active'));
      btn.classList.add('active');
      load(btn.dataset.course);
    });
  });
  const initial=document.querySelector('[data-course].active')?.dataset.course||'semi';
  load(initial);
})();
