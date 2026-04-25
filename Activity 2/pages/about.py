import streamlit as st
import base64

# Function to convert image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Convert your 'profile1.jpg'
try:
    img_base64 = get_base64_image("profile1.jpg")
    img_html = f'data:image/jpg;base64,{img_base64}'
except FileNotFoundError:
    img_html = "https://via.placeholder.com/250"

# --- SPACE THEME & PROFILE CSS ---
st.markdown("""
    <style>
    /* 1. APPLYING THE SPACE THEME FROM PAGE 1 */
    .stApp {
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
        color: #ffffff;
    }

    .star-bg {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: -1;
        background: transparent url('https://www.transparenttextures.com/patterns/stardust.png') repeat;
        opacity: 0.5;
    }

    /* 2. Floating Animation */
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(1deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }

    /* 3. Profile Image Styling */
    .profile-wrapper {
        display: flex;
        justify-content: center; /* Fixed typo from 'c' */
        align-items: center;
        padding: 20px;
    }

    .profile-pic {
        width: 250px;
        height: 250px;
        border-radius: 100%;
        object-fit: cover;
        border: 3px solid rgba(0, 212, 255, 0.5);
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.4), 
                    0 0 40px rgba(0, 212, 255, 0.2);
        animation: float 6s ease-in-out infinite; /* Added float to profile pic */
    }

    /* 4. Progress Bars Cyan Theme */
    div[data-baseweb="progress-bar"] > div > div {
        background-color: #00d4ff !important;
    }

    /* 5. Text Styling */
    .title-text {
        font-size: 45px;
        font-weight: 800;
        color: #FFFFFF;
        text-shadow: 0px 0px 10px rgba(0, 212, 255, 0.5);
    }
    
    .subtitle-text {
        color: #00d4ff;
        font-size: 22px;
        font-weight: 600;
        letter-spacing: 1px;
    }
    </style>
    <div class="star-bg"></div>
    """, unsafe_allow_html=True)

# --- CONTENT SECTION ---

st.markdown('<p class="title-text">👤 About Me</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.5], gap="large")

with col1:
    st.markdown(f"""
        <div class="profile-wrapper">
            <img src="{img_html}" class="profile-pic">
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<p class="subtitle-text">My Journey</p>', unsafe_allow_html=True)
    st.write("""
    I am **Jonathan M. Amangca**, a BSCS student aspiring to be a **Full-Stack Developer**. 
    My work revolves around transforming complex data into intuitive, actionable insights. 
    I believe that technology should be accessible, beautiful, and purposeful.
    
    When I'm not coding, I enjoy the tranquility of my backyard, spending time with my aquatic pets.
    """)

st.write("---")

# --- TECHNICAL TOOLBOX ---
st.write("### 🛠️ Technical Toolbox")

t_col1, t_col2 = st.columns(2, gap="medium")

with t_col1:
    st.write("Python & Data Science")
    st.progress(90)
    
    st.write("SQL & Databases")
    st.progress(70)

with t_col2:
    st.write("Streamlit & Web Apps")
    st.progress(85)
    
    st.write("UI/UX Design")
    st.progress(65)

# --- FOOTER INFO ---
st.write("")
st.info("💡 **Fun Fact:** This entire website was built using only Python!")

# Floating "Comet" at the bottom for consistency with Page 1
st.markdown("""
    <div style="font-size: 40px; animation: float 8s ease-in-out infinite; text-align: right; opacity: 0.4;">
        ☄️
    </div>
""", unsafe_allow_html=True)