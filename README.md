# 🎓 DIU FAQ Chatbot

An NLP-based Frequently Asked Questions chatbot for **Daffodil International University (DIU)**.

The project retrieves the most relevant FAQ answer for a user's question using:

- Python
- NLTK
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- Streamlit

> **Important:** This is an educational FAQ retrieval chatbot. It is not an official DIU support system. University information can change, so users should verify important admission, fee, deadline, and policy information from official DIU sources.

---

## ✨ Features

- 🎓 DIU-focused FAQ dataset
- 🔍 Natural-language question matching
- 🧹 NLP text preprocessing with NLTK
- 📊 TF-IDF vectorization
- 📐 Cosine similarity matching
- ⚠️ Similarity threshold for unknown questions
- 💬 Interactive Streamlit chat interface
- 🔗 Source shown with answers
- 📱 Responsive browser-based UI
- 🧩 Easy-to-edit JSON FAQ database

---

## 🏗️ Project Architecture

```text
                 User
                   │
                   ▼
          Streamlit Chat UI
                   │
                   ▼
           User Question
                   │
                   ▼
        NLTK Preprocessing
                   │
                   ▼
          TF-IDF Vectorizer
                   │
                   ▼
        Cosine Similarity
                   │
                   ▼
          Best FAQ Match
             │         │
        score >=      score <
        threshold     threshold
             │         │
             ▼         ▼
       FAQ Answer   Fallback
             │         │
             └────┬────┘
                  ▼
             Chat Response
```

---

## 📁 Project Structure

```text
DIU_FAQ_Chatbot/
│
├── data/
│   └── faqs.json
│
├── app.py
├── chatbot.py
├── preprocess.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 How to Run Locally

## 1. Install Python

Python 3.10+ is recommended.

Check:

```bash
python --version
```

---

## 2. Open the project folder

```bash
cd DIU_FAQ_Chatbot
```

---

## 3. Create a virtual environment

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then:

```powershell
.venv\Scripts\Activate.ps1
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run the chatbot

```bash
streamlit run app.py
```

The browser should open automatically.

If it does not, open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

---

# 🧪 Example Questions

Try:

```text
Where is DIU located?
```

```text
How can I apply for admission?
```

```text
What documents do I need for admission?
```

```text
Does DIU offer scholarships?
```

```text
How can I pay tuition fees?
```

```text
What should I do if I lose my student ID?
```

```text
Does DIU have hostel facilities?
```

---

# 🧠 How the Matching Works

Suppose the FAQ contains:

```text
How can I apply for admission?
```

The user may ask:

```text
What is the process to get admitted?
```

The system does not simply compare exact strings.

It:

1. Converts text to lowercase.
2. Tokenizes the text using NLTK.
3. Removes common stopwords.
4. Converts FAQ questions into TF-IDF vectors.
5. Converts the user question into a TF-IDF vector.
6. Calculates cosine similarity between the user question and every FAQ.
7. Selects the highest-scoring FAQ.
8. Returns its answer if the score is above the configured threshold.

---

# ⚠️ Unknown Question Handling

The chatbot uses a similarity threshold.

If the best match is too weak, it does not return a random FAQ answer.

Instead it responds:

```text
I'm sorry, I couldn't find a reliable answer to that question.
Please contact the DIU office or check the official DIU website
for the latest information.
```

This reduces misleading responses.

---

# 📝 Updating the FAQ Dataset

Open:

```text
data/faqs.json
```

Add a new object:

```json
{
  "question": "Your question here",
  "answer": "Your answer here.",
  "category": "Category",
  "source": "https://official-source-url"
}
```

After saving the JSON file, restart Streamlit.

---

# 🌐 Official DIU Sources

The dataset was prepared using publicly available DIU sources, including:

- DIU official website: https://daffodilvarsity.edu.bd/
- Admission: https://daffodilvarsity.edu.bd/admission
- Undergraduate admission information: https://daffodilvarsity.edu.bd/admission/undergraduate-information
- Location: https://daffodilvarsity.edu.bd/location
- Support contact directory: https://daffodilvarsity.edu.bd/support-contact
- DIU student handbook: https://webbackend.daffodilvarsity.edu.bd/brochure/student-handbook2024/PDF.pdf
- DIU payment guidelines: https://daffodilvarsity.edu.bd/noticeFile/payment-guidelines-7bb689937e.pdf

Always verify time-sensitive information such as admission deadlines, tuition fees, scholarship rules, and payment instructions on the latest official DIU pages.

---

# 🎯 Assignment Requirements Covered

| Requirement | Implementation |
|---|---|
| Collect FAQs | `data/faqs.json` |
| Preprocess text | NLTK |
| Match user questions | TF-IDF + Cosine Similarity |
| Display best answer | Streamlit chatbot |
| Simple chat UI | Streamlit |
| Low-confidence handling | Similarity threshold |

---

# 🔮 Future Improvements

This project can later be upgraded with:

- FastAPI backend
- PostgreSQL database
- Admin dashboard for FAQ management
- FAQ add/edit/delete interface
- DIU website chatbot widget
- Facebook Messenger integration
- Bengali + English multilingual support
- Semantic embeddings
- Vector database
- Authentication for administrators
- Analytics dashboard
- Human support escalation

---

## 👨‍💻 Author

**Shahariar Sadik**

Software Engineering Student  
Daffodil International University

---

## 📄 License

This project is intended for educational and demonstration purposes.



# 🚀 Deploy to Streamlit Community Cloud

This project is prepared for **Streamlit Community Cloud**.

### Recommended flow

```text
VS Code
   ↓
GitHub
   ↓
Streamlit Community Cloud
   ↓
Live DIU FAQ Chatbot
```

1. Push this repository to GitHub.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Create an app.
4. Select your GitHub repository.
5. Branch: `main`
6. Main file: `app.py`
7. Choose a memorable app subdomain.
8. Deploy.

After deployment, future committed changes pushed to GitHub are automatically reflected in the live app.

See `DEPLOYMENT_GUIDE.md` for the complete Git/GitHub workflow.

