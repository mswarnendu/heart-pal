import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from database import *

st.set_page_config(
    page_title="HeartPal | History",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="auto"
)

if not st.session_state.get("username"):
    st.warning("Please log in to view your risk history.")
else:

    st.title("Risk History")

    df = get_user_history(st.session_state.username)

    if df.empty:
        st.info("No assessments recorded yet.")
        st.stop()

    if len(df) == 1:
        st.metric("Current Risk", f"{df['risk_score'].iloc[0]:.1f}%")
        st.caption("Complete next month's assessment to start seeing your trend.")
        st.stop()

    else:

        df["date"] = pd.to_datetime(df["date"])
        df["month"] = df["date"].dt.to_period("M")

        df = df.groupby("month", as_index=False)["risk_score"].mean()
        df["date"] = df["month"].dt.to_timestamp()
        df = df.sort_values("date")
        df = df.drop_duplicates(subset=["date"])

        df["smoothed"] = df["risk_score"].rolling(
            window=2, min_periods=1
        ).mean()

        if len(df) >= 2:
            slope = df["risk_score"].iloc[-1] - df["risk_score"].iloc[-2]
            next_prediction = df["risk_score"].iloc[-1] + slope
        else:
            next_prediction = df["risk_score"].iloc[len(df) - 1]

        next_prediction = max(0, min(100, next_prediction))

        last_date = df["date"].iloc[len(df) - 1]
        next_month = last_date + pd.DateOffset(months=1)

        std = df["risk_score"].std() if len(df) > 1 else 5
        upper_band = df["smoothed"] + std
        lower_band = df["smoothed"] - std

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=df["date"],
            y=upper_band,
            line=dict(width=0),
            showlegend=False
        ))

        fig.add_trace(go.Scatter(
            x=df["date"],
            y=lower_band,
            fill='tonexty',
            fillcolor='rgba(100,100,255,0.15)',
            line=dict(width=0),
            name="Confidence Range"
        ))

        fig.add_trace(go.Scatter(
            x=df["date"],
            y=df["risk_score"],
            mode="lines+markers",
            name="Actual Risk",
            line=dict(width=2, color="#2E86DE"),
            marker=dict(size=7)
        ))

        fig.add_trace(go.Scatter(
            x=df["date"],
            y=df["smoothed"],
            mode="lines",
            name="Trend",
            line=dict(width=4, color="#1B4F72")
        ))

        fig.add_trace(go.Scatter(
            x=[next_month],
            y=[next_prediction],
            mode="markers",
            name="Next Month Prediction",
            marker=dict(size=14, color="red", symbol="diamond")
        ))

        fig.add_hrect(y0=0, y1=30, fillcolor="green",
                      opacity=0.08, line_width=0)
        fig.add_hrect(y0=30, y1=60, fillcolor="orange",
                      opacity=0.08, line_width=0)
        fig.add_hrect(y0=60, y1=100, fillcolor="red",
                      opacity=0.08, line_width=0)

        fig.update_layout(
            title="Heart Risk Trend (Clinical View)",
            xaxis_title="Month",
            yaxis_title="Risk Score (%)",
            hovermode="x unified",
            template="plotly_dark",
            margin=dict(l=20, r=20, t=40, b=20)
        )

        fig.update_xaxes(tickformat="%b %Y", tickangle=45)
        fig.update_yaxes(range=[0, 100])

        st.plotly_chart(fig, use_container_width=True)

        current = df["risk_score"].iloc[-1]

        trend = current - df["risk_score"].iloc[0]

        zone = (
            "Low Risk" if current < 30 else
            "Moderate Risk" if current < 60 else
            "High Risk"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric("Current Risk", f"{current:.1f}%")
        col2.metric("Next Month (Est.)", f"{next_prediction:.1f}%")
        col3.metric("Risk Level", zone)

        if len(df) == 1:
            st.caption("More data needed to build a reliable clinical trend.")
        else:
            if trend < 0:
                st.success("Your risk is improving over time")
            elif trend > 0:
                st.warning("Your risk is increasing over time")
            else:
                st.info("Your risk is stable")
