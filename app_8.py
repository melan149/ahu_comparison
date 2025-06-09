
import streamlit as st
import pandas as pd

# Load data from a file or GitHub URL
@st.cache_data
def load_data():
    # Replace with the raw GitHub link if hosted on GitHub
    # Example: url = "https://raw.githubusercontent.com/user/repo/branch/Data_2025.xlsx"
    url = "Data_2025.xlsx"
    df = pd.read_excel(url, sheet_name="data")
    return df

df = load_data()

# Sidebar Filters
st.sidebar.title("Filter Options")
unit_names = df["Unit name"].dropna().unique()
regions = df["Region"].dropna().unique()
years = df["Year"].dropna().unique()
quarters = df["Quarter"].dropna().unique()
recovery_types = df["Recovery type"].dropna().unique()
unit_sizes = df["Unit size"].dropna().unique()

selected_unit = st.sidebar.selectbox("Unit name", sorted(unit_names))
selected_region = st.sidebar.selectbox("Region", sorted(regions))
selected_year = st.sidebar.selectbox("Year", sorted(years))
selected_quarter = st.sidebar.selectbox("Quarter", sorted(quarters))
selected_recovery = st.sidebar.selectbox("Recovery type", sorted(recovery_types))
selected_size = st.sidebar.selectbox("Unit size", sorted(unit_sizes))

# Filter Data
filtered_df = df[
    (df["Unit name"] == selected_unit) &
    (df["Region"] == selected_region) &
    (df["Year"] == selected_year) &
    (df["Quarter"] == selected_quarter) &
    (df["Recovery type"] == selected_recovery) &
    (df["Unit size"] == selected_size)
]

# Display Comparison
st.title("Technical Data Comparison")
brands = filtered_df["Brand name"].dropna().unique()

if len(brands) >= 2:
    brand1, brand2 = brands[:2]
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"{brand1}")
        st.dataframe(filtered_df[filtered_df["Brand name"] == brand1].reset_index(drop=True))

    with col2:
        st.subheader(f"{brand2}")
        st.dataframe(filtered_df[filtered_df["Brand name"] == brand2].reset_index(drop=True))

elif len(brands) == 1:
    st.subheader(f"{brands[0]}")
    st.dataframe(filtered_df.reset_index(drop=True))
else:
    st.warning("No matching data found. Adjust filter criteria.")
