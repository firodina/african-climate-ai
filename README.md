# African Climate AI - Week 0 Challenge

This repository contains the setup for the African Climate AI challenge, focusing on exploratory analysis of historical climate data.

## Environment Setup

### Prerequisites
- Python 3.8 or higher
- Git

### Local Setup
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/climate-challenge-week0.git
   cd climate-challenge-week0
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Development
- Use the `src/` folder for source code.
- Use `notebooks/` for Jupyter notebooks.
- Use `scripts/` for utility scripts.
- Use `tests/` for unit tests.

### CI/CD
The repository includes a GitHub Actions workflow that installs dependencies on every push to the main branch.