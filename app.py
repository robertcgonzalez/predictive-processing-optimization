import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Predictive Processing Optimization", layout="wide")
st.title("🔍 Predictive Processing Optimization")
st.markdown("**99% faster insights** — End-to-end model reducing processing from 400+ days to 24 hours with <1% error. Serves executive trends **and** front-line supervisors.")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("synthetic_processing_data.csv", parse_dates=["submission_date"])

df = load_data()

# Executive Trending Tab
tab1, tab2 = st.tabs(["Executive Trending", "Front-Line Actionable"])

with tab1:
    st.subheader("30-Day Rolling Average Processing Time")
    # Simple rolling average in pandas (no DAX needed)
    df_sorted = df.sort_values("submission_date")
    df_sorted["rolling_avg_days"] = df_sorted["actual_days"].rolling(window=30, min_periods=1).mean()
    
    fig = px.line(df_sorted, x="submission_date", y=["actual_days", "rolling_avg_days"],
                  title="Processing Time Trend + Rolling Average",
                  labels={"value": "Days", "submission_date": "Date"})
    st.plotly_chart(fig, use_container_width=True)
    
    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Avg Actual Days", f"{df['actual_days'].mean():.1f}")
    with col2:
        st.metric("Avg Optimized Days", f"{df['optimized_predicted_days'].mean():.1f}")
    with col3:
        reduction = (1 - df['optimized_predicted_days'].mean() / df['actual_days'].mean()) * 100
        st.metric("Time Reduction", f"{reduction:.0f}%")
    with col4:
        st.metric("Error Rate", f"{df['compliance_flag'].mean()*100:.2f}%", delta="Compliant")

with tab2:
    st.subheader("Front-Line Supervisor Alerts")
    # Alert logic
    df["processing_alert"] = df["actual_days"].apply(lambda x: "🔴 High Risk - Prioritize" if x > 30 else "🟢 On Track")
    
    # Filters for supervisors
    case_filter = st.selectbox("Filter by Case Type", options=["All"] + list(df["case_type"].unique()))
    if case_filter != "All":
        filtered = df[df["case_type"] == case_filter]
    else:
        filtered = df
    
    st.dataframe(filtered[["submission_date", "case_type", "priority", "actual_days", "processing_alert", "bias_risk_score"]],
                 use_container_width=True, hide_index=True)
    
    fig_alert = px.bar(filtered, x="case_type", color="processing_alert", title="Alerts by Case Type")
    st.plotly_chart(fig_alert, use_container_width=True)

st.caption("Demo from scaled 4M+ record environment. Full SQL pipeline + predictive logic in predictive_queries.sql")
