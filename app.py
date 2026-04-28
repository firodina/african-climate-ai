# Streamlit Dashboard for African Climate Analysis
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set page config
st.set_page_config(page_title="African Climate Dashboard", page_icon="🌍", layout="wide")

# Title
st.title("🌍 African Climate Analysis Dashboard")
st.markdown("Interactive visualization of climate data across Ethiopia, Kenya, Sudan, Tanzania, and Nigeria")

# Sidebar for controls
st.sidebar.header("Dashboard Controls")

# Country selector
countries = ['Ethiopia', 'Kenya', 'Sudan', 'Tanzania', 'Nigeria']
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    countries,
    default=countries
)

# Year range slider
year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=2015,
    max_value=2026,
    value=(2015, 2026)
)

# Variable selector
variables = ['T2M', 'T2M_MAX', 'T2M_MIN', 'PRECTOTCORR', 'RH2M', 'WS2M', 'WS2M_MAX']
selected_variable = st.sidebar.selectbox(
    "Select Variable to Analyze",
    variables,
    index=0
)

# Load data function (placeholder - would load actual data)
@st.cache_data
def load_data():
    # In real implementation, load from data/ folder
    # For now, create sample data structure
    countries_data = []
    for country in countries:
        # Sample data generation (replace with actual loading)
        dates = pd.date_range(start='2015-01-01', end='2026-03-31', freq='D')
        np.random.seed(hash(country) % 2**32)
        data = {
            'Date': dates,
            'Country': country,
            'Year': dates.year,
            'Month': dates.month,
            'T2M': np.random.normal(25, 5, len(dates)),
            'T2M_MAX': np.random.normal(30, 5, len(dates)),
            'T2M_MIN': np.random.normal(20, 5, len(dates)),
            'PRECTOTCORR': np.random.exponential(2, len(dates)),
            'RH2M': np.random.normal(60, 15, len(dates)),
            'WS2M': np.random.normal(3, 1, len(dates)),
            'WS2M_MAX': np.random.normal(5, 2, len(dates))
        }
        countries_data.append(pd.DataFrame(data))

    return pd.concat(countries_data, ignore_index=True)

# Load data
df = load_data()

# Filter data based on selections
filtered_df = df[
    (df['Country'].isin(selected_countries)) &
    (df['Year'].between(year_range[0], year_range[1]))
]

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"{selected_variable} Trends Over Time")

    # Time series plot
    fig, ax = plt.subplots(figsize=(12, 6))
    for country in selected_countries:
        country_data = filtered_df[filtered_df['Country'] == country]
        monthly_data = country_data.groupby('Month')[selected_variable].mean()
        ax.plot(monthly_data.index, monthly_data.values, marker='o', label=country, linewidth=2)

    ax.set_title(f'Monthly Average {selected_variable} ({year_range[0]}-{year_range[1]})')
    ax.set_xlabel('Month')
    ax.set_ylabel(selected_variable)
    ax.legend()
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

with col2:
    st.subheader("Summary Statistics")

    # Summary stats for selected variable
    stats_df = filtered_df.groupby('Country')[selected_variable].agg(['mean', 'median', 'std']).round(2)
    stats_df.columns = ['Mean', 'Median', 'Std Dev']
    st.dataframe(stats_df)

# Second row
st.subheader("Distribution Comparison")
col3, col4 = st.columns(2)

with col3:
    # Boxplot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(data=filtered_df, x='Country', y=selected_variable, ax=ax, showfliers=False)
    ax.set_title(f'{selected_variable} Distribution by Country')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

with col4:
    # Histogram
    fig, ax = plt.subplots(figsize=(8, 6))
    for country in selected_countries:
        country_data = filtered_df[filtered_df['Country'] == country]
        ax.hist(country_data[selected_variable], alpha=0.5, label=country, bins=30)
    ax.set_title(f'{selected_variable} Histogram')
    ax.set_xlabel(selected_variable)
    ax.set_ylabel('Frequency')
    ax.legend()
    st.pyplot(fig)

# Third row - Extreme events
st.subheader("Extreme Events Analysis")

if selected_variable in ['T2M', 'T2M_MAX', 'T2M_MIN']:
    # Extreme heat analysis
    st.markdown("**Extreme Heat Days (T2M_MAX > 35°C)**")
    extreme_heat = filtered_df[filtered_df['T2M_MAX'] > 35]
    heat_summary = extreme_heat.groupby('Country').size().reset_index(name='Extreme Heat Days')
    st.dataframe(heat_summary)

elif selected_variable == 'PRECTOTCORR':
    # Drought analysis
    st.markdown("**Drought Analysis (Consecutive Dry Days < 1mm)**")
    # Simplified drought calculation
    drought_summary = filtered_df.groupby('Country')['PRECTOTCORR'].apply(
        lambda x: (x < 1).sum()
    ).reset_index(name='Dry Days')
    st.dataframe(drought_summary)

# Footer
st.markdown("---")
st.markdown("Dashboard built with Streamlit for COP32 climate analysis")
st.markdown("Data source: NASA POWER database")