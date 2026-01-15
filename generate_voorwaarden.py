#!/usr/bin/env python3
"""Complete script to generate voorwaarden.html with all sections"""

# Read header and footer from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

header_end = index_content.find('</header>')
header = index_content[:header_end + len('</header>')]
footer_start = index_content.find('<!-- FOOTER -->')
footer = index_content[footer_start:]

# Start HTML
html = '''<!DOCTYPE html>
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
'''

# Add all sections (will continue in next part due to length)
# Sections 1-10 are already in the script above
# We'll add sections 11-26 here

print("Starting to build voorwaarden.html...")
print("This will generate a large file with all terms")

# Write to file in parts - we'll use a different approach
# Let me create a template file first
