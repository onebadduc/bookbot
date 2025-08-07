def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(file_contents):
    file_split = file_contents.split()
    count = len(file_split)
    return count

def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    total_words = word_count(file_contents)
    print(f"{total_words} words found in the document")

main()