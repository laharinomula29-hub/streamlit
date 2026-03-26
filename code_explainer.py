import streamlit as st

st.title("💻 AI Code Explainer")

code = st.text_area("Paste your code here:")

def explain_code(code):
    explanation = []

    if "print" in code:
        explanation.append("This code prints output to the screen.")

    if "input" in code:
        explanation.append("This code takes input from the user.")

    if "for" in code:
        explanation.append("This code uses a for loop to repeat a set of instructions.")

    if "while" in code:
        explanation.append("This code uses a while loop that runs until a condition becomes false.")

    if "if" in code:
        explanation.append("This code uses a conditional statement (if/else).")

    if "def" in code:
        explanation.append("This code defines a function.")

    if "=" in code:
        explanation.append("Variables are used to store values.")

    if len(explanation) == 0:
        explanation.append("This code performs some operations.")

    return explanation


if st.button("Explain Code"):
    if code:
        st.subheader("📌 Your Code")
        st.code(code, language="python")

        st.subheader("📖 Explanation")
        result = explain_code(code)

        for line in result:
            st.write("- " + line)
    else:
        st.warning("Please paste some code.")