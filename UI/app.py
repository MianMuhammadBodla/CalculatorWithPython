import streamlit as st
import add
import sub
import mult
import divid

# Set the page config as the very first Streamlit command
st.set_page_config(page_title="My Calculator", page_icon=":wave:", layout="wide")

def main():
    """ Main function to navigate the app. """
    st.sidebar.title("Navigation")
    choice = st.sidebar.selectbox("Go to", ["Calculator", "About Me"])

    if choice == "Calculator":
        run_calculator()
    elif choice == "About Me":
        run_about_me()

def run_calculator():
    """ Runs calculator logic. """
    st.title("Simple Calculator")
    num1 = st.number_input("Enter First Number", format="%f")
    num2 = st.number_input("Enter Second Number", format="%f")
    operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        if operation == "Add":
            result = add.add(num1, num2)
        elif operation == "Subtract":
            result = sub.sub(num1, num2)
        elif operation == "Multiply":
            result = mult.multi(num1, num2)
        elif operation == "Divide":
            result = divid.divide(num1, num2)
        st.success(f"The result is {result}")

def run_about_me():
    """ Displays the 'About Me' section. """
    st.subheader("Hello! I'm Muhammad")
    st.write("""
    I'm a Certified Cloud Applied Generative AI Engineer specializing in Full Stack Web Development 
    with a focus on MicroServices and GPT integration. I develop Web 2.0 applications with custom GPTs 
    and chatbots, and have experience with Smart Contracts in Generative AI.
    """)

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
    - [YouTube](https://www.youtube.com/muhammadbodla)
    - [Email](mailto:mianmuhammadbodla@gmail.com)
    """)

    st.write("Thank you for visiting my profile. Looking forward to connecting and collaborating on innovative projects!")

if __name__ == "__main__":
    main()
