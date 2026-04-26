import streamlit as st
from cryptography.fernet import Fernet
import base64

# 1. High-Tech Green Styling
st.set_page_config(page_title="The Emerald Ledger", page_icon="📟")

st.markdown("""
    <style>
    .stApp {
        background-color: #000d00; /* Darkest Green */
    }
    h1, h2, h3 {
        color: #00FF00 !important; /* Classic Matrix Green */
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 10px #00FF00;
    }
    .stButton>button {
        background-color: #006400;
        color: #00FF00;
        border-radius: 5px;
        border: 1px solid #00FF00;
    }
    /* Matrix-style falling data effect */
    @keyframes matrix {
        0% { transform: translateY(-100%); }
        100% { transform: translateY(1000%); }
    }
    .matrix-char {
        position: fixed;
        color: #00FF00;
        font-family: 'Courier New', monospace;
        font-size: 20px;
        opacity: 0.3;
        animation: matrix 10s linear infinite;
        z-index: 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Adding the subtle background data effect
st.markdown('<div class="matrix-char" style="left:10%; animation-delay:1s;">01</div>', unsafe_allow_html=True)
st.markdown('<div class="matrix-char" style="left:40%; animation-delay:4s;">10</div>', unsafe_allow_html=True)
st.markdown('<div class="matrix-char" style="left:70%; animation-delay:2s;">11</div>', unsafe_allow_html=True)

st.title("📟 The Cyber Diary 📟")
st.subheader("Secure Communication Terminal")

# 2. Encryption Engine (Using your key: 262427)
def generate_key(secret_word):
    key = base64.urlsafe_b64encode(secret_word.ljust(32)[:32].encode())
    return key

user_key = generate_key("J262427")
cipher = Fernet(user_key)

# 3. Terminal Interface
tab1, tab2 = st.tabs(["🔒 ENCRYPT DATA", "🔓 DECRYPT DATA"])

with tab1:
    st.write("Input sensitive data for transmission:")
    input_text = st.text_area("Message:", placeholder="System update required...")
    if st.button("Generate Ciphertext"):
        if input_text:
            encrypted_text = cipher.encrypt(input_text.encode()).decode()
            st.success("Encryption Successful.")
            st.code(encrypted_text)
        else:
            st.warning("No data detected.")

with tab2:
    st.write("Input encrypted packet:")
    incoming_data = st.text_input("Ciphertext:")
    if st.button("Authorize Decryption"):
        try:
            decrypted_text = cipher.decrypt(incoming_data.encode()).decode()
            st.toast('Access Granted', icon='✅')
            st.markdown(f"### 🔓 Decrypted Output:\n**{decrypted_text}**")
        except:
            st.error("Access Denied: Key Mismatch or Corrupted Data.")

st.markdown("---")
st.write("🛡️ *Protocol J262427 Active*")
