# Digital Scientists Healthcare Website

23 production-ready HTML pages for the DS Healthcare vertical.

## Quick Deploy Options

### Option 1: Netlify (Easiest - Free)
1. Go to https://app.netlify.com/drop
2. Drag and drop this entire folder
3. Done! You'll get a live URL instantly

### Option 2: GitHub Pages (Free)
1. Create a new GitHub repository
2. Upload all HTML files to the repository
3. Go to Settings → Pages
4. Set Source to "main" branch
5. Your site will be live at `https://yourusername.github.io/repo-name/`

### Option 3: Vercel (Free)
1. Go to https://vercel.com/new
2. Import your GitHub repo or drag/drop folder
3. Deploy

### Option 4: Surge.sh (Free, CLI)
```bash
npm install -g surge
surge . your-site-name.surge.sh
```

## File Structure

```
index.html                              → Redirects to hub
ds-healthcare-v3-updated.html           → Main hub page (/healthcare/)
healthcare-assessment.html              → Primary conversion
healthcare-approach.html                → 8-step methodology

AI Solution Frameworks:
healthcare-ai-documentation-automation.html
healthcare-ai-back-office-agents.html
healthcare-ai-virtual-care-assistants.html
healthcare-ai-intelligent-scheduling.html

Domain Expertise:
healthcare-domains-mds-pdpm.html
healthcare-domains-raf-hcc-coding.html
healthcare-domains-revenue-cycle-ai.html
healthcare-domains-value-based-care.html
healthcare-domains-ambient-scribes.html
healthcare-domains-ehr-integrations.html

Markets:
healthcare-markets-skilled-nursing.html
healthcare-markets-home-health-hospice.html
healthcare-markets-senior-living.html
healthcare-markets-health-systems.html

Secondary Conversion:
healthcare-assessment-platform.html
healthcare-assessment-partnership.html

Case Studies:
work-never-alone.html
work-communicare-mds.html
work-raf-hcc-coding.html
work-healthcontext-ai.html
```

## For Production Deployment

When deploying to digitalscientists.com, update the navigation links from 
relative file paths (e.g., `healthcare-assessment.html`) to URL paths 
(e.g., `/healthcare/assessment/`) and configure your web server routing accordingly.
