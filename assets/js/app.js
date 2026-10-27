(function(){
  const drawer=document.getElementById('drawer');
  const openBtn=document.getElementById('menuOpen');
  const closeBtn=document.getElementById('menuClose');
  function open(){drawer?.classList.add('open');document.body.style.overflow='hidden';openBtn?.setAttribute('aria-expanded','true')}
  function close(){drawer?.classList.remove('open');document.body.style.overflow='';openBtn?.setAttribute('aria-expanded','false')}
  openBtn?.addEventListener('click',open);
  closeBtn?.addEventListener('click',close);
  drawer?.addEventListener('click',e=>{if(e.target===drawer) close()});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'){close();document.getElementById('searchOverlay')?.classList.remove('open')}});

  const cd=document.getElementById('countdown');
  if(cd){
    const target=new Date('2027-10-24T08:40:00+02:00').getTime();
    const tick=()=>{
      let d=Math.max(0,target-Date.now());
      const days=Math.floor(d/86400000); d-=days*86400000;
      const h=Math.floor(d/3600000); d-=h*3600000;
      const m=Math.floor(d/60000); d-=m*60000;
      const s=Math.floor(d/1000);
      const vals=[days,h,m,s];
      cd.querySelectorAll('[data-n]').forEach((el,i)=>{el.textContent=String(vals[i]).padStart(2,'0')});
    };
    tick(); setInterval(tick,1000);
  }

  const ANSWERS=window.LM_ANSWERS||{};
  window.showAnswer=function(key){
    const box=document.getElementById('ask-answer'); const item=ANSWERS[key]; if(!box||!item) return;
    box.classList.add('show');
    box.innerHTML=`<div style="opacity:.75;font-size:12px;margin-bottom:6px">${item.tag||''}</div><strong>${item.q||''}</strong><p style="margin:8px 0">${item.a}</p>`;
    const input=document.getElementById('ask-input'); if(input) input.value=item.q;
  };
  window.askSubmit=function(e){
    e.preventDefault();
    const v=(document.getElementById('ask-input')?.value||'').toLowerCase();
    if(v.includes('sac')||v.includes('bag')||v.includes('tasche')) return showAnswer('sac');
    if(v.includes('prix')||v.includes('price')||v.includes('preis')||v.includes('cost')||v.includes('combien')) return showAnswer('prix');
    if(v.includes('semi')||v.includes('half')||v.includes('heure')||v.includes('start')||v.includes('départ')||v.includes('depart')) return showAnswer('semi');
    if(v.includes('dossard')||v.includes('bib')||v.includes('startnummer')) return showAnswer('dossard');
    if(v.includes('ravit')||v.includes('aid')||v.includes('verpfleg')) return showAnswer('ravito');
    const box=document.getElementById('ask-answer'); if(!box) return;
    box.classList.add('show');
    box.innerHTML=`<p>${ANSWERS.fallback?.a||''}</p>`;
  };

  const path=location.pathname.split('/').pop()||'index.html';
  document.querySelectorAll('.bottom a').forEach(a=>{
    const href=a.getAttribute('href');
    if(href===path || (path==='index.html'&&href==='index.html')) a.classList.add('active');
  });

  // Global search
  const overlay=document.getElementById('searchOverlay');
  const openSearch=document.getElementById('searchOpen');
  const searchInput=document.getElementById('searchInput');
  const searchHits=document.getElementById('searchHits');
  const index=window.LM_SEARCH||[];
  function renderHits(q){
    if(!searchHits) return;
    const qq=(q||'').toLowerCase().trim();
    const hits=!qq?index.slice(0,8):index.filter(i=> (i.t+' '+i.k).toLowerCase().includes(qq)).slice(0,12);
    searchHits.innerHTML=hits.map(h=>`<a href="${h.href}"><strong>${h.t}</strong><small>${h.k}</small></a>`).join('')||'<p style="color:var(--muted);padding:8px">Aucun résultat</p>';
  }
  openSearch?.addEventListener('click',()=>{overlay?.classList.add('open');setTimeout(()=>searchInput?.focus(),50);renderHits('')});
  overlay?.addEventListener('click',e=>{if(e.target===overlay) overlay.classList.remove('open')});
  searchInput?.addEventListener('input',()=>renderHits(searchInput.value));
  document.addEventListener('keydown',e=>{
    if((e.metaKey||e.ctrlKey)&&e.key.toLowerCase()==='k'){e.preventDefault();openSearch?.click()}
  });
  // WhatsApp assistant demo (injects sticky FAB + sheet)
  (function loadWa(){
    if(document.querySelector('script[data-wa-demo]')) return;
    const s=document.createElement('script');
    s.src='../assets/js/whatsapp-demo.js';
    s.setAttribute('data-wa-demo','1');
    document.body.appendChild(s);
  })();
})();

/* partner pitch + reveal — robust: content visible without JS */
(function(){
  var root = document.documentElement;
  root.classList.add('js');

  function prefersReduced(){
    try { return window.matchMedia('(prefers-reduced-motion: reduce)').matches; }
    catch(e){ return false; }
  }

  function revealEl(el){
    if(!el) return;
    el.classList.add('in','revealed');
    if(el.classList.contains('kpi')) animateCount(el);
  }

  function revealAll(){
    document.querySelectorAll('.reveal').forEach(revealEl);
  }

  function animateCount(el){
    var target = parseInt(el.getAttribute('data-count')||'0',10);
    if(!target || el.dataset.done) return;
    el.dataset.done='1';
    var num = el.querySelector('.kpi-num');
    if(!num) return;
    var final = num.textContent;
    if(prefersReduced()){ return; }
    var start = performance.now();
    var dur = 900;
    function step(now){
      var p = Math.min(1,(now-start)/dur);
      var eased = 1-Math.pow(1-p,3);
      var v = Math.round(target*eased);
      try { num.textContent = v.toLocaleString(root.lang||'fr-CH'); }
      catch(e){ num.textContent = String(v); }
      if(p<1) requestAnimationFrame(step); else num.textContent = final;
    }
    requestAnimationFrame(step);
  }

  var targets = document.querySelectorAll('.partner-pitch .kpi, .partner-pitch .card, .partner-pitch .vis-item, .partner-pitch .proc-step, .partner-pitch .devenir-banner, .reveal-on-scroll');
  // Also allow explicit .reveal already in markup; don't blanket-hide every .card site-wide
  targets.forEach(function(el){ el.classList.add('reveal'); });

  if(prefersReduced() || !('IntersectionObserver' in window)){
    revealAll();
  } else {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting){
          revealEl(e.target);
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0, rootMargin: '0px 0px 12% 0px' });
    document.querySelectorAll('.reveal').forEach(function(el){ io.observe(el); });
    // Safety net: never leave content invisible (screenshots, slow IO, odd viewports)
    setTimeout(revealAll, 1500);
  }

  document.querySelectorAll('form[data-partner-demo]').forEach(function(form){
    form.addEventListener('submit', function(ev){
      ev.preventDefault();
      var ok = form.querySelector('.form-ok');
      if(ok) ok.hidden = false;
      form.querySelectorAll('input,textarea,select,button[type=submit]').forEach(function(x){
        if(x.type==='submit') x.disabled = true;
      });
    });
  });
})();

