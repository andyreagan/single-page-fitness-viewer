# Plain Text Fitness Activity Viewer

A self-contained, local-first fitness activity viewer that works with .fit and .gpx files. No database, no backend - just HTML, JavaScript, and your fitness data.

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

## Quick Start

1. **Place your activity data in a folder:**
   ```
   my-activity/
   ├── index.html          (symlink to single-page-local.html)
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
├── single-page-local.html    # Main viewer (single source of truth)
├── 20872270598/              # Example activity from Strava
│   ├── index.html → ../single-page-local.html
│   ├── activity.fit
│   ├── activity.gpx
│   └── metadata.yaml
└── test-cases/               # Test scenarios
    ├── full-activity/        # GPS data + metadata
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
- **Libraries**: Leaflet.js (maps), Chart.js (charts), js-yaml (metadata), fit-file-parser (FIT files)
- **Browser-based**: All processing happens client-side
- **No dependencies**: Works offline once libraries are cached

### Library Choices vs. Competitors

Our implementation uses **Chart.js** for charts and **Leaflet.js** for maps. For comparison:

- **Strava**: Uses D3.js v3.3 for charts and Mapbox GL JS (with Leaflet compatibility layer) for maps
- **Garmin Connect**: Uses Highcharts v11.4.1 for charts and Leaflet.js for maps

We chose Chart.js and Leaflet because they're:
- Lightweight and easy to embed in a single HTML file
- Well-documented with simple APIs
- Perfect for the types of fitness data visualization we need
- Free and open source with no API keys or accounts required

## Philosophy

This project follows the "plain text" philosophy:
- Your data is yours: human-readable text files
- No proprietary formats or databases
- No vendor lock-in
- Works offline
- Easy to version control (git)
- Future-proof: as long as you have a browser, you can view your data

## Export from Strava/Garmin

1. **Strava**: Go to activity → More (...) → Export GPX or Export TCX
2. **Garmin Connect**: Activity → Gear icon → Export to GPX or Export Original

Then add a `metadata.yaml` with your notes, shoes, weather, etc.

## Contributing

This is a single-file application by design. To modify:
1. Edit `single-page-local.html`
2. All activity folders use symlinks to this file
3. Test with `test-cases/test-runner.html`

## License

MIT - Do whatever you want with it!
