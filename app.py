import streamlit as st
import replicate
import os

st.set_page_config(page_title="Funny AI Video", layout="centered")

# Mengambil API Token dari Secrets Streamlit
replicate_token = st.secrets["REPLICATE_API_TOKEN"]
os.environ["REPLICATE_API_TOKEN"] = replicate_token

st.title("🎬 Generator Video Animasi Lucu")

prompt = st.text_input("Mau buat animasi lucu apa?", placeholder="Kucing main gitar sambil salto...")
style = st.selectbox("Gaya Animasi", ["Pixar Style", "Claymation", "Anime", "Cartoon"])

if st.button("Generate Video"):
    if prompt:
        with st.spinner("Lagi ngerjain... Proses ini makan waktu 1-2 menit ya!"):
            try:
                # Menggunakan model Stable Video Diffusion atau sejenisnya
             # Ganti blok replicate.run kamu dengan ini:
output = replicate.run(
    "lucataco/animate-diff:be113c56d53e144333688e21cc0d984381005f1f96409d9494a37c040d346cc0",
    input={
        "prompt": f"{prompt}, funny animation style, cute, high quality",
        "guidance_scale": 7.5,
        "num_inference_steps": 25,
        "num_frames": 16  # Ini akan menghasilkan video pendek yang stabil
    }
)

# Karena output model ini biasanya langsung berupa URL string atau list, 
# kita pastikan cara nampilinnya begini:
video_url = output[0] if isinstance(output, list) else output
st.video(video_url)
    else:
        st.warning("Isi dulu prompt-nya bos!")
