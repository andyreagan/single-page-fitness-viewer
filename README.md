# Plain Text Fitness Activity Viewer

A self-contained, local-first fitness activity viewer that works with .fit and .gpx files. No database, no backend, no server - just a single HTML file, your browser, and your fitness data.

Available in two versions: **Chart.js** (recommended, simpler) and **D3.js** (advanced, more flexible).

## Features

### Core Functionality
- **GPS Activity Viewing**: Load .fit and .gpx files to visualize your runs, rides, and other GPS activities
- **Interactive Map**: OpenStreetMap-based route visualization with distinctive start (green) and finish (red) markers
- **Real-time Charts**: Elevation, heart rate, and pace charts with synchronized hover interaction
- **Chart-to-Map Linking**: Hover over any chart to see a vertical crosshair on all charts and your position on the map
- **Unit Toggle**: Switch between metric (km) and imperial (mi) units on the fly
- **Media Gallery**: Automatically detect photos in a `media/` folder with full-screen gallery viewer
- **Metadata-Only Mode**: Works without GPS data for gym workouts, yoga, etc.

### Display
- Clean, compact Strava/Garmin Connect-inspired interface
- Activity stats: distance, duration, pace, elevation gain, heart rate
- Human-readable metadata in YAML or Org-mode format
- 64x64 photo thumbnails with click-to-expand gallery

## Two Implementations

This project includes **two complete implementations** of the activity viewer:

1. **Chart.js version** (`single-page-local.html`) - Recommended
   - Simpler API, easier to understand
   - Smaller file size (~50KB)
   - Great for most use cases

2. **D3.js version** (`single-page-d3.html`) - Advanced
   - More powerful and flexible
   - Fine-grained control over visualizations
   - Better for custom chart modifications

Both share the same map (Leaflet.js), file parsing, and metadata handling. Choose whichever you prefer!

## Quick Start

1. **Place your activity data in a folder:**
   ```
   my-activity/
   ├── index.html          (symlink to single-page-local.html or single-page-d3.html)
   ├── activity.fit        (optional)
   ├── activity.gpx        (optional)
   ├── metadata.yaml       (optional but recommended)
   └── media/              (optional - photos/videos)
       ├── photo1.jpg
       └── photo2.jpg
   ```

2. **Start a local web server:**
   ```bash
   python3 -m http.server 8000
   ```

3. **Open in browser:**
   ```
   http://localhost:8000/my-activity/
   ```

## Metadata Format (YAML)

```yaml
title: "Morning Run"
date: 2025-11-03
type: "running"
description: |
  Great morning run through the neighborhood.
  Weather was perfect and felt strong throughout.

weather: "Clear, 15°C"
effort: "Easy"
shoes: "Nike Pegasus 40"

tags:
  - morning
  - easy-run
  - neighborhood
```

All fields are optional. You can add any custom fields you want!

## File Structure

```
plain-text-fitness/
├── single-page-local.html    # Chart.js version (recommended)
├── single-page-d3.html       # D3.js version (advanced)
└── test-cases/               # Test scenarios
    ├── full-activity/        # Chart.js: GPS data + metadata
    ├── full-activity-d3/     # D3.js: GPS data + metadata
    ├── metadata-only/        # Gym workout (no GPS)
    ├── with-media/           # GPS data + photos
    ├── README.md             # Test documentation
    └── test-runner.html      # Manual test suite
```

## Testing

### Manual Testing
```bash
python3 -m http.server 8000
# Visit: http://localhost:8000/test-cases/test-runner.html
```

### Automated Testing
We have comprehensive Playwright + pytest automated tests with automatic server management:
```bash
# Install uv (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Install browser
uv run playwright install chromium

# Run tests (server starts automatically!)
uv run pytest test_activity_viewer.py -v
```

See `TESTING.md` for complete documentation.

## Use Cases

### GPS Activities
- Running, cycling, hiking with route visualization
- Full stats and charts
- Heart rate, pace, elevation analysis

### Non-GPS Activities
- Gym workouts
- Yoga sessions
- Strength training
- Just use metadata.yaml with title, date, description, and custom fields

### Photo Documentation
- Add photos to any activity in the `media/` folder
- Automatic thumbnail generation and gallery view
- Perfect for scenic runs, race photos, or form checks

## Technology Stack

- **No build step**: Single HTML file with embedded CSS/JS
- **Client-side processing**: All file parsing and rendering happens in your browser
- **External dependencies**: Libraries loaded from CDN (requires internet connection on first load)
  - Chart.js version: Leaflet.js, Chart.js, js-yaml, fit-file-parser
  - D3.js version: Leaflet.js, D3.js, js-yaml, fit-file-parser

### Library Choices vs. Competitors

We provide **two implementations** - one with Chart.js, one with D3.js. For comparison:

- **Strava**: Uses D3.js v3.3 for charts and Mapbox GL JS (with Leaflet compatibility layer) for maps
- **Garmin Connect**: Uses Highcharts v11.4.1 for charts and Leaflet.js for maps

**Chart.js version** (recommended):
- Lightweight and easy to understand
- Well-documented with simple API
- Perfect for standard fitness visualizations

**D3.js version** (advanced):
- More powerful and flexible
- Fine-grained control for custom visualizations
- Similar to what Strava uses

Both are free and open source with no API keys or accounts required.

## Philosophy

This project follows the "plain text" philosophy:
- Your data is yours: human-readable text files
- No proprietary formats or databases
- No vendor lock-in
- No server or cloud services required (runs locally)
- Easy to version control (git)
- Future-proof: as long as you have a browser, you can view your data

**Note on offline usage**: Currently requires internet connection to load libraries from CDN. A fully bundled offline version could be created in the future.

## Export from Strava/Garmin

1. **Strava**: Go to activity → More (...) → Export GPX or Export TCX
2. **Garmin Connect**: Activity → Gear icon → Export to GPX or Export Original

Then add a `metadata.yaml` with your notes, shoes, weather, etc.

## Contributing

Two single-file implementations by design:
- **Chart.js version**: Edit `single-page-local.html`
- **D3.js version**: Edit `single-page-d3.html`

Testing:
1. Manual: Use `test-cases/test-runner.html`
2. Automated: Run `uv run pytest test_activity_viewer.py -v`
   - 37 tests covering both Chart.js and D3.js versions
   - Automatic background server management

## License

MIT - Do whatever you want with it!
