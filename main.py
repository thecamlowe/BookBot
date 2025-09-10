import sys
from stats import get_wordcount, get_char_count, sort_by_char_counts

def get_book_text(filepath):
    with open(filepath) as contents:
        return contents.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    contents = get_book_text(filepath)
    wordcount = str(get_wordcount(contents))
    char_counts = sort_by_char_counts(get_char_count(contents))
    count_block = ""
    for char in char_counts:
        if char["char"].isalpha():
            line = f"%s: %s" % (char["char"], char["num"])
            if count_block == "":
                count_block += line
            else:
                count_block += "\n" + line
    print(f"""
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {wordcount} total words
--------- Character Count -------
{count_block}
============= END ===============
""")
    # print(str(get_wordcount(contents)) + " words found in the document")
    # print(str(get_char_count(contents)))

main()