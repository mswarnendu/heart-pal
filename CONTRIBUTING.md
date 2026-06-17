# Contributing to HeartPal

Thank you for your interest in contributing to **HeartPal**! Whether you're fixing a bug, optimizing the machine learning pipeline, or improving the user interface, your contributions are greatly appreciated.

As a project focused on healthcare data science and user-centric deployment, maintaining code quality, readability, and reliability is our top priority.

---

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9+**
- **pip (Python package installer)**

### Local Installation

Clone the repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com/yourusername/heartpal.git

# Navigate into the project directory
cd heartpal

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

Launch the Streamlit application locally with:

```bash
streamlit run app.py
```

---

## Code Standards & Guidelines

To keep the codebase clean and maintainable, please follow these guidelines.

### Python & Streamlit

#### Indentation

- Use **4 spaces** for indentation.
- Never mix tabs and spaces.

#### State Management

- Use `st.session_state` for preserving user data across pages and form submissions.
- Ensure conditional logic is properly structured to prevent duplicate rendering or state leakage.

#### Project Structure

- Separate machine learning logic from UI components whenever possible.
- Keep preprocessing, inference, and visualization modular.

#### Naming Conventions

Follow **PEP 8**:

- Functions and variables should use `snake_case`.
- Classes should use `PascalCase`.
- Constants should use `UPPER_CASE`.

Example:

```python
def calculate_risk_score():
    ...
```

---

## Git Workflow

1. Fork the repository.

2. Create a feature branch:

```bash
git checkout -b feature/your-awesome-feature
```

3. Commit your changes with clear commit messages:

```bash
git commit -m "Fix: Resolve duplicate monthly check-in rendering"
```

4. Push your branch:

```bash
git push origin feature/your-awesome-feature
```

5. Open a Pull Request against the `main` branch.

Please describe:

- What changed
- Why it changed
- Any related issues
- Screenshots (if UI changes were made)

---

## Reporting Bugs

Found a bug?

Please open a GitHub Issue and include:

- A clear description
- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Relevant error logs

---

## Suggesting Features

Feature requests are always welcome.

When opening an issue, please explain:

- The problem you're trying to solve
- Your proposed solution
- Any alternative approaches you've considered

---

## Thank You

Every contribution, whether it's code, documentation, bug reports, or ideas, helps make HeartPal better for everyone.

Thank you for helping keep **HeartPal** secure, reliable, and easy to use!
