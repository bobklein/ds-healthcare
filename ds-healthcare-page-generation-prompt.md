# DS Healthcare Solution Page Generation Prompt

Use this prompt to generate new solution pages or update existing pages for the Digital Scientists healthcare vertical website.

---

## MASTER PROMPT

```
You are generating a production-ready HTML page for Digital Scientists' healthcare vertical website.

## PAGE DETAILS
- **Page name**: [PAGE_NAME]
- **URL**: [FILENAME].html (flat file in root)
- **Primary persona**: [CEO/CFO/COO/CTO]
- **Page type**: [Solution Framework | Domain Expertise | Market | AI Guide | Case Study]

## REFERENCE FILES
Before generating, review:
1. `ds-healthcare-v3.html` - Main page for style, navigation, CTA pattern
2. `healthcare-ia-spec.md` - Content requirements for this page type
3. `page-templates.md` - Structure template
4. `DS_2026_GTM_Strategy_Comprehensive_01022026.docx` - Messaging and proof points

## TECHNICAL REQUIREMENTS

### File Structure
- Flat HTML file in root directory (not nested folders)
- Filename pattern: `healthcare-[category]-[name].html`
  - Solutions: `healthcare-ai-[name].html`
  - Domains: `healthcare-domains-[name].html`
  - Markets: `healthcare-markets-[name].html`
  - Guides: `[guide-name].html`

### Framework
- Tailwind CSS via CDN
- Colors: dsBlue (#304FFF), dsBlack (#050505), dsGray (#F5F5F5)
- Font: Inter via Google Fonts
- Fade-up animations with Intersection Observer

### Navigation (copy exactly from ds-healthcare-v3-updated.html)
Full mega-menu with dropdowns:
- Healthcare: Overview, Our Approach, Get AI Assessment
- AI Solutions: Documentation Automation, Back-Office Agents, Virtual Care Assistants, Intelligent Scheduling, AI Guides
- Domains: MDS/PDPM, RAF/HCC Coding, Revenue Cycle AI, Value-Based Care, Ambient Scribes, EHR Integrations
- Markets: Skilled Nursing, Home Health & Hospice, Senior Living, IDD Services, Health Systems
- Work: NeverAlone, CommuniCare MDS, RAF/HCC Coding, HealthContext.AI

### Logo Bar (immediately after hero)
```html
<section class="border-y border-gray-100 py-8 px-6">
    <div class="max-w-screen-xl mx-auto flex flex-wrap justify-center items-center gap-8 md:gap-16">
        <span class="text-xs text-gray-400 uppercase tracking-wider">Trusted By</span>
        <img src="https://digitalscientists.com/wp-content/uploads/2023/12/logo-chs-black.png" alt="CommuniCare" class="h-6 md:h-8 grayscale opacity-50 hover:grayscale-0 hover:opacity-100 transition">
        <img src="https://digitalscientists.com/wp-content/uploads/2023/10/McKesson_logo.png" alt="McKesson" class="h-5 md:h-6 grayscale opacity-50 hover:grayscale-0 hover:opacity-100 transition">
        <img src="https://digitalscientists.com/wp-content/uploads/2024/05/Screenshot_2-300x60.png" alt="Duke Health" class="h-5 md:h-6 grayscale opacity-50 hover:grayscale-0 hover:opacity-100 transition">
        <img src="https://digitalscientists.com/wp-content/uploads/2023/10/wellstar-logo.png" alt="WellStar" class="h-6 md:h-8 grayscale opacity-50 hover:grayscale-0 hover:opacity-100 transition">
    </div>
</section>
```

### CTA Section (blue background, two-column with form)
Copy exactly from ds-healthcare-v3-updated.html #contact section:
- Left: Headline, subhead, 3 checkmarks (Understand situation, Assess ROI, Determine fit)
- Right: White form card with First Name, Last Name, Email, Organization, Primary Interest dropdown
- "Schedule AI Opportunity Call" button
- Phone fallback: 404.654.3855

### Footer
Copy from ds-healthcare-v3-updated.html:
- Healthcare Solutions links (including Predictive Analytics)
- Capabilities links (to digitalscientists.com)
- EHR Integrations list
- Compliance badges

### Testimonial (if included)
Use working PNG logos, not SVGs:
```html
<img src="https://digitalscientists.com/wp-content/uploads/2023/12/logo-chs-black.png" alt="CommuniCare" class="h-10 md:h-12">
```

### Real Images Available
Hero/Dashboard:
- `https://digitalscientists.com/wp-content/uploads/2024/06/image-12-2.png` (RAF dashboard)
- `https://digitalscientists.com/wp-content/uploads/2024/06/image-9-1.png` (RAF scoring)

Architecture:
- `https://digitalscientists.com/wp-content/uploads/2024/06/Group-12069.png` (VBC architecture)

Team:
- `https://digitalscientists.com/wp-content/uploads/2024/06/P1000918-sm-1.png`
- `https://digitalscientists.com/wp-content/uploads/2024/06/P1000839-sm-1.png`
- `https://digitalscientists.com/wp-content/uploads/2024/06/Group-11208.png`

EHR Logos (for dark backgrounds):
- PointClickCare: `https://digitalscientists.com/wp-content/uploads/2023/10/pointclickcare-logo.png`
- Epic: `https://digitalscientists.com/wp-content/uploads/2023/10/Epic-Partner-Logo.png`
- Gehrimed: `https://digitalscientists.com/wp-content/uploads/2023/11/gEHRiMed-768x170.png`
- Netsmart: `https://digitalscientists.com/wp-content/uploads/2023/10/Netsmart-copy.png`

DS Logos:
- Header: `https://digitalscientists.com/wp-content/uploads/2022/11/header-logo-dark.svg`
- Footer: `https://digitalscientists.com/wp-content/uploads/2022/11/footer-logo.svg`

## INTERNAL LINKING RULES

### Contextual Links
Link the **first mention** of related terms to their respective pages:
- "predictive analytics" / "predictive scoring" / "risk scoring" → `predictive-analytics-healthcare.html`
- "documentation automation" / "ambient scribe" → `healthcare-ai-documentation-automation.html`
- "back-office" / "revenue cycle AI" → `healthcare-ai-back-office-agents.html`
- "virtual care" / "telehealth" / "RPM" → `healthcare-ai-virtual-care-assistants.html`
- "scheduling" / "no-show" → `healthcare-ai-intelligent-scheduling.html`
- "MDS" / "PDPM" → `healthcare-domains-mds-pdpm.html`
- "RAF" / "HCC" → `healthcare-domains-raf-hcc-coding.html`
- "value-based care" / "VBC" → `healthcare-domains-value-based-care.html`

**Rules:**
- One link per term per page (don't link every instance)
- Link within natural prose, not in headers
- Use descriptive anchor text (the term itself)

### Cross-Reference Sections
Include "Related Solutions" or "Often Combined With" sections linking to 2-4 related pages.

## KEY MESSAGING (pull from GTM docs)

### Proof Points
- $10M+ PDPM revenue recovered
- $2M quality incentives
- 96% treat-in-place rate
- 26K patients on NeverAlone across 7 states
- 100% production rate (vs 5% industry average)
- 45→5 minutes per visit documentation
- 200-300 bps EBITDA improvement

### 8-Step Value Chain
Data Foundation → Responsible AI → EHR Integration → Co-Design → Deployment → Change Management → Knowledge Transfer → KPI Accountability

### Why Custom AI
- 95% of healthcare AI fails to reach production
- 2x success rate for custom solutions
- Healthcare is different: compliance, EHR integration, reimbursement complexity

### Persona Messaging
- **CEO**: Transformation, platform company, sustainable advantage
- **CFO**: ROI, calendar year returns, financially verified results
- **COO**: Workflow fit, change management, staff adoption
- **CTO**: Technical feasibility, integration, 100% production rate

## STYLE RULES
- Clean black/white/gray foundation with blue accent used sparingly
- Blue (#304FFF) only for: links, section labels, occasional highlight stat
- NO gradient backgrounds
- Simple borders (`border border-gray-200`) over heavy shadows
- Minimal formatting - natural prose over bullet lists
- Mobile-responsive using Tailwind prefixes (md:, lg:)

## OUTPUT
Generate complete, production-ready HTML that can be deployed directly to GitHub Pages at bobklein.github.io/ds-healthcare/
```

---

## CHECKLIST BEFORE DEPLOYMENT

- [ ] Navigation matches ds-healthcare-v3-updated.html exactly
- [ ] Logo bar uses image URLs (not text placeholders)
- [ ] All internal links use relative paths (`.html` files)
- [ ] CTA section matches main page pattern
- [ ] Footer links are consistent
- [ ] Testimonials use PNG logos (not SVG)
- [ ] First mention of related terms are contextually linked
- [ ] Mobile responsive (test at 375px width)
- [ ] Fade-up animations included
- [ ] No broken image URLs

---

## PAGES TO GENERATE

### Solution Frameworks (AI Solutions dropdown)
- [x] `healthcare-ai-documentation-automation.html`
- [x] `healthcare-ai-back-office-agents.html`
- [x] `healthcare-ai-virtual-care-assistants.html`
- [x] `healthcare-ai-intelligent-scheduling.html`

### Domain Expertise (Domains dropdown)
- [ ] `healthcare-domains-mds-pdpm.html`
- [ ] `healthcare-domains-raf-hcc-coding.html`
- [ ] `healthcare-domains-revenue-cycle-ai.html`
- [ ] `healthcare-domains-value-based-care.html`
- [ ] `healthcare-domains-ambient-scribes.html`
- [ ] `healthcare-domains-ehr-integrations.html`

### Markets (Markets dropdown)
- [ ] `healthcare-markets-skilled-nursing.html`
- [ ] `healthcare-markets-home-health-hospice.html`
- [ ] `healthcare-markets-senior-living.html`
- [ ] `healthcare-markets-idd.html`
- [ ] `healthcare-markets-health-systems.html`

### Case Studies (Work dropdown)
- [ ] `work-never-alone.html`
- [ ] `work-communicare-mds.html`
- [ ] `work-raf-hcc-coding.html`
- [ ] `work-healthcontext-ai.html`

### Supporting Pages
- [ ] `healthcare-approach.html`
- [ ] `healthcare-assessment.html`
- [x] `predictive-analytics-healthcare.html` (SEO/capability page, footer only)

### AI Guides
- [x] `healthcare-ai-guides-landing.html`
- [x] `ar-collection-prioritization.html`
- [x] `claim-follow-up-triage.html`
- [x] `payer-contract-interpretation.html`
