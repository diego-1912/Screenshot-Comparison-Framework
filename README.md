# 📸 Screenshot Comparison Framework for UI Regression Testing

## 🎯 **Objective**
This framework is designed for **UI regression testing** by capturing screenshots of web pages and comparing them with baseline images. It helps **detect unintended UI changes** between different test runs.

The framework uses:
- **Playwright** for browser automation.
- **OpenCV** for image comparison.
- **Pytest** for test execution and reporting.

---

## 📦 **Libraries & Dependencies**
Before using this framework, install the required dependencies:

### 🔹 **Install Python Packages**
```bash
pip install pytest playwright opencv-python numpy pillow
playwright install
```

### **Libraries Used**
- **playwright** → Automates browsers (Chromium, Firefox, WebKit).
- **opencv-python** → Compares images for UI differences.
- **numpy** → Handles image matrix operations.
- **pillow** → Processes images.
- **pytest** → Runs test cases.

---

## 📂 **Project Folder Structure**
```plaintext
screenshot_comparison_framework/
│── tests/
│   ├── test_ui_regression.py    # UI regression test
│── utils/
│   ├── screenshot_utils.py      # Image comparison logic
│── baseline_images/             # Stores baseline screenshots (golden images)
│── new_screenshots/             # Stores new screenshots taken during tests
│── reports/                     # Stores diff images and test reports
│── conftest.py                   # Playwright fixture for browser setup
│── requirements.txt              # Dependencies list
│── README.md                     # Documentation
```

---

## 🚀 **How to Run Tests**

### 1️⃣ Ensure Playwright is installed
```bash
playwright install
```

### 2️⃣ Run the test cases
```bash
pytest -s -v tests/test_ui_regression.py
```

---

## 📜 **How the Framework Works**
1. The framework launches a browser and navigates to a URL.
2. It captures a screenshot of the current UI and saves it in `new_screenshots/`.
3. If a baseline screenshot does not exist, it creates one in `baseline_images/` and skips the test.
4. If a baseline exists, it compares it with the new screenshot:
   - If no significant differences → **Test passes ✅**.
   - If differences exceed threshold → **Test fails ❌** and saves a diff image in `reports/`.

---

## ⚙ **Configurable Settings**
Modify the `compare_images()` function inside `utils/screenshot_utils.py` to adjust comparison sensitivity:

```python
def compare_images(baseline_path, new_path, diff_path, threshold=5.0):
```

- `threshold=5.0` → Allows **5% UI changes** before failing.
- Increase threshold if **minor changes are acceptable**.

---

## 📊 **Handling Test Failures**
If a test fails:
1. Check the `reports/` folder for a diff image.
2. If changes are expected, update the baseline image:
   ```bash
   rm baseline_images/example_homepage.png
   ```
   *(or manually delete the file and rerun the test).*
3. Re-run the test to create a new baseline image.

---

## 🛠 **Troubleshooting**

| Issue | Possible Cause | Solution |
|--------|--------------------|------------|
| **Protocol error (Page.captureScreenshot): Unable to capture screenshot** | Page is still loading | Add `time.sleep(5)` before capturing screenshot. |
| **Test fails randomly** | UI elements (ads, popups) changed | Increase threshold to `10.0` in `compare_images()`. |
| **Differences in `diff_example_homepage.png`** | Fonts, images not fully loaded | Add `browser.wait_for_load_state("networkidle")` before screenshot. |

---

## 🔄 **Future Enhancements**
✅ Support for multiple resolutions.  
✅ Automated baseline updates via CI/CD.  
✅ Email notifications on test failures.

---

## 🏆 **Contributors**
👨‍💻 **Maintainer:** Diego Vargas  
📧 **Contact:** louvre.25@hotmail.com
🔗 **GitHub:** diego-1912

---
# Screenshot-Comparison-Framework
