import os
import time
import pytest
from utils.screenshot_utils import compare_images

BASELINE_DIR = "baseline_images/"
NEW_DIR = "new_screenshots/"
DIFF_DIR = "reports/"

@pytest.mark.parametrize("url, filename", [
    ("https://fr.wikipedia.org/wiki/Mus%C3%A9e_du_Louvre", "example_homepage.png"),
])
def test_ui_regression(browser, url, filename):
    os.makedirs(BASELINE_DIR, exist_ok=True)
    os.makedirs(NEW_DIR, exist_ok=True)
    os.makedirs(DIFF_DIR, exist_ok=True)

    baseline_path = os.path.join(BASELINE_DIR, filename)
    new_path = os.path.join(NEW_DIR, filename)
    diff_path = os.path.join(DIFF_DIR, "diff_" + filename)

    # Set viewport for consistent screenshots
    browser.set_viewport_size({"width": 1920, "height": 1080})

    # Load the page properly
    browser.goto(url, wait_until="networkidle", timeout=30000)
    browser.wait_for_load_state("networkidle")
    time.sleep(8)  # Ensure all fonts/images are loaded

    # Scroll down before taking a screenshot
    browser.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)

    # Take a new screenshot for comparison
    browser.screenshot(path=new_path, full_page=True)

    # If baseline does not exist, create it and skip test
    if not os.path.exists(baseline_path):
        print(f"Baseline image not found. Creating one: {baseline_path}")
        browser.screenshot(path=baseline_path, full_page=True)
        pytest.skip("Baseline image created. Rerun the test.")

    # Compare images
    assert compare_images(baseline_path, new_path, diff_path), "UI has changed!"

