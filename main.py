import re

def main():
    file_path = "books/frankenstein.txt"
    with open(file_path, "r") as file:
        book = file.read()

    word_count = count_words(book)
    char_count = count_chars(book)

    print("--- Analysis of Frankenstein.txt ---\n")
    print(f"The total word count is: {word_count}\n")
    print(f"Character Count Breakdown:")
    for item in char_count:
        print(f"The character '{list(item.keys())[0]}' has a total count of: {list(item.values())[0]}")
    return 0

def count_words(text_string: str):
    # remove_nls = text_string.replace("\n", " ")
    words = text_string.split()
    return len(words)


def count_chars(text_string: str):
    words = text_string.split()
    char_dict = {}
    for word in words:
        for char in word.lower():
            try:
                char_dict[char] = char_dict[char] + 1
            except:
                char_dict[char] = 1
    cleaned_char_dict = {key: value for (key, value) in char_dict.items() if re.match(r"[a-z]", key)}
    cleaned_char_list = [{key: value} for key, value in cleaned_char_dict.items()]
    cleaned_char_list.sort(key=lambda x: list(x.values())[0], reverse=True)
    return cleaned_char_list



if __name__ == "__main__":
    main()