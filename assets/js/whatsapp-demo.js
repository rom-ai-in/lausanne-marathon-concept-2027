(function(){
  if(document.getElementById('waFab')) return;
  const lang=(document.documentElement.lang||'fr').slice(0,2);
  const I18N={
    fr:{
      fabAria:'Démo — assistant WhatsApp (non actif)',
      fabBadge:'Démo',
      title:'Lausanne Marathon',
      status:'En ligne · réponse d’exemple',
      banner:'Démo — assistant WhatsApp (concept). Aucun message n’est envoyé.',
      inactive:'Démo — non actif',
      close:'Fermer',
      placeholder:'Écrire un message… (démo)',
      send:'Envoyer',
      chips:[
        {id:'horaires',label:'Horaires'},
        {id:'dossards',label:'Retrait des dossards'},
        {id:'parcours',label:'Parcours'},
        {id:'resultats',label:'Résultats'},
        {id:'photos',label:'Photos'},
        {id:'meteo',label:'Météo'},
        {id:'inscription',label:'Inscription'},
        {id:'sacs',label:'Sacs coureurs'},
        {id:'humain',label:'Parler à l’équipe'}
      ],
      hello:'Bonjour 👋 Je suis l’assistant WhatsApp du Lausanne Marathon (démo concept). Posez une question sur les horaires, les dossards ou le parcours — ou demandez à parler à l’équipe.',
      typing:'…',
      answers:{
        horaires:{
          user:'Quelles sont les heures de départ ?',
          bot:'Horaires de départ (édition 2026, à confirmer pour 2027) :<br>• Semi-marathon : <strong>08h40</strong><br>• Marathon : <strong>10h05</strong><br>• 10 km : <strong>14h00</strong><br>• Walking : <strong>14h30</strong><br>• Nordic Walking : <strong>dès 14h33</strong><br><a href="programme.html">Voir le programme →</a>'
        },
        dossards:{
          user:'Où retirer mon dossard ?',
          bot:'Retrait des dossards : Salle de sport Auguste Piccard, Ch. de Bellerive 36, Lausanne.<br>Horaires 2026 : ven. 15h–18h · sam. 11h–18h · dim. 07h–14h.<br><a href="dossards.html">Page dossards →</a>'
        },
        parcours:{
          user:'Où voir le parcours ?',
          bot:'La carte interactive (tracés indicatifs le long du Léman), les ravitaillements et le profil d’altitude sont sur la page Parcours.<br><a href="parcours.html">Ouvrir le parcours →</a>'
        },
        resultats:{
          user:'Où trouver les résultats ?',
          bot:'Chronométrage et classements via Datasport.<br><a href="resultats.html">Page résultats →</a>'
        },
        photos:{
          user:'Où retrouver mes photos ?',
          bot:'Les photos coureurs sont disponibles via Alphafoto. Lien depuis la page Photos de cette maquette.<br><a href="photos.html">Photos →</a>'
        },
        meteo:{
          user:'Quel temps prévu le jour J ?',
          bot:'Consultez la page Météo pour un rappel local le jour de course. Les consignes opérationnelles restent communiquées par l’organisation.<br><a href="meteo.html">Météo →</a>'
        },
        inscription:{
          user:'Comment m’inscrire pour 2027 ?',
          bot:'La pré-inscription 2027 est ouverte via Datasport. Tarifs et catégories : référence édition 2026.<br><a href="inscription.html">Inscription →</a> · <a href="https://onreg.datasport.com/lausanne-marathon-2026" target="_blank" rel="noopener">Datasport →</a>'
        },
        sacs:{
          user:'Où déposer mon sac ?',
          bot:'Dépôt possible à l’arrivée Bellerive-Plage (surveillé, sur présentation du dossard). Pas de transfert départ → arrivée (~420 m).<br><a href="sacs.html">Sacs coureurs →</a>'
        },
        humain:{
          user:'Je voudrais changer mon nom d’inscription / un remboursement.',
          bot:'Pour un changement de nom, un transfert ou un remboursement, je transmets votre demande à une personne de l’équipe.<div class="wa-ticket"><span class="wa-tag">Ticket d’exemple</span><br>Référence : <strong>LM-DEMO-2027-4821</strong><br>Statut : transmis à l’équipe (simulation)<br>Délai indicatif : réponse humaine sous 1–2 jours ouvrables.</div>Coordonnées officielles aussi sur <a href="contact.html">Contact</a> · Tél. +41 21 806 30 16.'
        }
      },
      fallback:{
        user:null,
        bot:'Dans la version réelle, l’assistant répondrait à partir des infos officielles et créerait un ticket si besoin. Essayez une suggestion ci-dessous, ou ouvrez <a href="faq.html">la FAQ</a> / <a href="contact.html">Contact</a>.'
      }
    },
    de:{
      fabAria:'Demo — WhatsApp-Assistent (nicht aktiv)',
      fabBadge:'Demo',
      title:'Lausanne Marathon',
      status:'Online · Beispielantwort',
      banner:'Demo — WhatsApp-Assistent (Konzept). Es wird keine Nachricht gesendet.',
      inactive:'Demo — nicht aktiv',
      close:'Schliessen',
      placeholder:'Nachricht schreiben… (Demo)',
      send:'Senden',
      chips:[
        {id:'horaires',label:'Startzeiten'},
        {id:'dossards',label:'Startnummern'},
        {id:'parcours',label:'Strecke'},
        {id:'resultats',label:'Resultate'},
        {id:'photos',label:'Fotos'},
        {id:'meteo',label:'Wetter'},
        {id:'inscription',label:'Anmeldung'},
        {id:'sacs',label:'Gepäck'},
        {id:'humain',label:'Team kontaktieren'}
      ],
      hello:'Hallo 👋 Ich bin der WhatsApp-Assistent des Lausanne Marathon (Konzept-Demo). Fragen Sie nach Startzeiten, Startnummern oder der Strecke — oder bitten Sie um Kontakt mit dem Team.',
      typing:'…',
      answers:{
        horaires:{
          user:'Wann sind die Startzeiten?',
          bot:'Startzeiten (Ausgabe 2026, für 2027 zu bestätigen):<br>• Halbmarathon: <strong>08:40</strong><br>• Marathon: <strong>10:05</strong><br>• 10 km: <strong>14:00</strong><br>• Walking: <strong>14:30</strong><br>• Nordic Walking: <strong>ab 14:33</strong><br><a href="programme.html">Programm ansehen →</a>'
        },
        dossards:{
          user:'Wo hole ich meine Startnummer ab?',
          bot:'Startnummern: Sporthalle Auguste Piccard, Ch. de Bellerive 36, Lausanne.<br>Zeiten 2026: Fr. 15–18 Uhr · Sa. 11–18 Uhr · So. 07–14 Uhr.<br><a href="dossards.html">Seite Startnummern →</a>'
        },
        parcours:{
          user:'Wo sehe ich die Strecke?',
          bot:'Interaktive Karte (indikative Strecken am Genfersee), Verpflegung und Höhenprofil auf der Seite Strecke.<br><a href="parcours.html">Strecke öffnen →</a>'
        },
        resultats:{
          user:'Wo finde ich die Resultate?',
          bot:'Zeitmessung und Ranglisten via Datasport.<br><a href="resultats.html">Resultate →</a>'
        },
        photos:{
          user:'Wo finde ich meine Fotos?',
          bot:'Läuferfotos über Alphafoto. Link auf der Seite Fotos dieses Mockups.<br><a href="photos.html">Fotos →</a>'
        },
        meteo:{
          user:'Wie wird das Wetter am Renntag?',
          bot:'Auf der Seite Wetter finden Sie einen lokalen Hinweis. Operative Vorgaben kommuniziert die Organisation.<br><a href="meteo.html">Wetter →</a>'
        },
        inscription:{
          user:'Wie melde ich mich für 2027 an?',
          bot:'Die Voranmeldung 2027 ist über Datasport geöffnet. Preise: Referenz 2026.<br><a href="inscription.html">Anmeldung →</a> · <a href="https://onreg.datasport.com/lausanne-marathon-2026" target="_blank" rel="noopener">Datasport →</a>'
        },
        sacs:{
          user:'Wo gebe ich mein Gepäck ab?',
          bot:'Abgabe am Ziel Bellerive-Plage möglich (bewacht, mit Startnummer). Kein Transfer Start → Ziel (~420 m).<br><a href="sacs.html">Gepäck →</a>'
        },
        humain:{
          user:'Ich möchte meinen Namen ändern / eine Rückerstattung.',
          bot:'Für Namensänderung, Transfer oder Rückerstattung leite ich Ihre Anfrage an eine Person weiter.<div class="wa-ticket"><span class="wa-tag">Beispiel-Ticket</span><br>Referenz: <strong>LM-DEMO-2027-4821</strong><br>Status: an das Team übermittelt (Simulation)<br>Richtwert: menschliche Antwort in 1–2 Werktagen.</div>Offizielle Kontakte auch unter <a href="contact.html">Kontakt</a> · Tel. +41 21 806 30 16.'
        }
      },
      fallback:{
        user:null,
        bot:'In der echten Version würde der Assistent aus offiziellen Infos antworten und bei Bedarf ein Ticket öffnen. Nutzen Sie eine Suggestion unten, oder öffnen Sie die <a href="faq.html">FAQ</a> / <a href="contact.html">Kontakt</a>.'
      }
    },
    en:{
      fabAria:'Demo — WhatsApp assistant (not active)',
      fabBadge:'Demo',
      title:'Lausanne Marathon',
      status:'Online · sample reply',
      banner:'Demo — WhatsApp assistant (concept). No message is sent.',
      inactive:'Demo — not active',
      close:'Close',
      placeholder:'Type a message… (demo)',
      send:'Send',
      chips:[
        {id:'horaires',label:'Start times'},
        {id:'dossards',label:'Bib pick-up'},
        {id:'parcours',label:'Course'},
        {id:'resultats',label:'Results'},
        {id:'photos',label:'Photos'},
        {id:'meteo',label:'Weather'},
        {id:'inscription',label:'Registration'},
        {id:'sacs',label:'Bag drop'},
        {id:'humain',label:'Talk to the team'}
      ],
      hello:'Hi 👋 I’m the Lausanne Marathon WhatsApp assistant (concept demo). Ask about start times, bib pick-up or the course — or ask to speak with the team.',
      typing:'…',
      answers:{
        horaires:{
          user:'What are the start times?',
          bot:'Start times (2026 edition, to be confirmed for 2027):<br>• Half marathon: <strong>08:40</strong><br>• Marathon: <strong>10:05</strong><br>• 10 km: <strong>14:00</strong><br>• Walking: <strong>14:30</strong><br>• Nordic Walking: <strong>from 14:33</strong><br><a href="programme.html">See the programme →</a>'
        },
        dossards:{
          user:'Where do I pick up my bib?',
          bot:'Bib pick-up: Auguste Piccard sports hall, Ch. de Bellerive 36, Lausanne.<br>2026 hours: Fri 15:00–18:00 · Sat 11:00–18:00 · Sun 07:00–14:00.<br><a href="dossards.html">Bib page →</a>'
        },
        parcours:{
          user:'Where can I see the course?',
          bot:'The interactive map (indicative routes along Lake Geneva), aid stations and elevation profile are on the Course page.<br><a href="parcours.html">Open the course →</a>'
        },
        resultats:{
          user:'Where are the results?',
          bot:'Timing and rankings via Datasport.<br><a href="resultats.html">Results page →</a>'
        },
        photos:{
          user:'Where can I find my photos?',
          bot:'Runner photos are available via Alphafoto. Link from the Photos page of this mockup.<br><a href="photos.html">Photos →</a>'
        },
        meteo:{
          user:'What’s the weather on race day?',
          bot:'Check the Weather page for a local reminder. Operational guidance comes from the organisers.<br><a href="meteo.html">Weather →</a>'
        },
        inscription:{
          user:'How do I register for 2027?',
          bot:'2027 pre-registration is open via Datasport. Fees: 2026 reference.<br><a href="inscription.html">Registration →</a> · <a href="https://onreg.datasport.com/lausanne-marathon-2026" target="_blank" rel="noopener">Datasport →</a>'
        },
        sacs:{
          user:'Where do I drop my bag?',
          bot:'Drop-off at the Bellerive-Plage finish (supervised, show your bib). No start → finish transfer (~420 m).<br><a href="sacs.html">Race bags →</a>'
        },
        humain:{
          user:'I need a name change / a refund.',
          bot:'For a name change, transfer or refund, I’ll hand your request to a person on the team.<div class="wa-ticket"><span class="wa-tag">Sample ticket</span><br>Reference: <strong>LM-DEMO-2027-4821</strong><br>Status: sent to the team (simulation)<br>Indicative: human reply within 1–2 business days.</div>Official details also on <a href="contact.html">Contact</a> · Tel. +41 21 806 30 16.'
        }
      },
      fallback:{
        user:null,
        bot:'In a live version the assistant would answer from official info and open a ticket when needed. Try a suggestion below, or open the <a href="faq.html">FAQ</a> / <a href="contact.html">Contact</a>.'
      }
    },
    it:{
      fabAria:'Demo — assistente WhatsApp (non attivo)',
      fabBadge:'Demo',
      title:'Lausanne Marathon',
      status:'Online · risposta di esempio',
      banner:'Demo — assistente WhatsApp (concept). Nessun messaggio viene inviato.',
      inactive:'Demo — non attivo',
      close:'Chiudi',
      placeholder:'Scrivi un messaggio… (demo)',
      send:'Invia',
      chips:[
        {id:'horaires',label:'Orari'},
        {id:'dossards',label:'Ritiro pettorali'},
        {id:'parcours',label:'Percorso'},
        {id:'resultats',label:'Risultati'},
        {id:'photos',label:'Foto'},
        {id:'meteo',label:'Meteo'},
        {id:'inscription',label:'Iscrizione'},
        {id:'sacs',label:'Borse'},
        {id:'humain',label:'Parlare al team'}
      ],
      hello:'Ciao 👋 Sono l’assistente WhatsApp del Lausanne Marathon (demo concept). Chiedi orari, pettorali o percorso — oppure di parlare con il team.',
      typing:'…',
      answers:{
        horaires:{
          user:'Quali sono gli orari di partenza?',
          bot:'Orari di partenza (edizione 2026, da confermare per il 2027):<br>• Mezza maratona: <strong>08:40</strong><br>• Maratona: <strong>10:05</strong><br>• 10 km: <strong>14:00</strong><br>• Walking: <strong>14:30</strong><br>• Nordic Walking: <strong>dalle 14:33</strong><br><a href="programme.html">Vedi il programma →</a>'
        },
        dossards:{
          user:'Dove ritiro il pettorale?',
          bot:'Ritiro pettorali: palestra Auguste Piccard, Ch. de Bellerive 36, Losanna.<br>Orari 2026: ven. 15–18 · sab. 11–18 · dom. 07–14.<br><a href="dossards.html">Pagina pettorali →</a>'
        },
        parcours:{
          user:'Dove vedo il percorso?',
          bot:'La mappa interattiva (tracciati indicativi lungo il Lemano), i rifornimenti e il profilo altimetrico sono sulla pagina Percorso.<br><a href="parcours.html">Apri il percorso →</a>'
        },
        resultats:{
          user:'Dove trovo i risultati?',
          bot:'Cronometraggio e classifiche via Datasport.<br><a href="resultats.html">Pagina risultati →</a>'
        },
        photos:{
          user:'Dove ritrovo le mie foto?',
          bot:'Le foto dei corridori sono disponibili via Alphafoto. Link dalla pagina Foto di questo mockup.<br><a href="photos.html">Foto →</a>'
        },
        meteo:{
          user:'Che tempo farà il giorno gara?',
          bot:'Consultate la pagina Meteo per un promemoria locale. Le indicazioni operative restano dell’organizzazione.<br><a href="meteo.html">Meteo →</a>'
        },
        inscription:{
          user:'Come mi iscrivo per il 2027?',
          bot:'La pre-iscrizione 2027 è aperta via Datasport. Tariffe: riferimento 2026.<br><a href="inscription.html">Iscrizione →</a> · <a href="https://onreg.datasport.com/lausanne-marathon-2026" target="_blank" rel="noopener">Datasport →</a>'
        },
        sacs:{
          user:'Dove deposito la borsa?',
          bot:'Deposito all’arrivo Bellerive-Plage (sorvegliato, con pettorale). Nessun trasferimento partenza → arrivo (~420 m).<br><a href="sacs.html">Borse →</a>'
        },
        humain:{
          user:'Vorrei cambiare il nome / un rimborso.',
          bot:'Per un cambio nome, un trasferimento o un rimborso, trasmetto la richiesta a una persona del team.<div class="wa-ticket"><span class="wa-tag">Ticket di esempio</span><br>Riferimento: <strong>LM-DEMO-2027-4821</strong><br>Stato: inviato al team (simulazione)<br>Indicativo: risposta umana entro 1–2 giorni lavorativi.</div>Coordinate ufficiali anche su <a href="contact.html">Contatti</a> · Tel. +41 21 806 30 16.'
        }
      },
      fallback:{
        user:null,
        bot:'Nella versione reale l’assistente risponderebbe dalle info ufficiali e aprirebbe un ticket se serve. Prova un suggerimento qui sotto, oppure apri la <a href="faq.html">FAQ</a> / <a href="contact.html">Contatti</a>.'
      }
    }
  };
  const t=I18N[lang]||I18N.fr;

  const waIcon='<svg viewBox="0 0 32 32" aria-hidden="true"><path fill="currentColor" d="M16.01 3C9.39 3 4 8.3 4 14.82c0 2.58.85 4.97 2.3 6.93L4.7 27.4l5.85-1.53A12.1 12.1 0 0 0 16 26.64c6.62 0 12-5.3 12-11.82C28 8.3 22.63 3 16.01 3zm6.95 16.76c-.3.84-1.73 1.54-2.42 1.64-.62.09-1.4.13-2.26-.14-.52-.16-1.19-.39-2.05-.76-3.61-1.56-5.96-5.18-6.14-5.42-.18-.24-1.48-1.97-1.48-3.76s.94-2.67 1.27-3.03c.33-.36.72-.45.96-.45h.69c.22 0 .52-.08.81.62.3.72 1.02 2.49 1.11 2.67.09.18.15.39.03.62-.12.24-.18.39-.36.6-.18.21-.38.47-.54.63-.18.18-.36.37-.15.72.21.36.93 1.53 2 2.48 1.37 1.21 2.53 1.59 2.89 1.77.36.18.57.15.78-.09.21-.24.9-1.05 1.14-1.41.24-.36.48-.3.81-.18.33.12 2.1.99 2.46 1.17.36.18.6.27.69.42.09.15.09.87-.21 1.71z"/></svg>';
  const sendIcon='<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>';

  const fab=document.createElement('button');
  fab.type='button'; fab.id='waFab'; fab.className='wa-fab';
  fab.setAttribute('aria-label',t.fabAria);
  fab.setAttribute('title',t.inactive);
  fab.innerHTML=waIcon+'<span class="wa-fab-badge">'+t.fabBadge+'</span>';
  document.body.appendChild(fab);

  const overlay=document.createElement('div');
  overlay.id='waOverlay'; overlay.className='wa-overlay'; overlay.setAttribute('role','dialog');
  overlay.setAttribute('aria-modal','true'); overlay.setAttribute('aria-label',t.banner);
  overlay.innerHTML=
    '<div class="wa-sheet" id="waSheet">'+
      '<div class="wa-head">'+
        '<div class="wa-avatar">'+waIcon+'</div>'+
        '<div class="wa-head-meta"><strong>'+t.title+'</strong><span>'+t.status+'</span></div>'+
        '<button type="button" class="wa-close" id="waClose" aria-label="'+t.close+'">✕</button>'+
      '</div>'+
      '<div class="wa-demo-banner">'+t.banner+'</div>'+
      '<div class="wa-thread" id="waThread" aria-live="polite"></div>'+
      '<div class="wa-chips" id="waChips"></div>'+
      '<form class="wa-composer" id="waForm">'+
        '<input id="waInput" type="text" autocomplete="off" placeholder="'+t.placeholder+'" aria-label="'+t.placeholder+'">'+
        '<button type="submit" class="wa-send" id="waSend" aria-label="'+t.send+'" title="'+t.inactive+'">'+sendIcon+'</button>'+
      '</form>'+
    '</div>';
  document.body.appendChild(overlay);

  const thread=document.getElementById('waThread');
  const chipsEl=document.getElementById('waChips');
  const form=document.getElementById('waForm');
  const input=document.getElementById('waInput');
  let busy=false;

  function timeNow(){
    const d=new Date();
    return String(d.getHours()).padStart(2,'0')+':'+String(d.getMinutes()).padStart(2,'0');
  }
  function addMsg(kind,html){
    const el=document.createElement('div');
    el.className='wa-msg '+kind;
    el.innerHTML=html+'<span class="wa-time">'+timeNow()+'</span>';
    thread.appendChild(el);
    thread.scrollTop=thread.scrollHeight;
    return el;
  }
  function renderChips(){
    chipsEl.innerHTML=t.chips.map(c=>'<button type="button" class="wa-chip" data-id="'+c.id+'">'+c.label+'</button>').join('');
  }
  function open(){
    overlay.classList.add('open');
    document.body.classList.add('wa-open');
    document.body.style.overflow='hidden';
    if(!thread.dataset.ready){
      addMsg('bot',t.hello);
      thread.dataset.ready='1';
    }
    setTimeout(()=>input?.focus(),180);
  }
  function close(){
    overlay.classList.remove('open');
    document.body.classList.remove('wa-open');
    document.body.style.overflow='';
  }
  function resolveKey(raw){
    const v=(raw||'').toLowerCase();
    if(/horaire|start|zeit|orari|départ|depart|heure|time|08h|10h|14h/.test(v)) return 'horaires';
    if(/dossard|bib|startnummer|pettoral|retrait|pick.?up|numéro|numero/.test(v)) return 'dossards';
    if(/parcours|course|strecke|percorso|carte|map|route/.test(v)) return 'parcours';
    if(/résultat|resultat|result|resultate|risultat|classement|ranking/.test(v)) return 'resultats';
    if(/photo|foto|alphafoto/.test(v)) return 'photos';
    if(/humain|équipe|equipe|team|ticket|rembours|refund|nom|name|transfer|transfert|parler|speak|kontakt|contatt/.test(v)) return 'humain';
    return null;
  }
  function reply(key,customUser){
    if(busy) return;
    const pack=key&&t.answers[key]?t.answers[key]:t.fallback;
    const userText=customUser||pack.user;
    busy=true;
    chipsEl.querySelectorAll('button').forEach(b=>b.disabled=true);
    if(userText) addMsg('user',userText);
    const typing=addMsg('bot',t.typing);
    setTimeout(()=>{
      typing.remove();
      addMsg('bot',pack.bot);
      busy=false;
      chipsEl.querySelectorAll('button').forEach(b=>b.disabled=false);
    },650);
  }

  renderChips();
  fab.addEventListener('click',open);
  document.getElementById('waClose').addEventListener('click',close);
  overlay.addEventListener('click',e=>{if(e.target===overlay) close()});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&overlay.classList.contains('open')) close()});
  chipsEl.addEventListener('click',e=>{
    const btn=e.target.closest('.wa-chip'); if(!btn||busy) return;
    reply(btn.dataset.id);
  });
  form.addEventListener('submit',e=>{
    e.preventDefault();
    const v=(input.value||'').trim(); if(!v||busy) return;
    input.value='';
    reply(resolveKey(v),v);
  });

  // Never cover bottom CTAs (partner strip / footer): tuck FAB while they are on screen
  (function(){
    var sel='.sponsor-strip-cta, .sponsor-strip, footer.footer, .devenir-banner';
    var targets=[].slice.call(document.querySelectorAll(sel));
    if(!targets.length) return;
    var hit=new Set();
    function sync(){
      if(hit.size) fab.classList.add('is-tucked');
      else fab.classList.remove('is-tucked');
    }
    if(!('IntersectionObserver' in window)){
      fab.classList.add('is-tucked');
      return;
    }
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting) hit.add(e.target);
        else hit.delete(e.target);
      });
      sync();
    }, {threshold:0, rootMargin:'12px 0px 12px 0px'});
    targets.forEach(function(el){ io.observe(el); });
  })();

  // Deep-link helpers from Contact page
  document.addEventListener('click',e=>{
    const a=e.target.closest('[data-wa-open]');
    if(!a) return;
    e.preventDefault();
    open();
    const id=a.getAttribute('data-wa-open');
    if(id&&id!=='1') setTimeout(()=>reply(id),200);
  });
})();
