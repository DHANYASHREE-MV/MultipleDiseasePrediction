import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Privacy Policy", layout="wide")

# Load Lottie animation
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

lottie_privacy = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_tfb3estd.json")

# Layout: Two columns
left_col, right_col = st.columns(2)

# Left column - Text
with left_col:
    st.title("🔒 Privacy Policy")
    st.markdown("""
    Your privacy is important to us. This policy explains how we handle your personal data:
    - We do not share your information with third parties.
    - Data is only used to improve your health predictions.
    - You can contact us to request data deletion at any time.

    We follow industry best practices to ensure your information is secure.
    """)

# Right column - Lottie Animation
with right_col:
    if lottie_privacy:
        st_lottie(lottie_privacy, height=300, key="privacy")
    else:
        st.info("🔒 Learn about our privacy practices below.")

























