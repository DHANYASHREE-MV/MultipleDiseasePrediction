import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Terms of Service", layout="wide")

# Load Lottie animation from a reliable source
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Use a reliable Lottie animation (contract/agreement theme)
lottie_url = "https://assets1.lottiefiles.com/packages/lf20_jcikwtux.json"
lottie_animation = load_lottieurl(lottie_url)

# Two-column layout
left_col, right_col = st.columns(2)

# Left: Terms of Service Text
with left_col:
    st.markdown("<h1 style='text-align: left;'>📘 Terms of Service</h1>", unsafe_allow_html=True)
    st.markdown("""
    By using our **Disease Prediction System**, you agree to the following terms:

    - This tool is for **educational and informational purposes** only.
    - We do **not** provide professional medical advice.
    - You are **responsible** for any decisions made based on the predictions.

    > Use this system responsibly and consult a licensed medical professional for clinical guidance.
    """)

# Right: Lottie animation
with right_col:
    if lottie_animation:
        st_lottie(lottie_animation, height=300, key="tos")
    else:
        st.warning("⚠️ Unable to load animation. Please try again later.")





















