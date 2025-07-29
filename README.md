# MySQL Site Automation

Automated end-to-end testing framework for the official [MySQL website](https://www.mysql.com), built with Python, Playwright, and Pytest.

This project includes user registration flows, login tests (positive & negative), and validation of documentation versioning such as release notes and reference manuals.

---

## Features

- Automated user **registration and login** flows
- **UI validation** of login success/failure
- Extraction and verification of **document versions**
- Modular and reusable **Page Object Model (POM)**
- **Cross-browser support** (Chromium, Firefox)
- Built with **Playwright (sync)** + **Pytest**

---

##  Tech Stack

| Tech        | Use Case                        |
|-------------|----------------------------------|
| Python      | Main programming language        |
| Playwright  | Browser automation               |
| Pytest      | Test framework                   |
| Selenium (partial) | For `Keys` import (can be removed if unused) |

---

##  Requirements

Create a virtual environment and install the following:

```bash
pip install -r requirements.txt
