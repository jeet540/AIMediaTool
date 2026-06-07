import streamlit as st
import core_engines

def render_studio():
    st.markdown("""<style>
    .main { background-color: #0b0e14; color: #ffffff; font-family: 'Segoe UI', Arial, sans-serif; }
    .studio-title { text-align: center; color: #00f2fe; font-size: 32px; font-weight: 800; margin-top: 5px; background: -webkit-linear-gradient(#00f2fe, #4facfe); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .studio-subtitle { text-align: center; color: #718096; font-size: 13px; margin-bottom: 15px; }
    .canvas-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px; margin-bottom: 15px; width: 100%; }
    .tool-card-active { background: #161b26; border: 2px solid #00f2fe; border-radius: 8px; padding: 8px; text-align: center; box-shadow: 0 0 8px rgba(0,242,254,0.2); }
    .tool-card-inactive { background: #121620; border: 1px solid #2d3748; border-radius: 8px; padding: 8px; text-align: center; opacity: 0.7; }
    .card-title { color: #00f2fe; font-size: 13px; font-weight: 600; }
    .card-desc { color: #a0aec0; font-size: 11px; }
    .workspace-box { background: #111622 !important; border: 2px dashed #4facfe !important; border-radius: 12px; padding: 15px; margin-top: 10px; width: 100%; }
    .stButton>button { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white !important; border: none; padding: 8px 20px; font-weight: bold; border-radius: 6px; width: 100%; margin-top: 8px; }
    div[data-testid="stDownloadButton"] button, div[data-testid="stDownloadButton"] button p, .stDownloadButton>button { background-color: #ffffff !important; color: #000000 !important; font-weight: 900 !important; font-size: 14px !important; border: 2px solid #00f2fe !important; border-radius: 6px !important; box-shadow: 0px 4px 12px rgba(255, 255, 255, 0.2) !important; text-transform: uppercase !important; }
    div[data-testid="stDownloadButton"] button:hover { background-color: #00f2fe !important; color: #000000 !important; }
    .legal-box { background: #161b26; border: 1px solid #2d3748; border-radius: 8px; padding: 15px; }
    .comment-box { background: #121620; border-radius: 6px; padding: 10px; margin-top: 6px; border-left: 4px solid #00f2fe; }
    video, audio { max-height: 260px !important; width: 100% !important; border-radius: 8px; object-fit: contain; }
    </style>""", unsafe_allow_html=True)
    
    st.markdown('<div class="studio-title">AI SMART MEDIA STUDIO</div>', unsafe_allow_html=True)
    st.markdown('<div class="studio-subtitle">Professional CapCut-Style Multi-Engine • Limit: 1000MB</div>', unsafe_allow_html=True)
    
    option = st.sidebar.radio("CHOOSE ACTIVE ENGINE:", ["AI VOICE CHANGER", "AUDIO NOISE CLEANER", "VIDEO TO MP3 CONVERTER", "SMART VIDEO CUTTER", "AI VIDEO SPEED CONTROLLER", "AI AUDIO BASS BOOSTER", "VIDEO NOISE CLEANER", "AI VIDEO COMPRESSOR"])
    legal_option = st.sidebar.selectbox("VIEW LEGAL PAGES:", ["NONE - SHOW STUDIO WORKSPACE", "ABOUT US", "PRIVACY POLICY", "COOKIES & TERMS"])
    
    st.markdown('<div class="canvas-container">', unsafe_allow_html=True)
    t_list = [("Voice Changer", "Shift pitch easily.", "AI VOICE CHANGER"), ("Noise Cleaner", "Remove audio hiss.", "AUDIO NOISE CLEANER"), ("Video To MP3", "Extract clear track.", "VIDEO TO MP3 CONVERTER"), ("Video Cutter", "Trim clips fast.", "SMART VIDEO CUTTER"), ("Speed Control", "Slow-mo & Fast.", "AI VIDEO SPEED CONTROLLER"), ("Bass Booster", "Boost frequencies.", "AI AUDIO BASS BOOSTER"), ("Video Denoise", "Clean video noise.", "VIDEO NOISE CLEANER"), ("Video Compress", "Reduce file size.", "AI VIDEO COMPRESSOR")]
    for title, desc, key in t_list:
        c_style = "tool-card-active" if (option == key and legal_option == "NONE - SHOW STUDIO WORKSPACE") else "tool-card-inactive"
        st.markdown(f'<div class="{c_style}"><div class="card-title">{title}</div><div class="card-desc">{desc}</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if legal_option == "ABOUT US": st.markdown('<div class="legal-box"><h4>About Our Studio</h4><p>Welcome to AI Smart Media Studio! We provide web-based tools designed to transform video and audio streams seamlessly.</p></div>', unsafe_allow_html=True)
    elif legal_option == "PRIVACY POLICY": st.markdown('<div class="legal-box"><h4>Privacy Policy</h4><p>Your data safety is our priority. Files are processed inside temp directories and permanently purged after downloads.</p></div>', unsafe_allow_html=True)
    elif legal_option == "COOKIES & TERMS": st.markdown('<div class="legal-box"><h4>Cookies & Terms</h4><p>This application uses cookies required by ad networks like Google AdSense.</p></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="workspace-box">', unsafe_allow_html=True)
        core_engines.run_workspace(option)
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown("<br><h4>💬 Community Review & Feedback</h4>", unsafe_allow_html=True)
    if 'comments' not in st.session_state: st.session_state.comments = ["Awesome CapCut style tool!", "Super fast video cutter, loved it!"]
    c_user = st.text_input("Drop your comment or review here:", placeholder="Type your experience...")
    if st.button("SUBMIT COMMENT") and c_user: st.session_state.comments.append(c_user); st.success("Thank you!"); st.experimental_rerun()
    for c in reversed(st.session_state.comments): st.markdown(f'<div class="comment-box">{c}</div>', unsafe_allow_html=True)
    st.markdown("""<br><hr style="border-color: #2d3748;"><div style="text-align: center; color: #718096; font-size: 11px; letter-spacing: 2px; margin-top: 5px; margin-bottom: 10px;">DEVELOPED ENGINE &bull; <span style="color: #00f2fe; font-weight: bold; text-shadow: 0 0 10px rgba(0,242,254,0.5);">POWERED BY KAINTH</span></div>""", unsafe_allow_html=True)
