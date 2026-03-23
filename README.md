# 🛒 Shufersal Automation — Playwright + Python

End-to-end automation test suite for [shufersal.co.il](https://www.shufersal.co.il/online/)
using **Playwright**, **Pytest**, and the **Page Object Model** pattern.



## 📁 Project Structure

```
shufersal_tests/
├── pages/
│   ├── base_page.py          # Shared Playwright methods (click, fill, get_text…)
│   └── home_page.py          # All 7 steps — one page object for the SPA
├── tests/
│   └── test_shufersal_milk_flow.py   # Full E2E + 5 individual step tests
├── fixtures/
│   └── browser_fixtures.py   # Browser / context / page / home_page fixtures
├── utils/
│   └── constants.py          # URLs, keywords, expected text, timeouts
├── conftest.py               # Registers fixtures globally for all tests
├── pytest.ini                # Test discovery and default CLI options
└── requirements.txt          # Python dependencies
```

---

## ⚙️ Setup

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Mac / Linux
venv\Scripts\activate           # Windows

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Install Playwright's Chromium browser
playwright install chromium
```

---

## ▶️ Running Tests

```bash

# Run with slow motion, ui visible and log prints to console
pytest -v -s --headed --slowmo=300

# Run all tests (headless)
pytest

# Run with visible browser
pytest --headed

# Run only the full E2E smoke test
pytest -m smoke --headed -v

# Run all shufersal tests
pytest -m shufersal -v

# Run a specific test
pytest tests/test_shufersal_milk_flow.py::TestShufersalMilkFlow::test_full_flow -v

# Run with HTML report
pytest --html=report.html --self-contained-html
```

---

## 🐛 Debugging

```bash
# Step-through debugger (Playwright Inspector)
PWDEBUG=1 pytest tests/test_shufersal_milk_flow.py --headed   # Mac/Linux
set PWDEBUG=1 && pytest tests/test_shufersal_milk_flow.py --headed  # Windows

# Slow down actions (500ms between steps) for visual debugging
pytest --headed --slowmo=500
```

# shufersal_automation_testing