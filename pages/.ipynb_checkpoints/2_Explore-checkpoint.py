import streamlit as st
from utils.io import load_weather
from charts.charts import chart_dashboard, temp_chart, interactive_chart

st.set_page_config(page_title="Explore", layout="wide")
df = load_weather()

st.title("Interactive Exploratory View")
st.write("Use interaction to validate and extend the story—focus on one weather type, then zoom into a time window.")

st.altair_chart(chart_dashboard(df), use_container_width=True)

st.markdown("**Guided prompts:**")
st.write("- Filter to one weather type (e.g., `sun`, `rain`)—does the temperature distribution shift?")
st.write("- Brush a specific year—do extremes cluster in particular periods?")
st.write("- Compare histogram shape across weather types—what changes most: center, spread, or tails?")

st.header("Simar Charts")

st.altair_chart(temp_chart(df), use_container_width=True)

st.altair_chart(interactive_chart(df), use_container_width=True)
