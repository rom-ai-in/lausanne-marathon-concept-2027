#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
I18N = Path(__file__).resolve().parent / "i18n"
LANGS = ["fr", "de", "en", "it"]
PAGES = [
  "index","marathon","semi","dix","walking","parcours","spectateurs","programme","acces","dossards",
  "sacs","faq","inscription","resultats","photos","race-hub","partenaires","devenir","benevoles",
  "riverains","histoire","organisation","presse","contact","infos","meneurs","vestiaires","massages",
  "recommandations","protection","mentions","foodtrucks","podiums","dates","securite","durabilite",
  "accessibilite","meteo","newsletter","plan","transfert","equipes","virement","disqualification"
]
SPONSORS_DATA = json.loads((ROOT/"data/sponsors.json").read_text(encoding="utf-8"))
DS = json.loads((ROOT/"data/datasport.json").read_text(encoding="utf-8"))
SPONSORS = [i["file"] for t in SPONSORS_DATA.values() if isinstance(t, dict) and "items" in t for i in t["items"]]

LM_PHOTOS = [
  ("lm-01","Photo : Lausanne Marathon"),
  ("lm-02","Photo : Lausanne Marathon"),
  ("lm-03","Photo : Lausanne Marathon"),
  ("lm-04","Photo : Lausanne Marathon"),
  ("lm-05","Photo : Lausanne Marathon"),
  ("lm-09","Photo : Lausanne Marathon"),
]
UNSPLASH = [
  ("u01","Photo : Unsplash"),
  ("u02","Photo : Unsplash"),
  ("u04","Photo : Unsplash"),
  ("u05","Photo : Unsplash"),
  ("u06","Photo : Unsplash"),
  ("u08","Photo : Unsplash"),
]

def load(lang):
  return json.loads((I18N/f"{lang}.json").read_text(encoding="utf-8"))

def href(lang, page):
  return f"{page}.html" if page != "index" else "index.html"

def lang_switch(lang, page):
  items=[]
  for L in LANGS:
    cur=' aria-current="true"' if L==lang else ""
    items.append(f'<a href="../{L}/{href(lang,page) if False else href(L,page)}"{cur}>{L.upper()}</a>'.replace(f'href="../{L}/{href(L,page)}"', f'href="../{L}/{page if page!="index" else "index"}.html"'))
  # fix properly
  items=[]
  for L in LANGS:
    cur=' aria-current="true"' if L==lang else ""
    fn = "index.html" if page=="index" else f"{page}.html"
    items.append(f'<a href="../{L}/{fn}"{cur}>{L.upper()}</a>')
  return "\n".join(items)


def ds_urls(lang):
  base = {"fr":"fr","de":"de","en":"en","it":"it"}[lang]
  return {
    "onreg": DS["onreg"],
    "startlist": DS["startlist"],
    "results": f"https://datasport.com/{base}/results/lausanne-marathon-2026",
    "course": f"https://datasport.com/{base}/course/lausanne-marathon-2026",
    "leaderboard": f"https://datasport.com/{base}/course/lausanne-marathon-2026/leaderboard",
    "live": DS["live"],
    "alphafoto": DS["alphafoto"],
  }

def search_index(t):
  items=[]
  for key, meta in t["pages"].items():
    page = "race-hub" if key=="racehub" else key
    items.append({"t": meta["title"], "k": meta.get("lead",""), "href": ("index.html" if page=="index" else f"{page}.html")})
  for k in ["marathon","semi","dix","walking"]:
    r=t["race_meta"][k]
    items.append({"t": r["name"], "k": r["blurb"], "href": f"{k}.html"})
  return items

NEXT_MAP = {
  "index": ("parcours","inscription"), "marathon": ("parcours","semi"), "semi": ("parcours","marathon"),
  "dix": ("parcours","walking"), "walking": ("parcours","dix"), "parcours": ("spectateurs","programme"),
  "programme": ("dossards","acces"), "acces": ("sacs","programme"), "dossards": ("sacs","inscription"),
  "sacs": ("dossards","vestiaires"), "faq": ("infos","contact"), "inscription": ("resultats","parcours"),
  "resultats": ("photos","race-hub"), "photos": ("resultats","histoire"), "race-hub": ("resultats","programme"),
  "partenaires": ("devenir","benevoles"), "devenir": ("partenaires","contact"), "benevoles": ("partenaires","contact"),
  "riverains": ("spectateurs","acces"), "histoire": ("organisation","resultats"), "organisation": ("contact","histoire"),
  "presse": ("contact","organisation"), "contact": ("organisation","plan"), "infos": ("programme","faq"),
  "meneurs": ("programme","parcours"), "vestiaires": ("sacs","infos"), "massages": ("recommandations","infos"),
  "recommandations": ("massages","infos"), "protection": ("mentions","inscription"), "mentions": ("protection","contact"),
  "foodtrucks": ("contact","partenaires"), "podiums": ("inscription","photos"), "dates": ("programme","inscription"),
  "securite": ("infos","contact"), "durabilite": ("organisation","partenaires"), "accessibilite": ("acces","infos"),
  "meteo": ("programme","infos"), "newsletter": ("contact","index"), "plan": ("index","contact"),
  "spectateurs": ("parcours","riverains"), "transfert": ("inscription","faq"), "equipes": ("inscription","faq"),
  "virement": ("inscription","faq"), "disqualification": ("inscription","protection"),
}

OFFICIAL = {
  "sacs": "https://fr.lausanne-marathon.com/info-coureurs/sacs-coureurs-depot/",
  "meneurs": "https://fr.lausanne-marathon.com/info-coureurs/meneurs-allure/",
  "vestiaires": "https://fr.lausanne-marathon.com/info-coureurs/vestiaires-objets-perdus-objets-de-valeur/",
  "massages": "https://fr.lausanne-marathon.com/info-coureurs/massages/",
  "recommandations": "https://fr.lausanne-marathon.com/info-coureurs/recommandations-physiques/",
  "protection": "https://fr.lausanne-marathon.com/info-coureurs/protection-des-donnees/",
  "devenir": "https://fr.lausanne-marathon.com/sponsors/devenez-sponsors-2025/",
  "foodtrucks": "https://fr.lausanne-marathon.com/contact/contact-stands-foodtrucks/",
  "podiums": "https://fr.lausanne-marathon.com/inscription/podiums-prix-cadeaux/",
  "dates": "https://fr.lausanne-marathon.com/conseils/dates-de-levenement/",
  "transfert": "https://fr.lausanne-marathon.com/inscription/transfert-de-dossard-changement-de-distance/",
  "equipes": "https://fr.lausanne-marathon.com/inscription/inscription-en-groupe/",
  "virement": "https://fr.lausanne-marathon.com/inscription/inscription-par-virement/",
  "disqualification": "https://fr.lausanne-marathon.com/inscription/disqualification-controle-antidopage/",
  "mentions": "https://fr.lausanne-marathon.com/contact/mentions-legales/",
}

def breadcrumb(t, page):
  if page=="index": return ""
  n=t["nav"]
  return f'<nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">{n["home"]}</a><span>›</span><strong>{n.get(page, t["pages"].get(page, t["pages"].get("racehub" if page=="race-hub" else page, {})).get("title", page))}</strong></nav>'

def next_nav(t, page):
  pair=NEXT_MAP.get(page)
  if not pair: return ""
  cards=[]
  for pkey, lbl in zip(pair, ["related","next"]):
    meta=t["pages"].get(pkey) or t["pages"].get("racehub" if pkey=="race-hub" else pkey) or {"title":pkey,"lead":""}
    href = "index.html" if pkey=="index" else f"{pkey}.html"
    cards.append(f'<a href="{href}"><div class="lbl">{t["nav"].get(lbl,lbl)}</div><strong>{meta["title"]}</strong><div style="color:var(--muted);font-size:13px;margin-top:4px">{meta.get("lead","")[:110]}</div></a>')
  return f'<div class="next-nav">{"".join(cards)}</div>'

def presented_hero(t):
  gm=SPONSORS_DATA["presenting"]["items"][0]
  return f'<a class="presented-hero" href="{gm["url"]}" target="_blank" rel="noopener"><span>{t["nav"]["presented_by"]}</span><img src="../img/sponsors/{gm["file"]}" alt="{gm["name"]}"></a>'

def ds_band(t, lang):
  u=ds_urls(lang); n=t["nav"]
  return (
    '<div class="ds-band">'
    f'<div><h3>{n["datasport"]}</h3><p>Inscription / resultats / live</p></div>'
    f'<a href="{u["onreg"]}" target="_blank" rel="noopener">{t["cta_reg_short"]} -></a>'
    f'<a href="{u["results"]}" target="_blank" rel="noopener">{n["resultats"]} -></a>'
    f'<a href="{u["live"]}" target="_blank" rel="noopener">{n["live"]} -></a>'
    '</div>'
  )

def sponsor_cards(tier_key, cols="cols-4"):
  tier=SPONSORS_DATA[tier_key]
  cards=[]
  for it in tier["items"]:
    cards.append(
      f'<a class="sponsor-card" href="{it["url"]}" target="_blank" rel="noopener">'
      f'<img src="../img/sponsors/{it["file"]}" alt="{it["name"]}" loading="lazy">'
      f'<span class="name">{it["name"]}</span></a>'
    )
  return "\n".join(cards), tier["title"], cols

def sponsor_strip_html():
  items=[]
  for key in ["presenting","principaux","sponsors"]:
    for it in SPONSORS_DATA[key]["items"]:
      items.append(f'<a href="{it["url"]}" target="_blank" rel="noopener" title="{it["name"]}"><img src="../img/sponsors/{it["file"]}" alt="{it["name"]}"></a>')
  return "".join(items[:12])


def header(t, lang, page):
  n=t["nav"]
  active=lambda p: ' class="active"' if page==p else ""
  gm=SPONSORS_DATA["presenting"]["items"][0]
  u=ds_urls(lang)
  return f"""<div class="disclaimer">{t["disclaimer"]}</div>
<header class="header"><div class="header-inner">
  <a class="logo" href="index.html" aria-label="Lausanne Marathon"><img src="../img/logo/logo-officiel.jpg" alt="Lausanne Marathon" width="250" height="135"></a>
  <a class="presented-by" href="{gm["url"]}" target="_blank" rel="noopener" title="{gm["name"]}">
    <span>{n["presented_by"]}</span><img src="../img/sponsors/{gm["file"]}" alt="{gm["name"]}">
  </a>
  <nav class="nav-desk" aria-label="Main">
    <a href="index.html"{active("index")}>{n["home"]}</a>
    <div class="item"><a href="parcours.html">{n["races"]}</a>
      <div class="mega">
        <a class="mega-vis" href="parcours.html"><img src="../img/photos/lm-09-md.jpg" alt=""><div class="cap"><strong>{n["parcours"]}</strong><span>Map / aid / GPX</span></div></a>
        <div>
          <h4>{n["races"]}</h4>
          <a href="marathon.html">{n["marathon"]}<small>42,195 km</small></a>
          <a href="semi.html">{n["semi"]}<small>21,0975 km</small></a>
          <a href="dix.html">{n["dix"]}<small>10 km</small></a>
          <a href="walking.html">{n["walking"]}<small>10 km</small></a>
        </div>
        <div>
          <h4>{n["more"]}</h4>
          <a href="parcours.html">{n["parcours"]}</a>
          <a href="spectateurs.html">{n["spectateurs"]}</a>
          <a href="meneurs.html">{n["meneurs"]}</a>
          <a href="podiums.html">{n["podiums"]}</a>
        </div>
      </div>
    </div>
    <div class="item"><a href="infos.html">{n["runners"]}</a>
      <div class="mega">
        <a class="mega-vis" href="programme.html"><img src="../img/photos/lm-12-md.jpg" alt=""><div class="cap"><strong>{n["programme"]}</strong></div></a>
        <div>
          <h4>{n["runners"]}</h4>
          <a href="programme.html">{n["programme"]}</a>
          <a href="dossards.html">{n["dossards"]}</a>
          <a href="sacs.html">{n["sacs"]}</a>
          <a href="acces.html">{n["acces"]}</a>
          <a href="faq.html">{n["faq"]}</a>
        </div>
        <div>
          <h4>{n["more"]}</h4>
          <a href="vestiaires.html">{n["vestiaires"]}</a>
          <a href="massages.html">{n["massages"]}</a>
          <a href="recommandations.html">{n["recommandations"]}</a>
          <a href="meteo.html">{n["meteo"]}</a>
          <a href="securite.html">{n["securite"]}</a>
          <a href="accessibilite.html">{n["accessibilite"]}</a>
        </div>
      </div>
    </div>
    <a href="inscription.html"{active("inscription")}>{n["inscription"]}</a>
    <div class="item"><a href="resultats.html">{n["resultats"]}</a>
      <div class="drop">
        <a href="resultats.html">{n["resultats"]}<small>Datasport</small></a>
        <a href="photos.html">{n["photos"]}<small>Alphafoto</small></a>
        <a href="race-hub.html">{n["racehub"]}</a>
        <a href="{u["live"]}" target="_blank" rel="noopener">{n["live"]}<small>Datasport</small></a>
        <a href="{u["startlist"]}" target="_blank" rel="noopener">{n["startlist"]}<small>Datasport</small></a>
      </div>
    </div>
    <div class="item"><a href="partenaires.html">{n["community"]}</a>
      <div class="mega">
        <a class="mega-vis" href="partenaires.html"><img src="../img/photos/lm-10-md.jpg" alt=""><div class="cap"><strong>{n["partenaires"]}</strong></div></a>
        <div>
          <h4>{n["community"]}</h4>
          <a href="partenaires.html">{n["partenaires"]}</a>
          <a href="devenir.html">{n["devenir"]}</a>
          <a href="benevoles.html">{n["benevoles"]}</a>
          <a href="riverains.html">{n["riverains"]}</a>
        </div>
        <div>
          <h4>{n["more"]}</h4>
          <a href="foodtrucks.html">{n["foodtrucks"]}</a>
          <a href="durabilite.html">{n["durabilite"]}</a>
          <a href="newsletter.html">{n["newsletter"]}</a>
        </div>
      </div>
    </div>
    <div class="item"><a href="organisation.html">{n["about"]}</a>
      <div class="drop">
        <a href="histoire.html">{n["histoire"]}</a>
        <a href="organisation.html">{n["organisation"]}</a>
        <a href="dates.html">{n["dates"]}</a>
        <a href="presse.html">{n["presse"]}</a>
        <a href="contact.html">{n["contact"]}</a>
        <a href="mentions.html">{n["mentions"]}</a>
        <a href="protection.html">{n["protection"]}</a>
        <a href="plan.html">{n["plan"]}</a>
      </div>
    </div>
  </nav>
  <div class="header-actions">
    <button class="search-btn" id="searchOpen" type="button" aria-label="{n["search"]}">&#8981;</button>
    <details class="lang"><summary>{lang.upper()}</summary><div class="lang-menu">{lang_switch(lang,page)}</div></details>
    <a class="btn btn-primary btn-sm" href="inscription.html">{t["cta_reg_short"]}</a>
    <button class="menu-toggle" id="menuOpen" type="button" aria-label="Menu" aria-expanded="false"><span></span></button>
  </div>
</div></header>
<div class="drawer" id="drawer"><div class="drawer-panel">
  <div class="drawer-head"><strong>Menu</strong><button class="btn btn-outline btn-sm" id="menuClose" type="button">&#10005;</button></div>
  <nav>
    <a href="index.html">{n["home"]}</a>
    <div class="sub">
      <a href="marathon.html">{n["marathon"]}</a>
      <a href="semi.html">{n["semi"]}</a>
      <a href="dix.html">{n["dix"]}</a>
      <a href="walking.html">{n["walking"]}</a>
      <a href="parcours.html">{n["parcours"]}</a>
      <a href="spectateurs.html">{n["spectateurs"]}</a>
    </div>
    <a href="programme.html">{n["programme"]}</a>
    <a href="infos.html">{n["infos"]}</a>
    <a href="dossards.html">{n["dossards"]}</a>
    <a href="sacs.html">{n["sacs"]}</a>
    <a href="faq.html">{n["faq"]}</a>
    <a href="inscription.html">{n["inscription"]}</a>
    <a href="resultats.html">{n["resultats"]}</a>
    <a href="photos.html">{n["photos"]}</a>
    <a href="race-hub.html">{n["racehub"]}</a>
    <a href="partenaires.html">{n["partenaires"]}</a>
    <a href="devenir.html">{n["devenir"]}</a>
    <a href="benevoles.html">{n["benevoles"]}</a>
    <a href="riverains.html">{n["riverains"]}</a>
    <a href="histoire.html">{n["histoire"]}</a>
    <a href="organisation.html">{n["organisation"]}</a>
    <a href="presse.html">{n["presse"]}</a>
    <a href="contact.html">{n["contact"]}</a>
    <a href="plan.html">{n["plan"]}</a>
  </nav>
  <div class="drawer-cta">
    <a class="btn btn-primary" href="{u["onreg"]}" target="_blank" rel="noopener">{t["cta_reg"]} Datasport</a>
    <div class="lang-menu" style="position:static;box-shadow:none;border:0;display:flex;gap:6px;flex-wrap:wrap">{lang_switch(lang,page)}</div>
  </div>
</div></div>
<div class="search-overlay" id="searchOverlay" role="dialog" aria-label="{n["search"]}">
  <div class="search-panel">
    <input id="searchInput" type="search" placeholder="{n["search"]}..." autocomplete="off">
    <div class="search-hits" id="searchHits"></div>
  </div>
</div>"""

def footer(t, lang):
  n=t["nav"]
  strip=sponsor_strip_html()
  u=ds_urls(lang)
  return f"""<div class="sponsor-strip"><div class="sponsor-strip-inner">
  <div class="lbl">{n["partenaires"]} / {SPONSORS_DATA["presenting"]["title"]}</div>
  <div class="sponsor-strip-track">{strip}</div>
  <p style="text-align:center;margin:14px 0 0"><a href="partenaires.html" style="color:#fff;font-weight:750">{n["partenaires"]} -></a>
  / <a href="devenir.html" style="color:#fff;font-weight:750">{n["devenir"]} -></a></p>
</div></div>
<footer class="footer"><div class="footer-inner">
  <div><h4>Lausanne Marathon</h4>Association - Av. de Rhodanie 54<br>1007 Lausanne - Suisse<br>Tel. +41 21 806 30 16<br><a href="mailto:info@lausanne-marathon.com">info@lausanne-marathon.com</a>
  <div class="socials">
    <a href="https://www.facebook.com/LausanneMarathon" target="_blank" rel="noopener">Facebook</a>
    <a href="https://www.instagram.com/lausanne_marathon/" target="_blank" rel="noopener">Instagram</a>
  </div>
  </div>
  <div><h4>{n["races"]}</h4><a href="marathon.html">{n["marathon"]}</a><br><a href="semi.html">{n["semi"]}</a><br><a href="dix.html">{n["dix"]}</a><br><a href="parcours.html">{n["parcours"]}</a><br><a href="spectateurs.html">{n["spectateurs"]}</a></div>
  <div><h4>{n["runners"]}</h4><a href="infos.html">{n["infos"]}</a><br><a href="inscription.html">{n["inscription"]}</a><br><a href="resultats.html">{n["resultats"]}</a><br><a href="faq.html">{n["faq"]}</a><br><a href="sacs.html">{n["sacs"]}</a></div>
  <div><h4>{n["about"]}</h4><a href="organisation.html">{n["organisation"]}</a><br><a href="partenaires.html">{n["partenaires"]}</a><br><a href="plan.html">{n["footer_sitemap"]}</a><br><a href="contact.html">{n["contact"]}</a><br>
  <a href="../fr/index.html">FR</a> / <a href="../de/index.html">DE</a> / <a href="../en/index.html">EN</a> / <a href="../it/index.html">IT</a><br>
  <a href="https://fr.lausanne-marathon.com/" target="_blank" rel="noopener">{t["official_site"]} -></a></div>
  <div class="legal">{t["footer_legal"]}<br>{t["footer_photo_lm"]} {t["footer_photo_unsplash"]}</div>
</div></footer>
<nav class="bottom" aria-label="Mobile">
  <a href="index.html"><span>&#127968;</span>{t["bottom"]["home"]}</a>
  <a href="parcours.html"><span>&#128506;</span>{t["bottom"]["parcours"]}</a>
  <a href="infos.html"><span>&#8505;</span>{t["bottom"]["infos"]}</a>
  <a href="inscription.html"><span>&#127915;</span>{t["bottom"]["insc"]}</a>
  <a href="partenaires.html"><span>&#10022;</span>{n["partenaires"]}</a>
</nav>
<div class="cta-rail"><a class="btn btn-primary btn-sm" href="{u["onreg"]}" target="_blank" rel="noopener">{t["cta_reg_short"]} Datasport</a></div>"""

def shell(t, lang, page, title, body, extra_head="", extra_js=""):
  return f"""<!DOCTYPE html>
<html lang="{t["html_lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow, noarchive">
<meta name="description" content="{t["disclaimer"]}">
<title>{title} · Lausanne Marathon</title>
<link rel="icon" href="../img/logo/logo-officiel.jpg">
<link rel="stylesheet" href="../assets/css/main.css">
{extra_head}
</head>
<body>
<div class="site">
{header(t, lang, page)}
{breadcrumb(t, page)}
{body}
<div class="wrap" style="padding-top:0">{next_nav(t, page)}</div>
{footer(t, lang)}
</div>
<script>
window.LM_ANSWERS={json.dumps({k:{**v,"tag":t["answers_tag"],"srcLabel":t["srcLabel"]} for k,v in t["answers"].items()}, ensure_ascii=False)};
window.LM_STARTS={json.dumps(t["starts"])};
window.LM_SEARCH={json.dumps(search_index(t), ensure_ascii=False)};
</script>
<script src="../assets/js/app.js"></script>
{extra_js}
</body></html>"""

def pic(name, size="md", folder="photos", credit=""):
  base = f"../img/{folder}/{name}"
  if folder=="photos":
    return f'<picture><source srcset="{base}-{size}.webp" type="image/webp"><img src="{base}-{size}.jpg" alt="" loading="lazy"></picture>'
  return f'<picture><source srcset="{base}.webp" type="image/webp"><img src="{base}.jpg" alt="" loading="lazy"></picture>'

def race_page(t, lang, key):
  r=t["race_meta"][key]
  u=ds_urls(lang)
  hero = "lm-03" if key=="marathon" else ("lm-01" if key=="semi" else "lm-05")
  body=f"""
<section class="hero compact"><img class="bg" src="../img/photos/{hero}-lg.jpg" alt=""><div class="veil"></div>
<div class="hero-inner">{presented_hero(t)}
<div class="eyebrow">{r["dist"]} · {r["start"]}</div>
<h1>{r["name"]}</h1><p class="lead">{r["blurb"]}</p>
<div class="hero-actions">
  <a class="btn btn-primary" href="{u["onreg"]}" target="_blank" rel="noopener">{t["cta_reg"]} Datasport</a>
  <a class="btn btn-ghost" href="parcours.html">{t["nav"]["parcours"]}</a>
</div>
<p class="credit">Photo : Lausanne Marathon</p></div></section>
<div class="wrap">
  <div class="stat-row section">
    <div class="stat"><strong>{r["dist"]}</strong><span>Distance</span></div>
    <div class="stat"><strong>{r["start"]}</strong><span>Start 2026</span></div>
    <div class="stat"><strong>{r["deniv"]}</strong><span>D+ / D- ({r["deniv_src"]})</span></div>
    <div class="stat"><strong>{r["price"]}</strong><span>CHF 2026</span></div>
  </div>
  {ds_band(t, lang)}
  <section class="section"><h2>{t["indicatif"]}</h2>
  <p class="sub">{r["route"]}</p>
  <p><a class="btn btn-blue" href="parcours.html">{t["home"].get("open_map","Map")}</a></p>
  <div class="note" style="margin-top:14px">{t["pages"]["parcours"]["note_map"]}</div>
  </section>
</div>"""
  return shell(t, lang, key if key!="walking" else "walking", r["name"], body)

def page_parcours(t, lang):
  p=t["pages"]["parcours"]
  body=f"""
<section class="hero compact"><img class="bg" src="../img/photos/lm-09-lg.jpg" alt=""><div class="veil"></div>
<div class="hero-inner">{presented_hero(t)}
<div class="eyebrow">{t["indicatif"]}</div><h1>{p["h1"]}</h1><p class="lead">{p["lead"]}</p>
<p class="credit">Photo : Lausanne Marathon</p></div></section>
<div class="wrap">
  <div class="map-shell fullscreen-mobile section map-stage">
    <div class="map-toolbar">
      <button type="button" class="active" data-course="semi">{t["nav"]["semi"]}</button>
      <button type="button" data-course="marathon">{t["nav"]["marathon"]}</button>
      <button type="button" data-course="dix">{t["nav"]["dix"]}</button>
      <span style="margin-left:auto;font-weight:700" id="map-course-label"></span>
    </div>
    <div id="route-map"></div>
    <div class="elev-wrap">
      <div class="elev-meta"><span id="elev-km">Km -</span><span id="elev-alt">- m</span></div>
      <div class="elev-chart" aria-label="Elevation"><svg id="elev-svg" viewBox="0 0 640 100" preserveAspectRatio="none"></svg><div class="elev-tip" id="elev-tip"></div></div>
    </div>
    <div class="map-note" id="map-note">{p["note_map"]}</div>
  </div>
  <div class="legend">
    <span><i style="background:#0f9d58"></i> Start</span>
    <span><i style="background:#ff5a1f"></i> Finish</span>
    <span><i style="background:#1aa7ff"></i> {t["nav"]["aid"]}</span>
    <span><i style="background:#e8b23a"></i> Waypoints</span>
    <span><i style="background:#0b1c33"></i> Km</span>
  </div>
  <div class="stat-row">
    <div class="stat"><strong id="meta-dist">-</strong><span>Distance</span></div>
    <div class="stat"><strong id="meta-deniv">-</strong><span>D+ / D-</span></div>
    <div class="stat"><strong id="meta-start">-</strong><span>Start 2026</span></div>
    <div class="stat"><strong>OSM</strong><span>{t["indicatif"]}</span></div>
  </div>
  <p style="margin:16px 0"><a class="btn btn-outline" id="gpx-link" href="../data/gpx/semi-indicatif.gpx" download>{t["nav"]["gpx"]}</a>
  <a class="btn btn-blue" href="spectateurs.html">{t["nav"]["spectateurs"]}</a></p>
  <section class="section"><h2>{t["nav"]["places"]}</h2>
    <div class="place-rail" id="place-rail"></div>
  </section>
  <section class="section"><h2>{t["nav"]["aid"]}</h2>
    <p class="sub">{p.get("no_sponge","")}</p>
    <div class="aid-list" id="aid-list"></div>
  </section>
  <section class="section"><h2>{p.get("spectators_h", t["nav"]["spectateurs"])}</h2>
    <p class="sub">{p.get("spectators_p","")}</p>
    <a class="btn btn-outline" href="spectateurs.html">{t["nav"]["spectateurs"]} -></a>
    <a class="btn btn-outline" href="riverains.html">{t["nav"]["riverains"]} -></a>
  </section>
</div>"""
  head='<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">'
  js='<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script><script src="../assets/js/map.js"></script>'
  return shell(t, lang, "parcours", p["title"], body, head, js)

def page_home(t, lang):
  h=t["home"]; n=t["nav"]; u=ds_urls(lang)
  races="".join(
    f'<a class="card race-card" href="{k}.html"><div class="body" style="padding:0"><h3>{t["race_meta"][k]["name"]}</h3><p>{t["race_meta"][k]["blurb"]}</p><div class="meta"><span class="pill">{t["race_meta"][k]["dist"]}</span><span class="pill orange">{t["race_meta"][k]["start"]}</span><span class="pill gold">CHF {t["race_meta"][k]["price"]}</span></div></div></a>'
    for k in ["marathon","semi","dix","walking"]
  )
  chips="".join(f'<button type="button" class="chip" onclick="showAnswer(\'{k}\')">{label}</button>' for k,label in t["chips"])
  gal="".join(f'<figure>{pic(name,"md")}<figcaption>{credit}</figcaption></figure>' for name,credit in LM_PHOTOS[:6])
  uns="".join(f'<figure><picture><source srcset="../img/unsplash/{name}.webp" type="image/webp"><img src="../img/unsplash/{name}.jpg" alt="" loading="lazy"></picture><figcaption>{credit}</figcaption></figure>' for name,credit in UNSPLASH)
  cards_p,_,_=sponsor_cards("presenting")
  cards_pr,_,_=sponsor_cards("principaux")
  body=f"""
<section class="hero"><img class="bg" src="../img/photos/lm-01-lg.jpg" alt=""><div class="veil"></div>
<div class="hero-inner">
  {presented_hero(t)}
  <div class="eyebrow">{h["eyebrow"]}</div>
  <h1>{h["h1"]}</h1>
  <p class="lead">{h["lead"]}</p>
  <div class="countdown" id="countdown">
    <div><strong data-n>--</strong><span>{h["cd_d"]}</span></div>
    <div><strong data-n>--</strong><span>{h["cd_h"]}</span></div>
    <div><strong data-n>--</strong><span>{h["cd_m"]}</span></div>
    <div><strong data-n>--</strong><span>{h["cd_s"]}</span></div>
  </div>
  <div class="hero-actions">
    <a class="btn btn-primary" href="{u["onreg"]}" target="_blank" rel="noopener">{t["cta_reg"]} Datasport</a>
    <a class="btn btn-ghost" href="parcours.html">{h["cta_parcours"]}</a>
    <a class="btn btn-ghost" href="race-hub.html">{h["cta_hub"]}</a>
  </div>
  <p class="credit">Photo : Lausanne Marathon</p>
</div></section>
<div class="wrap">
  {ds_band(t, lang)}
  <div class="stat-row section">
    <div class="stat"><strong>24.10.2027</strong><span>Date</span></div>
    <div class="stat"><strong>2026</strong><span>Sold out</span></div>
    <div class="stat"><strong>4</strong><span>{n["races"]}</span></div>
    <div class="stat"><strong>Bellerive</strong><span>Finish</span></div>
  </div>
  <section class="section"><h2>{h["races_h"]}</h2><p class="sub">{h["races_sub"]}</p><div class="grid grid-2">{races}</div></section>
  <section class="section"><div class="ask" id="ask"><h3 style="margin-top:0">{h["ask_h"]}</h3><p style="opacity:.9">{h["ask_p"]}</p>
    <form onsubmit="askSubmit(event)" style="display:flex;gap:8px;flex-wrap:wrap"><input id="ask-input" type="search" placeholder="{h["ask_ph"]}" style="flex:1;min-width:200px;border:0;border-radius:999px;padding:14px 16px"><button class="btn btn-primary" type="submit">{h["ask_ok"]}</button></form>
    <div class="chips">{chips}</div><div id="ask-answer" class="answer"></div>
  </div></section>
  <section class="section"><h2>{h["feat_h"]}</h2><p class="sub">{h["feat_sub"]}</p>
    <div class="grid grid-3">
      <a class="card" href="parcours.html"><h3>{n["parcours"]}</h3><p>{t["pages"]["parcours"]["lead"]}</p></a>
      <a class="card" href="programme.html"><h3>{n["programme"]}</h3><p>{t["pages"]["programme"]["lead"]}</p></a>
      <a class="card" href="partenaires.html"><h3>{n["partenaires"]}</h3><p>{t["pages"]["partenaires"]["lead"]}</p></a>
    </div>
  </section>
  <section class="section"><h2>{h["gallery_h"]}</h2><p class="sub">{h["gallery_sub"]}</p>
    <div class="gallery">{gal}{uns}</div>
    <p style="margin-top:12px"><a class="btn btn-outline" href="photos.html">{n["photos"]}</a></p>
  </section>
  <section class="section"><h2>{h["sponsors_h"]}</h2>
    <section class="tier tier-presenting" style="margin-bottom:16px"><div class="tier-head"><h2>{SPONSORS_DATA["presenting"]["title"]}</h2><span class="tier-badge">{SPONSORS_DATA["presenting"]["title"]}</span></div>
    <div class="sponsor-cards cols-2">{cards_p}</div></section>
    <div class="sponsor-cards cols-4" style="margin-bottom:12px">{cards_pr}</div>
    <p><a class="btn btn-blue" href="partenaires.html">{n["partenaires"]} -></a>
    <a class="btn btn-outline" href="devenir.html">{n["devenir"]}</a></p>
  </section>
</div>"""
  return shell(t, lang, "index", h["title"], body)

def page_partenaires(t, lang):
  p=t["pages"]["partenaires"]
  tiers=[]
  order=[
    ("presenting","tier-presenting","cols-2"),
    ("patronage","","cols-4"),
    ("communes","","cols-6"),
    ("principaux","tier-principaux","cols-4"),
    ("sponsors","","cols-4"),
    ("partenaires","","cols-5"),
    ("medias","","cols-5"),
  ]
  for key, klass, cols in order:
    cards, title, _ = sponsor_cards(key, cols)
    tiers.append(f"""<section class="tier {klass}" id="tier-{key}">
      <div class="tier-head"><h2>{title}</h2><span class="tier-badge">{title}</span></div>
      <div class="sponsor-cards {cols}">{cards}</div>
    </section>""")
  body=f"""
<section class="hero compact"><img class="bg" src="../img/photos/lm-10-lg.jpg" alt=""><div class="veil"></div>
<div class="hero-inner">{presented_hero(t)}
<h1>{p["h1"]}</h1><p class="lead">{p["lead"]}</p>
<p class="credit">Photo : Lausanne Marathon</p></div></section>
<div class="wrap">
  {"".join(tiers)}
  <div class="devenir-banner">
    <div><h2>{t["nav"]["devenir"]}</h2><p>{t["pages"]["devenir"]["lead"]}</p></div>
    <div style="display:flex;gap:10px;flex-wrap:wrap">
      <a class="btn btn-gold" href="devenir.html">{t["nav"]["devenir"]}</a>
      <a class="btn btn-ghost" href="{OFFICIAL["devenir"]}" target="_blank" rel="noopener">{t["official_site"]} -></a>
    </div>
  </div>
  <p class="sub" style="margin-top:18px">Source: <a href="https://fr.lausanne-marathon.com/sponsors/" target="_blank" rel="noopener">fr.lausanne-marathon.com/sponsors</a></p>
</div>"""
  return shell(t, lang, "partenaires", p["title"], body)

def simple_hero(t, lang, page_key, inner_html, img="lm-10"):
  p=t["pages"][page_key]
  body=f'''<section class="hero compact"><img class="bg" src="../img/photos/{img}-lg.jpg" alt=""><div class="veil"></div>
  <div class="hero-inner"><h1>{p["h1"]}</h1><p class="lead">{p["lead"]}</p><p class="credit">Photo : Lausanne Marathon</p></div></section>
  <div class="wrap">{inner_html}</div>'''
  return shell(t, lang, page_key if page_key!="racehub" else "race-hub", p["title"], body)

def build_all():
  for lang in LANGS:
    t=load(lang)
    d=ROOT/lang
    d.mkdir(exist_ok=True)
    pages = {
      "index.html": page_home(t, lang),
      "parcours.html": page_parcours(t, lang),
      "marathon.html": race_page(t, lang, "marathon"),
      "semi.html": race_page(t, lang, "semi"),
      "dix.html": race_page(t, lang, "dix"),
      "walking.html": race_page(t, lang, "walking"),
    }
    # programme
    tl="".join(f'<div class="t"><strong>{a}</strong><h3 style="margin:4px 0">{b}</h3><p style="margin:0;color:var(--muted)">{c}</p></div>' for a,b,c in t["programme"])
    pages["programme.html"]=simple_hero(t,lang,"programme",f'<div class="timeline">{tl}</div><div class="note">Sources: Départs–Horaires, Retrait dossards (édition 2026).</div>',"lm-12")
    # acces
    pages["acces.html"]=simple_hero(t,lang,"acces",'''
      <div class="grid grid-2">
        <div class="card"><h3>Start · Place de Milan</h3><p>Lausanne. All race starts (official schedules 2026).</p></div>
        <div class="card"><h3>Finish · Bellerive Plage</h3><p>Place / esplanade de Bellerive Plage.</p></div>
        <div class="card"><h3>Bib & Expo</h3><p>Salle Auguste Piccard, Ch. de Bellerive 36, 1007 Lausanne.</p></div>
        <div class="card"><h3>Public transport</h3><p>Example guidance: prefer tl / CFF. Confirm race-day notices on the official site.</p></div>
      </div>''',"lm-11")
    # dossards
    pages["dossards.html"]=simple_hero(t,lang,"dossards",'''
      <div class="grid grid-3">
        <div class="card"><h3>Fri</h3><p>15:00–18:00</p></div>
        <div class="card"><h3>Sat</h3><p>11:00–18:00</p></div>
        <div class="card"><h3>Sun</h3><p>07:00–14:00</p></div>
      </div>
      <div class="note" style="margin-top:14px">Source: Retrait des dossards (2026). Bring the email/SMS with bib number. Home delivery option via Datasport (+ CHF 5.–, Swiss address).</div>
      <p style="margin-top:14px"><a class="btn btn-outline" href="https://fr.lausanne-marathon.com/info-coureurs/retrait-des-dossards-sur-place-le-23-24-et-25-octobre/" target="_blank" rel="noopener">Official page →</a></p>''',"lm-12")
    # faq
    faq="".join(f'<details><summary>{q}</summary><p>{a}<br><a href="{s}" target="_blank" rel="noopener">Source →</a></p></details>' for q,a,s in t["faq"])
    pages["faq.html"]=simple_hero(t,lang,"faq",f'<div class="faq">{faq}</div>',"lm-10")
    # inscription
    rows=""
    for k in ["marathon","semi","dix","walking"]:
      r=t["race_meta"][k]
      rows+=f"<tr><td>{r['name']}</td><td>{r['start']}</td><td>{r['limit']}</td><td><strong>{r['price']}</strong></td></tr>"
    pages["inscription.html"]=simple_hero(t,lang,"inscription",f'''
      <div class="card" style="background:linear-gradient(135deg,#0e2744,#163a63);color:#fff;border:0">
        <h3 style="margin-top:0;color:#fff">{t["cta_reg"]}</h3>
        <p style="opacity:.9">Official site: pre-registration for 2027 is open. 2026 is sold out.</p>
        <a class="btn btn-primary" href="https://fr.lausanne-marathon.com/" target="_blank" rel="noopener">{t["official_site"]} →</a>
      </div>
      <section class="section"><h2>2026 fees</h2>
      <div class="table-wrap"><table><thead><tr><th>Race</th><th>Start</th><th>Limit</th><th>CHF</th></tr></thead><tbody>{rows}</tbody></table></div>
      <div class="note" style="margin-top:12px">Sources: Prix &amp; Catégories · Départs–Horaires. Semi time limit: 3h30 on Prices page / 4h00 on Time-limit page. Nordic: 14h32 (Prices) / from 14h33 (Starts).</div>
      </section>''',"lm-02")
    # resultats
    pages["resultats.html"]=simple_hero(t,lang,"resultats",'''
      <div class="grid grid-2">
        <div class="card"><h3>Datasport results</h3><p>Official timing and rankings.</p>
          <a class="btn btn-blue" style="margin-top:12px" href="https://datasport.com/fr/results/lausanne-marathon-2026" target="_blank" rel="noopener">Datasport 2026 →</a></div>
        <div class="card"><h3>Alphafoto</h3><p>Runner photos (external).</p>
          <a class="btn btn-outline" style="margin-top:12px" href="https://www.alphafoto.com/event.php?l=fr&eventID=2064" target="_blank" rel="noopener">Alphafoto →</a></div>
      </div>''',"lm-04")
    # photos
    gal="".join(f'<figure>{pic(n,"md")}<figcaption>{c}</figcaption></figure>' for n,c in LM_PHOTOS)
    uns="".join(f'<figure><picture><source srcset="../img/unsplash/{n}.webp" type="image/webp"><img src="../img/unsplash/{n}.jpg" alt="" loading="lazy"></picture><figcaption>{c}</figcaption></figure>' for n,c in UNSPLASH)
    pages["photos.html"]=simple_hero(t,lang,"photos",f'<div class="gallery">{gal}{uns}</div><p style="margin-top:16px"><a class="btn btn-primary" href="https://www.alphafoto.com/event.php?l=fr&eventID=2064" target="_blank" rel="noopener">Alphafoto →</a></p>',"lm-03")
    # race hub
    pages["race-hub.html"]=simple_hero(t,lang,"racehub",f'''
      <div class="card" style="background:var(--ink);color:#fff;border:0">
        <div class="pill" style="background:rgba(255,255,255,.12);color:#fff">{t["exemple"]} · Semi 2026</div>
        <h2 style="color:#fff;margin:10px 0 4px">Romain Magnin</h2>
        <p style="opacity:.85">Bib 30370 · 1:56:15,9 (example runner data)</p>
        <div class="stat-row" style="margin-top:14px">
          <div class="stat"><strong style="color:var(--ink)">{t["starts"]["semi"]}</strong><span>Start</span></div>
          <div class="stat"><strong style="color:var(--ink)">21,1 km</strong><span>Distance</span></div>
        </div>
      </div>
      <section class="section" id="checklist"><h2>Checklist</h2>
        <label class="card" style="display:block;margin-bottom:8px"><input type="checkbox" checked> Start time confirmed</label>
        <label class="card" style="display:block;margin-bottom:8px"><input type="checkbox"> Bag drop at Bellerive</label>
        <label class="card" style="display:block;margin-bottom:8px"><input type="checkbox"> Route to Place de Milan</label>
      </section>''',"lm-05")
    # partenaires
    pages["partenaires.html"]=page_partenaires(t, lang)
    pages["benevoles.html"]=simple_hero(t,lang,"benevoles",'''
      <div class="card"><h3>Join the team</h3><p>Contact the organisation via the official contact page to volunteer.</p>
      <a class="btn btn-primary" style="margin-top:12px" href="https://fr.lausanne-marathon.com/contact/contact/" target="_blank" rel="noopener">Official contact →</a></div>''',"lm-06")
    pages["riverains.html"]=simple_hero(t,lang,"riverains",'''
      <div class="grid grid-2">
        <a class="card" href="https://fr.lausanne-marathon.com/conseils/informations-aux-riverains/secteur-lausanne/" target="_blank" rel="noopener"><h3>Lausanne</h3><p>Official sector page →</p></a>
        <a class="card" href="https://fr.lausanne-marathon.com/conseils/informations-aux-riverains/secteur-pully/" target="_blank" rel="noopener"><h3>Pully–Paudex–Lutry</h3><p>Official sector page →</p></a>
        <a class="card" href="https://fr.lausanne-marathon.com/conseils/informations-aux-riverains/secteur-cully-rivaz-st-saphorin/" target="_blank" rel="noopener"><h3>Cully–Rivaz–St-Saphorin</h3><p>Official sector page →</p></a>
        <a class="card" href="https://fr.lausanne-marathon.com/conseils/informations-aux-riverains/secteur-riviera/" target="_blank" rel="noopener"><h3>Riviera</h3><p>Official sector page →</p></a>
      </div>''',"lm-11")
    pages["histoire.html"]=simple_hero(t,lang,"histoire",'''
      <div class="grid grid-2">
        <div class="card"><h3>Since 1993</h3><p>Lausanne Marathon has grown into a landmark autumn race on Lake Geneva.</p></div>
        <div class="card"><h3>Gallery of winners</h3><p><a href="https://fr.lausanne-marathon.com/conseils/la-galerie-des-vainqueurs/" target="_blank" rel="noopener">Official gallery →</a></p></div>
      </div>''',"lm-08")
    pages["organisation.html"]=simple_hero(t,lang,"organisation",'''
      <div class="card"><h3>Association Lausanne Marathon</h3>
      <p>Av. de Rhodanie 54, 1007 Lausanne<br>Tél. +41 21 806 30 16<br><a href="mailto:info@lausanne-marathon.com">info@lausanne-marathon.com</a></p>
      <p><a href="https://fr.lausanne-marathon.com/conseils/lorganisation/" target="_blank" rel="noopener">Organisation page →</a></p></div>''',"lm-10")
    pages["presse.html"]=simple_hero(t,lang,"presse",f'''
      <div class="card"><h3>{t["exemple"]}</h3><p>Media kit and accreditation flows would live here. For now, use the official contact.</p>
      <a class="btn btn-outline" href="https://fr.lausanne-marathon.com/contact/contact/" target="_blank" rel="noopener">Official contact →</a></div>''',"lm-02")
    pages["contact.html"]=simple_hero(t,lang,"contact",'''
      <div class="card"><h3>Lausanne Marathon</h3>
      <p>Av. de Rhodanie 54<br>1007 Lausanne · Suisse<br>Tél. +41 21 806 30 16<br>Fax +41 21 806 25 48<br><a href="mailto:info@lausanne-marathon.com">info@lausanne-marathon.com</a></p>
      <a class="btn btn-primary" href="https://fr.lausanne-marathon.com/contact/contact/" target="_blank" rel="noopener">Official contact →</a></div>''',"lm-11")
    # infos hub
    chips="".join(f'<button type="button" class="chip" onclick="showAnswer(\'{k}\')">{label}</button>' for k,label in t["chips"])
    pages["infos.html"]=simple_hero(t,lang,"infos",f'''
      <div class="ask" id="ask"><h3 style="margin-top:0">{t["home"]["ask_h"]}</h3>
      <form onsubmit="askSubmit(event)" style="display:flex;gap:8px;flex-wrap:wrap"><input id="ask-input" type="search" placeholder="{t["home"]["ask_ph"]}" style="flex:1;min-width:200px;border:0;border-radius:999px;padding:14px 16px"><button class="btn btn-primary" type="submit">OK</button></form>
      <div class="chips">{chips}</div><div id="ask-answer" class="answer"></div></div>
      <section class="section"><h2>{t["nav"]["programme"]}</h2>
      <div class="grid grid-2">
        <a class="card" href="programme.html"><h3>{t["nav"]["programme"]}</h3><p>{t["pages"]["programme"]["lead"]}</p></a>
        <a class="card" href="dossards.html"><h3>{t["nav"]["dossards"]}</h3><p>{t["pages"]["dossards"]["lead"]}</p></a>
        <a class="card" href="acces.html"><h3>{t["nav"]["acces"]}</h3><p>{t["pages"]["acces"]["lead"]}</p></a>
        <a class="card" href="faq.html"><h3>{t["nav"]["faq"]}</h3><p>{t["pages"]["faq"]["lead"]}</p></a>
      </div></section>''',"lm-12")

    for name, html in pages.items():
      (d/name).write_text(html, encoding="utf-8")
    print(lang, len(pages), "pages")

  # root redirect + robots + credits
  (ROOT/"index.html").write_text('''<!DOCTYPE html><html lang="fr"><head>
<meta charset="utf-8"><meta name="robots" content="noindex,nofollow,noarchive">
<meta http-equiv="refresh" content="0; url=fr/">
<link rel="canonical" href="fr/">
<title>Lausanne Marathon — Concept</title></head>
<body><p><a href="fr/">Français</a> · <a href="de/">Deutsch</a> · <a href="en/">English</a> · <a href="it/">Italiano</a></p></body></html>''', encoding='utf-8')
  (ROOT/"robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
  (ROOT/"README.md").write_text("""# Lausanne Marathon — concept exploratoire 2027

Maquette HTML/CSS/JS statique, non officielle, préparée à titre bénévole.
Langues: FR (défaut), DE, EN, IT.
Anti-indexation: meta robots + robots.txt Disallow.
Tracés: indicatifs (OSM/OSRM) faute de GPX officiel.
""", encoding="utf-8")
  print("OK")

if __name__ == "__main__":
  build_all()
