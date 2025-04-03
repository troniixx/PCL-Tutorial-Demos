import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

def nltk_demo():
    print("=== NLTK DEMONSTRATION ===\n")
    
    # Ensure required NLTK data is downloaded
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('stopwords')
    nltk.download('wordnet')
    
    text = """Natural Language Processing (NLP) is a branch of artificial intelligence 
    that helps computers understand human language. The field of NLP is growing rapidly, 
    and researchers are making significant progress. Companies are implementing NLP 
    solutions in their products."""
    
    # 1. Sentence Tokenization
    sentences = sent_tokenize(text)
    print("Sentence Tokenization:")
    for i, sent in enumerate(sentences, 1):
        print(f"{i}. {sent.strip()}")
    
    # 2. Word Tokenization
    words = word_tokenize(sentences[0])
    print("\nWord Tokenization (first sentence):")
    print(words)
    
    # 3. Part-of-Speech Tagging
    pos_tags = pos_tag(words)
    print("\nPOS Tagging:")
    print(pos_tags)
    
    # 4. Stop Words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    print("\nAfter removing stop words:")
    print(filtered_words)
    
    # 5. Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word) for word in filtered_words]
    print("\nAfter lemmatization:")
    print(lemmatized)
    
def main():
    print("Running NLTK Demo...")
    nltk_demo()
    
if __name__ == "__main__":
    main()