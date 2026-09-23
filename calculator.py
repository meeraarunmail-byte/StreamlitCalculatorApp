import streamlit as st

st.markdown("""
    <style>
    .stApp {
        background-color: blue;
    }
    </style>
""", unsafe_allow_html=True)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

st.title("Simple Calculator")
number1 = st.number_input("Enter the first number: ")
number2 = st.number_input("Enter the second number: ")

operation = st.selectbox(
    "Choose an operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

if st.button("Calculate"):

    if operation == "Add":
        result = add(number1, number2)
        st.success(f"Result: {result}")

    elif operation == "Subtract":
        result = subtract(number1, number2)
        st.success(f"Result: {result}")

    elif operation == "Multiply":
        result = multiply(number1, number2)
        st.success(f"Result: {result}")

    elif operation == "Divide":
        if number2 != 0:
            result = divide(number1, number2)
            st.success(f"Result: {result}")
        else:
            st.error("Cannot divide by zero.")


