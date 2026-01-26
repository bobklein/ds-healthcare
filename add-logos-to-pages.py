#!/usr/bin/env python3
"""
Add standardized client logo ribbon and tech logo sections to healthcare pages
"""

import re
import os

# Standard client logo ribbon HTML
CLIENT_LOGO_RIBBON = '''<!-- Healthcare Client Logos -->
<section class="py-8 border-b border-gray-100 bg-white">
    <div class="max-w-screen-xl mx-auto">
        <div class="flex flex-wrap justify-center items-center gap-8 md:gap-12">
            <img src="images/duke-health.png" alt="Duke Health" class="h-8 object-contain opacity-70 hover:opacity-100 transition">
            <img src="images/congruity-health.svg" alt="Congruity Health" class="h-8 object-contain opacity-70 hover:opacity-100 transition">
            <img src="images/mckesson.png" alt="McKesson" class="h-8 object-contain opacity-70 hover:opacity-100 transition">
            <img src="images/communicare.png" alt="CommuniCare" class="h-8 object-contain opacity-70 hover:opacity-100 transition">
            <img src="images/guardian.svg" alt="Guardian" class="h-8 object-contain opacity-70 hover:opacity-100 transition invert">
        </div>
    </div>
</section>

'''

# Tech logos section - common data/analytics stack
TECH_LOGOS_DATA = '''<!-- Technologies We Use -->
<section class="py-16 px-6 bg-dsGray">
    <div class="max-w-screen-xl mx-auto">
        <div class="fade-up text-center mb-12">
            <h2 class="text-2xl font-bold text-dsBlack mb-4">Technologies We Use</h2>
        </div>
        <div class="fade-up">
            <div class="grid grid-cols-4 md:grid-cols-6 lg:grid-cols-12 gap-4 max-w-4xl mx-auto">
                <!-- Python -->
                <div class="bg-white rounded-lg p-3 flex flex-col items-center justify-center h-20 border border-gray-100">
                    <svg viewBox="0 0 32 32" class="w-8 h-8 mb-1">
                        <defs>
                            <linearGradient id="pyBlue" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" style="stop-color:#387EB8"/>
                                <stop offset="100%" style="stop-color:#366994"/>
                            </linearGradient>
                            <linearGradient id="pyYellow" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" style="stop-color:#FFC836"/>
                                <stop offset="100%" style="stop-color:#FFD43B"/>
                            </linearGradient>
                        </defs>
                        <path fill="url(#pyBlue)" d="M15.9 2c-1.5 0-2.9.1-4.1.4-3.6.8-4.2 2.4-4.2 5.4v4h8.5v1.3H7.6c-2.5 0-4.6 1.5-5.3 4.3-.8 3.2-.8 5.2 0 8.6.6 2.5 2 4.3 4.5 4.3h2.9v-3.9c0-2.8 2.4-5.2 5.3-5.2h8.4c2.4 0 4.2-1.9 4.2-4.3V7.8c0-2.3-2-4.1-4.2-4.5C22 2.9 18.9 2 15.9 2zm-4.6 3.1c.9 0 1.6.7 1.6 1.6s-.7 1.6-1.6 1.6-1.6-.7-1.6-1.6.7-1.6 1.6-1.6z"/>
                        <path fill="url(#pyYellow)" d="M24.3 13.1v3.8c0 2.9-2.5 5.3-5.3 5.3h-8.4c-2.3 0-4.2 2-4.2 4.3v8.1c0 2.3 2 3.6 4.2 4.3 2.7.8 5.2.9 8.4 0 2.1-.6 4.2-1.9 4.2-4.3v-3.2h-8.4v-1.1h12.6c2.5 0 3.4-1.7 4.2-4.3.9-2.7.8-5.2 0-8.6-.6-2.4-1.7-4.3-4.2-4.3h-3.1zm-4.8 17.2c.9 0 1.6.7 1.6 1.6s-.7 1.6-1.6 1.6-1.6-.7-1.6-1.6.7-1.6 1.6-1.6z"/>
                    </svg>
                    <span class="text-xs text-gray-600 font-medium">Python</span>
                </div>
                <!-- R -->
                <div class="bg-white rounded-lg p-3 flex flex-col items-center justify-center h-20 border border-gray-100">
                    <svg viewBox="0 0 32 32" class="w-8 h-8 mb-1">
                        <ellipse cx="16" cy="18" rx="14" ry="10" fill="#CBCED0"/>
                        <ellipse cx="14" cy="16" rx="10" ry="8" fill="#276DC3"/>
                        <path fill="#CBCED0" d="M14 10c-4.4 0-8 2.7-8 6s3.6 6 8 6c2.2 0 4.2-.7 5.6-1.8L24 26h4l-6-8c1.3-1.4 2-3.1 2-5 0-3.3-3.6-6-8-6h-2zm0 3h2c2.2 0 4 1.3 4 3s-1.8 3-4 3h-2v-6z"/>
                    </svg>
                    <span class="text-xs text-gray-600 font-medium">R</span>
                </div>
                <!-- SQL -->
                <div class="bg-white rounded-lg p-3 flex flex-col items-center justify-center h-20 border border-gray-100">
                    <svg viewBox="0 0 32 32" class="w-8 h-8 mb-1">
                        <ellipse cx="16" cy="8" rx="12" ry="5" fill="#F29111"/>
                        <path fill="#F29111" d="M4 8v14c0 2.8 5.4 5 12 5s12-2.2 12-5V8c0 2.8-5.4 5-12 5S4 10.8 4 8z"/>
                        <ellipse cx="16" cy="8" rx="12" ry="5" fill="#FFDA44" opacity="0.5"/>
                    </svg>
                    <span class="text-xs text-gray-600 font-medium">SQL</span>
                </div>
                <!-- BigQuery -->
                <div class="bg-white rounded-lg p-3 flex flex-col items-center justify-center h-20 border border-gray-100">
                    <svg viewBox="0 0 32 32" class="w-8 h-8 mb-1">
                        <path fill="#4386FA" d="M16 4L6 10v12l10 6 10-6V10L16 4z"/>
                        <path fill="#669DF6" d="M16 4v12l10-6L16 4z"/>
                        <path fill="#AECBFA" d="M16 16v12l10-6V10l-10 6z"/>
                        <circle cx="16" cy="16" r="4" fill="white"/>
                    </svg>
                    <span class="text-xs text-gray-600 font-medium">BigQuery</span>
                </div>
                <!-- Google Cloud -->
                <div class="bg-white rounded-lg p-3 flex flex-col items-center justify-center h-20 border border-gray-100">
                    <svg viewBox="0 0 32 32" class="w-8 h-8 mb-1">
                        <path fill="#EA4335" d="M20 8l5-5h-4l-5 5h4z"/>
                        <path fill="#4285F4" d="M25 8v4l3-3V5l-3 3z"/>
                        <path fill="#34A853" d="M20 24l5 5v-4l-5-5v4z"/>
                        <path fill="#FBBC05" d="M7 21l-3 3h4l3-3H7z"/>
                        <circle cx="16" cy="16" r="6" fill="#4285F4"/>
                        <circle cx="16" cy="16" r="4" fill="white"/>
                    </svg>
                    <span class="text-xs text-gray-600 font-medium">GCP</span>
                </div>
                <!-- MS Fabric -->
                <div class="bg-white rounded-lg p-3 flex flex-col items-center justify-center h-20 border border-gray-100">
                    <svg viewBox="0 0 32 32" class="w-8 h-8 mb-1">
                        <path fill="#0078D4" d="M4 8h10v10H4z"/>
                        <path fill="#50E6FF" d="M18 8h10v10H18z"/>
                        <path fill="#0078D4" d="M4 18h10v10H4z"/>
                        <path fill="#50E6FF" d="M18 18h10v10H18z" opacity="0.6"/>
                    </svg>
                    <span class="text-xs text-gray-600 font-medium">Fabric</span>
                </div>
                <!-- Elasticsearch -->
                <div class="bg-white rounded-lg p-3 flex flex-col items-center justify-center h-20 border border-gray-100">
                    <svg viewBox="0 0 32 32" class="w-8 h-8 mb-1">
                        <path fill="#FEC514" d="M2 16c0 3.3 1.2 6.3 3.1 8.7l11.8-4.3L5.1 7.3C3.2 9.7 2 12.7 2 16z"/>
                        <path fill="#00BFB3" d="M30 16c0-3.3-1.2-6.3-3.1-8.7L15.1 11.6 26.9 24.7c1.9-2.4 3.1-5.4 3.1-8.7z"/>
                        <path fill="#F04E98" d="M5.1 7.3C8 3.8 12.2 2 16 2c3.8 0 7.4 1.4 10.2 4l-11.1 5.6L5.1 7.3z"/>
                        <path fill="#1BA9F5" d="M26.9 24.7C24 28.2 19.8 30 16 30c-3.8 0-7.4-1.4-10.2-4l11.1-5.6 10 4.3z"/>
                    </svg>
                    <span class="text-xs text-gray-600 font-medium">Elastic</span>
                </div>
                <!-- Tableau -->
                <div class="bg-white rounded-lg p-3 flex flex-col items-center justify-center h-20 border border-gray-100">
                    <svg viewBox="0 0 32 32" class="w-8 h-8 mb-1">
                        <path fill="#E97627" d="M15 2v6h-4v4H5v4h6v4h4v6h2v-6h4v-4h6v-4h-6V8h-4V2h-2z"/>
                        <path fill="#C72037" d="M15 8v4h-4v4h4v4h2v-4h4v-4h-4V8h-2z"/>
                    </svg>
                    <span class="text-xs text-gray-600 font-medium">Tableau</span>
                </div>
                <!-- Power BI -->
                <div class="bg-white rounded-lg p-3 flex flex-col items-center justify-center h-20 border border-gray-100">
                    <svg viewBox="0 0 32 32" class="w-8 h-8 mb-1">
                        <rect x="4" y="14" width="6" height="14" rx="1" fill="#F2C811"/>
                        <rect x="13" y="8" width="6" height="20" rx="1" fill="#F2C811"/>
                        <rect x="22" y="4" width="6" height="24" rx="1" fill="#F2C811"/>
                    </svg>
                    <span class="text-xs text-gray-600 font-medium">PowerBI</span>
                </div>
                <!-- Kibana -->
                <div class="bg-white rounded-lg p-3 flex flex-col items-center justify-center h-20 border border-gray-100">
                    <svg viewBox="0 0 32 32" class="w-8 h-8 mb-1">
                        <path fill="#E8478B" d="M6 6l20 10L6 26V6z"/>
                        <path fill="#00BFB3" d="M6 26l10-10L6 6v20z" opacity="0.7"/>
                    </svg>
                    <span class="text-xs text-gray-600 font-medium">Kibana</span>
                </div>
                <!-- Analytics -->
                <div class="bg-white rounded-lg p-3 flex flex-col items-center justify-center h-20 border border-gray-100">
                    <svg viewBox="0 0 32 32" class="w-8 h-8 mb-1">
                        <path fill="#F9AB00" d="M26 26H6a2 2 0 01-2-2V8a2 2 0 012-2h20a2 2 0 012 2v16a2 2 0 01-2 2z"/>
                        <path fill="white" d="M8 20v2h2v-2H8zm4-4v6h2v-6h-2zm4-4v10h2V12h-2zm4 2v8h2v-8h-2z"/>
                    </svg>
                    <span class="text-xs text-gray-600 font-medium">Analytics</span>
                </div>
                <!-- HL7/FHIR -->
                <div class="bg-white rounded-lg p-3 flex flex-col items-center justify-center h-20 border border-gray-100">
                    <svg viewBox="0 0 32 32" class="w-8 h-8 mb-1">
                        <rect x="4" y="4" width="24" height="24" rx="4" fill="#E44D26"/>
                        <path fill="white" d="M8 10h4v2h-2v2h2v2h-2v4H8V10zm6 0h4v2h-2v8h-2V10zm6 0h4v10h-2v-4h-2v-2h2v-2h-2v-2z"/>
                    </svg>
                    <span class="text-xs text-gray-600 font-medium">HL7/FHIR</span>
                </div>
            </div>
        </div>
    </div>
</section>

'''

# Pages to update
PAGES = [
    "healthcare-capabilities-ai-ml-nlp.html",
    "healthcare-capabilities-saas.html",
    "healthcare-capabilities-samd.html",
    "healthcare-capabilities-data-analytics.html",
    "healthcare-capabilities-ux-design.html",
    "healthcare-capabilities-mobile.html",
    "patient-engagement-portal.html",
    "telemedicine-virtual-care.html",
    "remote-patient-monitoring.html",
    "healthcare-interoperability.html",
    "clinical-decision-support.html",
    "ehr-practice-management.html",
    "population-health-management.html",
    "predictive-analytics-healthcare.html"
]

def has_client_logos(content):
    """Check if page already has client logo ribbon"""
    return "duke-health" in content.lower() or "Healthcare Client Logos" in content

def has_tech_logos(content):
    """Check if page already has tech logos section"""
    return "Technologies We Use" in content

def add_client_ribbon(content):
    """Add client logo ribbon after hero section"""
    # Look for end of hero section
    patterns = [
        r'(</section>\s*\n\s*<!-- Standard Logo Ribbon)',
        r'(</section>\s*\n\s*<!-- What)',
        r'(</section>\s*\n\s*<!-- Trust Badges)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            insert_pos = match.start()
            # Find the actual </section> before the comment
            section_end = content.rfind('</section>', 0, insert_pos + 20)
            if section_end > 0:
                insert_pos = section_end + len('</section>')
                return content[:insert_pos] + '\n\n' + CLIENT_LOGO_RIBBON + content[insert_pos:]
    
    return content

def add_tech_section(content):
    """Add tech logos section before FAQ or footer"""
    # Look for FAQ section or footer
    patterns = [
        r'(<!-- FAQ)',
        r'(<!-- Footer)',
        r'(<footer)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            insert_pos = match.start()
            return content[:insert_pos] + TECH_LOGOS_DATA + '\n' + content[insert_pos:]
    
    return content

def process_page(filepath):
    """Process a single page"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # Add client logos if missing
    if not has_client_logos(content):
        content = add_client_ribbon(content)
        if content != original:
            changes.append("Added client logo ribbon")
    
    # Add tech logos if missing
    if not has_tech_logos(content):
        content = add_tech_section(content)
        if content != original:
            changes.append("Added tech logos section")
    
    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    
    return None

def main():
    print("=" * 60)
    print("ADDING CLIENT LOGOS AND TECH SECTIONS")
    print("=" * 60)
    
    for page in PAGES:
        if os.path.exists(page):
            changes = process_page(page)
            if changes:
                print(f"✓ {page}")
                for c in changes:
                    print(f"    - {c}")
            else:
                print(f"• {page} (no changes needed)")
        else:
            print(f"✗ {page} (file not found)")

if __name__ == "__main__":
    main()
