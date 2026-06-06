import streamlit as st, moviepy.editor as mp, numpy as np, soundfile as sf, os, time
from scipy.io import wavfiledef save_file(uf, tp):
    try:
        with open(tp, "wb") as f:
            while True:
                chunk = uf.read(16 * 1024 * 1024)
                if not chunk: break
                f.write(chunk)
        return True
    except Exception: return False

def to_wav(in_p, out_p):
    try:
        ac = mp.AudioFileClip(in_p)
        ac.write_audiofile(out_p, fps=44100, nbytes=2, codec='pcm_s16le', logger=None)
        ac.close()
        return True
    except Exception: return False

def run_workspace(option):
    st.markdown('<div class="workspace-box">', unsafe_allow_html=True)
    t_id = int(time.time())
    
    if option == "AI VOICE CHANGER":
        st.markdown("### AI Voice Changer Workspace")
        uf = st.file_uploader("Upload Audio/Video", type=None, key="v1")
        if uf:
            st.success("✅ Uploaded!"); st.audio(uf)
            r, w, o = f"r_{t_id}.tmp", f"w_{t_id}.wav", f"o_{t_id}.wav"
            if save_file(uf, r) and st.button("EXECUTE TRANSFORMATION"):
                eff = st.radio("Select Effect:", ["High Pitch (Female Style)", "Low Pitch (Robot Style)"])
                if to_wav(r, w):
                    try:
                        d, sr = sf.read(w); nsr = int(sr * 0.7) if eff == "High Pitch (Female Style)" else int(sr * 1.4)
                        sf.write(o, d, nsr); st.success("✅ Complete!"); st.audio(o)
                        with open(o, "rb") as f: st.download_button("📥 DOWNLOAD VOICE", f, file_name="voice.wav")
                    except Exception as e: st.error(f"Error: {e}")
            for f in [r, w, o]: 
                if os.path.exists(f): os.remove(f)

    elif option == "AUDIO NOISE CLEANER":
        st.markdown("### AI Background Noise Cleaner & Enhancer")
        uf = st.file_uploader("Upload Audio/Video to Clean Noise", type=None, key="n1")
        if uf:
            st.success("✅ Uploaded!"); st.audio(uf)
            r, w, o = f"r_{t_id}.tmp", f"w_{t_id}.wav", f"o_{t_id}.wav"
            nst = st.slider("Noise Reduction Strength (%):", 20, 100, 70, 5)
            ven = st.slider("Voice Clarity (Boost dB):", 1.0, 3.0, 1.5, 0.5)
            if save_file(uf, r) and st.button("CLEAN BACKGROUND NOISE NOW"):
                if to_wav(r, w):
                    try:
                        rate, d = wavfile.read(w)
                        if len(d.shape) > 1: d = d.mean(axis=1)
                        lim = np.median(np.abs(d)) * (nst / 100.0)
                        c_d = np.clip(np.where(np.abs(d) < lim, d * (1.0 - (nst / 100.0)), d) * ven, -32768, 32767)
                        wavfile.write(o, rate, c_d.astype(np.int16)); st.success("✅ Studio Clean Successful!"); st.audio(o)
                        with open(o, "rb") as f: st.download_button("📥 DOWNLOAD CLEAN AUDIO", f, file_name="clean.wav")
                    except Exception as e: st.error(f"Error: {e}")
            for f in [r, w, o]: 
                if os.path.exists(f): os.remove(f)

    elif option == "VIDEO TO MP3 CONVERTER":
        st.markdown("### Video to MP3 Extraction Workspace")
        uf = st.file_uploader("Upload Video File", type=None, key="vm1")
        if uf:
            st.success("✅ Linked!"); st.video(uf)
            r, o = f"r_{t_id}.tmp", f"o_{t_id}.mp3"
            if save_file(uf, r) and st.button("EXTRACT AUDIO TRACK NOW"):
                try:
                    vid = mp.VideoFileClip(r)
                    if vid.audio:
                        vid.audio.write_audiofile(o, codec='mp3', logger=None); st.success("✅ Extracted!"); st.audio(o)
                        with open(o, "rb") as f: st.download_button("📥 DOWNLOAD MP3", f, file_name="audio.mp3")
                    else: st.error("No audio found!")
                    vid.close()
                except Exception as e: st.error(f"Error: {e}")
                finally: 
                    if os.path.exists(r): os.remove(r)
                    if os.path.exists(o): os.remove(o)

    elif option == "SMART VIDEO CUTTER":
        st.markdown("### Professional Video Trimmer Workspace")
        uf = st.file_uploader("Upload Video (.mp4)", type=None, key="vc1")
        if uf:
            st.success("✅ Linked!"); st.video(uf)
            r, o = f"r_{t_id}.tmp", f"o_{t_id}.mp4"
            if save_file(uf, r):
                try:
                    vid = mp.VideoFileClip(r); st.info(f"Duration: {vid.duration:.2f}s")
                    start = st.number_input("Start (s)", min_value=0.0, max_value=float(vid.duration), value=0.0)
                    end = st.number_input("End (s)", min_value=0.0, max_value=float(vid.duration), value=float(vid.duration))
                    if st.button("TRIM MEDIA TIMELINE"):
                        if start >= end: st.error("Start must be less than End!")
                        else:
                            with st.spinner("Trimming..."):
                                trm = vid.subclip(start, end); trm.write_videofile(o, codec="libx264", audio_codec="aac", preset="ultrafast", logger=None)
                                st.success("✅ Trimmed!"); st.video(o)
                                with open(o, "rb") as f: st.download_button("📥 DOWNLOAD VIDEO", f, file_name="trimmed.mp4")
                    vid.close()
                except Exception as e: st.error(f"Error: {e}")
                finally:
                    if os.path.exists(r): os.remove(r)
                    if os.path.exists(o): os.remove(o)

    elif option == "AI VIDEO SPEED CONTROLLER":
        st.markdown("### AI Video Speed Ramp Workspace")
        uf = st.file_uploader("Upload Video for Speed Effect", type=None, key="vs1")
        if uf:
            st.success("✅ Linked!"); st.video(uf)
            r, o = f"r_{t_id}.tmp", f"o_{t_id}.mp4"
            spd = st.slider("Select Speed Multiplier:", 0.5, 2.0, 1.0, 0.25)
            if save_file(uf, r) and st.button("APPLY SPEED EFFECT"):
                try:
                    vid = mp.VideoFileClip(r); m_vid = vid.fx(mp.vfx.speedx, spd)
                    m_vid.write_videofile(o, codec="libx264", audio_codec="aac", preset="ultrafast", logger=None)
                    st.success("✅ Speed Changed!"); st.video(o)
                    with open(o, "rb") as f: st.download_button("📥 DOWNLOAD SPEED VIDEO", f, file_name="speed.mp4")
                    vid.close()
                except Exception as e: st.error(f"Error: {e}")
                finally:
                    if os.path.exists(r): os.remove(r)
                    if os.path.exists(o): os.remove(o)

    elif option == "AI AUDIO BASS BOOSTER":
        st.markdown("### AI Audio Bass Booster Workspace")
        uf = st.file_uploader("Upload Video/Audio to Boost Bass", type=None, key="b1")
        if uf:
            st.success("✅ Uploaded!"); st.audio(uf)
            r, w, o = f"r_{t_id}.tmp", f"w_{t_id}.wav", f"o_{t_id}.wav"
            bst = st.slider("Select Bass Boost Level (dB):", 1.5, 4.0, 2.0, 0.5)
            if save_file(uf, r) and st.button("BOOST AUDIO BASS"):
                if to_wav(r, w):
                    try:
                        rate, d = wavfile.read(w); b_d = np.clip(d * bst, -32768, 32767)
                        wavfile.write(o, rate, b_d.astype(np.int16)); st.success("✅ Bass Boost Applied!"); st.audio(o)
                        with open(o, "rb") as f: st.download_button("📥 DOWNLOAD BASS AUDIO", f, file_name="bass.wav")
                    except Exception as e: st.error(f"Error: {e}")
            for f in [r, w, o]: 
                if os.path.exists(f): os.remove(f)
                        
    st.markdown('</div>', unsafe_allow_html=True)