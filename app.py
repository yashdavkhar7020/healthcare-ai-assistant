import streamlit as st
import requests

st.set_page_config(
    page_title="Healthcare AI Assistant",
    layout="centered"
)

st.title("🏥 Healthcare AI Assistant")

API_URL = "http://127.0.0.1:8000/ask"

user_input = st.text_input("Ask a healthcare question")

if st.button("Send") and user_input:

    try:
        response = requests.post(
            API_URL,
            json={"question": user_input}
        )

        data = response.json()

        st.markdown(f"### 🧑 You")
        st.write(user_input)

        st.markdown("---")

        st.markdown("### 🤖 Assistant")

        # Appointment Tool Response
        if "available_slots" in data:

            st.write(data["answer"])

            st.markdown("#### Available Slots")

            for slot in data["available_slots"]:
                st.markdown(f"- {slot}")

        # RAG Response
        else:

            st.write(data["answer"])

            if data.get("sources"):

                st.markdown("#### 📄 Sources")

                for source in data["sources"]:

                    with st.expander(source["document"]):

                        st.write(source["chunk"])

            if data.get("confidence"):

                st.markdown(
                    f"**Confidence:** `{data['confidence'].capitalize()}`"
                )

    except Exception as e:

        st.error(f"Error: {e}")