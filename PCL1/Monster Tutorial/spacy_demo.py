#! First, install spaCy and the English model using these commands in terminal:
#! pip install spacy (pip3 on mac)
#! python -m spacy download en_core_web_sm (python3 on mac)

import spacy

def spacy_demo():
    # First check if the model is installed
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        print("Model 'en_core_web_sm' not found. Installing...")
        import subprocess
        subprocess.run(["python3", "-m", "spacy", "download", "en_core_web_sm"]) #! change python3 to python on windows
        nlp = spacy.load("en_core_web_sm")
    
    print("\n=== spaCy DEMONSTRATION ===\n")
    
    text = """Apple Inc. is planning to open a new office in New York City. 
    The company's CEO, Tim Cook, announced the expansion yesterday. The new office 
    will employ 500 people in artificial intelligence research."""
    
    # Process the text
    doc = nlp(text)
    
    # 1. Named Entity Recognition
    print("Named Entities:")
    for ent in doc.ents:
        print(f"Text: {ent.text}, Label: {ent.label_}")
    
    # 2. Sentence Detection
    print("\nSentences:")
    for i, sent in enumerate(doc.sents, 1):
        print(f"{i}. {sent.text.strip()}")
    
    # 3. Part-of-Speech and Dependencies
    first_sent = next(doc.sents)
    print("\nPOS and Dependencies (first sentence):")
    for token in first_sent:
        print(f"Token: {token.text}")
        print(f"  POS: {token.pos_}")
        print(f"  Dependency: {token.dep_}")
        print(f"  Head: {token.head.text}")
    
    # 4. Word Vectors (if available in model)
    print("\nWord Similarity Example:")
    doc1 = nlp("cat")
    doc2 = nlp("dog")
    print(f"Similarity between 'cat' and 'dog': {doc1.similarity(doc2):.3f}")
    
    # 5. Tokenization with attributes
    print("\nTokenization with attributes:")
    for token in doc[:5]:  # First 5 tokens
        print(f"Token: {token.text}")
        print(f"  Is punctuation? {token.is_punct}")
        print(f"  Is space? {token.is_space}")
        print(f"  Like number? {token.like_num}")

def main():
    print("\nRunning spaCy Demo...")
    spacy_demo()

if __name__ == "__main__":
    main()