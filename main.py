from stats import word_count
from stats import character_count
from stats import sorted_list
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    char_count = {}
    sort_char = []
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    total_words = word_count(file_contents)
    char_count = character_count(file_contents)
    sort_char = sorted_list(char_count)
    char_count = dict(sort_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count -----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count ---------")
    for key, value in char_count.items():
        if key.isalpha():
            print(f"{key}: {value}")
        
    print("=========== END ===========")

main()