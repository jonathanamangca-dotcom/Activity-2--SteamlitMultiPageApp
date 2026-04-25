import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Visionary Portfolio", page_icon="🚀", layout="wide")

# --- CUSTOM CSS FOR UI/UX ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        font-family: 'Inter', sans-serif;
        background-color: #0E1117; 
        color: #FFFFFF;
    }

    [data-testid="stSidebar"] {
        background-color: #161B22 !important;
        border-right: 1px solid #30363D;
    }

    /* High Visibility Buttons Styling */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        background: linear-gradient(135deg, #00B4DB, #0083B0); 
        color: white !important;
        border: 2px solid rgba(255, 255, 255, 0.8) !important;
        box-shadow: 0 4px 15px rgba(0, 180, 219, 0.4);
        padding: 10px 20px;
    }

    .stButton>button:hover {
        transform: translateY(-3px);
        background: linear-gradient(135deg, #00d2ff, #3a7bd5);
        box-shadow: 0 8px 25px rgba(0, 210, 255, 0.6);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🚀 My Portfolio ")
    st.caption("Developed by Jonathan M. Amangca")
    st.divider()

# --- NAVIGATION SETUP ---
pages = {
    "General": [
        st.Page("pages/home.py", title="Home", icon="🏠"),
        st.Page("pages/about.py", title="About Me", icon="👤"),
    ],
    "Showcase": [
        st.Page("pages/projects.py", title="Projects", icon="💻"),
        st.Page("pages/certificates.py", title="Certificates", icon="📜"), # Added this line
        st.Page("pages/contact.py", title="Contact", icon="📧"),
    ],
}

pg = st.navigation(pages)
pg.run()