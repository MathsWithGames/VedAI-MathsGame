import streamlit as st

st.title("🎮 VedAI Maths Game")
st.write("Created by Dr Shalinee")
st.write("Solve the question:")

answer = st.text_input("What is 7 × 8?")

if st.button("Submit Answer"):
    if answer == "56":
        st.success("🎉 Correct!")
    else:
        st.error("❌ Try again!")