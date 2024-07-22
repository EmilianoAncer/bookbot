def main():
    with open("books/frankenstein.txt") as f:
        file_contects = f.read()
        split_content = file_contects.split()
        print(len(split_content))
        char_count = {}
        for char in file_contects:
            lower_char = char.lower()
            if lower_char not in char_count.keys():
                char_count[lower_char] = 1
            else:
                char_count[lower_char] += 1


        print(char_count)

main()
