import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Econ Dash", page_icon="👌", layout="wide")

# loading the dataset
df = pd.read_csv("test_econ_data.csv")


col1, col2, col3 = st.columns([0.33, 0.06, 0.60])

with col1:
    country = st.selectbox("Country:", sorted(df["Country"].unique()))
    years = sorted(df["Year"].unique())
    year_range = st.slider("Year Range", int(min(years)), int(max(years)), (2000, 2024))

    # filtered df
    filtered_df = df[(df["Country"] == country) &
                 (df["Year"] >= year_range[0]) &
                 (df["Year"] <= year_range[1])]

with col3:
    st.title(f"Economic Status for {country}")
    st.subheader(f"From {year_range[0]} to {year_range[1]}")

st.write("#")
def format_billions(x):
    return f"{x/1e9:.1f}B"

def format_percent(x):
    return f"{x:.1f}%"


bol1, bol_half, bol2, bol3 = st.columns([0.33, 0.06 , 0.33, 0.27])

with bol1:
    # GDP Chart
    fig_gdp = px.line(filtered_df, x="Year", y="GDP", title="GDP (Billions USD)")
    fig_gdp.update_traces(hovertemplate="%{x}: " + filtered_df["GDP"].map(format_billions))
    fig_gdp.update_layout(height=400)
    st.plotly_chart(fig_gdp, use_container_width=True)

    # Inflation Rate Chart
    fig_inflation = px.line(filtered_df, x="Year", y="Inflation Rate", title="Inflation Rate(%)")
    fig_inflation.update_traces(hovertemplate="%{x}: " + filtered_df["Inflation Rate"].map(format_percent))
    fig_inflation.update_layout(height=400)
    st.plotly_chart(fig_inflation, use_container_width=True)

    # Unemployment Rate Chart
    fig_unemployment = px.line(filtered_df, x="Year", y="Unemployment Rate", title="Unemployment Rate (%)")
    fig_unemployment.update_traces(hovertemplate="%{}: " + filtered_df["Unemployment Rate"].map(format_percent))
    fig_unemployment.update_layout(height=400)
    st.plotly_chart(fig_unemployment, use_container_width=True)

with bol2:
    # Interest Rate Chart
    fig_interest = px.line(filtered_df, x="Year", y="Interest Rate", title="Interest Rate (%)")
    fig_interest.update_traces(hovertemplate="%{}: " + filtered_df["Interest Rate"].map(format_percent))
    fig_interest.update_layout(height=400)
    st.plotly_chart(fig_interest, use_container_width=True)

    # Exchange Rate Chart
    fig_exchange = px.line(filtered_df, x="Year", y="Exchange Rate", title="Exchange Rate (Local currency per USD)")
    fig_exchange.update_traces(hovertemplate="%{x}: %{y:.2f}")
    fig_exchange.update_layout(height=400)
    st.plotly_chart(fig_exchange, use_container_width=True)

    # Remittances Chart
    fig_remittances = px.line(filtered_df, x="Year", y="Remittances", title="Remittances (Billions USD)")
    fig_remittances.update_traces(hovertemplate="%{x}: " + filtered_df["Remittances"].map(format_billions))
    fig_remittances.update_layout(height=400)
    st.plotly_chart(fig_remittances, use_container_width=True)

st.write("#")

st.markdown("**Note:** Data shown is simulated for demonstration purposes.")

st.write(filtered_df)
