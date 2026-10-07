#!/usr/bin/env python3
"""Genera el sitio estático de Adripsykcare en ./site"""
import os, re, json, datetime

BASE = os.environ.get("SITE_URL", "https://www.adripsykcare.com")
# PREVIEW=True: modo "barbecho" -> no indexable por buscadores. Poner False al publicar con el dominio.
PREVIEW = True

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")

MENU = [("om-oss", "Om Oss"), ("utredning", "Utredning"), ("behandling", "Behandling"),
        ("akupunktur", "Akupunktur"), ("etik", "Etik"), ("kontakt", "Kontakt"), ("pris", "Pris")]

def img(name, alt, style=""):
    st = f' style="{style}"' if style else ""
    return f'<figure class="img"><img src="/img/{name}" alt="{alt}" loading="lazy"{st}></figure>'

PAGES = {}

PAGES["om-oss"] = dict(
    title="Om Oss",
    desc="Barn- och ungdomspsykiater Adriana Manea och leg. psykolog/leg. psykoterapeut Mona Pettersson – neuropsykiatriska utredningar och psykiatrisk behandling i Gävle.",
    body=f"""
{img("om-oss.jpg", "Ljust arbetsrum med laptop, blommor och kaffe")}
<p>På mottagningen arbetar barn- och ungdomspsykiater Adriana Manea och leg. psykolog/leg. psykoterapeut Mona Pettersson. Vi har arbetat tillsammans under många år och vårt fokus har varit att utföra neuropsykiatriska utredningar samt psykiatriska behandlingar. Vi har hjälpt många personer/ klienter och deras familj att hitta vägar till ett bättre mående och funktion.</p>
<p>Vårt mål är att vara följsamma utifrån barnens och ungdomarnas utveckling, att se dem utifrån deras förutsättningar och bidra med verktyg för att bygga en hälsosam och meningsfull framtid. I kontakten med vuxna har vi som syfte att identifiera de hinder som stör funktionen i vardagen, på arbetet och i relationer samt guida dem att hitta vägen till ett mer fungerande liv.</p>
{img("adriana-manea.jpg", "Adriana Manea, barn- och ungdomspsykiater", "height:500px;width:auto")}
<p><strong>Adriana Manea</strong></p>
<p>Jag är läkare, specialiserad i Barn och ungdomspsykiatri sedan 2008. Jag har arbetat på barn- och ungdomspsykiatri (BUP) i Gävle som överläkare sedan 2011. Jag har också arbetat privat i Region Dalarna sedan 2018 och har haft korta uppdrag i Stockholm, Västerås, Örebro. Jag har bred erfarenhet av neuropsykiatriska utredningar, barnpsykiatrisk bedömning samt psykiatrisk medicinsk behandling för barn i alla åldrar samt unga vuxna. Det glädjer mig att bredda min erfarenhet genom att erbjuda utredning, bedömning och medicinsk behandling även till vuxna. Jag arbetar fortsatt deltid på BUP i Gävle för att bibehålla min kompetens på en nivå som ger goda förutsättningar för att bedriva ett gediget arbete.</p>
<p><strong>Min filosofi</strong></p>
<p>”Psykiatriska tillstånd” definierar jag som en tillfällig variation i vårt psyke som gör att vi inte fungerar som vi brukar och inte känner igen oss själva. Variationen kan förstås genom olika förklaringsmodeller. Ibland orsakas den av stress som samhället och livet påtvingar våra hjärnor, andra gånger kan det finnas genetiska orsaker och oftast finns en kombination av flera olika faktorer. Man behöver förstå sina sårbarheter och styrkor för att kunna hitta den balans som leder till psykisk hälsa. I vår kontakt strävar vi mot att hitta vägen till balans.</p>
<p>I mitt privata liv tycker jag om att vara med familjen, att läsa, att utmana mig i att lära mig helt nya saker och jag älskar att vara i naturen. Jag hittar inspiration i naturens skiftningar vilket har bidragit till att se hur viktigt och vackert det är att vi människor är olik varandra men också hur viktigt det är att ha anpassade förutsättningar för att kunna växa och blomma tillsammans.</p>
{img("mona-pettersson.jpg", "Mona Pettersson, leg. psykolog och leg. psykoterapeut", "height:500px;width:auto")}
<p><strong>Mona Pettersson</strong></p>
<p>Under mina 18 år som psykolog och legitimerad psykoterapeut så har jag arbetat med barn, ungdomar och vuxna i flera olika sammanhang, både inom primärvården, psykiatrin och i mitt företag ”KBT i Dalarna”. Jag har främst arbetat i Region Gävleborg och Region Dalarna och utfört neuropsykiatriska utredningar (NP-utredningar) parallellt med psykoterapier. Utifrån mitt perspektiv är inte diagnosen det viktigaste under utredandeprocessen utan det är att på djupet förstå sig själv och kunna se sina förmågor och vad det är som gör att man har hinder att använda sig av dessa. Ibland beror det på en diagnos och ibland kan det vara andra typer av hinder och då behövs andra typer av insatser. För mig är det också viktigt att personer som står nära, tex anhöriga förstår vad hindren består av, för att kunna skilja på när man inte vill respektive, när man inte kan. Då blir det lättare att stötta och hitta konstruktiva lösningar.</p>
<p><strong>Vilka fördelar finns det med att välja en liten mottagning?</strong></p>
<p>På vår mottagning har vi en total överblick och kan erbjuda en snabb och trygg kontakt, bredare bedömningar samt kontinuitet. Tillsammans letar vi efter ledtrådar och information för att förstå problematiken i grunden. Vi bidrar med kunskap, öppenhet, trygghet och att lyssna och reflektera tillsammans.</p>
<p>Varje individ möts på sina premisser och utredningen kan ibland gå fort och ibland ta längre tid. Det kan också vara så att man efter en tid behöver få ses igen och påminnas om vad vi kommit fram till eller få stöd i att hitta hjälp framåt så då det har tillkommit nya omständigheter. Vi kan följa upp över tid eller remittera vidare.</p>
<p>Vi arbetar utifrån Socialstyrelsen-, Svenska föreningen för barn- och ungdomspsykiatri- (SFBUP), Svenska psykiatriska föreningens (SPF) riktlinjer. Vi utbildar oss kontinuerligt för att hålla oss uppdaterade vilket är viktigt för att kunna erbjuda rätt insatser. Vårt mål är att kunna erbjuda ett snabbt och professionellt mottagande till alla. Hos oss har du en kontaktperson som hjälper och vägleder dig genom hela processen.</p>
<figure class="img"><img src="/img/dsm5-icd11.png" alt="DSM-5 och ICD-11 – de diagnostiska manualerna för psykiatriska tillstånd" loading="lazy" style="max-width:304px"></figure>
<figure class="img"><img src="/img/nationella-riktlinjer-adhd-autism.png" alt="Socialstyrelsen: Nationella riktlinjer för vård och stöd vid adhd och autism" loading="lazy" style="max-width:462px"></figure>
<p><strong>Detta kan vi erbjuda</strong></p>
<p>Vi erbjuder en privatfinansierad utredning samt medicinsk behandling, detta innebär att det är du som bekostar den själv.</p>
<p>Vi erbjuder ett första familjesamtal där vi gör en fördjupad intervju för att tillsammans komma fram till om det finns behov av utredning eller andra insatser. Om andra insatser skulle behövas kan familjen guidas vidare.</p>
<p>Vid beslut om att inleda en utredning eller behandling erbjuds en vårdplan med information om vad vår kontakt kommer att innebära samt kostnaden för detta.</p>
<p>Vi erbjuder ”second opinion” bedömningar för de som inte längre känner igen sig i sin diagnos och heller inte har en funktionsnedsättning utifrån sina tidigare svårigheter.</p>
<p><strong>Sammanfattningsvis kan vi erbjuda</strong></p>
<ul>
<li>Familjesamtal med fördjupad intervju och screening</li>
<li>Läkarbedömning</li>
<li>Endast psykologutredning</li>
<li>Neuropsykiatrisk utredning av psykolog och läkare</li>
<li>Second opinion angående diagnostik</li>
<li>Medicinsk behandling vid ADHD/ADD</li>
<li>Medicinsk behandling av depression, ångest, mfl. tillstånd</li>
<li>Intyg (Omvårdnadsbidrag, Transportstyrelsen, VAB kopplat till psykisk ohälsa, Intyg gällande centralstimulerande mediciner vid utlandsresor)</li>
</ul>
""")

PAGES["utredning"] = dict(
    title="Utredning",
    desc="Hur går en neuropsykiatrisk utredning (NP-utredning) till? Psykologutredning, läkarbedömning och sambedömning – privatfinansierad utredning i Gävle.",
    body=f"""
{img("utredning-1.jpg", "Barn som utforskar naturen med förstoringsglas")}
<p><strong>Hur går en utredning till?</strong></p>
<p>Som underlag för utredning tar vi emot remisser men man kan även ta själv kontakt för att få starta en privatfinansierad utredning.</p>
<p>En NP-utredning består av psykologutredning, läkarbedömning samt sambedömning psykolog-läkare.</p>
<p>Under psykologutredningen får föräldrar och barn/ungdom eller vuxen fylla i skattningsformulär och man genomgår en psykologtestning som väljs ut utifrån frågeställning och ålder. Psykologen tar även ibland kontakt med pedagog på skolan för att få ytterligare information.</p>
{img("utredning-2.jpg", "Två vandrare på väg längs kusten i solnedgång")}
<p>Under utredning av vuxen person görs intervju om möjligt med förälder eller annan närstående person som kan berätta om barndom/tidig tid.</p>
<p>Det ingår alltid en begåvningstestning om det inte redan har gjorts en sådan under de senaste två åren. Testningstillfället ger även en bra möjlighet att observera hur barnet/ungdomen eller vuxen agerar i olika situationer tex under tidspress. Antal träffar/besök anpassas efter behov och förmåga.</p>
<p>Under mötet med läkaren görs somatisk och neurologisk undersökning och läkaren ställer då frågor till patient/klient och föräldrar/anhörig. Läkaren kan rekommendera blodprovstagning för att utesluta somatiska orsaker till eventuella symtom som personen kan ha drabbas av. Vid information/misstanke om drogbruk kommer drogtestning krävas.</p>
{img("utredning-3.jpg", "Händer som planterar en ung växt i jord")}
<p>Psykolog och läkare gör därefter en sambedömning och eventuella diagnoser fastställs.</p>
<p>Då utredningen är färdigskriven får familjen möjlighet att granska utlåtandet så inga missförstånd finns. I utredningen finns rekommendationer till familjen, skolan och BUP/VUP. Utredande psykolog gör även en återkoppling av resultat till patient/klient, familj och vid önskemål även till skola.</p>
<p>Utifrån familjens önskemål kan utredningen och remiss skickas vidare till BUP/VUP på hemorten för övertagande.</p>
""")

PAGES["behandling"] = dict(
    title="Behandling",
    desc="Privatfinansierad medicinsk behandling vid ADHD/ADD för barn från 6 år och vuxna, enligt Socialstyrelsens rekommendationer.",
    body=f"""
{img("behandling-1.jpg", "Människor som hjälper varandra upp på en klippa")}
<p><strong>Medicinsk behandling ADHD/ADD</strong></p>
<p>För dig som har fått en ADHD/ADD diagnos hos oss eller sedan tidigare hos annan vårdgivare erbjuder vi privatfinansierad medicinsk behandling. Behandlingen vänder sig till barn från 6års ålder samt till vuxna. Den väljs i samråd utifrån Socialstyrelsens rekommendationer och i enlighet med Läkemedelsverket och SFBUP:s, SPF:s riktlinjer. Bedömning om behandling hos oss styrs av vilket vårdbehov som föreligger. Har man behov av mer omfattande insatser kan remiss skickas till specialistvård.</p>
{img("behandling-2.jpg", "Familj som promenerar tillsammans på en landsväg")}
<p><strong>Tillsammans hittar vi rätt!</strong></p>
<p>Medicinsk behandling ska vara ett komplement till andra insatser du bör få från vården och skolan.<br>Människor har olika biologiska förutsättningar som gör att man får ett varierande svar på olika medicinska preparat och det finns flera mediciner att tillgå. Man vill gärna individualisera behandlingen så mycket det går för att passa den till individens behov, möjligheter och biologisk variation.</p>
<p>Förutom medicinering så är det viktigt med goda strategier för att hantera de hinder och svårigheter som kan uppstå vid NP-problematik. Vid utredningens resultatgenomgång så är målet att den utredde personen ska känna igen sig i allt som beskrivs och få en ökad förståelse för hur man fungerar och vad man behöver för att må bra. Utifrån detta görs rekommendationer gemensamt. Det finns också möjlighet att återkomma efter utredningen för att få stöd i att lotsas till rätt typ av insatser.</p>
""")

PAGES["akupunktur"] = dict(
    title="Akupunktur",
    desc="Västerländsk akupunktur som komplement till medicinsk behandling – vid stress, sömnstörning, nedstämdhet, ångest och långvarig smärta. För barn från 12 år och vuxna.",
    body=f"""
{img("akupunktur.jpg", "Maskrosfrön i närbild")}
<p><strong>Akupunktur- Alternativ behandling – västerländsk akupunktur</strong></p>
<p>Dr. Adriana är utbildad i västerländsk akupunktur och erbjuder en komplementär behandling till den medicinska behandlingen. Akupunktur kan underlätta symtom relaterade till stress, sömnstörning, nedstämdhet och ångest och mot långvarig smärta.</p>
<p>Akupunkturbehandlingen erbjuds till barn, från 12 års ålder och vuxna.</p>
<p>Akupunktur är en metod som använder kroppens egna mekanismer för att frigöra smärta och muskelansträngning. Akupunktur hjälper kroppen och hjärnan både lokalt dvs där akupunkturnålar sätts in samt centralt dvs stimulerar hjärnas förmåga att utsöndra hormoner som minskar stressen och ökar skyddsmekanismer bla. genom immunsystemet.</p>
<p>Socialstyrelsen godkände västerländsk akupunktur för behandling mot smärta 1984. Västerländsk akupunktur innebär att förklaringsmodellerna för hur metoden fungerar bygger på fysiologiskt resonemang. 1993 utvidgades indikationsområdet att även innefatta vissa sjukdomstillstånd enligt påvisad vetenskap och beprövad erfarenhet (ryggsmärta, nacksmärta, artros, spädbarnskolik).</p>
<p>Akupunkturbehandlingen innebär att man sticker in akupunkturnålar i vissa kända, utvalda punkter på kroppen. En session varar ca 60min och under denna tid tas information om aktuellt tillstånd och akupunkturnålarna stimuleras några gånger. För att behandlingen ska ge maximalt resultat rekommenderas en session, en gång per vecka under 10-12veckor. Under första och andra veckan kan erbjudas två sessioner/vecka. Efter en hel behandling behövs ibland underhållsbehandling en gång/månad och ibland behövs upprepas behandlingen efter en period. Behandlingen planeras i samråd och utifrån behov.</p>
""")

PAGES["etik"] = dict(
    title="Etik",
    desc="Sekretess, tolk, transparens och tydlighet – så arbetar Adripsykcare, och vilka tillstånd vi inte utreder eller behandlar.",
    body=f"""
{img("etik.jpg", "Öppen anteckningsbok på en klippa vid en flod")}
<p>Sekretess är viktigt för oss och vi är noga med att ta reda på vad varje individ ser som privat då vi tex. redogör för utredningens resultat till skolan.</p>
<p>Tolk beställs varje gång det behövs. Att kunna göra sig förstådd är viktig för en bra kommunikation och ingen språkbarriär ska få påverka samtal och bedömning.</p>
<p>Transparens, tydlighet och ärlighet är också viktigt för oss. I situationer då vår bedömning är att ett psykiatriskt tillstånd är för allvarligt och kräver andra och mer omfattande insatser än vad vi kan bidra med kommer teamet att förmedla detta och guida personen vidare.</p>
<p>Utredning och behandling på vår klinik kommer INTE erbjudas vid nedanstående tillstånd men vi kan ge förslag på vart man kan söka vård för att komma vidare.</p>
<ul>
<li>pågående missbruk</li>
<li>svår depression som kräver inneliggande vård</li>
<li>svår ångest som kräver inneliggande vård</li>
<li>bipolär sjukdom med ostabilt mående som kräver inneliggande vård</li>
<li>svår ätstörningsproblematik som kräver inneliggande vård</li>
<li>svårt tvångssyndrom som kräver inneliggande vård</li>
<li>schizofreni eller andra psykossjukdomar</li>
</ul>
<p>Vi strävar efter korta väntetider och anpassade besökstider. Vi har möjlighet att kombinera bedömningar på plats och online men vi vill alltid träffas minst en gång på plats till läkare respektive psykolog.</p>
<p>Vi hjälper gärna till med remiss för övertagning till specialistnivå- barn- och ungdomspsykiatri eller vuxenpsykiatri. Vi säkerställer din medicinering tills du fått en stabil kontakt inom den offentliga vården.</p>
<p>Läkarbedömning och medicinsk behandling erbjuds inte till invånare med ålder under 18år som är inskrivna i en av kommunerna som tillhör Region Gävleborg. Detta för att undvika intressekonfliktpolicy med Region Gävleborg.</p>
<p>Däremot psykologbedömning/screening erbjuds till invånare från alla Sveriges kommuner.</p>
""")

PAGES["kontakt"] = dict(
    title="Kontakt",
    desc="Kontakta Adripsykcare – ring psykolog Mona Pettersson eller läkare Adriana Manea, eller mejla oss. Drottninggatan 28, 803 11 Gävle.",
    body="""
<p>Vi är öppna för olika kontaktmöjligheter. Vi kan höras på telefon, digitalt men behöver också ses på plats i någon av våra lokaler i Gävle eller Falun.</p>
<p>Ring oss och få direkt kontakt</p>
<div class="contact-grid">
  <div class="contact-card">
    <p><strong>Psykolog Mona Pettersson</strong></p>
    <p><a href="tel:+46704946843">070-494 68 43</a></p>
  </div>
  <div class="contact-card">
    <p><strong>Läkare Adriana Manea</strong></p>
    <p><a href="tel:+46765955364">076-595 53 64</a></p>
  </div>
</div>
<p><strong>E-post</strong></p>
<p><a class="button" href="mailto:info@adripsykcare.com?subject=Kontakt%20via%20webbplatsen">info@adripsykcare.com</a></p>
<p class="note">Skicka inte känsliga personuppgifter eller journaluppgifter via e-post. Beskriv kort ditt ärende så återkommer vi.</p>
<p><strong>Hitta hit</strong></p>
<p><a href="https://www.google.com/maps/search/?api=1&amp;query=Drottninggatan+28,+803+11+G%C3%A4vle" target="_blank" rel="noopener">Drottninggatan 28, 803 11 Gävle</a></p>
""")

PAGES["pris"] = dict(
    title="Pris",
    desc="Priser för familjesamtal, neuropsykiatrisk utredning, psykologutredning, medicinsk behandling, intyg och akupunktur hos Adripsykcare.",
    body=f"""
{img("pris.jpg", "Glasflaskor med gröna växter på rad")}
<ul>
<li>Nybesök familjesamtal med fördjupad intervju 2000 kr</li>
<li>Återbesök läkare 1750 kr</li>
<li>Neuropsykiatrisk utredning (både psykolog och läkare) 23000 kr (inkluderar första familjesamtalet)</li>
<li>Enbart psykologutredning 11&nbsp;000 kr</li>
<li>Second opinion- varierande pris beroende på hur omfattande bedömningen är</li>
<li>Medicinskt behandlingspaket vid ny kontakt 7000 kr/6mån (information, medicininsättning, telefonuppföljning samt två uppföljande besök på plats/online)</li>
<li>Medicinskt behandlingspaket vid utredning hos oss 5000 kr/6mån (information, medicininsättning, telefonuppföljning samt två uppföljande besök på plats/online)</li>
<li>Recept 400 kr</li>
<li>Telefonkonsultation 500 kr</li>
<li>Intyg vid ny kontakt 1000 kr (VAB, Omvårdnadsbidrag, Transportstyrelsen)</li>
<li>Intyg VAB och Omvårdnadsbidrag vid utredning hos oss inkluderas av utredningspriset</li>
<li>Akupunkturbehandling 1200 kr/session</li>
</ul>
""")

CARDS = [("om-oss", "arbetsrum.jpg", "Ljust arbetsrum med laptop och blommor"),
         ("utredning", "barn-forstoringsglas.jpg", "Barn som utforskar naturen med förstoringsglas"),
         ("behandling", "vandrare-hjalper-varandra.jpg", "Vänner som hjälper varandra upp på ett berg"),
         ("akupunktur", "maskros.jpg", "Maskrosfrö i närbild"),
         ("etik", "bok-i-naturen.jpg", "Öppen bok och reservoarpenna i naturen"),
         ("pris", "flaskor-med-orter.jpg", "Glasflaskor med gröna växter på rad")]

HOME_DESC = "Välkommen till AdripsykCare, en specialistmottagning i Gävle med fokus på psykisk hälsa för barn, ungdomar och vuxna – NP-utredning, ADHD-behandling och akupunktur."

JSONLD = {
    "@context": "https://schema.org",
    "@type": "MedicalClinic",
    "name": "AdripsykCare",
    "legalName": "AdripsykCare AB",
    "url": BASE + "/",
    "telephone": "+46765955364",
    "email": "info@adripsykcare.com",
    "taxID": "559157-9213",
    "address": {"@type": "PostalAddress", "streetAddress": "Drottninggatan 28",
                "postalCode": "803 11", "addressLocality": "Gävle", "addressCountry": "SE"},
    "medicalSpecialty": ["Psychiatric", "Pediatric"],
    "availableService": ["Neuropsykiatrisk utredning", "ADHD-behandling", "Akupunktur"],
}

def layout(slug, title, desc, main, og_img):
    url = BASE + (f"/{slug}/" if slug else "/")
    full_title = f"{title} – Adripsykcare" if slug else "Adripsykcare – Vi tar hand om din psykiska hälsa"
    nav = "\n".join(
        f'<li><a href="/{s}/"{" aria-current=\"page\"" if s == slug else ""}>{t}</a></li>' for s, t in MENU)
    ld = f'<script type="application/ld+json">{json.dumps(JSONLD, ensure_ascii=False)}</script>' if not slug else ""
    return f"""<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
{'<meta name="robots" content="noindex, nofollow">' if PREVIEW else ""}
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Adripsykcare">
<meta property="og:locale" content="sv_SE">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/img/{og_img}">
<link rel="preload" href="/fonts/epilogue-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/style.css">
{ld}
</head>
<body>
<a class="skip" href="#main">Hoppa till innehåll</a>
<header class="site-header">
  <a class="site-title" href="/">Adripsykcare</a>
  <button class="menu-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Meny"><span></span></button>
  <nav id="site-nav" aria-label="Huvudmeny"><ul>
{nav}
  </ul></nav>
</header>
<main id="main">
{main}
</main>
<footer class="site-footer">
  <div>© AdripsykCare</div>
  <div>Drottninggatan 28, 803 11 Gävle<br><a href="tel:+46765955364">0765955364</a><br><a href="mailto:info@adripsykcare.com">info@adripsykcare.com</a></div>
  <div>AdripsykCare AB; Org.nr 559157-9213</div>
</footer>
<script>
const b=document.querySelector('.menu-toggle'),n=document.getElementById('site-nav');
b.addEventListener('click',()=>{{const o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)}});
</script>
</body>
</html>
"""

def home():
    cards = "\n".join(
        f'<li><a href="/{s}/"><img src="/img/{im}" alt="{alt}" width="1024" height="683"{"" if i < 2 else " loading=\"lazy\""}><h2>{dict(MENU)[s]}</h2></a></li>'
        for i, (s, im, alt) in enumerate(CARDS))
    return f"""<h1 class="visually-hidden">Adripsykcare – specialistmottagning för psykisk hälsa i Gävle</h1>
<div class="home">
  <div class="intro">
    <p><strong>Välkommen till AdripsykCare, en specialistmottagning med fokus på psykisk hälsa gällande barn, ungdomar samt vuxna.</strong></p>
    <p>Varje människa är unik och det är viktigt för oss att möta varje individ utifrån dess särskilda behov. Vi arbetar utifrån beforskade och utprövade metoder, i nära samarbete med våra klienter, och då det behövs andra viktiga personer som kan bidra med information. Vårt mål är att skapa en miljö där den som utreds kan känna sig trygg och komma till sin rätt.</p>
  </div>
  <ul class="cards">
{cards}
  </ul>
</div>"""

def write(path, text):
    # rutas relativas: funciona igual en usuario.github.io/repo/ y en el dominio propio
    if path.endswith(".html"):
        rel = "../" * path.count("/") or "./"
        text = re.sub(r'(href|src)="/(?!/)', lambda m: f'{m.group(1)}="{rel}', text)
        text = text.replace(f'href="{rel}"', f'href="{rel}"')
    p = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(text)

def main():
    write("index.html", layout("", "Adripsykcare", HOME_DESC, home(), "arbetsrum.jpg"))
    og = {"om-oss": "om-oss.jpg", "utredning": "utredning-1.jpg", "behandling": "behandling-1.jpg", "akupunktur": "akupunktur.jpg",
          "etik": "etik.jpg", "kontakt": "arbetsrum.jpg", "pris": "pris.jpg"}
    for slug, _ in MENU:
        pg = PAGES[slug]
        main_html = f'<article class="page"><h1>{pg["title"]}</h1>\n{pg["body"]}</article>'
        write(f"{slug}/index.html", layout(slug, pg["title"], pg["desc"], main_html, og[slug]))
    write("404.html", layout("404", "Sidan hittades inte", "Sidan hittades inte.",
          '<article class="page"><h1>Sidan hittades inte</h1><p><a href="/">Till startsidan</a></p></article>', "arbetsrum.jpg")
          .replace('<link rel="canonical"', '<meta name="robots" content="noindex">\n<link rel="canonical"'))
    today = datetime.date.today().isoformat()
    urls = [""] + [f"{s}/" for s, _ in MENU]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "".join(f"  <url><loc>{BASE}/{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    if PREVIEW:
        write("robots.txt", "User-agent: *\nDisallow: /\n")
    else:
        write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    open(os.path.join(OUT, ".nojekyll"), "w").close()

if __name__ == "__main__":
    main()
