(function(){
  const el=document.getElementById('route-map');
  if(!el || typeof L==='undefined') return;
  const map=L.map(el,{scrollWheelZoom:false, tap:true, zoomControl:true, zoomSnap:0.25, zoomDelta:0.5});
  window.LM_MAP=map;
  // Lake Geneva / Lausanne default so first paint is never Epalinges hinterland
  map.setView([46.505, 6.66], 12);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom:19
  }).addTo(map);
  function fitRoute(bounds){
    if(!bounds || !bounds.isValid()) return;
    const doFit=()=>{
      map.invalidateSize({animate:false});
      const size=map.getSize();
      if(size.x < 40 || size.y < 40) return;
      const hPad = Math.max(36, Math.round(size.x * 0.12));
      const vPad = Math.max(28, Math.round(size.y * 0.10));
      map.fitBounds(bounds, {
        paddingTopLeft: L.point(hPad, vPad),
        paddingBottomRight: L.point(hPad, vPad),
        maxZoom: size.x < 720 ? 12 : 13,
        animate: false
      });
    };
    doFit();
    requestAnimationFrame(()=>requestAnimationFrame(doFit));
    setTimeout(doFit, 200);
    setTimeout(doFit, 550);
  }
  let layer=null, markers=[], cursor=null, latlngs=[], profile=[], currentKey='semi';
  map.whenReady(()=>map.invalidateSize({animate:false}));
  window.addEventListener('resize', ()=>{
    if(layer) fitRoute(layer.getBounds());
  });
  if (window.ResizeObserver){
    new ResizeObserver(()=>{ if(layer) fitRoute(layer.getBounds()); }).observe(el);
  }
  const colors={semi:'#1657d9',marathon:'#ff5a1f',dix:'#0f9d58'};
  const labelEl=document.getElementById('map-course-label');
  const noteEl=document.getElementById('map-note');
  const elevEl=document.getElementById('elev-svg');
  const elevTip=document.getElementById('elev-tip');
  const elevKm=document.getElementById('elev-km');
  const elevAlt=document.getElementById('elev-alt');
  const aidEl=document.getElementById('aid-list');
  const metaDist=document.getElementById('meta-dist');
  const metaDeniv=document.getElementById('meta-deniv');
  const metaStart=document.getElementById('meta-start');
  const gpxLink=document.getElementById('gpx-link');
  let waypoints={};

  fetch('../data/waypoints.json').then(r=>r.json()).then(w=>{waypoints=w}).catch(()=>{});

  function distToIndex(d){
    if(!profile.length) return 0;
    let best=0, bd=1e9;
    for(let i=0;i<profile.length;i++){
      const dd=Math.abs(profile[i].d-d);
      if(dd<bd){bd=dd;best=i}
    }
    return best;
  }
  function setCursorAt(i){
    if(!latlngs.length) return;
    const idx=Math.max(0,Math.min(latlngs.length-1, Math.round(i/(Math.max(1,profile.length-1))*(latlngs.length-1))));
    const ll=latlngs[idx];
    if(!cursor){
      cursor=L.circleMarker(ll,{radius:8,color:'#fff',weight:3,fillColor:'#e8b23a',fillOpacity:1,interactive:false}).addTo(map);
    } else cursor.setLatLng(ll);
    if(profile[i]){
      if(elevKm) elevKm.textContent=`Km ${profile[i].d.toFixed(1).replace('.',',')}`;
      if(elevAlt) elevAlt.textContent=`${Math.round(profile[i].e)} m`;
    }
  }
  function drawProfile(prof, color){
    if(!elevEl||!prof?.length) return;
    profile=prof;
    const w=640,h=100,pad=6;
    const ds=prof.map(p=>p.d), es=prof.map(p=>p.e);
    const minE=Math.min(...es), maxE=Math.max(...es);
    const minD=Math.min(...ds), maxD=Math.max(...ds)||1;
    const xy=prof.map(p=>{
      const x=pad+(p.d-minD)/(maxD-minD)*(w-pad*2);
      const y=h-pad-(p.e-minE)/Math.max(1,maxE-minE)*(h-pad*2);
      return [x,y];
    });
    const pts=xy.map(([x,y])=>`${x.toFixed(1)},${y.toFixed(1)}`).join(' ');
    elevEl.setAttribute('viewBox',`0 0 ${w} ${h}`);
    elevEl.innerHTML=`
      <defs><linearGradient id="eg" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="${color}" stop-opacity=".55"/><stop offset="100%" stop-color="${color}" stop-opacity=".05"/>
      </linearGradient></defs>
      <polyline fill="url(#eg)" stroke="none" points="${pad},${h-pad} ${pts} ${w-pad},${h-pad}"/>
      <polyline fill="none" stroke="${color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" points="${pts}"/>
      <circle id="elev-dot" r="5" fill="#e8b23a" stroke="#fff" stroke-width="2" cx="${xy[0][0]}" cy="${xy[0][1]}"/>`;
    const chart=elevEl.closest('.elev-chart')||elevEl.parentElement;
    const onMove=(clientX)=>{
      const rect=elevEl.getBoundingClientRect();
      const x=Math.max(pad, Math.min(w-pad, (clientX-rect.left)/rect.width*w));
      const d=minD+(x-pad)/(w-pad*2)*(maxD-minD);
      const i=distToIndex(d);
      const [ex,ey]=xy[i];
      const dot=document.getElementById('elev-dot');
      if(dot){dot.setAttribute('cx',ex);dot.setAttribute('cy',ey)}
      setCursorAt(i);
      if(elevTip){
        elevTip.style.display='block';
        elevTip.style.left=((ex/w)*rect.width)+'px';
        elevTip.style.top=((ey/h)*rect.height)+'px';
        elevTip.textContent=`Km ${prof[i].d.toFixed(1).replace('.',',')} · ${Math.round(prof[i].e)} m`;
      }
    };
    chart.onmousemove=e=>onMove(e.clientX);
    chart.ontouchmove=e=>{if(e.touches[0]) onMove(e.touches[0].clientX)};
    chart.onmouseleave=()=>{if(elevTip) elevTip.style.display='none'};
  }

  function load(key){
    currentKey=key;
    Promise.all([
      fetch('../data/routes.json').then(r=>r.json()),
      waypoints[key]?Promise.resolve(waypoints):fetch('../data/waypoints.json').then(r=>r.json()).catch(()=>({}))
    ]).then(([data, wp])=>{
      waypoints=wp||waypoints;
      const c=data.courses[key]; if(!c) return;
      if(layer) map.removeLayer(layer);
      markers.forEach(m=>map.removeLayer(m)); markers=[];
      if(cursor){map.removeLayer(cursor);cursor=null}
      layer=L.geoJSON(c.geojson,{style:{color:colors[key]||'#1657d9',weight:5,opacity:.92}}).addTo(map);
      fitRoute(layer.getBounds().pad(0.08));
      latlngs=c.geojson.geometry.coordinates.map(([lon,lat])=>[lat,lon]);

      // km markers every 5km along profile
      (c.profile||[]).forEach(p=>{
        if(p.d>0 && Math.abs(p.d%5)<0.15){
          const i=distToIndex(p.d);
          const idx=Math.round(i/(Math.max(1,(c.profile.length-1)))*(latlngs.length-1));
          const ll=latlngs[Math.max(0,Math.min(latlngs.length-1,idx))];
          const m=L.marker(ll,{icon:L.divIcon({className:'',html:`<div style="background:#0b1c33;color:#fff;border:2px solid #fff;border-radius:999px;font:700 10px/1 Inter,sans-serif;padding:4px 6px;box-shadow:0 4px 12px rgba(0,0,0,.25)">${Math.round(p.d)}</div>`,iconSize:[28,20],iconAnchor:[14,10]})}).addTo(map);
          markers.push(m);
        }
      });

      const start=L.circleMarker([c.start.lat,c.start.lon],{radius:9,color:'#fff',weight:2,fillColor:'#0f9d58',fillOpacity:1}).bindPopup(`<strong>Départ</strong><br>${c.start.name}`).addTo(map);
      const finish=L.circleMarker([c.finish.lat,c.finish.lon],{radius:9,color:'#fff',weight:2,fillColor:'#ff5a1f',fillOpacity:1}).bindPopup(`<strong>Arrivée</strong><br>${c.finish.name}`).addTo(map);
      markers.push(start,finish);

      (c.aid||[]).forEach(a=>{
        const m=L.circleMarker([a.lat,a.lon],{radius:6,color:'#fff',weight:1.5,fillColor:'#1aa7ff',fillOpacity:1})
          .bindPopup(`<strong>Km ${a.km} · ${a.name}</strong><br>${a.offer}`).addTo(map);
        markers.push(m);
      });

      (waypoints[key]||[]).forEach(w=>{
        if(w.kind==='start'||w.kind==='finish') return;
        const m=L.circleMarker([w.lat,w.lon],{radius:5,color:'#fff',weight:1.5,fillColor:'#e8b23a',fillOpacity:1})
          .bindPopup(`<strong>${w.name}</strong>`).addTo(map);
        markers.push(m);
      });

      if(labelEl) labelEl.textContent=c.name;
      if(noteEl) noteEl.textContent=data.note;
      if(metaDist) metaDist.textContent=String(c.official_km).replace('.',',')+' km';
      if(metaDeniv && c.official_deniv) metaDeniv.textContent=`${c.official_deniv.dplus} / ${c.official_deniv.dminus} m`;
      if(metaStart) metaStart.textContent=window.LM_STARTS?.[key]||'—';
      if(gpxLink){ gpxLink.href=`../data/gpx/${key}-indicatif.gpx`; gpxLink.setAttribute('download',`${key}-indicatif.gpx`); }
      drawProfile(c.profile, colors[key]||'#1657d9');
      if(aidEl){
        aidEl.innerHTML=(c.aid||[]).map(a=>`<div class="aid"><div class="km">Km ${a.km}</div><div><strong>${a.name}</strong><div style="color:var(--muted);font-size:13px">${a.offer}</div></div></div>`).join('');
      }
      // Refit to include polyline + start/finish (+ markers) with padding
      try{
        const group=L.featureGroup([layer, ...markers].filter(Boolean));
        if(group.getLayers().length) fitRoute(group.getBounds().pad(0.1));
      }catch(e){}
      const places=document.getElementById('place-rail');
      if(places){
        const photos={
          'Ouchy':'../img/photos/lm-05-md.jpg','Pully':'../img/photos/lm-09-md.jpg','Lutry':'../img/photos/lm-04-md.jpg',
          'Cully':'../img/photos/lm-03-md.jpg','Lavaux':'../img/photos/lm-03-md.jpg','Vevey':'../img/photos/lm-02-md.jpg',
          'La Tour-de-Peilz':'../img/photos/lm-02-md.jpg','Place de Milan':'../img/photos/lm-01-md.jpg','Bellerive':'../img/photos/lm-01-md.jpg'
        };
        places.innerHTML=(waypoints[key]||[]).map(w=>{
          let src='../img/photos/lm-09-md.jpg';
          for(const [k,v] of Object.entries(photos)){ if(w.name.includes(k)) {src=v;break} }
          return `<div class="place"><img src="${src}" alt=""><div class="body"><strong>${w.name}</strong><span>${w.kind==='start'?'Départ':w.kind==='finish'?'Arrivée':'Point de passage'}</span></div></div>`;
        }).join('');
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
