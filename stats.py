def get_wordcount(contents):
    words = contents.split()
    wordcount = 0
    for word in words:
        wordcount += 1
    return wordcount

def get_char_count(contents):
    characters = contents.lower()
    char_counts = {}
    for char in characters:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_on(item):
    return item["num"]

def sort_by_char_counts(char_counts):
    new_counts = []
    for char in char_counts:
        char_dict = {}
        char_dict["char"] = char
        char_dict["num"] = char_counts[char]
        new_counts.append(char_dict)
    new_counts.sort(reverse=True, key=sort_on)
    return new_counts
