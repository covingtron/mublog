"""Render the one-chord repro page to a local PNG."""

from pathlib import Path

from playwright.sync_api import sync_playwright

html = Path('scripts/chord_repro.html').resolve()
png = Path('scripts/chord-repro.png').resolve()

with sync_playwright() as playwright:
    page = playwright.chromium.launch().new_page(
        viewport={'width': 160, 'height': 140}, device_scale_factor=2
    )
    page.goto(html.as_uri())
    page.screenshot(path=str(png))
