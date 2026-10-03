import re
import nltk
from nltk.tokenize import RegexpTokenizer

# RegexpTokenizer does not require downloading punkt data.
tokenizer = RegexpTokenizer(r"\w+")

STOPWORDS = {
    "a", "an", "the", "is", "are", "am", "was", "were", "be", "been",
    "being", "to", "of", "for", "in", "on", "at", "by", "with", "from",
    "and", "or", "as", "it", "this", "that", "these", "those", "i",
    "we", "you", "he", "she", "they", "my", "our", "your", "their",
    "can", "could", "would", "should", "do", "does", "did", "how",
    "what", "where", "when", "which", "who", "why", "is", "there"
}

def preprocess_text(text: str) -> str:
    """Lowercase, tokenize, remove common stopwords, and return clean text."""
    text = text.lower().strip()
    tokens = tokenizer.tokenize(text)
    tokens = [token for token in tokens if token not in STOPWORDS]
    return " ".join(tokens)
