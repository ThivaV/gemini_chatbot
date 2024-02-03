import google.generativeai as genai
import streamlit as st


def main():
    """main"""

    st.set_page_config(
        page_title="Gemini Chatbot",
        page_icon="🤖",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    st.header("The Gemini Chatbot 🤖", divider="rainbow")

    st.subheader(
        "Enjoy :red[talking] with :green[Google Gemini] :sunglasses:"
    )

    st.markdown("[check out the repository](https://github.com/ThivaV/gemini_chatbot)")

    gemini_key = st.text_input("Enter your Google Gemini API key 👇", type="password")

    genai.configure(api_key=gemini_key)

    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat(history=[])

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Say something"):
        # user message
        with st.chat_message("user"):
            st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

        response = chat.send_message(prompt, stream=True)
        complete_response = ""
        with st.chat_message("assistant"):
            for chunk in response:
                complete_response += chunk.text
                st.write(chunk.text)

            st.session_state.messages.append(
                {"role": "assistant", "content": complete_response}
            )


if __name__ == "__main__":

    # initialize streamlit session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    main()
