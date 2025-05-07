import sys

from stats import count_words_in_a_text, count_characters, sort_character_dictionaries

def get_book_text(filepath):
    file_contents = ""

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
   args = sys.argv

   if len(args) < 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)

   file_contents = get_book_text(args[1])

   words_count = count_words_in_a_text(file_contents)
   character_dict = count_characters(file_contents)
   char_dict_list = sort_character_dictionaries(character_dict)

   print("============ BOOKBOT ============\n Analyzing book found at books/frankenstein.txt...\n")
   print(f"----------- Word Count ----------\n Found {words_count} total words")
   print("--------- Character Count -------")

   for dict in char_dict_list:
       print(f"{dict["char"]}: {dict["num"]}")

   print("============= END ===============")


main()
