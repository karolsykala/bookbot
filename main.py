def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.lower()
    word_count = len(words.split())
    dictionary = {}
    for letter in words:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    list_of_dict = [{"char": k, "num": l} for k,l in dictionary.items()]
    def sort_dic(dict):
        return dict["num"]
    list_of_dict.sort(reverse=True, key=sort_dic)
    print(list_of_dict)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{word_count} words found in the document')
    for dict in list_of_dict:
        for k,l in dict.items():
            if k.isalpha():
                print(f'The character "{k}" was found {l} times')


if __name__ == "__main__":
    main()