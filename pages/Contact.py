import streamlit as st
import requests
from streamlit_lottie import st_lottie
import smtplib
from email.message import EmailMessage

# ----- Page Configuration -----
st.set_page_config(page_title="Contact Us", layout="wide")

# ----- Load Lottie Animation -----
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

lottie_contact = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_kdx6cani.json")

# ----- Page Header -----
st.title("📞 Contact Us")
st.write("Reach out to us using the form below or using the contact info on the right.")

# ----- Layout: Left (form) | Right (info + animation) -----
col1, col2 = st.columns(2)

with col1:
    with st.form("contact_form"):
        policy_number = st.text_input("Policy Number")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not policy_number or not name or not email or not message:
                st.warning("⚠️ Please fill in all the fields.")
            else:
                try:
                    # Email setup
                    sender = st.secrets["email"]["sender"]
                    password = st.secrets["email"]["password"]
                    receiver = st.secrets["email"]["receiver"]
                    smtp_server = st.secrets["email"]["smtp_server"]
                    smtp_port = st.secrets["email"]["smtp_port"]

                    msg = EmailMessage()
                    msg["Subject"] = f"New Contact Form Submission from {name}"
                    msg["From"] = sender
                    msg["To"] = receiver
                    msg.set_content(
                        f"Policy Number: {policy_number}\nName: {name}\nEmail: {email}\n\nMessage:\n{message}"
                    )

                    with smtplib.SMTP(smtp_server, smtp_port) as server:
                        server.starttls()
                        server.login(sender, password)
                        server.send_message(msg)

                    st.success("✅ Your message has been sent successfully!")
                except Exception as e:
                    st.error(f"❌ Failed to send message: {e}")

with col2:
    if lottie_contact:
        st_lottie(lottie_contact, height=250, key="contact_anim")

    st.markdown("---")
    st.markdown("### 📇 Contact Info")
    st.markdown("📞 **Phone:** +91-9876543210")
    st.markdown("✉️ **Email:** support@example.com")
    st.markdown("🏠 **Address:** 123, HealthCare Lane, Bengaluru, India")






















































