#!/usr/bin/env python3
"""Script to create the complete voorwaarden.html page"""

# Read header and footer from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract header (until </header>)
header_end = index_content.find('</header>')
header = index_content[:header_end + len('</header>')]

# Extract footer (from <!-- FOOTER -->)
footer_start = index_content.find('<!-- FOOTER -->')
footer = index_content[footer_start:]

# Build the page
html_content = '''<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Algemene voorwaarden - UGC.NL</title>
  <meta name="description" content="Algemene voorwaarden en betalingsvoorwaarden van UGC.NL">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
''' + header + '''

  <!-- HERO SECTION -->
  <section class="section" style="padding-top: var(--spacing-3xl); padding-bottom: var(--spacing-lg);">
    <div class="container">
      <h1 style="font-size: clamp(32px, 4vw, 48px); font-weight: var(--font-weight-bold); margin-bottom: var(--spacing-sm);">Algemene- en betalingsvoorwaarden</h1>
      <p style="color: var(--color-text-secondary); font-size: var(--font-size-body);">Effective Date: 26 November, 2025</p>
    </div>
  </section>

  <!-- MAIN CONTENT -->
  <section class="section" style="padding-top: 0;">
    <div class="terms-page-container">
      <!-- CONTENT LEFT -->
      <div class="terms-content">
        <!-- SECTION 1 -->
        <div class="terms-section" id="section-1">
          <h2>1. Partijen</h2>
          <p><strong>1.</strong> UGC.NL: UGC.NL, geregistreerd bij de Kamer van Koophandel onder nummer 88229912, gevestigd te Amsterdam aan de Keizersgracht 520 H (1017 EK).</p>
          <p><strong>1.1.</strong> Verdere gegevens van UGC.NL:</p>
          <ul>
            <li>Website: UGC.NL</li>
            <li>Btw-identificatienummer: NL864546749B01</li>
          </ul>
          <p><strong>1.2.</strong> Gebruiker: een natuurlijk persoon die al dan niet handelt in de uitoefening van een bedrijf of beroep, een bezoeker van de website van UGC.NL;</p>
          <p><strong>1.3.</strong> Account: een door Gebruiker bij UGC.NL aangevraagde, en door UGC.NL verleende, mogelijkheid om in te loggen op de website van UGC.NL</p>
        </div>

        <!-- SECTION 2 -->
        <div class="terms-section" id="section-2">
          <h2>2. Toepasselijkheid</h2>
          <p><strong>2.1.</strong> UGC.NL verklaart deze algemene voorwaarden van toepassing op het gebruik van de website en elk aanbod van UGC.NL en, al dan niet daaruit voortvloeiende, overeenkomsten die UGC.NL en Gebruiker met elkaar zijn aangegaan. Voor zover de inhoud hiervan niet is gewijzigd of er geen specifiekere voorwaarden tussen partijen gelden, zullen deze algemene voorwaarden tevens voor toekomstige verbintenisrechtelijke verhoudingen tussen partijen gelden.</p>
          <p><strong>2.2.</strong> Afwijkingen van deze voorwaarden gelden uitsluitend voor zover deze door partijen uitdrukkelijk schriftelijk zijn overeengekomen.</p>
          <p><strong>2.3.</strong> Algemene (inkoop)voorwaarden van Gebruiker worden uitdrukkelijk van de hand gewezen.</p>
          <p><strong>2.4.</strong> Derden die door UGC.NL worden betrokken kunnen zich eveneens op deze algemene voorwaarden beroepen.</p>
          <p><strong>2.5.</strong> Indien een of meer (gedeelte(n)) van de bepalingen van deze algemene voorwaarden nietig zijn, dan wel worden vernietigd, blijven de overige bepalingen van deze algemene voorwaarden van toepassing. Partijen zullen alsdan in overleg treden om ter vervanging van de nietige c.q. vernietigde bepalingen nieuwe regels overeen te komen, waarin zoveel mogelijk doel en strekking van de nietige c.q. vernietigde bepalingen tot uiting zullen komen.</p>
          <p><strong>2.6.</strong> De door deze voorwaarden gereguleerde rechtsverhouding komt tot stand op het moment dat Gebruiker de website van UGC.NL bezoekt en/of een Account heeft aangemaakt op de website van UGC.NL, waarbij Gebruiker deze voorwaarden heeft geaccepteerd.</p>
          <p><strong>2.7.</strong> UGC.NL is geen partij bij de overeenkomst die tussen Gebruiker en derden tot stand komt, tenzij uitdrukkelijk anders vermeld. Geschillen die uit een dergelijke overeenkomst voortvloeien dienen partijen zelf op te lossen. UGC.NL speelt hierbij geen enkele rol.</p>
        </div>

        <!-- SECTION 3 -->
        <div class="terms-section" id="section-3">
          <h2>3. Vertoning, wijziging en gebruik van de website</h2>
          <p><strong>3.1.</strong> UGC.NL behoudt zich het recht voor de indeling van de website (incl. zoekopties et cetera) te allen tijde en naar eigen inzicht te wijzigen zonder dat Gebruiker recht heeft op schadevergoeding.</p>
          <p><strong>3.2.</strong> UGC.NL spant zich ervoor in haar website storingsvrij online te publiceren. UGC.NL garandeert echter niet dat haar website storingvrij en/of foutloos wordt gepubliceerd dan wel dat de uitgave te allen tijde toegankelijk is. UGC.NL is gerechtigd, zonder voorafgaande bekendmaking, de website buiten gebruik te stellen en/of het gebruik ervan te beperken indien zulks naar haar redelijke oordeel noodzakelijk is, bijvoorbeeld in het kader van het benodigde onderhoud van de website. Eventueel onderhoud wordt zoveel mogelijk in de nachtelijke uren van 00.00 – 06.00 uitgevoerd.</p>
          <p><strong>3.3.</strong> Indien naar het oordeel van UGC.NL een gevaar ontstaat voor het functioneren van de computersystemen of het netwerk van UGC.NL of derden en/of de leveringen van UGC.NL worden ge- of verhinderd door, maar niet beperkt tot, storingen of uitvallen van internet, de telecommunicatieinfrastructuur, synflood, netwerkaanval, DoS- of DDoS-aanvallen, stroomstoringen, binnenlandse onlusten, mobilisatie, oorlog, stremming in het vervoer, staking, uitsluiting, bedrijfsstoornissen, stagnatie in toelevering, brand, overstroming, in- en uitvoerbelemmeringen, worden alle verplichtingen van UGC.NL opgeschort en is UGC.NL B.V. gerechtigd alle maatregelen te nemen die zij redelijkerwijs nodig acht om dit gevaar/deze verhindering af te wenden dan wel te voorkomen, zonder dat de Gebruiker enig recht op schadevergoeding heeft. Indien nakoming door overmacht langer dan één maand onmogelijk is of er andere omstandigheden zijn waardoor het voor UGC.NL onevenredig bezwarend is om aan haar verplichtingen te voldoen, is UGC.NL bevoegd de overeenkomst door een mededeling aan de Gebruiker en zonder gerechtelijke tussenkomst geheel of gedeeltelijk te ontbinden, zonder dat er in dat geval een verplichting tot schadevergoeding bestaat.</p>
        </div>

        <!-- SECTION 4 -->
        <div class="terms-section" id="section-4">
          <h2>4. Aansprakelijkheid</h2>
          <p><strong>4.1.</strong> UGC.NL staat niet in voor de kwaliteit en de kwantiteit van de weergave de informatie en/of teksten op de website.</p>
          <p><strong>4.2.</strong> UGC.NL is op geen enkele wijze aansprakelijk voor de inhoud van teksten en/of informatie inclusief foto- en/of ander beeldmateriaal.</p>
          <p><strong>4.3.</strong> UGC.NL is op geen enkele wijze aansprakelijk voor enige schade die voortvloeit uit het (tijdelijk) niet beschikbaar zijn van de website en/of informatie inclusief foto- en/of ander beeldmateriaal.</p>
          <p><strong>4.4.</strong> UGC.NL is op geen enkele wijze aansprakelijk voor enige schade als gevolg van malware of andere virussen.</p>
          <p><strong>4.5.</strong> UGC.NL is bij eventuele tekortkomingen in de nakoming van de overeenkomst aan haar zijde uitsluitend slechts verplicht de teksten aan te passen, zonder daarbij gehouden te zijn tot het voldoen van een schadevergoeding aan Gebruiker.</p>
          <p><strong>4.5.</strong> Mocht UGC.NL jegens Gebruiker aansprakelijk zijn, dan is deze aansprakelijkheid te allen tijde beperkt tot het bedrag waarop de door UGC.NL gesloten beroeps- of bedrijfsaansprakelijkheidsverzekering aanspraak geeft, maar te allen tijde (ook als er geen verzekering is waarop een aanspraak kan worden gemaakt) tot een maximum van EUR. 5.000,- per voorval. Indien voorvallen gelijktijdig plaatsvinden, elkaar veroorzaken of anderszins met elkaar verbandhouden wordt dit beschouwd als één voorval.</p>
          <p><strong>4.6.</strong> Aansprakelijkheid van UGC.NL reikt te allen tijde niet tot gevolgschade en behoudens opzet of grove schuld eveneens niet tot zaakschade, immateriële schade of gederfde winst.</p>
          <p><strong>4.7.</strong> UGC.NL staat niet in voor uitlatingen, handelingen of prestaties van Gebruikers en/of derden, al dan niet middels haar website. UGC.NL biedt derhalve geen garanties voor de kwantiteit of kwaliteit van de leveringen (producten of diensten) van derden. Alle aanspraken en andere geschillen dienen zij onderling op te lossen.</p>
          <p><strong>4.8.</strong> De website van UGC.NL kan eventuele urls/links bevatten naar websites van derden. Deze doorverwijzingsmogelijkheden worden geboden als faciliteit en hebben niet de kwalificatie van aanbeveling door UGC.NL. UGC.NL is op geen enkele wijze aansprakelijk voor de content van de gelinkte websites of voor het handelen en nalaten van deze derden.</p>
        </div>

        <!-- SECTION 5 -->
        <div class="terms-section" id="section-5">
          <h2>5. Registratie voor een Account</h2>
          <p><strong>5.1.</strong> De Gebruiker kan een Account aanvragen door het online registratieformulier volledig in te vullen en te versturen naar UGC.NL.</p>
          <p><strong>5.2.</strong> Het is Gebruiker niet toegestaan een Account aan te maken en gebruik te maken van de diensten van UGC.NL zolang hij of zij minderjarig is en daarvoor geen toestemming heeft gekregen van zijn of haar ouders of wettelijke vertegenwoordigers.</p>
          <p><strong>5.3.</strong> Het is Gebruiker alleen toegestaan om zelf een persoonlijke Account aan te maken of door een derde met autorisatie van Gebruiker.</p>
          <p><strong>5.4.</strong> Bij het aanmaken van een Account is het niet toegestaan om een naam te kiezen die een [url] of een gedeelte van een [url] bevat.</p>
          <p><strong>5.5.</strong> Elke Account dient de identiteit van Gebruiker te beschrijven. Gevraagde gegevens dienen naar waarheid te worden ingevuld. Gebruiker mag derhalve geen fictieve personage creëren of een andere identiteit vertegenwoordigen.</p>
          <p><strong>5.6.</strong> Het is niet toegestaan om inloggegevens aan derden te verstrekken. Het is niet toegestaan om inloggegevens van derden te gebruiken voor het afnemen van aangeboden goederen en diensten. Gebruiker is verantwoordelijk voor elk gebruik/handelen dat, al dan niet met toestemming van Gebruiker, via het Account van Gebruiker wordt gebezigd. Gebruiker is verplicht om al het onbevoegde gebruik van het Account van Gebruiker zo spoedig mogelijk aan UGC.NL te melden.</p>
          <p><strong>5.7.</strong> Het Account komt tot stand nadat UGC.NL een wachtwoord en een activatiecode heeft toegestuurd naar het door de Gebruiker opgegeven e-mailadres waarmee de Gebruiker zijn Account kan activeren.</p>
          <p><strong>5.8.</strong> UGC.NL behoudt zich het recht voor een aanvraag voor een Account te weigeren of het Account na registratie weer op te heffen, bijvoorbeeld bij schending van de huisregels van UGC.NL B.V. door Gebruiker.</p>
          <p><strong>5.9.</strong> De inloggegevens zijn strikt persoonlijk en mogen niet aan derden ter beschikking worden gesteld. De Gebruiker staat in voor het gebruik dat van zijn inloggegevens wordt gemaakt, ook al gebeurt dat zonder zijn medeweten.</p>
          <p><strong>5.10.</strong> De Gebruiker zal UGC.NL onmiddellijk waarschuwen als hij vermoedt dat zijn inloggegevens bij een derde bekend zijn of zich anderszins onregelmatigheden voordoen.</p>
          <p><strong>5.11.</strong> Het is de Gebruiker niet toegestaan meer dan één (1) Account aan te vragen of te beheren. Het is de Gebruiker verder niet toegestaan (opnieuw) een Account aan te vragen of te beheren nadat UGC.NL de aanvraag van een Gebruiker voor een Account heeft geweigerd of een Account van de Gebruiker na registratie heeft opgeheven.</p>
        </div>

        <!-- SECTION 6 -->
        <div class="terms-section" id="section-6">
          <h2>6. Delen van persoonsgegevens met derden</h2>
          <p><strong>6.1.</strong> Wij verkopen persoonsgegevens uiteraard niet aan derden en verstrekken deze uitsluitend aan anderen indien dat nodig is voor de uitvoering van onze overeenkomst met u of om te voldoen aan een wettelijke verplichting. Met bedrijven die uw gegevens verwerken in onze opdracht sluiten wij verwerkersovereenkomsten om ervoor te zorgen dat onze partners eenzelfde niveau van beveiliging en vertrouwelijkheid van de persoonsgegevens hanteren.</p>
        </div>

        <!-- SECTION 7 -->
        <div class="terms-section" id="section-7">
          <h2>7. Opheffen Account</h2>
          <p><strong>7.1.</strong> De Gebruiker kan zijn Account laten opheffen indien hij niet langer van de diensten van UGC.NL gebruik wenst te maken. De Gebruiker dient dit per e-mail aan UGC.NL kenbaar te maken onder opgave van zijn inloggegevens.</p>
          <p><strong>7.2.</strong> UGC.NL heeft het recht het Account van de Gebruiker op te heffen indien de Gebruiker gedurende twaalf (12) maanden geen gebruik heeft gemaakt van zijn inloggegevens. Daarnaast heeft UGC.NL het recht om de Account en/of de overeenkomst met Gebruiker met onmiddellijke ingang voor de toekomst door middel van een schriftelijke kennisgeving zonder (nadere) voorafgaande ingebrekestelling en zonder enig recht op schadevergoeding, te ontbinden indien:</p>
          <ul>
            <li>a) Aan Gebruiker (al of niet voorlopig) surseance van betaling wordt verleend of Gebruiker in staat van faillissement wordt verklaard, Gebruiker een verzoek tot toepassing van een schuldsaneringsregeling indient of Gebruiker onder curatele of bewind wordt gesteld.</li>
            <li>b) Op enig moment blijkt dat Gebruiker onjuiste informatie heeft verstrekt of UGC.NL op enig andere wijze heeft misleid, zoals bijvoorbeeld ten aanzien van de identiteit en persoonlijke eigenschappen van Gebruiker.</li>
            <li>c) Gebruiker deze of andere van toepassing zijnde voorwaarden schendt.</li>
          </ul>
          <p><strong>7.3.</strong> UGC.NL is niet gehouden tot vergoeding van kosten of schade van de Gebruiker in verband met het opheffen van een Account op welke reden dan ook.</p>
        </div>

        <!-- SECTION 8 -->
        <div class="terms-section" id="section-8">
          <h2>8. Intellectueel eigendom</h2>
          <p><strong>8.1.</strong> Alle intellectuele eigendomsaanspraken op de content van de website, zoals afbeeldingen, video's, teksten, informatie, software, komen toe aan UGC.NL. Derden mogen zonder de voorafgaande toestemming van de houder van die intellectueel eigendommen deze niet commercieel gebruiken of anderzijds vermenigvuldigen.</p>
          <p><strong>8.2.</strong> Het is Gebruiker niet toegestaan om software in te zetten om gegevens van de website van UGC.NL te verzamelen en te verwerken.</p>
          <p><strong>8.3.</strong> Het is Gebruiker niet toegestaan om aan UGC.NL en/of derden ongevraagde post of e-mails, of andere spam, te versturen, ongevraagd telefonisch te benaderen of op enig andere wijze te contacteren met als doel om producten en/of diensten van hemzelf of derden aan te prijzen of te verkopen.</p>
          <p><strong>8.4.</strong> Gebruiker garandeert dat zij de website en alle daarmee samenhangende producten, diensten en bescheiden/documentatie, gebruikt in overeenstemming met alle van toepassing zijnde wet en regelgeving op het gebied van intellectueel eigendom en privacybescherming.</p>
          <p><strong>8.5.</strong> Indien Gebruiker in strijd met dit artikel handelt, verbeurt UGC.NL een direct en volledig opeisbare boete van EUR. 5.000,- per overtreding en EUR. 500,- voor iedere dag of gedeelte daarvan dat deze overtreding voortduurt. De hiervoor genoemde boete laat onverlet de gehoudenheid van Gebruiker tot betaling van een volledige schadevergoeding aan UGC.NL indien de schade meer mocht belopen dan gemeld boetebedrag.</p>
          <p><strong>8.6</strong> Alle communicatie tussen Gebruikers die verband houdt met het gebruik van het UGC.NL-platform, opdrachten, offertes, betalingen of transacties dient uitsluitend plaats te vinden via de door UGC.NL beschikbaar gestelde communicatiemiddelen, waaronder het chatsysteem.</p>
          <p>Het is Gebruikers uitdrukkelijk niet toegestaan om via het platform:</p>
          <ul>
            <li>contactgegevens uit te wisselen, zoals e-mailadressen, telefoonnummers, socialmedia-accounts of andere externe contactmogelijkheden;</li>
            <li>op enige wijze contact buiten het platform om te zoeken of te faciliteren;</li>
            <li>transacties, betalingen of afspraken buiten het platform om te initiëren of af te handelen.</li>
          </ul>
          <p>UGC.NL is gerechtigd om communicatie die via het platform plaatsvindt te monitoren en te analyseren teneinde:</p>
          <ul>
            <li>misbruik en fraude te voorkomen en te bestrijden;</li>
            <li>naleving van deze algemene voorwaarden te controleren;</li>
            <li>overtredingen van dit artikel vast te stellen;</li>
            <li>passende maatregelen te nemen ter bescherming van gebruikers en het platform.</li>
          </ul>
          <p>De monitoring kan (deels) plaatsvinden door middel van geautomatiseerde systemen, waaronder het herkennen van bepaalde woorden, patronen of signalen. Indien noodzakelijk kan aanvullende menselijke beoordeling plaatsvinden.</p>
          <p>Indien UGC.NL vaststelt dat een Gebruiker handelt in strijd met dit artikel, is UGC.NL gerechtigd om, zonder voorafgaande ingebrekestelling en zonder verplichting tot schadevergoeding, één of meerdere van de volgende maatregelen te nemen:</p>
          <ul>
            <li>Het geven van een waarschuwing;</li>
            <li>het beperken of blokkeren van (delen van) de functionaliteit van het platform;</li>
            <li>het tijdelijk of permanent beëindigen van het Account;</li>
          </ul>
        </div>

        <!-- SECTION 9 -->
        <div class="terms-section" id="section-9">
          <h2>9. Privacy</h2>
          <p><strong>9.1.</strong> UGC.NL verwerkt de persoonsgegevens van Gebruiker die nodig zijn voor het in stand houden van de website en het verlenen van diensten aan Gebruiker.</p>
          <p><strong>9.2.</strong> Gebruiker wordt uitdrukkelijk verzocht haar persoonlijke gegevens zoveel mogelijk te beschermen. UGC.NL verzoekt Gebruiker niet zonder meer iedere persoonlijke informatie, zoals wachtwoorden, kopie van identiteitsbewijzen of IBAN-nummers, aan derden te verstrekken. Gebruiker is zelf verantwoordelijk voor de gevolgen doordat zij gegevens aan derden verstrekt.</p>
          <p><strong>9.3.</strong> Gebruiker kan op ieder gewenst moment bezwaar maken tegen de verwerking van persoonsgegevens die niet noodzakelijk zijn voor de nakoming van de overeenkomst. Het maken van bezwaar en het daardoor zullen staken van de verwerking door UGC.NL, geeft UGC.NL het recht de overeenkomst te ontbinden.</p>
          <p><strong>9.4.</strong> Persoonsgegevens worden nimmer zonder toestemming van Gebruiker aan derden verstrekt. Het is wel mogelijk dat gegevens aan derden worden verstrekt indien en voor zover dit noodzakelijk is voor de uitvoering van deze overeenkomst. Deze gegevens worden door de hier bedoelde derden nooit voor een ander doel gebruikt en na uitvoering van de overeenkomst verwijderd.</p>
          <p><strong>9.5.</strong> Alle gegevens kunnen, nadat zij geanonimiseerd zijn, door UGC.NL worden gebruikt voor promotie-, trainings- en adviesdoeleinden. Alle gegevens worden na verwijdering, om welke reden dan ook, geanonimiseerd bewaard en als zodanig mogelijk gebruikt.</p>
        </div>

        <!-- SECTION 10 -->
        <div class="terms-section" id="section-10">
          <h2>10. Forum-, rechtskeuze en overdracht van rechten</h2>
          <p><strong>10.1.</strong> UGC.NL is bevoegd haar rechten en verplichtingen onder deze overeenkomst aan een derde partij over te dragen. Gebruiker is slechts bevoegd haar rechten en plichten aan een derde over te dragen met schriftelijke toestemming van UGC.NL.</p>
          <p><strong>10.2.</strong> Op deze - en andere tussen partijen gesloten - overeenkomst(en) is uitsluitend Nederlands recht van toepassing, met uitdrukkelijke uitzondering van het Weens Koopverdrag. Mocht in de toekomst tussen partijen een verbintenis ontstaan, anders dan voortvloeiend uit een overeenkomst, dan is op die verbintenis tevens Nederlands recht van toepassing.</p>
          <p><strong>10.3.</strong> In het geval dat uit de overeenkomst tussen partijen een geschil voortvloeit, is de exclusief absoluut bevoegde rechter de rechter in het arrondissement van de gemeente waarin het hoofdkantoor van UGC.NL gevestigd is. In het geval dat tussen partijen een geschil ontstaan omtrent niet-contractuele verbintenissen is tevens de exclusief absoluut bevoegde rechter de rechter in het arrondissement van de gemeente waarin het hoofdkantoor van UGC.NL gevestigd is.</p>
        </div>
'''

# Continue with payment terms sections (11-25) and OPP section (26)
# Due to length, I'll continue in the next part...

print("Created first part of content")
