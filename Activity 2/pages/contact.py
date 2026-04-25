import streamlit as st

# --- SPACE THEME & FORM CSS ---
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

    /* 4. Glassmorphism Contact Form */
    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        border: 1px solid rgba(0, 212, 255, 0.2);
        padding: 30px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
    }

    /* 5. Input Field Styling */
    input, textarea {
        background-color: rgba(255, 255, 255, 0.07) !important;
        color: white !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
    }

    /* 6. Form Button Styling (Cyan Neon) */
    button[kind="primaryFormSubmit"] {
        background: linear-gradient(135deg, #00B4DB, #0083B0) !important;
        border: 2px solid rgba(255, 255, 255, 0.8) !important;
        color: white !important;
        font-weight: 700 !important;
        width: 100% !important;
        transition: 0.3s !important;
        box-shadow: 0 4px 15px rgba(0, 180, 219, 0.4) !important;
    }

    button[kind="primaryFormSubmit"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(0, 210, 255, 0.6) !important;
        border-color: white !important;
    }

    /* 7. Title Animation */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    .contact-title {
        font-size: 45px;
        font-weight: 800;
        color: #ffffff !important;
        text-shadow: 0px 0px 15px rgba(0, 212, 255, 0.6);
        animation: float 5s ease-in-out infinite;
    }
    </style>
    <div class="star-bg"></div>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="contact-title">📧 Get In Touch</p>', unsafe_allow_html=True)
st.write("Have a question or want to collaborate? Send a transmission through the void.")

st.divider()

# --- CONTACT FORM ---
with st.form("contact_form"):
    st.write("### 🛸 Transmission Details")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    message = st.text_area("Your Message", placeholder="Type your message here...")
    
    submit_button = st.form_submit_button("Send Transmission")

if submit_button:
    if name and email and message:
        st.balloons()
        st.success(f"Transmission successful! Thank you, {name}. I will respond shortly.")
    else:
        st.error("Error: All fields must be populated before sending.")

# --- FOOTER DECORATION ---
st.markdown("""
    <div style="font-size: 40px; text-align: right; margin-top: 30px; opacity: 0.5;">
        📡
    </div>
""", unsafe_allow_html=True)# --- SOCIAL LINKS SECTION ---
st.write("---")
st.write("### 🌌 Connect with me in the Multiverse")

# Adding Font Awesome for icons
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">', unsafe_allow_html=True)

# Custom CSS for Social Icons
st.markdown("""
    <style>
    .social-container {
        display: flex;
        justify-content: center;
        gap: 30px;
        padding: 20px;
    }
    .social-icon {
        font-size: 40px;
        color: white;
        transition: 0.3s;
        text-decoration: none;
    }
    .social-icon:hover {
        color: #00d4ff;
        transform: scale(1.2);
        text-shadow: 0px 0px 20px rgba(0, 212, 255, 0.8);
    }
    .facebook:hover { color: #1877F2; }
    .instagram:hover { color: #E4405F; }
    .gmail:hover { color: #DB4437; }
    </style>
    
    <div class="social-container">
        <a href="https://www.facebook.com/igoopps" target="_blank" class="social-icon facebook">
            <i class="fab fa-facebook"></i>
        </a>
        <a href="https://instagram.com/tannnnnnnyy" target="_blank" class="social-icon instagram">
            <i class="fab fa-instagram"></i>
        </a>
        <a href="mailto:jonathanamangca@gmail.com" target="_blank" class="social-icon gmail">
            <i class="fas fa-envelope"></i>
        </a>
    </div>
""", unsafe_allow_html=True)

# Floating Satellite Icon
st.markdown("""
    <div style="font-size: 40px; text-align: right; margin-top: 10px; opacity: 0.5; animation: float 6s ease-in-out infinite;">
        📡
    </div>
""", unsafe_allow_html=True)