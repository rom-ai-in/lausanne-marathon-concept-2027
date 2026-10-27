#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate import (
  ROOT, LANGS, load, simple_hero, page_partenaires, page_parcours, page_home,
  race_page, ds_urls, ds_band, OFFICIAL, pic, LM_PHOTOS, UNSPLASH
)

def build_finish():
  for lang in LANGS:
    t=load(lang); n=t["nav"]; u=ds_urls(lang)
    d=ROOT/lang; d.mkdir(exist_ok=True)
    (d/"index.html").write_text(page_home(t, lang), encoding="utf-8")
    (d/"parcours.html").write_text(page_parcours(t, lang), encoding="utf-8")
    (d/"partenaires.html").write_text(page_partenaires(t, lang), encoding="utf-8")
    for k in ["marathon","semi","dix","walking"]:
      (d/f"{k}.html").write_text(race_page(t, lang, k), encoding="utf-8")
    rows=""
    for k in ["marathon","semi","dix","walking"]:
      r=t["race_meta"][k]
      rows+=f"<tr><td>{r['name']}</td><td>{r['start']}</td><td>{r['limit']}</td><td><strong>{r['price']}</strong></td></tr>"
    ins = ds_band(t, lang)
    ins += f"""
      <div class="card" style="background:linear-gradient(135deg,#0e2744,#1657d9);color:#fff;border:0">
        <h3 style="margin-top:0;color:#fff">{t["cta_reg"]}</h3>
        <p style="opacity:.9">Datasport OnReg. Pre-registration 2027 on official site; 2026 sold out.</p>
        <a class="btn btn-primary" href="{u["onreg"]}" target="_blank" rel="noopener">Datasport OnReg -></a>
        <a class="btn btn-ghost" href="{u["startlist"]}" target="_blank" rel="noopener">{n["startlist"]} -></a>
      </div>
      <section class="section"><h2>2026</h2>
      <div class="table-wrap"><table><thead><tr><th>Race</th><th>Start</th><th>Limit</th><th>CHF</th></tr></thead><tbody>{rows}</tbody></table></div>
      <div class="grid grid-2" style="margin-top:16px">
        <a class="card" href="transfert.html"><h3>{n["transfert"]}</h3><p>{t["pages"]["transfert"]["lead"]}</p></a>
        <a class="card" href="equipes.html"><h3>{n["equipes"]}</h3><p>{t["pages"]["equipes"]["lead"]}</p></a>
        <a class="card" href="virement.html"><h3>{n["virement"]}</h3><p>{t["pages"]["virement"]["lead"]}</p></a>
        <a class="card" href="podiums.html"><h3>{n["podiums"]}</h3><p>{t["pages"]["podiums"]["lead"]}</p></a>
        <a class="card" href="disqualification.html"><h3>{n["disqualification"]}</h3><p>{t["pages"]["disqualification"]["lead"]}</p></a>
      </div></section>"""
    (d/"inscription.html").write_text(simple_hero(t,lang,"inscription",ins,"lm-02"), encoding="utf-8")
    res = ds_band(t, lang)
    res += f"""
      <div class="grid grid-2">
        <div class="card"><h3>{n["resultats"]} Datasport 2026</h3><p>Official timing.</p>
          <a class="btn btn-blue" style="margin-top:12px" href="{u["results"]}" target="_blank" rel="noopener">Results -></a>
          <a class="btn btn-outline" style="margin-top:12px" href="{u["leaderboard"]}" target="_blank" rel="noopener">Leaderboard -></a>
          <a class="btn btn-outline" style="margin-top:12px" href="{u["course"]}" target="_blank" rel="noopener">Course hub -></a></div>
        <div class="card"><h3>{n["live"]}</h3><p>Datasport live racenr=28110.</p>
          <a class="btn btn-primary" style="margin-top:12px" href="{u["live"]}" target="_blank" rel="noopener">Live -></a>
          <a class="btn btn-outline" style="margin-top:12px" href="{u["startlist"]}" target="_blank" rel="noopener">{n["startlist"]} -></a></div>
        <div class="card"><h3>Alphafoto</h3><p>Runner photos.</p>
          <a class="btn btn-outline" style="margin-top:12px" href="{u["alphafoto"]}" target="_blank" rel="noopener">Alphafoto -></a></div>
        <div class="card"><h3>{n["diploma"]}</h3><p>Diplomas via Datasport account after race (from results).</p>
          <a class="btn btn-outline" style="margin-top:12px" href="{u["results"]}" target="_blank" rel="noopener">Datasport -></a></div>
      </div>
      <p class="sub" style="margin-top:14px">Archives: <a href="https://fr.lausanne-marathon.com/palmares/" target="_blank" rel="noopener">palmares</a></p>"""
    (d/"resultats.html").write_text(simple_hero(t,lang,"resultats",res,"lm-04"), encoding="utf-8")
    hub = ds_band(t, lang)
    hub += f"""
      <div class="card" style="background:var(--ink);color:#fff;border:0">
        <div class="pill" style="background:rgba(255,255,255,.12);color:#fff">{t["exemple"]} Semi 2026</div>
        <h2 style="color:#fff;margin:10px 0 4px">Romain Magnin</h2>
        <p style="opacity:.85">Bib 30370 / 1:56:15,9 (example)</p>
        <p style="margin-top:14px"><a class="btn btn-primary" href="{u["results"]}" target="_blank" rel="noopener">Datasport -></a>
        <a class="btn btn-ghost" href="{u["live"]}" target="_blank" rel="noopener">{n["live"]} -></a></p>
      </div>"""
    (d/"race-hub.html").write_text(simple_hero(t,lang,"racehub",hub,"lm-05"), encoding="utf-8")
    for key in ["sacs","meneurs","vestiaires","massages","recommandations","protection","foodtrucks","podiums","dates","transfert","equipes","virement","disqualification","mentions"]:
      inner=(
        f'<div class="card"><h3>{t["pages"][key]["h1"]}</h3><p>{t["pages"][key]["lead"]}</p>'
        f'<a class="btn btn-primary" style="margin-top:12px" href="{OFFICIAL[key]}" target="_blank" rel="noopener">{t["official_site"]} -></a></div>'
      )
      (d/f"{key}.html").write_text(simple_hero(t,lang,key,inner,"lm-10"), encoding="utf-8")
    (d/"devenir.html").write_text(simple_hero(t,lang,"devenir",f'''
      <div class="devenir-banner"><div><h2>{n["devenir"]}</h2><p>{t["pages"]["devenir"]["lead"]}</p></div>
      <a class="btn btn-gold" href="{OFFICIAL["devenir"]}" target="_blank" rel="noopener">{t["official_site"]} -></a></div>
      <p class="sub" style="margin-top:16px">info@lausanne-marathon.com / +41 21 806 30 16</p>''',"lm-10"), encoding="utf-8")
    (d/"securite.html").write_text(simple_hero(t,lang,"securite",f'''
      <div class="card"><h3>{n["securite"]}</h3><p>{t["pages"]["securite"]["lead"]}</p>
      <p>Partenaire securite officiel: <strong>SOS Surveillance</strong>.</p>
      <a class="btn btn-outline" href="https://www.sos-surveillance.ch/fr" target="_blank" rel="noopener">SOS Surveillance -></a>
      <a class="btn btn-outline" href="partenaires.html">{n["partenaires"]}</a>
      <div class="note" style="margin-top:14px">{t["exemple"]} — no invented medical protocol.</div></div>''',"lm-11"), encoding="utf-8")
    (d/"durabilite.html").write_text(simple_hero(t,lang,"durabilite",
      f'<div class="card"><h3>{n["durabilite"]}</h3><p>{t["pages"]["durabilite"]["lead"]}</p><div class="note" style="margin-top:12px">{t["exemple"]}</div></div>',"lm-09"), encoding="utf-8")
    (d/"accessibilite.html").write_text(simple_hero(t,lang,"accessibilite",
      f'<div class="card"><h3>{n["accessibilite"]}</h3><p>{t["pages"]["accessibilite"]["lead"]}</p><a class="btn btn-outline" style="margin-top:12px" href="acces.html">{n["acces"]}</a><div class="note" style="margin-top:12px">{t["exemple"]}</div></div>',"lm-11"), encoding="utf-8")
    (d/"meteo.html").write_text(simple_hero(t,lang,"meteo",
      f'<div class="card"><h3>{n["meteo"]}</h3><p>{t["pages"]["meteo"]["lead"]}</p><a class="btn btn-blue" style="margin-top:12px" href="https://www.meteosuisse.admin.ch/" target="_blank" rel="noopener">MeteoSuisse -></a><div class="note" style="margin-top:12px">{t["exemple"]}</div></div>',"lm-01"), encoding="utf-8")
    (d/"newsletter.html").write_text(simple_hero(t,lang,"newsletter",
      f'<div class="card"><h3>{n["newsletter"]}</h3><p>{t["pages"]["newsletter"]["lead"]}</p><a class="btn btn-outline" style="margin-top:12px" href="https://fr.lausanne-marathon.com/" target="_blank" rel="noopener">{t["official_site"]} -></a><div class="note" style="margin-top:12px">{t["exemple"]}</div></div>',"lm-02"), encoding="utf-8")
    spec = []
    spec.append('<p class="sub">'+t["pages"]["parcours"].get("spectators_p","")+'</p>')
    spec.append('<div class="grid grid-3">')
    for title, img, blurb in [
      ("Ouchy","lm-05-md.jpg","Lakeside."),
      ("Lutry","lm-04-md.jpg","Lavaux approach."),
      ("Cully / Lavaux","lm-03-md.jpg","Depending on race."),
      ("Vevey / La Tour-de-Peilz","lm-02-md.jpg","Marathon."),
      ("Bellerive","lm-01-md.jpg","Finish."),
    ]:
      spec.append(f'<div class="card media"><img src="../img/photos/{img}" alt=""><div class="body"><h3>{title}</h3><p>{blurb}</p></div></div>')
    spec.append('</div>')
    spec.append(f'<p style="margin-top:14px"><a class="btn btn-blue" href="parcours.html">{n["parcours"]}</a> <a class="btn btn-outline" href="riverains.html">{n["riverains"]}</a></p>')
    (d/"spectateurs.html").write_text(simple_hero(t,lang,"spectateurs","".join(spec),"lm-09"), encoding="utf-8")
    chips="".join('<button type="button" class="chip" onclick="showAnswer(\'%s\')">%s</button>' % (k,label) for k,label in t["chips"])
    info = ds_band(t, lang) if False else ""
    info += '<div class="ask" id="ask"><h3 style="margin-top:0">'+t["home"]["ask_h"]+'</h3>'
    info += '<form onsubmit="askSubmit(event)" style="display:flex;gap:8px;flex-wrap:wrap"><input id="ask-input" type="search" placeholder="'+t["home"]["ask_ph"]+'" style="flex:1;min-width:200px;border:0;border-radius:999px;padding:14px 16px"><button class="btn btn-primary" type="submit">OK</button></form>'
    info += '<div class="chips">'+chips+'</div><div id="ask-answer" class="answer"></div></div>'
    info += '<section class="section"><h2>'+n["runners"]+'</h2><div class="grid grid-3">'
    for key in ["programme","dossards","sacs","acces","meneurs","vestiaires","massages","recommandations","meteo","securite","accessibilite","faq"]:
      info += f'<a class="card" href="{key}.html"><h3>{n[key]}</h3><p>{t["pages"][key]["lead"]}</p></a>'
    info += '</div></section>'
    (d/"infos.html").write_text(simple_hero(t,lang,"infos",info,"lm-12"), encoding="utf-8")
    names=sorted(x.name for x in d.glob("*.html"))
    sm=[]
    for name in names:
      key=name.replace(".html","")
      meta=t["pages"].get(key) or t["pages"].get("racehub" if key=="race-hub" else key) or {"title":key}
      sm.append(f'<a href="{name}">{meta["title"]}</a>')
    sm.append('<a href="plan.html">'+t["pages"]["plan"]["title"]+'</a>')
    (d/"plan.html").write_text(simple_hero(t,lang,"plan",'<div class="sitemap-grid">'+ "".join(sm)+'</div>',"lm-10"), encoding="utf-8")
    print(lang, len(list(d.glob("*.html"))), "pages")

if __name__ == "__main__":
  from generate import build_all
  build_all()
  build_finish()
  print("FINISH OK")
