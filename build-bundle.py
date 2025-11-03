#!/usr/bin/env python3
"""
Build bundled/offline versions of the activity viewer.

This script takes the CDN-based HTML files and creates bundled versions
with all dependencies inlined.
"""

import re
from pathlib import Path


def bundle_html(input_file: str, output_file: str, chart_lib: str):
    """Bundle an HTML file with all dependencies inlined."""

    print(f"\nBundling {input_file} -> {output_file}")

    # Read the source HTML
    with open(input_file, 'r') as f:
        html = f.read()

    # Read the library files
    libs_dir = Path('libs')

    leaflet_css = (libs_dir / 'leaflet.css').read_text()
    leaflet_js = (libs_dir / 'leaflet.js').read_text()
    js_yaml = (libs_dir / 'js-yaml.js').read_text()
    fit_parser = (libs_dir / 'fit-parser.js').read_text()

    if chart_lib == 'chartjs':
        chart_js = (libs_dir / 'chart.js').read_text()
    else:  # d3
        chart_js = (libs_dir / 'd3.js').read_text()

    # Helper function to safely replace - escapes backslashes in replacement
    def safe_replace(pattern, replacement_template, content_var):
        # Use a lambda to avoid interpreting backslashes in the content
        return re.sub(pattern, lambda m: replacement_template.format(content=content_var), html)

    # Replace Leaflet CSS link with inline style
    leaflet_css_pattern = r'<link rel="stylesheet" href="https://unpkg\.com/leaflet@[\d\.]+/dist/leaflet\.css"\s*/>'
    html = re.sub(leaflet_css_pattern, lambda m: f'<style>/* Leaflet CSS */\n{leaflet_css}\n</style>', html)

    # Replace script tags with inline scripts
    # Leaflet
    leaflet_js_pattern = r'<script src="https://unpkg\.com/leaflet@[\d\.]+/dist/leaflet\.js"></script>'
    html = re.sub(leaflet_js_pattern, lambda m: f'<script>/* Leaflet.js */\n{leaflet_js}\n</script>', html)

    # Chart.js or D3.js
    if chart_lib == 'chartjs':
        chart_pattern = r'<script src="https://cdn\.jsdelivr\.net/npm/chart\.js@[\d\.]+/dist/chart\.umd\.min\.js"></script>'
        html = re.sub(chart_pattern, lambda m: f'<script>/* Chart.js */\n{chart_js}\n</script>', html)
    else:
        d3_pattern = r'<script src="https://d3js\.org/d3\.v7\.min\.js"></script>'
        html = re.sub(d3_pattern, lambda m: f'<script>/* D3.js */\n{chart_js}\n</script>', html)

    # js-yaml
    yaml_pattern = r'<script src="https://cdn\.jsdelivr\.net/npm/js-yaml@[\d\.]+/dist/js-yaml\.min\.js"></script>'
    html = re.sub(yaml_pattern, lambda m: f'<script>/* js-yaml */\n{js_yaml}\n</script>', html)

    # fit-file-parser (with CommonJS shim)
    # Match the shim, library, and global assignment scripts together
    fit_pattern = r'<script>\s*//[^\n]*CommonJS[^<]*</script>\s*<script src="https://cdn\.jsdelivr\.net/npm/fit-file-parser@[\d\.]+/dist/fit-parser\.min\.js"></script>\s*<script>\s*//[^\n]*FitParser[^<]*</script>'
    html = re.sub(
        fit_pattern,
        lambda m: f'<script>/* fit-file-parser with CommonJS shim */\nvar module = {{ exports: {{}} }};\nvar exports = module.exports;\n{fit_parser}\nwindow.FitParser = module.exports.default || module.exports.FitParser || module.exports;\n</script>',
        html
    )

    # Add a comment at the top indicating this is a bundled version
    html = re.sub(
        r'(<!DOCTYPE html>)',
        r'\1\n<!-- BUNDLED VERSION: All JavaScript/CSS dependencies inlined.\n     Note: Map tiles still load from OpenStreetMap servers (requires internet for maps).\n     Charts, stats, and data processing work fully offline. -->',
        html
    )

    # Write the bundled HTML
    with open(output_file, 'w') as f:
        f.write(html)

    # Get file size
    size_kb = Path(output_file).stat().st_size / 1024
    print(f"  Created: {output_file} ({size_kb:.1f} KB)")


def main():
    # Check that libs directory exists
    if not Path('libs').exists():
        print("Error: libs/ directory not found!")
        print("Run ./build-offline.sh first to download dependencies.")
        return

    print("Building bundled/offline versions...")

    # Bundle Chart.js version
    bundle_html('single-page-local.html', 'single-page-bundled.html', 'chartjs')

    # Bundle D3.js version
    bundle_html('single-page-d3.html', 'single-page-d3-bundled.html', 'd3')

    print("\n✅ Bundled versions created!")
    print("\nFiles created:")
    print("  - single-page-bundled.html (Chart.js version)")
    print("  - single-page-d3-bundled.html (D3.js version)")
    print("\nNote: All JavaScript/CSS is bundled, but map tiles still load from")
    print("      OpenStreetMap servers (internet required for maps).")
    print("      Charts, stats, and data processing work fully offline.")


if __name__ == '__main__':
    main()
