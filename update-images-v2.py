#!/usr/bin/env python3
"""
DS Healthcare - Image URL Updater v2
Maps WP URLs to YOUR existing image names + new supplemental images
Run from ds-healthcare folder: python3 update-images-v2.py
"""

import os
import glob

IMAGE_REPLACEMENTS = {
    # ===== YOUR EXISTING IMAGES (using YOUR naming) =====
    "https://digitalscientists.com/wp-content/uploads/2024/05/easterseals-300x108.png": "images/easterseals-logo.png",
    "https://digitalscientists.com/wp-content/uploads/2022/03/1L9A2506-scaled.jpg": "images/nurse-patient.jpg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Window-768x982.png": "images/healthcontext-ai.png",
    "https://digitalscientists.com/wp-content/uploads/2022/12/image-28.png": "images/mds-optimizer.png",
    "https://digitalscientists.com/wp-content/uploads/2022/03/ipad-app-full-schedule.png": "images/neveralone-ipad.png",
    "https://digitalscientists.com/wp-content/uploads/2022/03/mobile-app-screen-video-call-steps.png": "images/neveralone-mobile.png",
    "https://digitalscientists.com/wp-content/uploads/2022/12/quote-image.png": "images/any-severino.png",
    
    # ===== CLIENT LOGOS (add to images/) =====
    "https://digitalscientists.com/wp-content/uploads/2024/05/Screenshot_2-300x60.png": "images/duke-health.png",
    "https://digitalscientists.com/wp-content/uploads/2023/12/congruity-health-1.svg": "images/congruity-health.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/McKesson_logo_full.png": "images/mckesson.png",
    "https://digitalscientists.com/wp-content/uploads/2023/12/logo-chs-black.png": "images/communicare.png",
    "https://digitalscientists.com/wp-content/uploads/2023/12/Guardian-Logo-Lockup2-White-1.svg": "images/guardian.svg",
    
    # ===== EHR PARTNER LOGOS =====
    "https://digitalscientists.com/wp-content/uploads/2023/10/pointclickcare-logo.png": "images/pointclickcare.png",
    "https://digitalscientists.com/wp-content/uploads/2023/10/Epic-Partner-Logo.png": "images/epic.png",
    "https://digitalscientists.com/wp-content/uploads/2023/11/gEHRiMed-768x170.png": "images/gehrimed.png",
    "https://digitalscientists.com/wp-content/uploads/2023/10/Netsmart-copy.png": "images/netsmart.png",
    
    # ===== DS LOGOS =====
    "https://digitalscientists.com/wp-content/uploads/2022/11/header-logo-dark.svg": "images/header-logo-dark.svg",
    "https://digitalscientists.com/wp-content/uploads/2022/11/header-logo-light.svg": "images/header-logo-light.svg",
    "https://digitalscientists.com/wp-content/uploads/2022/11/footer-logo.svg": "images/footer-logo.svg",
    
    # ===== TECHNOLOGY LOGOS =====
    "https://digitalscientists.com/wp-content/uploads/2024/05/image-91-1.png": "images/tech-elasticsearch.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/image-70.png": "images/tech-tableau.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/image-88.png": "images/tech-kibana.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/image-72.png": "images/tech-sql.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/image-87.png": "images/tech-python.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/image-69.png": "images/tech-powerbi.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/image-85.png": "images/tech-r.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/image-90.png": "images/tech-bigquery.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/image-92.png": "images/tech-google-analytics.png",
    "https://digitalscientists.com/wp-content/uploads/2024/06/image-63.png": "images/tech-google-cloud.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/image-86.png": "images/tech-microsoft-fabric.png",
    "https://digitalscientists.com/wp-content/uploads/2024/06/image-43.png": "images/tech-zoom.png",
    "https://digitalscientists.com/wp-content/uploads/2024/01/image-39.png": "images/tech-openai.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/image-79.png": "images/tech-chime.png",
    "https://digitalscientists.com/wp-content/uploads/2024/06/image-41.png": "images/tech-bandwidth.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/image-77.png": "images/tech-twilio.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/image-76.png": "images/tech-react.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/image-78.png": "images/tech-healthkit.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Group1.svg": "images/tech-android.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Vector1.svg": "images/tech-apple.svg",
    "https://digitalscientists.com/wp-content/uploads/2023/01/hl7fhir-300x74.png": "images/tech-hl7fhir.png",
    
    # ===== MVP PROCESS ICONS =====
    "https://digitalscientists.com/wp-content/uploads/2024/10/icon-idea-prioritization-1.svg": "images/icon-discovery.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/10/icon-validate-strategy-1.svg": "images/icon-blueprint.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/10/icon-launch-wh-1.svg": "images/icon-launch.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/10/grow-white-1.svg": "images/icon-grow.svg",
    
    # ===== CTA ICONS =====
    "https://digitalscientists.com/wp-content/uploads/2024/05/deploy.svg": "images/icon-deploy.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/direct.svg": "images/icon-direct.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/mvp.svg": "images/icon-mvp.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/launch-white1.svg": "images/icon-launch-white.svg",
    
    # ===== MOBILE REQUIREMENTS ICONS =====
    "https://digitalscientists.com/wp-content/uploads/2024/08/Wearable-Technology.svg": "images/icon-wearable.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/08/Specialized-Medical-Devices.svg": "images/icon-medical-devices.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/08/Data-Security.svg": "images/icon-data-security.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/08/Regulatory-Compliance.svg": "images/icon-regulatory.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/08/Reliability-and-Performance.svg": "images/icon-reliability.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/08/Real-time-Functionality.svg": "images/icon-realtime.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/08/Interoperability.svg": "images/icon-interop.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/08/User-Experience-UX.svg": "images/icon-ux.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/08/Integration-Capabilities.svg": "images/icon-integration.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/08/Patient-Engagement.svg": "images/icon-patient-engage.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/08/Scalability.svg": "images/icon-scalability.svg",
    
    # ===== SOLUTION ICONS =====
    "https://digitalscientists.com/wp-content/uploads/2024/05/Group-120084.svg": "images/icon-predictive.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Group-120085.svg": "images/icon-telehealth.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Group-120086.svg": "images/icon-rpm.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Group-120087.svg": "images/icon-interop-sol.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Group-120088.svg": "images/icon-cdss.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Group-1200814.svg": "images/icon-medical-ai.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Group-1200815.svg": "images/icon-ehr.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Group-120089.svg": "images/icon-population.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Group-1200810.svg": "images/icon-patient-portal.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Group-1200811.svg": "images/icon-risk-adjust.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Group-1200812.svg": "images/icon-web-apps.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Group-1200813.svg": "images/icon-care-mgmt.svg",
    
    # ===== CAPABILITY ICONS =====
    "https://digitalscientists.com/wp-content/uploads/2024/06/icon-design.svg": "images/icon-design.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/06/icon-research.svg": "images/icon-research.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/06/Group-11999.svg": "images/icon-saas.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/06/Group-11998.svg": "images/icon-samd.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/06/Group-12000.svg": "images/icon-data.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/06/Group-11997.svg": "images/icon-ux-cap.svg",
    
    # ===== ARCHITECTURE DIAGRAMS =====
    "https://digitalscientists.com/wp-content/uploads/2024/06/Group-12069.png": "images/arch-predictive.png",
    "https://digitalscientists.com/wp-content/uploads/2024/06/Group-12070.png": "images/arch-telemedicine.png",
    "https://digitalscientists.com/wp-content/uploads/2024/06/Group-12071.png": "images/arch-rpm.png",
    "https://digitalscientists.com/wp-content/uploads/2025/02/Frame-1073713437.png": "images/arch-vbc.png",
    
    # ===== HERO / FEATURE IMAGES =====
    "https://digitalscientists.com/wp-content/uploads/2024/06/image-12-2.png": "images/hero-raf-trends.png",
    "https://digitalscientists.com/wp-content/uploads/2024/06/image-9-1.png": "images/hero-raf-models.png",
    "https://digitalscientists.com/wp-content/uploads/2024/06/image-55.png": "images/hero-telehealth.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Accessibility-photo1.png": "images/hero-accessibility.png",
    "https://digitalscientists.com/wp-content/uploads/2024/01/Mask-group.png": "images/hero-vbc.png",
    "https://digitalscientists.com/wp-content/uploads/2024/01/Group-239-768x442.png": "images/hero-pharma.png",
    "https://digitalscientists.com/wp-content/uploads/2024/01/senior-patient-talking-doctor-video-call-1.png": "images/hero-population.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/senior-patient-talking-doctor-video-call-1.png": "images/hero-senior-ipad.png",
    "https://digitalscientists.com/wp-content/uploads/2024/06/guardian-image-hero-block.png": "images/hero-guardian.png",
    
    # ===== TEAM / EXPERT PHOTOS =====
    "https://digitalscientists.com/wp-content/uploads/2024/06/P1000918-sm-1.png": "images/team-bob-klein.png",
    "https://digitalscientists.com/wp-content/uploads/2024/06/P1000839-sm-1.png": "images/team-expert-2.png",
    "https://digitalscientists.com/wp-content/uploads/2024/06/Group-11208.png": "images/team-expert-3.png",
    "https://digitalscientists.com/wp-content/uploads/2025/01/Kelley-Rose-small-img2.png": "images/team-kelley-rose.png",
    "https://digitalscientists.com/wp-content/uploads/2024/06/Frame-191.png": "images/team-greg-zancewicz.png",
    "https://digitalscientists.com/wp-content/uploads/2024/06/Frame-191-1.png": "images/team-jerry-deng.png",
    "https://digitalscientists.com/wp-content/uploads/2024/06/Frame-191-2.png": "images/team-michelle-titolo.png",
    "https://digitalscientists.com/wp-content/uploads/2023/01/bob-klein@2x-1.jpg": "images/team-bob-klein-small.jpg",
    
    # ===== TESTIMONIAL / QUOTE =====
    "https://digitalscientists.com/wp-content/uploads/2024/06/Group.svg": "images/logo-communicare-quote.svg",
    
    # ===== CASE STUDY IMAGES =====
    "https://digitalscientists.com/wp-content/uploads/2022/03/CHS-CallCenter-CALL-Main-V1-–-1-1.png": "images/case-neveralone-platform.png",
    "https://digitalscientists.com/wp-content/uploads/2022/03/senior-woman-using-app.png": "images/case-neveralone-senior.png",
    "https://digitalscientists.com/wp-content/uploads/2023/03/digital_health_hero_v2-e1678383561507.png": "images/case-healthcontext-hero.png",
    "https://digitalscientists.com/wp-content/uploads/2022/01/guardian-monitor-with-text-message-and-background.png": "images/case-guardian-monitor.png",
    "https://digitalscientists.com/wp-content/uploads/2024/07/McKesson-Pharmaceutical-warehouse-thumbnail.jpg": "images/case-mckesson-warehouse.jpg",
    "https://digitalscientists.com/wp-content/uploads/2024/06/c24e85b54bd332760d535ae2bc35cf79-768x512.jpg": "images/case-study-1.jpg",
    "https://digitalscientists.com/wp-content/uploads/2024/06/4a7089cff928f1a1fd75e7f3d7f2329e-768x512.jpg": "images/case-study-2.jpg",
    "https://digitalscientists.com/wp-content/uploads/2024/06/9905520ab70f3499ab67ded94dece005-768x513.jpg": "images/case-study-3.jpg",
    
    # ===== CASE STUDY LOGOS =====
    "https://digitalscientists.com/wp-content/uploads/2024/06/logo.svg": "images/case-logo-neveralone.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/06/Frame-11197.svg": "images/case-logo-healthcontext.svg",
    "https://digitalscientists.com/wp-content/uploads/2024/06/VBC-Insights.svg": "images/case-logo-vbc.svg",
    
    # ===== COMPLIANCE =====
    "https://digitalscientists.com/wp-content/uploads/2024/05/svgviewer-png-output1.png": "images/compliance-hipaa-onc.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Group-3.png": "images/compliance-hipaa.png",
    "https://digitalscientists.com/wp-content/uploads/2024/05/Group-41.png": "images/compliance-data.png",
}

def update_html_files():
    html_files = glob.glob("*.html")
    if not html_files:
        print("ERROR: No HTML files found. Run from ds-healthcare folder.")
        return
    
    print(f"Found {len(html_files)} HTML files")
    print(f"Image mappings: {len(IMAGE_REPLACEMENTS)}")
    print("-" * 50)
    
    total_replacements = 0
    files_updated = []
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        file_replacements = 0
        for wp_url, local_path in IMAGE_REPLACEMENTS.items():
            if wp_url in content:
                content = content.replace(wp_url, local_path)
                file_replacements += 1
        
        if file_replacements > 0:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            files_updated.append((html_file, file_replacements))
            total_replacements += file_replacements
    
    print(f"\nFiles updated: {len(files_updated)}")
    print(f"Total replacements: {total_replacements}")
    for filename, count in sorted(files_updated):
        print(f"  {filename}: {count}")
    print("\n✓ Done!")

if __name__ == "__main__":
    update_html_files()
