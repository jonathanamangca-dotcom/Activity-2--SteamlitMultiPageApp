import streamlit as st
import pandas as pd
import numpy as np

# --- SPACE THEME & WHITE TEXT CSS ---
st.markdown("""
    <style>
    /* 1. Main Space Background & Global White Text */
    .stApp {
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
        color: #ffffff !important;
    }

    /* 2. Starry Background Overlay */
    .star-bg {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: -1;
        background: transparent url('https://www.transparenttextures.com/patterns/stardust.png') repeat;
        opacity: 0.5;
    }

    /* 3. Force all text elements to White */
    /* This targets headers, labels, and standard text */
    h1, h2, h3, p, span, label, .stMarkdown {
        color: white !important;
    }

    /* 4. Table Styling: Glassmorphism + White Text */
    .stTable, [data-testid="stTable"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        color: white !important;
    }
    
    /* Ensure table headers and cell text are white */
    th, td {
        color: white !important;
    }

    /* 5. Customizing Selectbox to be readable */
    div[data-baseweb="select"] > div {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
    }
    
    div[data-testid="stWidgetLabel"] p {
        color: white !important;
    }

    /* 6. Title Glow Animation */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    .project-title {
        font-size: 40px;
        font-weight: 800;
        color: #ffffff !important;
        text-shadow: 0px 0px 15px rgba(0, 212, 255, 0.6);
        animation: float 5s ease-in-out infinite;
    }
    </style>
    <div class="star-bg"></div>
    """, unsafe_allow_html=True)

# --- CONTENT ---

# Using the custom class for the floating glow effect
st.markdown('<p class="project-title">🚀 My Projects</p>', unsafe_allow_html=True)

# Dynamic interaction: Filter projects
project_type = st.selectbox("Select Category", ["All", "Machine Learning", "Web Dev", "Data Analysis"])

projects = [
    {"Name": "Neural Vision", "Type": "Machine Learning", "Status": "Complete"},
    {"Name": "EcoTrack App", "Type": "Web Dev", "Status": "In Progress"},
    {"Name": "Market Insights", "Type": "Data Analysis", "Status": "Complete"}
]

df = pd.DataFrame(projects)

if project_type != "All":
    df = df[df["Type"] == project_type]

# The table will now inherit the white text and glass background
st.table(df)

st.write("---")

# Dynamic Chart Example
st.write("### 📈 Project Growth")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
st.line_chart(chart_data)

# Bottom decorative icon
st.markdown("""
    <div style="font-size: 40px; text-align: center; margin-top: 50px; opacity: 0.6;">
        🛰️
    </div>
""", unsafe_allow_html=True)