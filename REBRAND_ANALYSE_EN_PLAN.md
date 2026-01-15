# Rebrand Analyse & Plan - UGC.NL

## 1. Brand Spec (samenvatting uit Rebrand PDF)

### Kleuren
Het kleurenpalet bestaat uit **drie hoofdkleuren**:

| Kleurcode | Omschrijving | Toepassing |
|-----------|--------------|------------|
| `#2484E4` | Primair blauw (logo-kleur) | CTA's, accenten, carrousels, highlights |
| `#F3F7FF` | Lichtblauw | Achtergronden van secties, carrousels en selectieblokken |
| `#FAFAFB` | Lichtgrijs | Algemene achtergronden en rustpunten in de layout |

**Belangrijke regel:** Fades mogen gebruikt worden, mits de donkerste kleur nooit donkerder is dan `#2484E4`.

### Fonts & Typografie

**Huidige situatie:**
- Het huidige lettertype voldoet niet aan de wensen
- Gebruikt momenteel: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif`

**Gewenste font-eigenschappen:**
- Duidelijk onderscheid tussen **light** en **regular** gewicht
- Modern en professioneel
- Past bij een SaaS-gedreven/speels platform
- Zwart moet echt zwart zijn (geen grijze tinten)

**Inspiratie:** Het lettertype van Billo (www.billo.app) wordt als inspirerend gezien, maar mag niet één-op-één worden overgenomen.

**Typografie schaal (huidige implementatie):**
- **H1:** `clamp(36px, 5vw, 64px)` | Bold (700) | Line-height: 1.1 | Letter-spacing: -0.02em
- **H2:** `clamp(28px, 4vw, 48px)` | Bold (700) | Line-height: 1.2 | Letter-spacing: -0.01em
- **H3:** `clamp(24px, 3vw, 32px)` | Semibold (600) | Line-height: 1.3
- **H4:** `20px` | Semibold (600) | Line-height: 1.4
- **Body:** `16px` | Regular (400) | Line-height: 1.6
- **Body Large:** `20px` | Regular (400) | Line-height: 1.5
- **Body Small:** `14px` | Regular (400) | Line-height: 1.5

### Spacing

**Huidige spacing-schaal (CSS variabelen):**
- `--spacing-xs`: 8px
- `--spacing-sm`: 16px
- `--spacing-md`: 24px
- `--spacing-lg`: 32px
- `--spacing-xl`: 48px
- `--spacing-2xl`: 64px
- `--spacing-3xl`: 96px

**Container:**
- Max-width: `1200px`
- Padding: `24px`

### Buttons & UI-stijl

**Button-stijlen:**
1. **Primary Button** (`.btn-primary`)
   - Achtergrond: `#2484E4` (primair blauw)
   - Tekst: Wit
   - Hover: Donkerder blauw (`#1f6fc7`)
   - Border-radius: `8px`
   - Padding: `14px 28px`
   - Font-weight: Semibold (600)

2. **Secondary Button** (`.btn-secondary`)
   - Achtergrond: Transparant
   - Tekst: Zwart
   - Border: 2px solid zwart
   - Hover: Zwarte achtergrond, witte tekst

3. **Outline Button** (`.btn-outline`)
   - Achtergrond: Transparant
   - Tekst: Primair blauw
   - Border: 2px solid primair blauw
   - Hover: Blauwe achtergrond, witte tekst

**UI-principes:**
- **Afgeronde hoeken:** Carrousels en componenten hebben afgeronde hoeken (border-radius: 12px voor cards, 8px voor buttons)
- **Witruimte:** Ruim gebruik van witruimte voor rust en overzicht
- **Consistentie:** Eenduidige styling door hele website
- **Modern & professioneel:** Strakke, moderne uitstraling die past bij SaaS-platform

---

## 2. Huidige Website Structuur

### Tech Stack
- **Frontend:** HTML5 + CSS3
- **Styling:** Custom CSS met CSS variabelen (design system)
- **Framework:** Tailwind CSS (genoemd in PDF, maar momenteel vooral custom CSS)
- **Geen JavaScript frameworks:** Geen React, Vue of Angular
- **Geen build tools:** Geen package.json of build proces gevonden

### Bestandsstructuur
```
website-rebrand/
├── index.html          (Homepage - momenteel alleen test content)
├── blog.html           (Blog overzicht)
├── cases.html          (Succesverhalen overzicht)
├── creators.html       (Vind Creators pagina)
├── services.html       (Services overzicht)
├── login.html          (Inloggen pagina)
├── signup.html         (Registreren pagina)
├── styles.css          (Hoofd CSS bestand met design system)
├── Logo/               (Logo bestanden)
│   └── FULL LOGO.png
├── Brief/              (Rebrand documentatie)
│   └── Rebrand.pdf
└── Rev/                (Screenshot referenties)
```

### Belangrijke Componenten

#### 1. **Header** (`.header`)
- Sticky header met logo, navigatie en CTA's
- Logo: `Logo/FULL LOGO.png`
- Navigatie links: Services, Vind Creators, Blog, Succesverhalen
- CTA rechts: Inloggen (link) + Registreer gratis (button)

#### 2. **Hero Section** (`.hero-section`)
- Verschillende varianten per pagina
- Hero strip met creator profielen (op homepage)
- Tekst sectie met headline, subheadline en CTA's

#### 3. **Footer** (`.footer`)
- Logo bovenaan
- Drie kolommen: Platform, Bedrijf, Juridisch
- Copyright onderaan

#### 4. **Buttons** (`.btn`)
- Drie varianten: primary, secondary, outline
- Consistente styling met hover states

#### 5. **Container & Sections**
- Container: max-width 1200px, centered
- Sections: padding met spacing variabelen

### Huidige Pagina's

1. **Homepage** (`index.html`)
   - Momenteel alleen test content
   - Moet volledig worden herontworpen volgens PDF

2. **Services** (`services.html`)
   - Overzichtspagina met service cards
   - 5 services: E-commerce, Agencies, TikTok, Instagram, Facebook

3. **Vind Creators** (`creators.html`)
   - Creator database met grid layout
   - Hero sectie met gradient achtergrond

4. **Blog** (`blog.html`)
   - Blog overzicht met grid van artikelen
   - Moet naar Storyblok worden gemigreerd

5. **Succesverhalen** (`cases.html`)
   - Case studies overzicht
   - Moet naar Storyblok worden gemigreerd

6. **Login** (`login.html`)
   - Eenvoudig login formulier
   - Moet worden aangepast met nieuw contentblok links

7. **Registreren** (`signup.html`)
   - Registratieformulier met keuze Bedrijf/Creator
   - Moet worden aangepast met nieuw contentblok links

### Design System (huidig)
Het project heeft een goed gestructureerd design system in `styles.css`:
- CSS variabelen voor kleuren, typografie, spacing
- Herbruikbare component classes
- Responsive typography met clamp()
- Consistente button styles

---

## 3. Rebrand Plan (Stappenplan)

### Fase 1: Design System Update

#### Stap 1.1: Font Selectie & Implementatie
- [ ] Onderzoek doen naar geschikte fonts die voldoen aan eisen:
  - Duidelijk onderscheid light/regular
  - Modern & professioneel
  - SaaS-geschikt
  - Echt zwart
- [ ] Font selecteren (bijv. Inter, Poppins, DM Sans, of custom font)
- [ ] Font implementeren in CSS variabelen
- [ ] Testen op verschillende gewichten (light, regular, semibold, bold)

#### Stap 1.2: Kleurenpalet Verificatie
- [ ] Controleren of huidige kleuren (`#2484E4`, `#F3F7FF`, `#FAFAFB`) correct zijn
- [ ] Fade-kleuren definiëren (max donkerste: `#2484E4`)
- [ ] Kleuren toevoegen aan CSS variabelen indien nodig

#### Stap 1.3: Spacing & Typography Review
- [ ] Huidige spacing-schaal evalueren
- [ ] Typography schaal verifiëren (H1-H6, body)
- [ ] Aanpassingen maken indien nodig volgens nieuwe brand guide

### Fase 2: Homepage Redesign

#### Stap 2.1: Hero Section
- [ ] **Optie 1 implementeren:** Grote automatisch doorschuivende carrousels (Figma referentie)
  - Afgeronde hoeken
  - Creator profielen uit database
- [ ] **Optie 2 implementeren:** Carrousels rechts met cirkelvormige animatie (Tailwind CSS referentie)
  - Links draaiend
  - Creator profielen
- [ ] Beide opties live zetten voor vergelijking
- [ ] Teksten implementeren:
  - Titel: "Snelle, betaalbare advertentievideo's via creators."
  - Subtekst: (uit PDF)
  - Primaire CTA: "Registreer gratis" (dropdown: Creator/Bedrijf)
  - Secundaire CTA: "Boek een demo"

#### Stap 2.2: Merken Carrousel
- [ ] Logo cloud redesign:
  - Alle logo's zelfde visuele grootte
  - Zwart-wit weergave
  - Volledige breedte vulling
- [ ] Titel: "Vertrouwd door 2,000+ merken"
- [ ] Logo's ophalen uit Google Drive en verwerken
- [ ] Achtergrondkleur bepalen (wit/grijs/blauw)

#### Stap 2.3: Brug tussen Merken en Creators
- [ ] Split-screen design: Links grijs, rechts blauw met fade
- [ ] Links: Bedrijven sectie
  - Titel, subtitel, subtext
  - 4 bullet points
  - CTA: "Ontdek meer"
- [ ] Rechts: Creators sectie
  - Titel, subtitel, subtext
  - 4 bullet points
  - CTA: "Ontdek meer"
- [ ] Content pieces ophalen uit Google Drive

#### Stap 2.4: Waarom UGC.NL Carrousel
- [ ] Nieuwe iconen ontwerpen (consistent met bestaande stijl)
- [ ] Carrousel restylen (inspiratie: Billo)
- [ ] Teksten implementeren:
  - Titel: "Waarom slimme merken kiezen voor UGC.NL"
  - Subtekst: "Vind creators en ontvang direct inzetbare ads."

#### Stap 2.5: Zo werkt UGC.NL
- [ ] Stap 3 verwijderen (voor creators én bedrijven)
- [ ] 3-stappen proces implementeren
- [ ] Design inspiratie: Billo "how it works"
- [ ] Achtergrond: Fade met `#F3F7FF`
- [ ] Content pieces ophalen uit Google Drive

#### Stap 2.6: Creator Overview (NIEUW)
- [ ] Nieuw carrousel met creator preview per niche
- [ ] 10 niches: Tech, Food & Health, Fashion, Beauty, Pets, Fitness, Travel, Home & Interior, Recruitment, Family & Kids
- [ ] Iconen ontwerpen per niche
- [ ] Talen weergave: Nederlands, Vlaams, Engels, Duits + "en meer"
- [ ] CTA: "Vind creators"
- [ ] Design consistent met `/vind-creators` pagina

#### Stap 2.7: Boek een Demo Balk
- [ ] Restylen (huidige fade te donker)
- [ ] Tekst: "Benieuwd hoe UGC.NL werkt? Boek gratis een korte demo."
- [ ] CTA: "Plan een gesprek"
- [ ] Bestanden ophalen uit Google Drive

#### Stap 2.8: UGC Advertentievideo's Sectie (NIEUW)
- [ ] Split design (zoals "Brug tussen merken en creators")
- [ ] Links: Voor bedrijven (eCom, digitale producten, B2B)
- [ ] Rechts: Voor agencies
- [ ] Content pieces ophalen uit Google Drive
- [ ] CTA's: "Lees meer" en "Bekijk het aanbod"

#### Stap 2.9: Vergelijking Carrousel (NIEUW)
- [ ] Design inspiratie: Billo vergelijking
- [ ] Tekst aanpassen: "1,500+ actieve creators"
- [ ] CTA: "Probeer gratis!"
- [ ] (i)-iconen toevoegen bij kopteksten (tooltip/hover)
- [ ] 6 voordelen implementeren

#### Stap 2.10: Merksucces Carrousel (NIEUW)
- [ ] Preview van case studies (3-4 stuks)
- [ ] Filters voor relevante cases
- [ ] CTA: "Lees volledige case study"
- [ ] Case studies ophalen uit Google Drive

#### Stap 2.11: Alles op één plek (RESTYLE)
- [ ] Achtergrondfade aanpassen (max donkerste: `#2484E4`)
- [ ] Lichte herontwerp voor betere aansluiting
- [ ] Fade met `#F3F7FF` (zoals Billo)

#### Stap 2.12: Flexibele Prijsopties (RESTYLE)
- [ ] Iconen restylen (linkerzijde)
- [ ] Rechterzijde behouden (gebruikt in dashboard)

#### Stap 2.13: FAQ (RESTYLE)
- [ ] Nieuwe styling (strakker, frisser)
- [ ] Scheiding tussen bedrijven en creators (tabs/filters/secties)
- [ ] Nieuwe Q&A's implementeren (uit Google Drive)

#### Stap 2.14: Footer (RESTYLE)
- [ ] Volledig nieuw ontwerp
- [ ] Consistent met nieuwe visuele stijl

### Fase 3: Overige Pagina's

#### Stap 3.1: Vind Creators Pagina
- [ ] Hero sectie:
  - Titel: "1500+ handmatig gescreende creators"
  - Subtext: (uit PDF)
  - Achtergrond: Fade met `#F3F7FF`
- [ ] Merken carrousel toevoegen (bovenaan)
- [ ] Creator overview carrousel (zoals homepage)
- [ ] Case studies carrousel toevoegen
- [ ] Dedicated FAQ sectie

#### Stap 3.2: Blog Pagina
- [ ] Storyblok integratie voorbereiden
- [ ] Design inspiratie: Billo blog
- [ ] Overzichtelijke structuur
- [ ] Visueel aangepast aan branding

#### Stap 3.3: Succesverhalen Pagina
- [ ] Storyblok integratie voorbereiden
- [ ] Hero: "Zo helpen we merken zoals dat van jou groeien"
- [ ] Merken carrousel onder button
- [ ] Case studies grid
- [ ] Niches filter (bolletjes, zoals Vind Creators)
- [ ] Detail pagina design (inspiratie: Billo)
- [ ] Demo call inplanner onder thumbnails

#### Stap 3.4: Services Pagina's
- [ ] **E-commerce pagina:**
  - Hero, Merken, Waarom UGC.NL, Creators carrousel, Succesverhalen, Demo call, FAQ
- [ ] **Agencies pagina:**
  - Hero, Merken, Creators carrousel, Contactformulier, Succesverhalen
- [ ] **Socials pagina's (TikTok, Instagram, Facebook):**
  - Hero, Merken, Creators carrousel, Succesverhalen, Vergelijking carrousel, Demo call, FAQ
- [ ] Storyblok integratie voorbereiden
- [ ] Bestanden ophalen uit Google Drive

#### Stap 3.5: Boek een Call (Hidden Page)
- [ ] Design inspiratie: Billo book-a-call
- [ ] Calendly integratie: `https://calendly.com/ugccall/30min`
- [ ] Titel: "Boek een call"
- [ ] Subtext: (uit PDF)
- [ ] Vlaggen: Nederland, België, Engeland, Duitsland
- [ ] Tekst: "1500+ geverifieerde creators"
- [ ] "Vertrouwd door 2,000 merken" toevoegen

#### Stap 3.6: Registreren/Inloggen
- [ ] Nieuw contentblok links toevoegen
- [ ] Bestanden ophalen uit Google Drive
- [ ] Design aanpassen aan nieuwe stijl

#### Stap 3.7: Algemene Voorwaarden/Privacy
- [ ] Design inspiratie: Billo terms
- [ ] Restylen volgens nieuwe branding

### Fase 4: Technische Implementatie

#### Stap 4.1: JavaScript Functionaliteit
- [ ] Carrousel functionaliteit (automatisch doorschuiven)
- [ ] Dropdown functionaliteit (registreer gratis)
- [ ] FAQ accordion/tabs
- [ ] Filter functionaliteit (creators, case studies)
- [ ] Smooth scroll voor anchors
- [ ] Tooltip/hover functionaliteit (vergelijking carrousel)

#### Stap 4.2: Responsive Design
- [ ] Mobile-first approach
- [ ] Breakpoints definiëren
- [ ] Carrousels responsive maken
- [ ] Navigation mobile menu
- [ ] Forms responsive testen

#### Stap 4.3: Performance Optimalisatie
- [ ] Image optimization (logo's, creator profielen)
- [ ] Lazy loading voor carrousels
- [ ] CSS optimalisatie
- [ ] Font loading optimalisatie

#### Stap 4.4: Storyblok Integratie (Toekomst)
- [ ] Blog CMS setup
- [ ] Case studies CMS setup
- [ ] Services subpagina's CMS setup
- [ ] Content modellen definiëren

### Fase 5: Content & Assets

#### Stap 5.1: Assets Verzamelen
- [ ] Logo's voor merken carrousel (Google Drive)
- [ ] Creator video's voor carrousels (Google Drive)
- [ ] Content pieces voor verschillende secties (Google Drive)
- [ ] Case studies (Word documenten)
- [ ] FAQ content (Google Drive)
- [ ] Iconen ontwerpen (niches, features)

#### Stap 5.2: Content Review
- [ ] Alle teksten controleren op consistentie
- [ ] ALT-teksten voor SEO
- [ ] Meta descriptions per pagina
- [ ] CTA teksten optimaliseren

### Fase 6: Testing & Launch

#### Stap 6.1: Cross-browser Testing
- [ ] Chrome, Firefox, Safari, Edge
- [ ] Mobile browsers (iOS, Android)

#### Stap 6.2: User Testing
- [ ] Navigatie testen
- [ ] Conversie flows testen
- [ ] Formulier validatie
- [ ] Link checking

#### Stap 6.3: SEO Check
- [ ] Meta tags
- [ ] ALT-teksten
- [ ] Structured data
- [ ] Sitemap

#### Stap 6.4: Launch
- [ ] Staging environment testen
- [ ] Production deploy
- [ ] Monitoring opzetten

---

## Belangrijke Opmerkingen

### Referenties
- **Billo.app** wordt gebruikt als inspiratie (niet kopiëren)
- **Figma** templates voor carrousel designs
- **Tailwind CSS** UI blocks voor hero secties

### Google Drive Links (uit PDF)
- Brand guide: https://drive.google.com/drive/u/0/search?q=brandguide
- Logo & overige: https://drive.google.com/drive/u/0/folders/1TgvqyyXiV77-Kf5nBTTu6is2GXBKxkuv
- Creator video's: https://drive.google.com/drive/u/0/folders/1O_hSXKttjmn35E7eJem4ucIDwPUsIbkJ
- Merken logo's: https://drive.google.com/drive/u/0/folders/1geCfcRHQ4jP-pkbNUFVnuRkyZGS2OG9b
- Content pieces (brug): https://drive.google.com/drive/u/0/folders/1JhriBmrd8gSkKyaT7axBOriByhyDtJYc
- Content pieces (zo werkt): https://drive.google.com/drive/u/0/folders/1sB0TjI4iBkQNU53naw0jLQFoTbZBAQje
- Case studies: https://drive.google.com/drive/u/0/folders/18pnMrOqWqh-qaVQ2ztXPqpQncvKqKNo6
- FAQ content: https://drive.google.com/drive/u/0/folders/1PqjOAFZFvupP8jk3z34E_DEj72N-j19i
- Demo call assets: https://drive.google.com/drive/folders/1KDxd7hzFSKhX0njhKpFrMth3u72XTXuI
- Services assets: https://drive.google.com/drive/u/0/folders/1w7K2af7bFXb4knaJ3YTlFmz4Lxc9TP18
- Registreren/inloggen content: https://drive.google.com/drive/u/0/folders/1E7KoGmmLmjtiB9fbRM65YhNKDnX-GYI2

### Prioriteiten
1. **Hoog:** Homepage redesign (volledig)
2. **Hoog:** Font selectie & implementatie
3. **Medium:** Vind Creators pagina
4. **Medium:** Services pagina's
5. **Laag:** Blog & Succesverhalen (Storyblok integratie later)

---

*Document gegenereerd op basis van Rebrand PDF en huidige codebase analyse.*









