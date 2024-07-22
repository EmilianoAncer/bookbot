def sort_on(dict):
    return dict["count"]
def main():
    with open("books/frankenstein.txt") as f:
        file_contects: str = f.read()
        split_content: list[str] = file_contects.split()
        word_count = len(split_content)
        char_count: dict[str, int] = {}
        for char in file_contects:
            lower_char: str = char.lower()
            if lower_char not in char_count.keys():
                char_count[lower_char] = 1
            else:
                char_count[lower_char] += 1

        char_list = []
        for key in char_count:
            char_list += [{'char': key, 'count': char_count[key]}]

        char_list.sort(reverse=True, key=sort_on)

        print('--- Begin report of books/frankenstein.txt ---')
        print(str(word_count) + ' words found in the document')
        print("")
        for char in char_list:
            if char['char'].isalpha():
                print(f"The '{char['char']}' character was found {char['count']} times.")
        print('--- End report ---')

main()
