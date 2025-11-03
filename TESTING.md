# Testing Guide

This project uses automated end-to-end tests with Playwright and pytest.

## Setup

### Option 1: Using uv (Recommended)

1. **Install uv**: https://docs.astral.sh/uv/getting-started/installation/
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Install Playwright browsers:**
   ```bash
   uv run playwright install chromium
   ```

### Option 2: Using Python venv

1. **Create virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install pytest playwright pytest-playwright
   ```

3. **Install Playwright browsers:**
   ```bash
   playwright install chromium
   ```

## Running Tests

### Quick Start

The tests automatically start a background HTTP server, so you only need one terminal:

**With uv:**
```bash
uv run pytest test_activity_viewer.py -v
```

**With venv:**
```bash
pytest test_activity_viewer.py -v
```

The background server starts on port 8000 and is automatically cleaned up after tests complete.

### Other Test Commands

Run tests with headed browser (see what's happening):
```bash
uv run pytest test_activity_viewer.py -v --headed
```

Run tests with full output:
```bash
uv run pytest test_activity_viewer.py -v -s
```

Run specific test class:
```bash
uv run pytest test_activity_viewer.py::TestFullActivity -v
```

Run specific test:
```bash
uv run pytest test_activity_viewer.py::TestFullActivity::test_activity_title -v
```

## Test Server

The tests automatically start and manage a background HTTP server on port 8000.

The server is:
- Started before any tests run (session-scoped fixture)
- Health-checked to ensure it's ready
- Automatically cleaned up after all tests complete

No manual server management is needed!

## Test Structure

### Test Files
- `test_activity_viewer.py` - Main test suite with Playwright tests
- `conftest.py` - Pytest configuration and fixtures
- `pytest.ini` - Pytest settings

### Test Cases

**TestFullActivity** - Tests complete GPS activity
- Page loads correctly
- Activity title and metadata display
- Map renders with markers
- Charts render (elevation, heart rate, pace)
- Stats cards display
- Unit toggle works (km ↔ mi)
- Files detected shown
- Chart hover interaction

**TestMetadataOnly** - Tests non-GPS activity (gym workout)
- Page loads correctly
- Title and description display
- Map/charts/stats NOT displayed
- Unit toggle NOT displayed

**TestWithMedia** - Tests activity with photos
- All GPS features work
- Media thumbnails display (64x64)
- Modal opens on click
- Modal closes (ESC, close button)
- Arrow key navigation works

**TestCrossBrowser** - General tests
- No console errors
- Responsive layout

## Writing New Tests

1. Add test methods to existing test classes or create new classes
2. Use Playwright's `expect()` for assertions
3. Follow the naming convention: `test_*`
4. Use descriptive test names and docstrings

Example:
```python
def test_my_feature(self, page: Page, base_url: str):
    """Test that my feature works correctly."""
    page.goto(f"{base_url}/test-cases/full-activity/")
    expect(page.locator("#myElement")).to_be_visible()
```

## CI/CD

To run tests in CI:
```bash
uv sync
uv run playwright install chromium
uv run pytest test_activity_viewer.py -v --browser chromium
```

## Troubleshooting

**"Connection refused" errors:**
- Make sure the HTTP server is running (`python -m http.server 8000`)
- Check that port 8000 is available

**"Browser not found" errors:**
- Run `uv run playwright install chromium`

**Tests timeout:**
- Increase timeout in test with `timeout=30000` parameter
- Check if server is responding: `curl http://localhost:8000`

**Flaky tests:**
- Add `time.sleep()` or use Playwright's auto-waiting
- Check for race conditions in async operations

## Manual Testing

For manual testing, use the interactive test runner:
```bash
python -m http.server 8000
# Visit: http://localhost:8000/test-cases/test-runner.html
```
