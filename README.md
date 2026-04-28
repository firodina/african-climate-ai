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

## Dashboard Development

### Streamlit App

The project includes an interactive Streamlit dashboard for visualizing climate data across African countries.

#### Development Process

1. **Branch Creation**: Created `dashboard-dev` branch for dashboard development
2. **App Structure**: Organized dashboard code in `app/main.py`
3. **Data Integration**: App reads cleaned CSV files from `data/` directory
4. **UI Components**: Implemented multi-select country widget, year range slider, temperature trend chart, and precipitation boxplot
5. **Git Hygiene**: Maintained clean commit history with descriptive messages

#### Features

- **Country Selection**: Multi-select dropdown to filter by countries (Ethiopia, Kenya, Sudan, Tanzania, Nigeria)
- **Time Filtering**: Year range slider to focus on specific periods (2015-2026)
- **Temperature Trends**: Line chart showing monthly average temperature (T2M) over time
- **Precipitation Analysis**: Boxplot displaying precipitation distribution across countries
- **Summary Statistics**: Tables showing mean and standard deviation for temperature and precipitation

#### Usage Instructions

1. Ensure cleaned data files exist in `data/` directory:
   - `ethiopia_clean.csv`
   - `kenya_clean.csv`
   - `sudan_clean.csv`
   - `tanzania_clean.csv`
   - `nigeria_clean.csv`

2. Run the dashboard locally:
   ```
   streamlit run app/main.py
   ```

3. Access the dashboard in your browser at `http://localhost:8501`

4. Use the sidebar controls to:
   - Select countries to include in analysis
   - Adjust the year range for temporal filtering
   - View interactive charts and statistics

#### Deployment

The dashboard is ready for deployment to Streamlit Community Cloud:
1. Push the repository to GitHub
2. Connect to Streamlit Cloud
3. Deploy from the `app/main.py` file
