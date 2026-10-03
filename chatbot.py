import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess_text


class FAQChatbot:
    def __init__(self, faq_path="data/faqs.json", threshold=0.18):
        self.faq_path = Path(__file__).resolve().parent / faq_path
        self.threshold = threshold
        self.faqs = self._load_faqs()

        self.questions = [faq["question"] for faq in self.faqs]
        self.clean_questions = [preprocess_text(q) for q in self.questions]

        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        self.faq_matrix = self.vectorizer.fit_transform(self.clean_questions)

    def _load_faqs(self):
        with open(self.faq_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_response(self, user_question: str):
        if not user_question.strip():
            return {
                "answer": "Please enter a question.",
                "matched_question": None,
                "score": 0.0,
                "source": None
            }

        clean_question = preprocess_text(user_question)
        user_vector = self.vectorizer.transform([clean_question])

        scores = cosine_similarity(user_vector, self.faq_matrix)[0]
        best_index = scores.argmax()
        best_score = float(scores[best_index])
        best_faq = self.faqs[best_index]

        if best_score < self.threshold:
            return {
                "answer": (
                    "I'm sorry, I couldn't find a reliable answer to that question. "
                    "Please contact the DIU office or check the official DIU website "
                    "for the latest information."
                ),
                "matched_question": None,
                "score": best_score,
                "source": "https://daffodilvarsity.edu.bd/"
            }

        return {
            "answer": best_faq["answer"],
            "matched_question": best_faq["question"],
            "score": best_score,
            "source": best_faq.get("source")
        }
