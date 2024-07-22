def main():
    with open("books/frankenstein.txt") as f:
        file_contects = f.read()
        split_content = file_contects.split()
        print(len(split_content))

main()
