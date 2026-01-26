# Digital Scientists Healthcare Site - Standards & Style Guide

**Repository:** https://github.com/bobklein/ds-healthcare  
**Live Site:** https://bobklein.github.io/ds-healthcare/  
**Last Updated:** January 26, 2026

---

## Table of Contents

1. [File Structure](#file-structure)
2. [Image Standards](#image-standards)
3. [HTML Structure Patterns](#html-structure-patterns)
4. [Design System](#design-system)
5. [Common Issues & Solutions](#common-issues--solutions)
6. [Page Templates](#page-templates)
7. [Component Library](#component-library)
8. [Deployment Checklist](#deployment-checklist)

---

## File Structure

```
ds-healthcare/
├── index.html                          # Homepage
├── healthcare-hub.html                 # Main healthcare landing page
├── 1012DS_Logo_Native_Black (1).svg    # CRITICAL: Header logo (must be in root)
│
├── healthcare-markets-*.html           # Market segment pages (5)
├── healthcare-capabilities-*.html      # Capability pages (6)
├── healthcare-domains-*.html           # Domain expertise pages (6)
├── healthcare-ai-*.html                # AI solution framework pages (5)
├── healthcare-assessment*.html         # Assessment/discovery pages (3)
├── ai-framework-*.html                 # Individual AI framework pages (7)
├── work-*.html                         # Case study pages (4)
├── [solution-specific].html            # Individual solution pages (~20)
│
├── images/
│   ├── case-studies/                   # Case study specific images
│   │   ├── mds-*.png/jpg              # MDS/CommuniCare images
│   │   ├── raf-*.png                  # RAF/HCC coding images
│   │   ├── healthcontext-*.png        # HealthContext images
│   │   └── digital-health-hero.png    # Generic healthcare hero
│   │
│   ├── testimonials/                   # Testimonial headshots
│   │   ├── dr-matthew-wayne.jpg       # CommuniCare CMO
│   │   └── donna-elbrecht.jpg         # Easterseals executive
│   │
│   ├── hero-*.png                      # Hero section images
│   ├── case-*.png/jpg                  # Case study images (root level)
│   ├── arch-*.png                      # Architecture diagrams
│   ├── icon-*.svg                      # UI icons
│   ├── tech-*.png/svg                  # Technology logos
│   ├── team-*.png/jpg                  # Team member photos
│   │
│   ├── header-logo-dark.svg           # Dark logo for light backgrounds
│   ├── header-logo-light.svg          # Light logo for dark backgrounds
│   ├── footer-logo.svg                # Footer logo
│   │
│   └── [client-logos]                  # Client/partner logos
│       ├── duke-health.png
│       ├── mckesson-full.webp
│       ├── communicare-black.webp
│       ├── congruity-health-new.svg
│       ├── logo-guardian.png
│       ├── easterseals-gray.png
│       └── ...
│
└── downloads/
    └── neveralone/                     # NeverAlone market PDFs
        ├── NeverAlone-Skilled-Nursing.pdf
        ├── NeverAlone-Assisted-Living.pdf
        ├── NeverAlone-Home-Health.pdf
        ├── NeverAlone-IDD.pdf
        └── NeverAlone-IDD-Group-Home.pdf
```

### Critical Files

| File | Location | Notes |
|------|----------|-------|
| Header Logo | `1012DS_Logo_Native_Black (1).svg` | **MUST be in root directory** - Referenced by all pages |
| NeverAlone Video | `images/neveralone-video.mp4` | 29MB marketing video |
| Video Poster | `images/neveralone-video-poster.png` | Frame at 20s showing logo |

---

## Image Standards

### Naming Conventions

| Type | Pattern | Examples |
|------|---------|----------|
| Hero images | `hero-[topic].png` | `hero-telehealth.png`, `hero-senior-ipad.png` |
| Case study | `case-[client]-[element].png` | `case-neveralone-senior.png`, `case-raf-dashboard.png` |
| Architecture | `arch-[topic].png` | `arch-telemedicine.png`, `arch-vbc.png` |
| Icons | `icon-[name].svg` | `icon-ehr.svg`, `icon-telehealth.svg` |
| Tech logos | `tech-[name].png/svg` | `tech-openai.png`, `tech-react.png` |
| Team photos | `team-[name].png/jpg` | `team-bob-klein.png` |
| Testimonials | `testimonials/[name].jpg` | `testimonials/dr-matthew-wayne.jpg` |

### Testimonial Photo Requirements

**CRITICAL:** Each testimonial must have a unique, correctly-matched photo.

| Person | Role | Image File |
|--------|------|------------|
| Amy Severino | Chief Innovation Officer, NeverAlone | `images/any-severino.png` |
| Justin Scott, M.D., FASA | CEO, Vigilant Medical Solutions | `images/justin-scott.png` |
| Dr. Matthew Wayne | Chief Medical Officer, CommuniCare | `images/testimonials/dr-matthew-wayne.jpg` |
| Donna K. Elbrecht | VP, Easterseals | `images/testimonials/donna-elbrecht.jpg` |

**Verification:** Run MD5 hash check to ensure no duplicate placeholder images:
```bash
md5sum images/*severino* images/justin-scott* images/testimonials/*
```

### Client Logo Specifications

**Healthcare Logo Ribbon (6 logos):**
- Duke Health: `duke-health.png` - height: 2.5rem, grayscale filter
- Congruity Health: `congruity-health-new.svg` - height: 2.5rem, grayscale filter
- McKesson: `mckesson-full.webp` - height: 1.5rem (no filter needed)
- CommuniCare: `communicare-black.webp` - height: 3rem (no filter needed)
- Guardian: `logo-guardian.png` - height: 2.5rem, grayscale filter
- Easterseals: `easterseals-gray.png` - height: 2.5rem (pre-grayed)

**Homepage Logo Ribbon (7 logos):**
- Intuit Mailchimp, McKesson, Cox 2M, CommuniCare, NAPA, INPO, GoFan

### Image Sizing Guidelines

| Context | Recommended Size | Format |
|---------|-----------------|--------|
| Hero images | 800-1200px wide | PNG or WebP |
| Case study screenshots | 600-1000px wide | PNG |
| Testimonial headshots | 200x200px minimum | JPG (circular crop in CSS) |
| Client logos | 100-200px wide | SVG preferred, PNG/WebP acceptable |
| Icons | 48x48px base | SVG only |

---

## HTML Structure Patterns

### Standard Page Skeleton

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Page Title] | Digital Scientists</title>
    <meta name="description" content="[Meta description 150-160 chars]">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        dsBlue: '#0066FF',
                        dsBlack: '#111111',
                        dsGray: '#F5F5F5',
                        dsLime: '#BFFF00',
                        dsTeal: '#00CED1',
                    }
                }
            }
        }
    </script>
    <!-- Fade animation styles -->
    <style>
        .fade-up {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.6s ease-out, transform 0.6s ease-out;
        }
        .fade-up.visible {
            opacity: 1;
            transform: translateY(0);
        }
    </style>
</head>
<body class="bg-white text-gray-800 font-sans">

<!-- START DS-NAV -->
[Navigation component - see Component Library]
<!-- END DS-NAV -->

<!-- Fade Animation Script -->
<script>
document.addEventListener('DOMContentLoaded', function() {
    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -50px 0px',
        threshold: 0.1
    };
    const fadeObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);
    document.querySelectorAll('.fade-up').forEach(el => {
        fadeObserver.observe(el);
    });
});
</script>

<!-- Hero Section -->
<header class="pt-32 pb-16 px-6">
    [Content]
</header>

<!-- Content Sections -->
<section class="py-20 px-6">
    [Content]
</section>

<section class="py-20 px-6 bg-dsGray">
    [Content - alternating background]
</section>

<section class="py-20 px-6 bg-dsBlack text-white">
    [Content - dark section]
</section>

<!-- Footer -->
[Footer component]

</body>
</html>
```

### Hero Section - Two Column Layout

```html
<!-- Hero Section -->
<header class="pt-32 pb-16 px-6">
    <div class="max-w-screen-xl mx-auto">
        <div class="grid lg:grid-cols-2 gap-12 items-center">
            <!-- Left Content -->
            <div class="fade-up">
                <div class="inline-flex items-center gap-2 text-sm text-dsBlue font-medium mb-6">
                    <span class="w-1.5 h-1.5 bg-dsBlue rounded-full"></span>
                    Category Label
                </div>
                
                <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold text-dsBlack mb-6 leading-[1.1]">
                    Main Headline Here
                </h1>
                
                <p class="text-xl text-gray-600 leading-relaxed mb-8">
                    Supporting description text goes here.
                </p>
                
                <a href="#" class="inline-flex items-center gap-2 bg-dsBlue text-white px-6 py-3 text-sm font-medium rounded-full hover:bg-dsBlack transition">
                    Call to Action
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                    </svg>
                </a>
            </div>
            
            <!-- Right Image -->
            <div class="fade-up">
                <img src="images/[appropriate-image].png" alt="Descriptive alt text" class="rounded-xl shadow-lg w-full">
            </div>
        </div>
    </div>
</header>
```

### Stats Row

```html
<div class="grid grid-cols-2 md:grid-cols-4 gap-6">
    <div class="border border-gray-200 rounded-xl p-6">
        <span class="text-3xl md:text-4xl font-bold text-dsBlue">100K+</span>
        <p class="text-gray-500 text-sm mt-1">Calls Completed</p>
    </div>
    <div class="border border-gray-200 rounded-xl p-6">
        <span class="text-3xl md:text-4xl font-bold text-dsBlack">96%</span>
        <p class="text-gray-500 text-sm mt-1">Treat-in-Place</p>
    </div>
    <!-- Additional stat cards -->
</div>
```

### Case Study Section (Dark Background)

```html
<section class="py-20 px-6 bg-dsBlack text-white">
    <div class="max-w-screen-xl mx-auto">
        <div class="grid lg:grid-cols-2 gap-12 items-center">
            <!-- Text Content -->
            <div class="fade-up">
                <span class="text-xs font-medium text-dsBlue uppercase tracking-wider">Case Study</span>
                <h2 class="text-3xl md:text-4xl font-bold mt-3 mb-6">
                    Client Name: Headline Result
                </h2>
                <p class="text-gray-400 mb-6">
                    Description of the case study and outcomes.
                </p>
                
                <div class="grid grid-cols-2 gap-6 mb-6">
                    <div>
                        <span class="text-3xl font-bold text-dsBlue">$10M+</span>
                        <p class="text-gray-400">Metric Description</p>
                    </div>
                    <!-- Additional metrics -->
                </div>
                
                <a href="work-[case-study].html" class="inline-flex items-center gap-2 text-dsBlue font-medium hover:gap-3 transition-all">
                    Read Full Case Study <span>→</span>
                </a>
            </div>
            
            <!-- Image - MUST HAVE IMAGE, NOT EMPTY DIV -->
            <div class="fade-up">
                <div class="bg-gray-900 rounded-xl overflow-hidden">
                    <img src="images/case-studies/[image].jpg" alt="Case study visual" class="w-full h-full object-cover">
                </div>
            </div>
        </div>
    </div>
</section>
```

### Testimonial Component

```html
<div class="bg-dsGray border border-gray-200 rounded-xl p-6">
    <div class="flex gap-4">
        <img src="images/testimonials/[person-name].jpg" alt="Person Name" class="w-16 h-16 rounded-full object-cover flex-shrink-0">
        <div>
            <p class="text-gray-700 mb-3 text-sm italic">"Quote text here..."</p>
            <p class="font-semibold text-dsBlack">Person Name</p>
            <p class="text-sm text-gray-500">Title, Organization</p>
        </div>
    </div>
</div>
```

### Healthcare Client Logo Ribbon

```html
<!-- Healthcare Client Logos -->
<section class="bg-gray-50 py-12">
    <div class="max-w-screen-xl mx-auto px-6">
        <div style="display: flex; flex-wrap: nowrap; justify-content: center; align-items: center; overflow-x: auto;">
            <div style="display: flex; align-items: center; justify-content: center; padding: 1rem 2rem; border-right: 1px solid #d1d5db;">
                <img src="images/duke-health.png" alt="Duke Health" style="height: 2.5rem; filter: grayscale(100%);">
            </div>
            <div style="display: flex; align-items: center; justify-content: center; padding: 1rem 2rem; border-right: 1px solid #d1d5db;">
                <img src="images/congruity-health-new.svg" alt="Congruity Health" style="height: 2.5rem; filter: grayscale(100%);">
            </div>
            <div style="display: flex; align-items: center; justify-content: center; padding: 1rem 2rem; border-right: 1px solid #d1d5db;">
                <img src="images/mckesson-full.webp" alt="McKesson" style="height: 1.5rem;">
            </div>
            <div style="display: flex; align-items: center; justify-content: center; padding: 1rem 2rem; border-right: 1px solid #d1d5db;">
                <img src="images/communicare-black.webp" alt="CommuniCare" style="height: 3rem;">
            </div>
            <div style="display: flex; align-items: center; justify-content: center; padding: 1rem 2rem; border-right: 1px solid #d1d5db;">
                <img src="images/logo-guardian.png" alt="Guardian" style="height: 2.5rem; filter: grayscale(100%);">
            </div>
            <div style="display: flex; align-items: center; justify-content: center; padding: 1rem 2rem;">
                <img src="images/easterseals-gray.png" alt="Easterseals" style="height: 2.5rem;">
            </div>
        </div>
    </div>
</section>
```

**IMPORTANT:** Use inline styles for logo ribbon to prevent CSS conflicts and wrapping issues.

---

## Design System

### Color Palette

| Name | Hex | Tailwind Class | Usage |
|------|-----|----------------|-------|
| DS Blue | `#0066FF` | `text-dsBlue`, `bg-dsBlue` | Primary brand, links, CTAs |
| DS Black | `#111111` | `text-dsBlack`, `bg-dsBlack` | Headlines, dark sections |
| DS Gray | `#F5F5F5` | `bg-dsGray` | Alternating section backgrounds |
| DS Lime | `#BFFF00` | `bg-dsLime` | Accent highlights |
| DS Teal | `#00CED1` | `text-dsTeal`, `bg-dsTeal` | Secondary accent |

### Typography

- **Headlines:** `font-bold` with tight line-height (`leading-[1.1]`)
- **Body:** Default sans-serif, `text-gray-600` or `text-gray-400` on dark
- **Labels:** `text-xs font-medium uppercase tracking-wider`
- **Stats:** `text-3xl md:text-4xl font-bold`

### Spacing

- **Section padding:** `py-20 px-6`
- **Hero padding:** `pt-32 pb-16 px-6`
- **Container:** `max-w-screen-xl mx-auto`
- **Grid gaps:** `gap-6` (cards), `gap-12` (two-column layouts)

### Border Radius

- Cards: `rounded-xl`
- Buttons: `rounded-full`
- Images: `rounded-xl`
- Testimonial photos: `rounded-full`

---

## Common Issues & Solutions

### Issue: Empty Image Containers

**Problem:** Divs with classes but no `<img>` tag inside, causing blank areas.

```html
<!-- BAD -->
<div class="my-8 rounded-xl overflow-hidden shadow-lg fade-up">
</div>

<!-- GOOD -->
<div class="my-8 rounded-xl overflow-hidden shadow-lg fade-up">
    <img src="images/[image].png" alt="Description" class="w-full">
</div>
```

**Detection:**
```bash
grep -rn "overflow-hidden.*>\s*</div>" *.html
```

### Issue: Images Breaking Grid Layouts

**Problem:** Image divs incorrectly nested inside card components.

```html
<!-- BAD - Image nested inside first card breaks 3-column grid -->
<div class="grid md:grid-cols-3 gap-6">
    <div class="border border-gray-200 rounded-xl p-6">
        <span>15-20%</span>
        <h3>No-show rates</h3>
        <p>Description</p>
        
        <div class="my-8 fade-up">
            <img src="..." alt="...">  <!-- WRONG LOCATION -->
        </div>
    </div>
    <div class="border...">...</div>
    <div class="border...">...</div>
</div>

<!-- GOOD - Cards are clean, image is separate -->
<div class="grid md:grid-cols-3 gap-6">
    <div class="border border-gray-200 rounded-xl p-6">
        <span>15-20%</span>
        <h3>No-show rates</h3>
        <p>Description</p>
    </div>
    <div class="border...">...</div>
    <div class="border...">...</div>
</div>
```

### Issue: Missing Logo File

**Problem:** `1012DS_Logo_Native_Black (1).svg` must exist in root directory.

**Solution:** Copy from `images/header-logo-dark.svg`:
```bash
cp images/header-logo-dark.svg "1012DS_Logo_Native_Black (1).svg"
```

### Issue: Logo Ribbon Wrapping

**Problem:** Flexbox logos wrap to multiple rows on smaller screens.

**Solution:** Use inline styles to enforce single-row layout:
```html
<div style="display: flex; flex-wrap: nowrap; justify-content: center; align-items: center; overflow-x: auto;">
```

### Issue: White Logo on Light Background

**Problem:** `guardian.svg` is white and invisible on gray backgrounds.

**Solution:** Use `logo-guardian.png` (blue version) with grayscale filter:
```html
<img src="images/logo-guardian.png" alt="Guardian" style="height: 2.5rem; filter: grayscale(100%);">
```

### Issue: Mismatched Testimonial Photos

**Problem:** Same placeholder image used for multiple people.

**Verification:**
```bash
md5sum images/*severino* images/justin-scott* images/testimonials/*
# All hashes should be UNIQUE
```

**Source for correct photos:**
- Extract from NeverAlone PDFs using PyMuPDF
- Download from WordPress media library

---

## Page Templates

### Market Segment Page

File pattern: `healthcare-markets-[segment].html`

Sections (in order):
1. Hero with market-specific image
2. Market Challenges (3-column cards)
3. Solutions Grid (linked cards)
4. Case Study (dark background with image)
5. Why Digital Scientists (4-column cards)
6. AI Solution Frameworks (linked cards)
7. Healthcare Client Logo Ribbon
8. CTA Section
9. Footer

### AI Solution Framework Page

File pattern: `healthcare-ai-[solution].html`

Sections (in order):
1. Hero with solution screenshot/visual
2. Problem Statement (3-column stat cards)
3. The Solution (dark background)
4. How It Works (numbered steps)
5. Case Study/Proof Points
6. Related Solutions
7. CTA Section
8. Footer

### Case Study Page

File pattern: `work-[client].html`

Sections (in order):
1. Hero with client context
2. The Challenge
3. Our Approach
4. The Solution (with screenshots)
5. Results/Outcomes (stats)
6. Testimonial
7. Related Work
8. CTA Section
9. Footer

---

## Deployment Checklist

### Before Creating ZIP Package

- [ ] All images referenced in HTML exist in `/images/`
- [ ] `1012DS_Logo_Native_Black (1).svg` exists in root
- [ ] No empty image containers (`grep -rn "overflow-hidden.*>\s*</div>"`)
- [ ] Testimonial photos are unique (MD5 check)
- [ ] Logo ribbon uses inline styles (not Tailwind flex classes)
- [ ] All links point to correct `.html` files
- [ ] PDFs exist in `/downloads/` if referenced

### After Deployment

- [ ] Test navigation on all pages
- [ ] Verify all images load (check DevTools console)
- [ ] Test mobile responsiveness
- [ ] Verify video plays (work-never-alone.html)
- [ ] Check logo ribbon displays in single row
- [ ] Verify testimonial photos match names

### Version Naming Convention

Format: `ds-healthcare-v[##]-[DESCRIPTION].zip`

Examples:
- `ds-healthcare-v38-SNF-PAGE-FIX.zip`
- `ds-healthcare-v39-AI-PAGE-IMAGES.zip`
- `ds-healthcare-v40-SCHEDULING-LAYOUT-FIX.zip`

---

## Quick Reference Commands

```bash
# Find all empty image containers
grep -rn "overflow-hidden.*>\s*</div>" *.html

# Check for missing images
for img in $(grep -roh 'src="images/[^"]*"' *.html | sed 's/src="//;s/"$//' | sort -u); do
    [ ! -f "$img" ] && echo "MISSING: $img"
done

# Verify testimonial photo uniqueness
md5sum images/*severino* images/justin-scott* images/testimonials/* 2>/dev/null

# Count pages and images
find . -name "*.html" | wc -l
find ./images -type f | wc -l

# Create deployment package
zip -r ds-healthcare-v[##]-[DESC].zip . -x "*.py" -x ".git/*"
```

---

## Contact & Resources

- **Repository:** https://github.com/bobklein/ds-healthcare
- **WordPress Source:** https://digitalscientists.com
- **NeverAlone PDFs:** Source for testimonial photos and content
- **PowerPoint Source:** `Never_Alone___Health_Context__Care_Platform_2024.pptx`

---

*This document should be updated whenever new patterns are established or issues are resolved.*
