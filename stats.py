from curses.ascii import isalpha
def count_words_in_a_text(text):
    count = 0

    count = len(text.split())

    return count

def count_characters(text):
    character_list = {}
    characters = list(text)

    for char in characters:
        char = char.lower()

        if char in character_list:
            character_list[char] += 1
        else:
            character_list[char] = 1

    return(character_list)

def sort_character_dictionaries(character_dict):
    characters_dicts_list = []

    for char in character_dict:
        if char.isalpha() is False:
            continue

        characters_dicts_list.append({
            "char": char,
            "num": character_dict[char]
        })

    characters_dicts_list.sort(reverse=True, key=helper_sort_character_dictionaries)

    return characters_dicts_list

def helper_sort_character_dictionaries(dict):
    return dict["num"]
