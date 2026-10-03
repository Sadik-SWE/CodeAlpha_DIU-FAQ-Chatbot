# Project Report — DIU FAQ Chatbot

## 1. Project Title
DIU FAQ Chatbot — NLP-based Frequently Asked Questions Retrieval System

## 2. Objective
The objective is to build a chatbot that can understand a student's natural-language question, find the most similar question from a predefined DIU FAQ dataset, and return the corresponding answer.

## 3. Problem Statement
Students frequently ask repeated questions about admission, programs, tuition fees, scholarships, payments, campus facilities, and student services. A FAQ chatbot can provide quick answers to common questions without requiring a human to answer every repeated query.

## 4. Methodology
The system follows this pipeline:

User Question → Preprocessing → TF-IDF → Cosine Similarity → Best FAQ → Answer

## 5. Technologies
- Python
- NLTK
- Scikit-learn
- Streamlit
- JSON

## 6. Why TF-IDF?
TF-IDF converts text into numerical vectors based on word importance. It provides a simple and explainable baseline for FAQ matching.

## 7. Why Cosine Similarity?
Cosine similarity measures how close two text vectors are in direction. A higher value means the questions are more similar in the TF-IDF feature space.

## 8. Limitations
This is a retrieval-based chatbot. It does not generate new answers like a large language model. Its performance depends on the quality and coverage of the FAQ dataset.

## 9. Future Scope
The system can be extended with:
- multilingual Bengali/English support
- semantic embeddings
- vector databases
- FastAPI
- PostgreSQL
- admin dashboard
- website widget
- Facebook Messenger integration

## 10. Viva Questions

### What is NLP?
Natural Language Processing is a field of AI that enables computers to process and analyze human language.

### What is TF-IDF?
TF-IDF stands for Term Frequency-Inverse Document Frequency. It assigns weights to terms based on their importance in a document relative to a collection of documents.

### What is cosine similarity?
Cosine similarity measures the similarity between two vectors using the cosine of the angle between them.

### Why not exact string matching?
Users can ask the same question using different wording. Similarity matching allows the system to find a related FAQ even when the wording is not identical.

### Is this a generative AI chatbot?
No. It is a retrieval-based FAQ chatbot. It selects an existing answer from the FAQ dataset.

### Why is a threshold used?
A threshold prevents the system from returning an unrelated FAQ when no sufficiently similar question exists.
