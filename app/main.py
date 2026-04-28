import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set page config
st.set_page_config(page_title="African Climate Dashboard", layout="wide")

# Title
st.title("🌍 African Climate Dashboard")

# Load data function
@st.cache_data
def load_climate_data():
    countries = ['ethiopia', 'kenya', 'sudan', 'tanzania', 'nigeria']
    dfs = []

    for country in countries:
        file_path = f'data/{country}_clean.csv'
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df['Country'] = country.capitalize()
            dfs.append(df)
        else:
            st.warning(f"Data file for {country} not found. Please ensure data/{country}_clean.csv exists.")

    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)
        combined_df['Date'] = pd.to_datetime(combined_df['Date'])
        combined_df['Year'] = combined_df['Date'].dt.year
        combined_df['Month'] = combined_df['Date'].dt.month
        return combined_df
    else:
        return pd.DataFrame()

# Load data
df = load_climate_data()

if df.empty:
    st.error("No data available. Please check that cleaned CSV files exist in the data/ directory.")
    st.stop()

# Sidebar controls
st.sidebar.header("Dashboard Controls")

# Country multi-select
countries = df['Country'].unique().tolist()
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    countries,
    default=countries[:2]  # Default to first 2 countries
)

# Year range slider
min_year = int(df['Year'].min())
max_year = int(df['Year'].max())
year_range = st.sidebar.slider(
    "Select Year Range",
    min_year,
    max_year,
    (min_year, max_year)
)

# Filter data
filtered_df = df[
    (df['Country'].isin(selected_countries)) &
    (df['Year'].between(year_range[0], year_range[1]))
]

# Main content
col1, col2 = st.columns(2)

# Temperature trend line chart
with col1:
    st.subheader("Temperature Trend (T2M)")

    if not filtered_df.empty:
        monthly_temp = filtered_df.groupby(['Country', 'Month'])['T2M'].mean().reset_index()

        fig, ax = plt.subplots(figsize=(10, 6))
        for country in selected_countries:
            country_data = monthly_temp[monthly_temp['Country'] == country]
            if not country_data.empty:
                ax.plot(country_data['Month'], country_data['T2M'],
                       marker='o', label=country, linewidth=2)

        ax.set_title(f'Monthly Average Temperature ({year_range[0]}-{year_range[1]})')
        ax.set_xlabel('Month')
        ax.set_ylabel('Temperature (°C)')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_xticks(range(1, 13))

        st.pyplot(fig)
    else:
        st.info("No data available for selected filters.")

# Precipitation distribution boxplot
with col2:
    st.subheader("Precipitation Distribution")

    if not filtered_df.empty:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=filtered_df, x='Country', y='PRECTOTCORR', ax=ax, showfliers=False)
        ax.set_title(f'Precipitation Distribution ({year_range[0]}-{year_range[1]})')
        ax.set_xlabel('Country')
        ax.set_ylabel('Precipitation (mm/day)')
        ax.tick_params(axis='x', rotation=45)

        st.pyplot(fig)
    else:
        st.info("No data available for selected filters.")

# Summary statistics
st.subheader("Summary Statistics")
if not filtered_df.empty:
    temp_stats = filtered_df.groupby('Country')['T2M'].agg(['mean', 'std']).round(2)
    precip_stats = filtered_df.groupby('Country')['PRECTOTCORR'].agg(['mean', 'std']).round(2)

    col3, col4 = st.columns(2)
    with col3:
        st.write("**Temperature Statistics (°C)**")
        st.dataframe(temp_stats)
    with col4:
        st.write("**Precipitation Statistics (mm/day)**")
        st.dataframe(precip_stats)
else:
    st.info("No data available for selected filters.")