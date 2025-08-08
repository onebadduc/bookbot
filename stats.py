
def word_count(file_contents):
    file_split = file_contents.split()
    count = len(file_split)
    return count

def character_count(file_split):
    lower_case = file_split.lower()
    char_count = {}
    for char in lower_case:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sorted_list(char_count):
    sort_char = []
    sort_char = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    return sort_char
