import streamlit as st
from ai_service import ask_question

st.set_page_config(
    page_title="STAT Study Assistant",
)

st.title("STAT Study Assistant")
st.write("Paste your course materials here, and ask a question.")

notes = st.text_area("Course Materials", height=300, placeholder="Paste your course materials here...")

question = st.text_input("Ask a Question", placeholder="Type your question here...")

if st.button("Ask", type="primary"):
    if not notes.strip():
        st.warning("Please enter some course materials before asking a question.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            with st.spinner("Thinking..."):
                answer = ask_question(notes, question)
            st.subheader("Answer:")
            # Display the answer in a markdown format to preserve formatting and line breaks
            st.markdown(answer)
        except ValueError as error:
            st.error(str(error))

        except Exception as error:
            st.error(f"Error: {str(error)}")