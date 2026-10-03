import streamlit as st
from chatbot import FAQChatbot

st.set_page_config(
    page_title="DIU FAQ Chatbot",
    page_icon="🎓",
    layout="centered"
)


@st.cache_resource
def load_chatbot():
    return FAQChatbot()


bot = load_chatbot()


# -----------------------------
# Page Header
# -----------------------------
st.title("🎓 DIU FAQ Chatbot")

st.caption(
    "Daffodil International University — FAQ-based student support assistant"
)

st.info(
    "Ask about admission, programs, tuition fees, scholarships, campus services, "
    "payment, student services, and other common DIU questions."
)


# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("matched_question"):
            st.caption(
                f"Matched FAQ: {message['matched_question']} "
                f"• Similarity: {message['score']:.2f}"
            )

        if message.get("source"):
            st.caption(f"Source: {message['source']}")


# -----------------------------
# Function to process question
# -----------------------------
def process_question(user_question):

    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    # Get chatbot response
    result = bot.get_response(user_question)

    # Add assistant response to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": result["answer"],
        "matched_question": result.get("matched_question"),
        "score": result.get("score", 0),
        "source": result.get("source")
    })

    # Refresh page
    st.rerun()


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("💡 Suggested Questions")

    examples = [
        "Where is DIU located?",
        "How can I apply for admission?",
        "What documents do I need for admission?",
        "Does DIU offer scholarships?",
        "How can I pay tuition fees?",
        "What should I do if I lose my ID card?"
    ]

    # Clickable suggested questions
    for i, example in enumerate(examples):

        if st.button(
            example,
            key=f"example_{i}",
            use_container_width=True
        ):
            process_question(example)


    st.divider()


    # About section
    st.header("ℹ️ About")

    st.write(
        "This project uses NLP preprocessing, TF-IDF vectorization, "
        "and cosine similarity to retrieve the most relevant FAQ answer."
    )


    st.divider()


    # Clear Chat
    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()


# -----------------------------
# Normal Chat Input
# -----------------------------
user_question = st.chat_input(
    "Ask your question about DIU..."
)


if user_question:
    process_question(user_question)