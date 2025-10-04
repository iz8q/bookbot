import sys
from stats import get_num_words, get_num_chars, get_sorted_num_chars

if len(sys.argv) != 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

book = get_book_text(sys.argv[1])

def main():
  print(f"Analyzing book found at {sys.argv[1]}...")
  print(f"Found {get_num_words(book)} total words")
  for obj in get_sorted_num_chars(get_num_chars(book)):
    print(f"{obj['char']}: {obj['num']}")
main()