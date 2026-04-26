import streamlit as st
from cryptography.fernet import Fernet
import base64

# 1. Cyber-Terminal Styling
st.set_page_config(page_title="Emerald Protocol", page_icon="📟")

st.markdown("""
    <style>
    /* Dark terminal background */
    .stApp {
        background-color: #000b00; 
    }
    /* Glowing Green Headers */
    h1, h2, h3 {
        color: #00FF41 !important; 
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 8px #00FF41;
    }
    /* Terminal-style buttons */
    .stButton>button {
        background-color: #003300;
        color: #00FF41;
        border: 1px solid #00FF41;
        border-radius: 2px;
        font-family: 'Courier New', monospace;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #00FF41;
        color: black;
    }
    /* Matrix-style falling code effect */
    @keyframes fall {
        0% { transform: translateY(-100%); }
        100% { transform: translateY(100vh); }
    }
    .matrix-bg {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none;
        z-index: -1;
        opacity: 0.1;
        color: #00FF41;
        font-family: monospace;
        overflow: hidden;
    }
    </style>
    <div class="matrix-bg">
        <div style="position:absolute; left:10%; animation: fall 10s linear infinite;">01011001 11010101</div>
        <div style="position:absolute; left:30%; animation: fall 7s linear infinite;">11100010 00101111</div>
        <div style="position:absolute; left:60%; animation: fall 12s linear infinite;">10101011 11001100</div>
        <div style="position:absolute; left:85%; animation: fall 9s linear infinite;">00011101 10101010</div>
    </div>
    """, unsafe_allow_html=True)

st.title("📟 Cyber Diary")
st.subheader("Secure Messenger v1.0")

# 2. The Engine (Using your personal key: 262427)
def generate_key(secret_word):
    key = base64.urlsafe_b64encode(secret_word.ljust(32)[:32].encode())
    return key

# Your personal secret key
user_key = generate_key("J262427")
cipher = Fernet(user_key)

# 3. Interface Tabs
tab1, tab2 = st.tabs(["🔒 ENCRYPT", "🔓 DECRYPT"])

with tab1:
    st.write("### Input Plaintext for Encryption:")
    msg = st.text_area("Message:", placeholder="Enter secret transmission...")
    if st.button("EXECUTE ENCRYPTION"):
        if msg:
            token = cipher.encrypt(msg.encode()).decode()
            st.success("DATA ENCRYPTED")
            st.code(token)
        else:
            st.warning("ERROR: NO INPUT DETECTED")

with tab2:
    st.write("### Input Ciphertext for Decryption:")
    code = st.text_input("Encrypted Packet:")
    if st.button("AUTHORIZE ACCESS"):
        try:
            original = cipher.decrypt(code.encode()).decode()
            st.toast('Access Granted', icon='✅')
            st.markdown(f"#### 🔓 DECODED MESSAGE:\n> **{original}**")
            st.markdown(f"<p style='color: white; font-size: 20px; font-weight: bold;'>{original}</p>", unsafe_allow_html=True)
        except:
            st.error("FATAL ERROR: INVALID KEY OR CORRUPTED DATA")

st.markdown("---")
st.write("🟢 *System Status: Secure | Port J262427 Online*")
