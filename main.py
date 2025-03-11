import sys
from stats import get_book_text, get_num_words, get_character_frequencies, sort_letter_counts

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 

print(get_num_words(get_book_text(sys.argv[1])))
print(sort_letter_counts(get_character_frequencies(get_book_text(sys.argv[1]))))

