import streamlit as st, os, time
st.set_page_config(page_title="AI Smart Media Studio", layout="wide")
st.markdown("""
    <style>
    p, div { color: white !important; }
    </style>
    """, unsafe_allow_html=True)
# Google AdSense Script Integration
st.markdown('<script async src="https://googlesyndication.com" crossorigin="anonymous"></script><meta name="google-adsense-account" content="ca-pub-3995974960275140">', unsafe_allow_html=True)

import ui_layout

# Pure Python Local State Engine (Locks Preference for 30 Days - Never Repeats)
cookie_lock_file = ".cookie_lock_state"

if 'cookie_consent' not in st.session_state:
    if os.path.exists(cookie_lock_file):
        with open(cookie_lock_file, "r") as f:
            data = f.read().strip().split(",")
            if len(data) == 2 and (time.time() - float(data[1])) < (30 * 24 * 60 * 60):
                st.session_state.cookie_consent = data[0]
            else: st.session_state.cookie_consent = None
    else: st.session_state.cookie_consent = None

# Custom Compact CSS Style Sheet
st.markdown("""<style>
.cookie-banner { background-color: #1a1f2c; border: 1px solid #00f2fe; padding: 12px; border-radius: 8px; margin-bottom: 15px; text-align: center; width: 100%; display: block; clear: both; }
</style>""", unsafe_allow_html=True)

# 100% Fixed Consent Logic Panel
if st.session_state.cookie_consent is None:
    st.markdown('<div class="cookie-banner"><span style="color:#ffffff; font-size:14px; font-weight:bold; margin-right:15px;">🍪 This website uses cookies to optimize your media workflow and deliver tailored AdSense experiences.</span></div>', unsafe_allow_html=True)
    b1, b2 = st.columns(2)
    with b1:
        if st.button("ACCEPT ALL COOKIES"):
            st.session_state.cookie_consent = "accepted"
            with open(cookie_lock_file, "w") as f: f.write(f"accepted,{time.time()}")
            st.experimental_rerun()
    with b2:
        if st.button("REJECT ALL"):
            st.session_state.cookie_consent = "rejected"
            with open(cookie_lock_file, "w") as f: f.write(f"rejected,{time.time()}")
            st.experimental_rerun()

# Render Studio Content Panel Instantly
ui_layout.render_studio()
