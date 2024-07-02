# Automation Project

## Project Structure

- `config/`: Contains configuration files.
- `conftest.py`: Pytest configuration and fixtures.
- `pages/`: Contains page object models for web pages.
- `components/`: Contains reusable UI components.
- `tests/`: Contains test cases.
- `README.md`: Project documentation.
- `.gitignore`: Git ignore file.
- `requirements.txt`: List of dependencies.

## Setup Instructions

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Install Dependencies

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd automation_project
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install required packages**:
    ```sh
    pip install -r requirements.txt
    playwright install
    ```

### Running Tests

1. **Navigate to the project directory**:
    ```sh
    cd /path/to/your/project
    ```

2. **Run tests with pytest**:
    ```sh
    pytest tests/
    ```

## PageManager

The `PageManager` dynamically initializes and provides access to different page objects. It uses a dictionary to store page instances and initializes them on demand.

### Available Pages

- `page`: The browser page instance.
- `playwright_page`: The `PlaywrightPage` instance.
- `example_page`: The `ExamplePage` instance.

### Usage Example

```python
from pages.page_manager import PageManager

def test_playwright(browser):
    manager = PageManager(browser)
    manager.playwright_page.open()
    manager.playwright_page.get_started_button.click()
    assert manager.page.title() == "Getting Started · Playwright"
    manager.close()
