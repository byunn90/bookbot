def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    words = text.split()
    return (
        f"============ BOOKBOT ============\n"
        f"Analyzing book found at books/frankenstein.txt...\n"
        f"----------- Word Count ----------\n"
        f"Found {len(words)} words total words"
    )
def get_character_frequencies(letters):
	num_of_letter = {}
	for i in letters.lower():
	   if i in num_of_letter:
	     num_of_letter[i] += 1
	   else:
	     num_of_letter[i] = 1
	return num_of_letter
def sort_letter_counts(character):
	char_list = [{"char": key, "num": value} for key, value in character.items()]
	for char in char_list:
       	 print(f"{char['char']}: {char['num']}") 





# print(get_character_frequencies(get_book_text()))
# print(sort_letter_counts(get_character_frequencies(get_book_text())))
print(get_num_words(get_book_text()))
print(sort_letter_counts(get_character_frequencies(get_book_text())))

