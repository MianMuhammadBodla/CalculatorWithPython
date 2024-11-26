import streamlit as st
import base64
from PIL import Image
import io

def display_round_image(image_path):
    """Displays an image with rounded borders."""
    try:
        image = Image.open(image_path)
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        st.markdown(
            f'<img src="data:image/jpeg;base64,{img_str}" class="img-fluid" style="border-radius: 50%; width: 150px; height: 150px; object-fit: cover; display: block; margin-left: auto; margin-right: auto; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);">',
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.error("Error: Image file not found. Please check the path and try again.")

def run_about_me():
    """Function to run the About Me page."""
    st.subheader("Hello! I'm Muhammad")
    st.write("""
    I'm a Certified Cloud Applied Generative AI Engineer specializing in Full Stack Web Development 
    with a focus on MicroServices and GPT integration. I develop Web 2.0 applications with custom GPTs 
    and chatbots, and have experience with Smart Contracts in Generative AI.
    """)

    display_round_image("Portfolio-portrait-.jpeg")

    st.subheader("Watch My Short Film")
    video_url = "https://www.youtube.com/embed/QW9yOYjvlWc"
    st.markdown(f'<div class="video-container"><iframe src="{video_url}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></div>', unsafe_allow_html=True)

    st.subheader("Activities and Societies:")
    st.write("""
    - President, Junior Biological Club (2023-24)
    - Finance Secretary, Junior Biological Club (2022-23)
    - Parliamentary Debater, Formanites Debating Society (2022-24)
    - And More
    """)

    st.subheader("Technologies I've been working with recently:")
    techs = ["Python", "Custom GPTs", "Streamlit", "TypeScript", "Docker", "Cloud Computing", "Generative AI"]
    st.write(", ".join(techs))

    st.subheader("Connect With Me")
    st.write("""
    - [LinkedIn](https://www.linkedin.com/in/muhammad-bodla)
    - [Facebook](https://www.facebook.com/muhammadbodla)
    - [Instagram](https://www.instagram.com/muhammadbodla)
    - [GitHub](https://github.com/muhammadbodla)
    - [YouTube](https://www.youtube.com/@MuhammadBodla)
    - [Email](mailto:mianmuhammadbodla@gmail.com)
    """)

    st.write("Thank you for visiting my profile. Looking forward to connecting and collaborating on innovative projects!")

if __name__ == "__main__":
    st.set_page_config(page_title="About Muhammad", layout="wide", initial_sidebar_state="expanded")
    run_about_me()
