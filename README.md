# African Climate AI - Week 0 Challenge

This repository contains a comprehensive analysis of historical climate data for five African countries as part of the African Climate AI Week 0 challenge. The project demonstrates end-to-end data science workflow including data acquisition, cleaning, exploratory data analysis (EDA), cross-country comparison, vulnerability assessment, and interactive dashboard development.

## 📁 Project Structure

```
african-climate-ai/
├── .github/
│   └── workflows/
│       └── ci.yml                    # GitHub Actions CI/CD pipeline
├── app/
│   └── main.py                       # Streamlit interactive dashboard
├── data/
│   ├── Data Legend.txt               # NASA POWER data documentation
│   ├── ethiopia.csv                  # Raw climate data for Ethiopia
│   ├── kenya.csv                     # Raw climate data for Kenya
│   ├── nigeria.csv                   # Raw climate data for Nigeria
│   ├── sudan.csv                     # Raw climate data for Sudan
│   └── tanzania.csv                  # Raw climate data for Tanzania
├── notebooks/
│   ├── compare_countries.ipynb       # Cross-country comparison analysis
│   ├── ethiopia_eda.ipynb            # Ethiopia climate data EDA
│   ├── kenya_eda.ipynb               # Kenya climate data EDA
│   ├── nigeria_eda.ipynb             # Nigeria climate data EDA
│   ├── sudan_eda.ipynb               # Sudan climate data EDA
│   ├── tanzania_eda.ipynb            # Tanzania climate data EDA
│   └── README.md                     # Notebooks documentation
├── scripts/                          # Utility scripts (placeholder)
├── src/                              # Source code (placeholder)
├── tests/                            # Unit tests (placeholder)
├── .gitignore                        # Git ignore rules
├── README.md                         # This file
├── requirements.txt                  # Python dependencies
└── app.py                            # Legacy dashboard file
```

## 🎯 Tasks Completed

### Task 1: Git & Environment Setup
- ✅ Initialized Git repository with conventional commit messages
- ✅ Created `.gitignore` to exclude data files and Python cache
- ✅ Added `requirements.txt` with all necessary dependencies
- ✅ Set up GitHub Actions CI/CD workflow for automated testing
- ✅ Established branching strategy (setup-task, eda-*, compare-countries, dashboard-dev)

### Task 2: Data Profiling, Cleaning & EDA
- ✅ **Data Acquisition**: Downloaded NASA POWER satellite climate data for 5 African countries
- ✅ **Data Cleaning**:
  - Replaced -999 sentinel values with NaN
  - Handled missing values using forward-fill method
  - Retained outliers for climate analysis (not removed as they represent extreme weather events)
- ✅ **Individual Country Analysis**: Created comprehensive EDA notebooks for each country including:
  - Data loading and initial inspection
  - Statistical summaries and distributions
  - Time series analysis of temperature and precipitation
  - Outlier detection using Z-score method
  - Correlation analysis between climate variables
  - Monthly and seasonal patterns
- ✅ **Visualization**: Generated plots for trends, distributions, and correlations

### Task 3: Cross-Country Comparison & Vulnerability Ranking
- ✅ **Data Integration**: Combined cleaned datasets from all countries
- ✅ **Statistical Comparison**: Performed ANOVA tests to identify significant differences
- ✅ **Vulnerability Assessment**: Created composite scoring system based on:
  - Temperature variability (coefficient of variation)
  - Precipitation variability
  - Extreme weather frequency
- ✅ **Country Ranking**: Ranked countries by climate vulnerability for COP32 context
- ✅ **Comparative Visualizations**: Box plots, trend comparisons, and statistical summaries

### Dashboard Development
- ✅ **Interactive Streamlit App**: Built comprehensive dashboard with:
  - **Country Multi-select Widget**: Filter analysis by selected countries
  - **Year Range Slider**: Focus on specific time periods (2015-2026)
  - **Temperature Trend Line Chart**: Monthly average temperature over time
  - **Precipitation Distribution Boxplot**: Compare precipitation patterns across countries
  - **Summary Statistics Tables**: Mean and standard deviation for climate variables
- ✅ **Data Integration**: Reads cleaned CSV files from `data/` directory
- ✅ **User Experience**: Intuitive sidebar controls and responsive layout
- ✅ **Deployment Ready**: Configured for Streamlit Community Cloud deployment

## 🛠️ Technology Stack

- **Python 3.8+**: Core programming language
- **Data Analysis**: pandas, numpy, scipy
- **Visualization**: matplotlib, seaborn
- **Interactive Dashboard**: Streamlit
- **Version Control**: Git with GitHub
- **CI/CD**: GitHub Actions
- **Data Source**: NASA POWER satellite climate data

## 📊 Data Overview

The analysis uses NASA POWER satellite-derived climate data including:
- **T2M**: Average daily temperature (°C)
- **PRECTOTCORR**: Total precipitation (mm/day)
- **Time Period**: 2015-2026 (monthly data)
- **Countries**: Ethiopia, Kenya, Sudan, Tanzania, Nigeria

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git

### Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/firodina/african-climate-ai.git
   cd african-climate-ai
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Analysis

1. **Jupyter Notebooks**: Open and run notebooks in `notebooks/` directory
2. **Dashboard**: Launch the interactive Streamlit app
   ```bash
   streamlit run app/main.py
   ```
   Access at `http://localhost:8501`

### Data Files

Ensure the following cleaned data files exist in `data/` directory:
- `ethiopia_clean.csv`
- `kenya_clean.csv`
- `sudan_clean.csv`
- `tanzania_clean.csv`
- `nigeria_clean.csv`

## 📈 Key Findings

- **Temperature Trends**: Rising temperatures observed across all countries with seasonal patterns
- **Precipitation Variability**: High variability in precipitation, critical for agriculture
- **Vulnerability Ranking**: Countries ranked by climate risk for policy prioritization
- **Extreme Events**: Outliers represent significant climate events requiring attention

## 🔄 CI/CD Pipeline

The repository includes GitHub Actions workflow that:
- Installs dependencies on every push
- Runs basic validation checks
- Ensures code quality standards

## 📝 Development Workflow

- **Branching**: Feature branches for each major task
- **Commits**: Conventional commit messages (feat, docs, chore, ci)
- **Merging**: Fast-forward merges to maintain linear history
- **Documentation**: Comprehensive README and inline code comments

## 🌍 Impact & Applications

This analysis provides:
- **Climate Risk Assessment**: For African countries facing climate change
- **Policy Support**: Data-driven insights for COP32 and climate negotiations
- **Agricultural Planning**: Precipitation and temperature patterns for farming
- **Interactive Tool**: Dashboard for stakeholders to explore climate data

## 🤝 Contributing

This is a challenge submission repository. For improvements or questions, please open an issue or pull request.

## 📄 License

This project is part of the African Climate AI challenge and follows challenge guidelines.
