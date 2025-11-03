# Quick Start Guide

## Running Tests

### One-Time Setup

```bash
# 1. Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Install dependencies
uv sync

# 3. Install Playwright browser
uv run playwright install chromium
```

### Running Tests

```bash
# Just run the tests - the server starts automatically!
uv run pytest test_activity_viewer.py -v
```

## Test Results

✅ All 30 tests passing:
- Full activity with GPS data (map, charts, stats)
- Metadata-only mode (gym workouts)
- Media gallery functionality
- Unit conversion (km/mi)
- Chart hover interaction
- Cross-browser compatibility

## Viewing Activities

```bash
# Start server
python -m http.server 8000

# Open in browser
open http://localhost:8000/test-cases/full-activity/
open http://localhost:8000/test-cases/metadata-only/
open http://localhost:8000/test-cases/with-media/
```

## Documentation

- **TESTING.md** - Complete testing guide
- **TEST_IMPLEMENTATION.md** - Test architecture details
- **README.md** - Project overview
- **test-cases/README.md** - Test scenarios
