#!/bin/bash
# Build offline/bundled versions of the activity viewer

set -e

echo "Creating libs/ directory..."
mkdir -p libs

echo "Downloading dependencies..."

# Leaflet
echo "  - Leaflet.js..."
curl -sL https://unpkg.com/leaflet@1.9.4/dist/leaflet.js -o libs/leaflet.js
echo "  - Leaflet CSS..."
curl -sL https://unpkg.com/leaflet@1.9.4/dist/leaflet.css -o libs/leaflet.css

# Chart.js
echo "  - Chart.js..."
curl -sL https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js -o libs/chart.js

# D3.js
echo "  - D3.js..."
curl -sL https://d3js.org/d3.v7.min.js -o libs/d3.js

# js-yaml
echo "  - js-yaml..."
curl -sL https://cdn.jsdelivr.net/npm/js-yaml@4.1.0/dist/js-yaml.min.js -o libs/js-yaml.js

# fit-file-parser
echo "  - fit-file-parser..."
curl -sL https://cdn.jsdelivr.net/npm/fit-file-parser@2.0.8/dist/fit-parser.min.js -o libs/fit-parser.js

echo ""
echo "Dependencies downloaded to libs/"
echo ""
echo "Now run build-bundle.py to create the bundled HTML files"
