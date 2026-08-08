import streamlit as st

st.set_page_config(
    page_title="STAT Study Assistant",
    page_icon=":book:",
)

st.title("STAT Study Assistant")
st.write("Paste your course materials here, and ask a question.")

notes = st.text_area("Course Materials", height=300, placeholder="Paste your course materials here...")

question = st.text_input("Ask a Question", placeholder="Type your question here...")

if st.button("Ask"):
    if not notes.strip():
        st.warning("Please paste your course materials before asking a question.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        st.success("Question has been submitted!")
        st.write("You asked:", question)
        st.write("Placeholder response.")