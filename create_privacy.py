#!/usr/bin/env python3
"""Script to create the complete privacy.html page"""

# Read header and footer from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract header (until </header>)
header_end = index_content.find('</header>')
header = index_content[:header_end + len('</header>')]

# Extract footer (from <!-- FOOTER -->)
footer_start = index_content.find('<!-- FOOTER -->')
footer = index_content[footer_start:]

# Privacy content sections
privacy_content = '''        <!-- SECTION INTRO -->
        <div class="terms-section" id="section-intro">
          <h2>Privacy Policy</h2>
          <p>Bij UGC.NL hechten we waarde aan de bescherming van de privacy van iedereen die onze diensten gebruikt. In deze privacy policy geven we aan hoe wij met persoonsgegevens omgaan en uw privacy beschermen.</p>
        </div>

        <!-- SECTION CONTACT -->
        <div class="terms-section" id="section-contact">
          <h2>Contactgegevens</h2>
          <ul>
            <li>Website: UGC.NL</li>
            <li>Adres: Keizersgracht 520 H</li>
            <li>Postcode: 1017 EK</li>
          </ul>
        </div>

        <!-- SECTION PROCESSING -->
        <div class="terms-section" id="section-processing">
          <h2>Verwerking van persoonsgegevens</h2>
          <p>Wij verwerken alleen persoonsgegevens voor zover dat nodig is om invulling te geven aan onze taken.</p>
          <p>De volgende persoonsgegevens verwerken wij:</p>
          <ul>
            <li>e-mailadres,</li>
            <li>voornaam,</li>
            <li>tussenvoegsel,</li>
            <li>achternaam,</li>
            <li>adresgegevens,</li>
            <li>geboortedatum,</li>
            <li>geboorteplaats,</li>
            <li>geslacht,</li>
            <li>telefoonnummer,</li>
            <li>klantnummer,</li>
            <li>bestelhistorie,</li>
            <li>bankgegevens,</li>
            <li>overige relevante persoonsgegevens.</li>
          </ul>
          <p>De persoonsgegevens gebruiken we alleen voor de volgende doelen:</p>
          <ul>
            <li>om contact met u te kunnen onderhouden,</li>
            <li>uitvoering van de overeenkomst met u,</li>
            <li>verzenden van nieuwsbrieven,</li>
            <li>u op de hoogte te brengen van nieuwe ontwikkelingen, waaronder aanbiedingen,</li>
            <li>te voldoen aan onze administratieve verplichtingen,</li>
            <li>fraude te bestrijden.</li>
          </ul>
        </div>

        <!-- SECTION SENSITIVE -->
        <div class="terms-section" id="section-sensitive">
          <h2>Bijzondere en/of gevoelige persoonsgegevens</h2>
          <p>Wij verwerken alleen persoonsgegevens van personen jonger dan 16 jaar als we daar toestemming voor hebben van diegene met het ouderlijk gezag. Door persoonsgegevens ter verwerking aan ons aan te bieden verklaart u ten minste 16 jaar oud te zijn of voor de verwerking toestemming te hebben van ouders of andere personen met het ouderlijk gezag. Als we constateren dat een persoon in ons bestand jonger is dan 16 jaar en voor de verwerking niet is ingestemd door een persoon met het ouderlijk gezag dan verwijderen we de persoonsgegevens.</p>
          <p>Mocht u aanwijzingen hebben dat wij zonder toestemming van de bevoegde persoon persoonsgegevens van een persoon jonger dan 16 verwerken, neem dan contact met ons op via contact@ugc.nl zodat wij de betreffende gegevens kunnen verwijderen.</p>
        </div>

        <!-- SECTION RETENTION -->
        <div class="terms-section" id="section-retention">
          <h2>Bewaartermijn van persoonsgegevens</h2>
          <p>Om het risico op verlies van persoonsgegevens zo veel mogelijk te beperken, bewaren wij persoonsgegevens maar één jaar. Dit doen we voor uw gemak. Door uw persoonsgegevens een jaar te bewaren, is het voor u niet nodig om telkens uw persoonsgegevens aan ons te verstrekken.</p>
        </div>

        <!-- SECTION SECURITY -->
        <div class="terms-section" id="section-security">
          <h2>Beveiliging van persoonsgegevens</h2>
          <p>We zijn zuinig op uw persoonsgegevens en we hebben daarom de volgende maatregelen genomen om misbruik, verlies, onbevoegde toegang, ongewenste openbaarmaking en ongeoorloofde wijziging tegen te gaan.</p>
          <ul>
            <li>De verbinding met de website UGC.NL komt tot stand door middel van een beveiligde verbinding.</li>
            <li>De computers waarop de persoonsgegevens worden verwerkt en opgeslagen zijn altijd voorzien van de laatste veiligheidsupdates van Windows of Apple.</li>
            <li>De computers waarop de persoonsgegevens worden verwerkt en opgeslagen zijn voorzien van een adequate virusscanner.</li>
            <li>De groep van medewerkers die toegang hebben tot de persoonsgegevens is tot een minimum beperkt.</li>
            <li>Alle medewerkers die toegang hebben tot persoonsgegevens zijn gebonden aan een geheimhoudingsovereenkomst gericht op de bescherming van de persoonsgegevens.</li>
            <li>Met alle externe partijen die inzage hebben in persoonsgegevens is een verwerkersovereenkomst gesloten op grond waarvan deze derden zich hebben verplicht om geheimhouding in acht te nemen en de persoonsgegevens alleen in opdracht van UGC.NL te verwerken.</li>
          </ul>
          <p>Hebt u toch het vermoeden dat uw gegevens niet goed beveiligd zijn of hebt u aanwijzingen van misbruik van uw gegevens, laat ons dat dan weten via het aanvraagformulier.</p>
        </div>

        <!-- SECTION SHARING -->
        <div class="terms-section" id="section-sharing">
          <h2>Delen van persoonsgegevens met derden</h2>
          <p>Wij verkopen persoonsgegevens uiteraard niet aan derden en verstrekken deze uitsluitend aan anderen indien dat nodig is voor de uitvoering van onze overeenkomst met u of om te voldoen aan een wettelijke verplichting. Met bedrijven die uw gegevens verwerken in onze opdracht sluiten wij verwerkersovereenkomsten om ervoor te zorgen dat onze partners eenzelfde niveau van beveiliging en vertrouwelijkheid van de persoonsgegevens hanteren.</p>
        </div>

        <!-- SECTION COOKIES -->
        <div class="terms-section" id="section-cookies">
          <h2>Cookies op UGC.NL</h2>
          <p>Om onze website optimaal te laten functioneren, gebruiken we diensten van derden, maar ook hierbij denken we aan uw privacy. De cookies op onze website brengen uw privacy niet in gevaar. Een cookie is een klein tekstbestand dat bij het eerste bezoek aan onze website wordt opgeslagen op de computer, tablet of smartphone. De cookies zorgen ervoor dat de website naar behoren functioneert en dat voorkeursinstellingen bewaard blijven. Wij, en de door ons eventueel ingeschakelde derden, verwerken uw IP-adres niet op een wijze die herleidbaar is tot u. Via de instellingen van uw browser kunnen cookies worden verwijderd. Daarnaast is het ook mogelijk om de browser zo in te stellen dat cookies niet meer worden opgeslagen.</p>
        </div>

        <!-- SECTION MONITORING -->
        <div class="terms-section" id="section-monitoring">
          <h2>Monitoring en analyse van communicatie via het platform</h2>
          <p>Communicatie tussen gebruikers die plaatsvindt via het UGC.NL-platform kan persoonsgegevens bevatten. UGC.NL verwerkt deze communicatiegegevens in beperkte mate.</p>
          <p>UGC.NL monitort en analyseert communicatie via het platform uitsluitend voor de volgende doeleinden:</p>
          <ul>
            <li>het voorkomen en bestrijden van misbruik, fraude en andere ongewenste handelingen;</li>
            <li>het handhaven van de algemene voorwaarden van UGC.NL, waaronder het verbod op het zoeken van contact buiten het platform om;</li>
            <li>het waarborgen van de veiligheid en integriteit van het platform en haar gebruikers;</li>
            <li>het verkrijgen van inzichten ter verbetering en optimalisatie van het platform en de dienstverlening.</li>
          </ul>
          <p>De verwerking van deze communicatiegegevens vindt plaats op basis van het gerechtvaardigd belang van UGC.NL, bestaande uit het beschermen van het platform, het handhaven van contractuele afspraken en het verbeteren van haar diensten.</p>
          <p>Voor deze doeleinden kan gebruik worden gemaakt van (deels) geautomatiseerde analyse, zoals het herkennen van bepaalde woorden of patronen in communicatie. Besluiten die gevolgen kunnen hebben voor gebruikers worden niet uitsluitend gebaseerd op geautomatiseerde verwerking; waar nodig vindt altijd menselijke beoordeling plaats.</p>
          <p>De inhoud van communicatie wordt niet langer bewaard dan noodzakelijk voor de hierboven genoemde doeleinden en in overeenstemming met de in deze privacy policy opgenomen bewaartermijnen.</p>
        </div>

        <!-- SECTION RIGHTS -->
        <div class="terms-section" id="section-rights">
          <h2>Rechten van personen waarvan wij persoonsgegevens verwerken</h2>
          <p>Uw gegevens blijven van u. U hebt altijd de mogelijkheid om in te zien welke gegevens we van u verwerken, de gegevens te laten corrigeren of te laten verwijderen. Daarnaast kunt u uw toestemming voor de gegevensverwerking intrekken of bezwaar maken tegen de verwerking van uw gegevens door ons. Als u dat wilt versturen wij uw gegevens in een computerbestand naar u of naar een door u aangewezen organisatie.</p>
        </div>

        <!-- SECTION OTHER -->
        <div class="terms-section" id="section-other">
          <h2>Overig</h2>
          <h3>Geautomatiseerde besluitvorming</h3>
          <p>Wij gebruiken persoonsgegevens niet voor geautomatiseerde besluiten. Dit spreekt uiteraard voor zich maar zijn wij verplicht om het te vermelden.</p>
          <h3>Klachten bij de Autoriteit Persoonsgegevens</h3>
          <p>Voor de volledigheid wijzen we erop dat er een mogelijkheid is om bij de Autoriteit Persoonsgegevens over de verwerking van uw gegevens te klagen. Dat kan via de volgende link.</p>
          <h3>Wijzigingen</h3>
          <p>UGC.NL behoudt zich het recht voor om zonder nadere kennisgeving wijzigingen aan te brengen in de Privacy Policy. Deze wijzigingen zullen direct na het plaatsen ervan op de site van kracht zijn.</p>
          <p>Deze Privacy Policy is voor het laatst gewijzigd op 8 maart 2024.</p>
          <p>Wij hopen u hiermee voldoende te hebben geïnformeerd.</p>
          <p>Deze privacy policy is opgesteld door Bleijerveld Juridisch advies.</p>
        </div>

        <!-- SECTION OPP PRIVACY -->
        <div class="terms-section" id="section-opp-privacy">
          <h2>Aanvullende Privacyverklaring – Online Payment Platform B.V.</h2>
          <p>De onderstaande tekst is afkomstig van Online Payment Platform B.V. ("OPP") en geldt voor iedereen die via UGC.NL B.V. gebruikmaakt van de betaaldiensten van OPP. Deze verklaring maakt geen onderdeel uit van het privacybeleid van UGC.NL B.V., maar geldt aanvullend daarop.</p>
          <p>UGC.NL B.V. publiceert deze verklaring uitsluitend om haar gebruikers volledig te informeren over het beleid van OPP.</p>
          <p>Alle rechten, plichten en verantwoordelijkheden die hieronder worden beschreven, liggen bij OPP.</p>
          <h3>1. Inleiding</h3>
          <p>Deze privacyverklaring beschrijft hoe Online Payment Platform B.V. en haar groepsmaatschappijen in de Europese Unie en het Verenigd Koninkrijk (gezamenlijk: "OPP", "wij", "ons" of "onze") persoonsgegevens van gebruikers verzamelen, gebruiken, bewaren en delen. Het document legt uit welke soorten gegevens wij verwerken, voor welke doeleinden, hoe lang wij deze bewaren en welke rechten jij hebt.</p>
          <p>Wij verzamelen en verwerken persoonsgegevens uitsluitend om onze betaaldiensten correct te laten verlopen en om te voldoen aan wettelijke verplichtingen. Wij delen deze gegevens alleen met derden wanneer dit noodzakelijk is voor het uitvoeren van onze diensten of wanneer wij daartoe wettelijk verplicht zijn.</p>
          <h3>2. Algemene uitgangspunten</h3>
          <p>Onze privacyverklaring is opgesteld om jou een duidelijk overzicht te geven. Wij maken gebruik van begrijpelijke taal en een gestructureerde opbouw.</p>
          <p>Je leest hierin:</p>
          <ul>
            <li>Welke persoonsgegevens wij verwerken;</li>
            <li>Hoe wij deze gegevens gebruiken;</li>
            <li>Hoe en waar wij deze gegevens opslaan;</li>
            <li>Welke rechten jij hebt en hoe je deze kunt uitoefenen.</li>
          </ul>
          <h3>3. Derden en externe links</h3>
          <p>Onze website en omgeving kunnen links bevatten naar externe websites, plug-ins en applicaties van derden. Wanneer je op een dergelijke link klikt of deze inschakelt, kunnen deze derden gegevens over jou verzamelen. OPP heeft geen invloed op deze externe partijen en is niet verantwoordelijk voor hun privacybeleid.</p>
          <p>Wij raden aan om altijd het privacybeleid van iedere externe partij te lezen voordat je persoonsgegevens verstrekt.</p>
          <h3>4. Onze organisatie</h3>
          <p>Online Payment Platform B.V. is een vergunninghoudende betaalinstelling onder toezicht van De Nederlandsche Bank (DNB) en opereert binnen de Europese Economische Ruimte. Wij faciliteren betalingen voor begunstigden via platformen en marktplaatsen ("Platformpartners") die onze software en diensten hebben geïntegreerd.</p>
          <p>Daarnaast opereert OPP in het Verenigd Koninkrijk onder een vergunning van de Financial Conduct Authority (FCA). Gelden die wij namens begunstigden ontvangen, worden beheerd door de Stichting Online Payments Foundation, die deze gelden gescheiden houdt van het vermogen van OPP.</p>
          <h3>5. Categorieën persoonsgegevens die wij verzamelen</h3>
          <ul>
            <li><strong>Contactgegevens:</strong> zoals naam, adres, e-mailadres en telefoonnummer.</li>
            <li><strong>Identiteitsgegevens:</strong> zoals voornaam, achternaam, gebruikersnaam, kopie van legitimatiebewijs, fiscaal identificatienummer of BSN (indien wettelijk verplicht).</li>
            <li><strong>KYC-gegevens (Know Your Customer):</strong> inclusief adres, contactgegevens, bankrekeningnummer, gegevens van wettelijke vertegenwoordigers en aandeelhouders, informatie over uiteindelijke begunstigden, bankafschriften, handtekening, uittreksel uit het handelsregister, en andere aanvullende identificatiegegevens.</li>
            <li><strong>Transactiegegevens:</strong> details over betalingen die via OPP plaatsvinden tussen betaler en begunstigde.</li>
            <li><strong>Technische gegevens:</strong> IP-adres, inloggegevens, browsertype en -versie, tijdzone, locatiegegevens, plug-inversies, besturingssysteem en andere technische gegevens.</li>
            <li><strong>Gebruiksgegevens:</strong> informatie over hoe onze website en diensten worden gebruikt.</li>
            <li><strong>Sollicitatiegegevens:</strong> gegevens verstrekt bij sollicitaties, zoals CV, motivatiebrief, werkervaring, kwalificaties, geboortedatum en geslacht.</li>
            <li><strong>Marketing- en communicatiegegevens:</strong> voorkeuren voor het ontvangen van marketinginformatie, nieuwsbrieven en promoties.</li>
            <li><strong>Gegevens van speciale categorieën:</strong> waaronder informatie over ras of etniciteit, religieuze of filosofische overtuigingen, seksuele geaardheid, politieke opvattingen, vakbondslidmaatschap, gezondheidsinformatie en gegevens over strafrechtelijke veroordelingen of beschuldigingen.</li>
            <li><strong>Geaggregeerde gegevens:</strong> statistische of demografische gegevens die niet herleidbaar zijn tot een individu.</li>
          </ul>
          <h3>6. Gevolgen van het niet verstrekken van gegevens</h3>
          <p>Indien wij wettelijk verplicht zijn om gegevens te verzamelen, of deze noodzakelijk zijn voor het uitvoeren van onze overeenkomst, en jij weigert deze te verstrekken, kan dit ertoe leiden dat wij onze diensten niet (volledig) kunnen uitvoeren.</p>
          <h3>7. Bronnen van gegevens</h3>
          <ul>
            <li><strong>Direct contact:</strong> via formulieren, e-mail, telefoon, post, onze website of het betaalportaal.</li>
            <li><strong>Automatisch:</strong> door cookies, serverlogs en andere technologieën tijdens gebruik van onze website of systemen.</li>
            <li><strong>Derden:</strong> zoals Platform-partners, openbare registers, sociale media en andere externe bronnen.</li>
          </ul>
          <h3>8. Doeleinden en rechtsgrondslagen voor verwerking</h3>
          <p>Wij gebruiken persoonsgegevens alleen als dit wettelijk is toegestaan, op basis van:</p>
          <ul>
            <li>Uitvoering van een overeenkomst;</li>
            <li>Wettelijke verplichting;</li>
            <li>Gerechtvaardigd belang;</li>
            <li>Toestemming.</li>
          </ul>
          <p>Voorbeelden van verwerkingsdoeleinden:</p>
          <ul>
            <li><strong>Onboarding:</strong> aanmaken en beheren van accounts, uitvoeren van identificatie- en verificatieprocedures.</li>
            <li><strong>Levering betaaldiensten:</strong> verwerken van betalingen, uitvoeren van escrow-diensten, bemiddelen bij geschillen.</li>
            <li><strong>Beveiliging:</strong> fraudepreventie, witwascontrole, bescherming tegen cyberaanvallen.</li>
            <li><strong>Communicatie:</strong> klantenservice, notificaties, marketing (indien toegestaan).</li>
            <li><strong>Werving:</strong> verwerking van sollicitatiegegevens en uitvoering van selectieprocedures.</li>
          </ul>
          <h3>9. Delen van persoonsgegevens</h3>
          <p>Wij delen gegevens alleen met derden wanneer dit noodzakelijk is voor onze dienstverlening of wanneer wij daartoe wettelijk verplicht zijn.</p>
          <p>Derden kunnen zijn:</p>
          <ul>
            <li>IT-dienstverleners;</li>
            <li>Betaalpartners en banken;</li>
            <li>KYC-verificatiepartners;</li>
            <li>Juridische en fiscale adviseurs;</li>
            <li>Overheidsinstanties en toezichthouders.</li>
          </ul>
          <p>Met al onze dienstverleners sluiten wij verwerkersovereenkomsten om de bescherming van jouw gegevens te waarborgen.</p>
          <h3>10. Bewaartermijnen</h3>
          <p>Wij bewaren persoonsgegevens niet langer dan nodig is voor het doel waarvoor ze zijn verzameld, tenzij een langere bewaartermijn wettelijk verplicht is of noodzakelijk is om juridische claims te behandelen.</p>
          <p>Sollicitatiegegevens bewaren wij:</p>
          <ul>
            <li><strong>Nederland:</strong> 1 maand na afwijzing (tenzij toestemming voor langer bewaren, maximaal 1 jaar).</li>
            <li><strong>Andere EER-landen:</strong> 6 maanden (tenzij toestemming voor langer bewaren, maximaal 1 jaar).</li>
          </ul>
          <h3>11. Beveiligingsmaatregelen</h3>
          <p>Wij hanteren technische en organisatorische maatregelen om persoonsgegevens te beschermen tegen ongeoorloofde toegang, verlies, vernietiging of wijziging. Deze maatregelen worden regelmatig geëvalueerd en aangepast aan de actuele dreigingen.</p>
          <h3>12. Doorgifte buiten de EER</h3>
          <p>Wanneer wij gegevens doorgeven buiten de Europese Economische Ruimte of het Verenigd Koninkrijk, doen wij dit uitsluitend met passende waarborgen, zoals:</p>
          <ul>
            <li>Standaardcontractbepalingen;</li>
            <li>Intragroepsovereenkomsten;</li>
            <li>Andere door de wet goedgekeurde mechanismen.</li>
          </ul>
          <h3>13. Jouw rechten</h3>
          <ul>
            <li>Inzage te vragen in jouw persoonsgegevens;</li>
            <li>Correctie van onjuiste gegevens te vragen;</li>
            <li>Verwijdering van gegevens te verzoeken;</li>
            <li>Beperking van verwerking te eisen;</li>
            <li>Bezwaar te maken tegen verwerking op basis van gerechtvaardigd belang;</li>
            <li>Gegevensoverdraagbaarheid te vragen;</li>
            <li>Toestemming in te trekken (waar van toepassing).</li>
          </ul>
          <h3>14. Klachten</h3>
          <p>Voor vragen of klachten kun je contact opnemen met:</p>
          <ul>
            <li>E-mail: privacy@onlinepaymentplatform.com</li>
            <li>Adres: Kanaalweg 1, 2628 EB Delft, Nederland</li>
          </ul>
          <p>Je kunt ook een klacht indienen bij de Autoriteit Persoonsgegevens of een andere bevoegde toezichthouder.</p>
          <h3>15. Wijzigingen in deze verklaring</h3>
          <p>Deze verklaring kan worden gewijzigd wanneer wetgeving of onze werkwijze verandert. De actuele versie is altijd beschikbaar op onze website.</p>
        </div>

        <!-- SECTION OPP ACCOUNT -->
        <div class="terms-section" id="section-opp-account">
          <h2>Beleid voor Account Sluiten – Online Payment Platform B.V.</h2>
          <p>Dit beleid is opgesteld door Online Payment Platform B.V. (OPP) en geldt aanvullend op de voorwaarden van UGC.NL B.V. Alle hieronder beschreven procedures en verplichtingen komen rechtstreeks van OPP.</p>
          <h3>1. Sluiten van je account</h3>
          <p>Je kunt jouw OPP-account op elk moment sluiten. Hiervoor gelden de volgende stappen:</p>
          <ul>
            <li>Inloggen op jouw account;</li>
            <li>Contact opnemen met onze klantenservice via de supportpagina;</li>
            <li>Eventuele openstaande transacties afronden;</li>
            <li>Bevestiging van de sluiting ontvangen via e-mail.</li>
          </ul>
          <h3>2. Gevolgen van accountsluiting</h3>
          <ul>
            <li>Je hebt geen toegang meer tot de OPP-diensten;</li>
            <li>Eventuele lopende escrow-betalingen worden eerst afgehandeld;</li>
            <li>Wettelijke bewaartermijnen voor transactiegegevens blijven van kracht.</li>
          </ul>
          <h3>3. Sluiting door OPP</h3>
          <p>OPP kan jouw account sluiten in de volgende gevallen:</p>
          <ul>
            <li>Overtreding van de gebruiksvoorwaarden;</li>
            <li>Fraude of misbruik;</li>
            <li>Wettelijke verplichting.</li>
          </ul>
          <h3>4. Contact</h3>
          <ul>
            <li>E-mail: support@onlinepaymentplatform.com</li>
            <li>Adres: Kanaalweg 1, 2628 EB Delft, Nederland</li>
          </ul>
        </div>
'''

# TOC
toc = '''      <!-- TOC RIGHT -->
      <div class="terms-toc">
        <h3>Inhoudsopgave</h3>
        <ul class="terms-toc-list">
          <li class="terms-toc-item"><a href="#section-intro" class="terms-toc-link">Privacy Policy</a></li>
          <li class="terms-toc-item"><a href="#section-contact" class="terms-toc-link">Contactgegevens</a></li>
          <li class="terms-toc-item"><a href="#section-processing" class="terms-toc-link">Verwerking van persoonsgegevens</a></li>
          <li class="terms-toc-item"><a href="#section-sensitive" class="terms-toc-link">Bijzondere en/of gevoelige persoonsgegevens</a></li>
          <li class="terms-toc-item"><a href="#section-retention" class="terms-toc-link">Bewaartermijn van persoonsgegevens</a></li>
          <li class="terms-toc-item"><a href="#section-security" class="terms-toc-link">Beveiliging van persoonsgegevens</a></li>
          <li class="terms-toc-item"><a href="#section-sharing" class="terms-toc-link">Delen van persoonsgegevens met derden</a></li>
          <li class="terms-toc-item"><a href="#section-cookies" class="terms-toc-link">Cookies op UGC.NL</a></li>
          <li class="terms-toc-item"><a href="#section-monitoring" class="terms-toc-link">Monitoring en analyse van communicatie via het platform</a></li>
          <li class="terms-toc-item"><a href="#section-rights" class="terms-toc-link">Rechten van personen waarvan wij persoonsgegevens verwerken</a></li>
          <li class="terms-toc-item"><a href="#section-other" class="terms-toc-link">Overig</a></li>
          <li class="terms-toc-item"><a href="#section-opp-privacy" class="terms-toc-link">Aanvullende Privacyverklaring – Online Payment Platform B.V.</a></li>
          <li class="terms-toc-item"><a href="#section-opp-account" class="terms-toc-link">Beleid voor Account Sluiten – Online Payment Platform B.V.</a></li>
        </ul>
      </div>'''

# Build the page
html_content = '''<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Privacyverklaring - UGC.NL</title>
  <meta name="description" content="Privacyverklaring van UGC.NL">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
''' + header + '''

  <!-- HERO SECTION -->
  <section class="section" style="padding-top: var(--spacing-3xl); padding-bottom: var(--spacing-lg);">
    <div class="container">
      <h1 style="font-size: clamp(32px, 4vw, 48px); font-weight: var(--font-weight-bold); margin-bottom: var(--spacing-sm);">Privacyverklaring</h1>
      <p style="color: var(--color-text-secondary); font-size: var(--font-size-body);">Laatst gewijzigd: 8 maart 2024</p>
    </div>
  </section>

  <!-- MAIN CONTENT -->
  <section class="section" style="padding-top: 0;">
    <div class="terms-page-container">
      <!-- CONTENT LEFT -->
      <div class="terms-content">
''' + privacy_content + '''
      </div>
      
''' + toc + '''
    </div>
  </section>
''' + footer + '''
  <script src="script.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const tocLinks = document.querySelectorAll('.terms-toc-link');
      const sections = document.querySelectorAll('.terms-section');

      tocLinks.forEach(link => {
        link.addEventListener('click', function(e) {
          e.preventDefault();
          const targetId = this.getAttribute('href').substring(1);
          const targetSection = document.getElementById(targetId);
          if (targetSection) {
            window.scrollTo({
              top: targetSection.offsetTop - 90,
              behavior: 'smooth'
            });
          }
        });
      });

      const updateActiveTOC = () => {
        let currentActive = '';
        const scrollPosition = window.scrollY + 200;
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;
        
        const isAtBottom = window.scrollY + windowHeight >= documentHeight - 100;
        
        for (let i = sections.length - 1; i >= 0; i--) {
          const section = sections[i];
          const sectionTop = section.offsetTop;
          const sectionBottom = sectionTop + section.offsetHeight;
          
          if (isAtBottom && i === sections.length - 1) {
            if (scrollPosition >= sectionTop) {
              currentActive = section.id;
              break;
            }
          } else if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
            currentActive = section.id;
            break;
          }
        }

        tocLinks.forEach(link => {
          link.classList.remove('active');
          const href = link.getAttribute('href');
          if (href === `#${currentActive}` && currentActive !== '') {
            link.classList.add('active');
          }
        });
      };

      window.addEventListener('scroll', updateActiveTOC);
      updateActiveTOC();
    });
  </script>
</body>
</html>
'''

# Write the file
with open('privacy.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Created privacy.html successfully!")
