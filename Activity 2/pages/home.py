import streamlit as st

# --- SPACE THEME CSS & ANIMATION ---
st.markdown("""
    <style>
    /* Main background container */
    .stApp {
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
        color: #ffffff;
    }

    /* Floating Planet Animation */
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(5deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }

    /* Starry background effect */
    .star-bg {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: -1;
        background: transparent url('https://www.transparenttextures.com/patterns/stardust.png') repeat;
        opacity: 0.5;
    }

    /* Aesthetic Button Styling */
    .stButton>button {
        border: 1px solid #4f5b66;
        background: rgba(255, 255, 255, 0.05);
        color: #00d4ff;
        transition: 0.3s;
        backdrop-filter: blur(5px);
    }
    .stButton>button:hover {
        border-color: #00d4ff;
        background: rgba(0, 212, 255, 0.1);
        box-shadow: 0px 0px 15px rgba(0, 212, 255, 0.4);
        color: white;
    }
    </style>
    <div class="star-bg"></div>
    """, unsafe_allow_html=True)

# --- MOVING OBJECTS (Floating Planet Icon) ---
col_space, col_title = st.columns([1, 4])
with col_space:
    # A floating "Saturn" emoji representing a moving object
    st.markdown("""
        <div style="font-size: 80px; animation: float 6s ease-in-out infinite; text-align: center;">
            🪐
        </div>
    """, unsafe_allow_html=True)

with col_title:
    st.title("🚀 Welcome to My Digital Space")
    st.subheader("Building the future through code and data.")

# --- HERO SECTION ---
col1, col2 = st.columns([2, 1])

with col1:
    st.write("""
    I am a developer focused on creating **clean, efficient, and user-centric** applications. 
    This platform serves as a hub for my latest experiments and professional journey.
    """)
    if st.button("✨ Explore My Work"):
        st.balloons()
        st.switch_page("pages/projects.py")



st.write("---")

# --- QUICK NAVIGATION ---
st.write("### 🧭 Quick Navigation")
nav_col1, nav_col2, nav_col3 = st.columns(3)

with nav_col1:
    if st.button("👤 About Me", use_container_width=True):
        st.switch_page("pages/about.py")

with nav_col2:
    if st.button("💻 Projects", use_container_width=True):
        st.switch_page("pages/projects.py")

with nav_col3:
    if st.button("📧 Contact", use_container_width=True):
        st.switch_page("pages/contact.py")

# Floating "Moon" at the bottom
st.markdown("""
    <div style="font-size: 40px; animation: float 8s ease-in-out infinite; text-align: right; opacity: 0.6;">
        ☄️
    </div>
""", unsafe_allow_html=True)