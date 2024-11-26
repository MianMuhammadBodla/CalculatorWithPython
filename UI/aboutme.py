import streamlit as st

def display_round_image(image_url):
    """Displays an image with rounded borders using a URL."""
    st.markdown(
        f'''
        <style>
        .img-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 20px;
        }}
        .img-fluid {{
            border-radius: 50%;
            width: 150px;
            height: 150px;
            object-fit: cover;
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
            border: 3px solid #fff;
        }}
        </style>
        <div class="img-container">
            <img src="{image_url}" class="img-fluid">
        </div>
        ''',
        unsafe_allow_html=True
    )

def run_about_me():
    """Function to run the About Me page."""
    st.subheader("Hello! I'm Muhammad")
    st.write("""
    I'm a Certified Cloud Applied Generative AI Engineer specializing in Full Stack Web Development 
    with a focus on MicroServices and GPT integration. I develop Web 2.0 applications with custom GPTs 
    and chatbots, and have experience with Smart Contracts in Generative AI.
    """)

    # Pass the corrected direct link of the image
    display_round_image("https://dl.dropboxusercontent.com/scl/fi/7lb36lr0m10kczeirtm4x/Portfolio-portrait.jpeg?rlkey=3w71dryy5144r0l7i5kb9wz50&st=3lahnyky&dl=1")

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
