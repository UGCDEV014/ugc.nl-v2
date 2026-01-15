# This script generates privacy.html
# It's too large to do in one go, so we'll use file operations

import re

# Read template
with open("voorwaarden.html", "r", encoding="utf-8") as f:
    template = f.read()

# Update title/meta
template = template.replace("Algemene- en betalingsvoorwaarden", "Privacyverklaring")
template = template.replace("Algemene voorwaarden - UGC.NL", "Privacyverklaring - UGC.NL")
template = template.replace("Algemene voorwaarden en betalingsvoorwaarden van UGC.NL", "Privacyverklaring van UGC.NL")
template = template.replace("Effective Date: 26 November, 2025", "Laatst gewijzigd: 8 maart 2024")

# Find content area
content_start = template.find("<div class=\"terms-content\">")
content_end = template.find("</div>\n      \n      <!-- TOC RIGHT -->")

print(f"Found content area: {content_start} to {content_end}")
print("Privacy content will be inserted here")
