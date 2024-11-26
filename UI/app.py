import streamlit as st
import add
import sub
import mult
import divid
import aboutme  # Import the aboutme module (make sure this file exists)

# Set the page config as the very first Streamlit command
st.set_page_config(page_title="My Calculator", page_icon=":wave:", layout="wide")

def main():
    """ Main function to navigate the app. """
    st.sidebar.title("Navigation")
    choice = st.sidebar.selectbox("Go to", ["Calculator", "About Me"])

    if choice == "Calculator":
        run_calculator()
    elif choice == "About Me":
        aboutme.run_about_me()  # Call the run_about_me function from aboutme.py

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

if __name__ == "__main__":
    main()
