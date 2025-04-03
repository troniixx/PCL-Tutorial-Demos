import argparse
import re
from collections import Counter

# Fake lemmatizer for demo purposes
def lemmatize(word):
    lemmas = {"running": "run", "cars": "car", "mice": "mouse"}
    return lemmas.get(word, word)

# Dummy stopword list
STOPWORDS = {"the", "is", "in", "at", "of", "a", "an", "and", "on", "for"}

def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

def main():
    parser = argparse.ArgumentParser(
        description="Simple text analysis tool for tokenization and frequency analysis."
    )

    parser.add_argument("file", help="Path to the input text file")

    parser.add_argument(
        "-n", "--num",
        type=int,
        default=10,
        help="Number of top frequent words to show (default: 10)"
    )

    parser.add_argument(
        "-s", "--stopwords",
        action="store_true",
        help="Remove stopwords from the analysis"
    )

    parser.add_argument(
        "-l", "--lemmatize",
        action="store_true",
        help="Lemmatize tokens before counting frequencies"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print detailed processing info"
    )

    args = parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as f:
        text = f.read()

    if args.verbose:
        print(f"[INFO] Loaded text from {args.file}")

    tokens = tokenize(text)

    if args.verbose:
        print(f"[INFO] Tokenized {len(tokens)} words")

    if args.stopwords:
        tokens = [t for t in tokens if t not in STOPWORDS]
        if args.verbose:
            print(f"[INFO] Removed stopwords, {len(tokens)} tokens left")

    if args.lemmatize:
        tokens = [lemmatize(t) for t in tokens]
        if args.verbose:
            print("[INFO] Lemmatization applied")

    counter = Counter(tokens)

    print(f"\nTop {args.num} most frequent words:\n")
    for word, count in counter.most_common(args.num):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()

# Usage:
# Just tokenization and frequency count:
# python argparser.py input.txt

# With stopwords removed and lemmatization:
# python argparser.py input.txt -s -l

# With verbose output:
# python argparser.py input.txt -s -l -v

# All arguments
# python argparser.py input.txt -n 5 -s -l -v