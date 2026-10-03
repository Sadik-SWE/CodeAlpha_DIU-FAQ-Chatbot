# 🎓 DIU FAQ Chatbot

An NLP-based FAQ chatbot built for **Daffodil International University (DIU)** that retrieves relevant answers to common student questions using Natural Language Processing and similarity-based information retrieval.

The application provides an interactive **Streamlit** chat interface where users can ask questions about admission, academic programs, tuition fees, scholarships, campus services, payments, student services, and other common university-related topics.

> **Note:** This is an educational and demonstration project. It is not an official DIU support system. University information may change over time, so users should verify important admission, fee, deadline, scholarship, and policy information through official DIU sources.

---

## 🌐 Live Demo

🚀 **Try the chatbot online:**

https://codealphadiu-faq-chatbot-34nlrana9p5vd9bchnwdys.streamlit.app/

---

## 📂 GitHub Repository

🔗 **Source Code:**

https://github.com/Sadik-SWE/CodeAlpha_DIU-FAQ-Chatbot

---

## ✨ Features

- 🎓 DIU-focused FAQ dataset
- 💬 Interactive chatbot interface
- 🧠 NLP-based question processing
- 🧹 Text preprocessing using NLTK
- 📊 TF-IDF vectorization
- 📐 Cosine similarity matching
- 🎯 Best-match FAQ retrieval
- ⚠️ Similarity threshold for low-confidence questions
- 💡 Clickable suggested questions
- 📝 Chat history
- 🔗 Source reference for answers
- 📱 Responsive browser-based interface
- 🧩 Easy-to-edit JSON FAQ database
- 🚀 Deployable with Streamlit Community Cloud

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **NLTK** | Text preprocessing |
| **Scikit-learn** | TF-IDF and cosine similarity |
| **Streamlit** | Web application and chat UI |
| **JSON** | FAQ data storage |
| **Git & GitHub** | Version control and source code hosting |
| **Streamlit Community Cloud** | Live deployment |

---

## 🏗️ Project Architecture

```text
                         User
                           │
                           ▼
                 ┌───────────────────┐
                 │  Streamlit Chat UI │
                 └─────────┬─────────┘
                           │
                           ▼
                    User Question
                           │
                           ▼
                 ┌───────────────────┐
                 │ NLTK Preprocessing│
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ TF-IDF Vectorizer │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Cosine Similarity │
                 └─────────┬─────────┘
                           │
                           ▼
                    Best FAQ Match
                      /          \
                     /            \
            Score ≥ Threshold   Score < Threshold
                   │                    │
                   ▼                    ▼
              FAQ Answer            Fallback
                   │                    │
                   └──────────┬─────────┘
                              ▼
                         Chat Response
