import streamlit as st

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
    h1, h2, h3, p, span, label, .stMarkdown {
        color: white !important;
    }

    /* 4. Certificate Card Styling */
    .cert-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        border: 1px solid rgba(0, 212, 255, 0.2);
        padding: 20px;
        text-align: center;
        transition: 0.3s;
    }
    .cert-card:hover {
        border-color: #00d4ff;
        box-shadow: 0px 0px 15px rgba(0, 212, 255, 0.3);
        transform: translateY(-5px);
    }

    /* 5. Title Glow Animation */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    .cert-title {
        font-size: 40px;
        font-weight: 800;
        color: #ffffff !important;
        text-shadow: 0px 0px 15px rgba(0, 212, 255, 0.6);
        animation: float 5s ease-in-out infinite;
    }
    </style>
    <div class="star-bg"></div>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="cert-title">📜 My Certificates</p>', unsafe_allow_html=True)
st.write("A verified collection of my academic achievements.")

st.divider()

# --- CERTIFICATE GALLERY ---
st.write("### 🏆 Achievement Gallery")

# You can manually add your certificates here by replacing the image paths
# Example: st.image("assets/python_cert.jpg")
col1, col2 = st.columns(2, gap="large")

with col1:
    
    st.image("cer1.png", caption="Full-Stack Web Development", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    
    st.image("cer2.png", caption="Introduction to Golang", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


st.markdown("""
    <div style="font-size: 40px; text-align: center; margin-top: 50px; opacity: 0.4;">
        🎖️
    </div>
""", unsafe_allow_html=True)