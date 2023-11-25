import os
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function", autouse=True)
def browser_context_args(request):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, args=['--start-maximized'])
        context = browser.new_context(no_viewport=True)
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        yield page

        try:
            # Check if the test failed
            if request.session.testsfailed > 0:
                # If the test failed, stop the tracing and save it
                context.tracing.stop(path="artifacts/tracing/trace.zip")
        finally:
            page.pause()
            page.close()
            browser.close()


# Clean up the trace file after the test
@pytest.fixture(scope="session")
def trace_file_cleaning():
    file_path = os.path.join(os.path.dirname(__file__), "artifacts", "fails", "file.txt")
    with open(file_path, "w") as file:
        file.truncate(0)
