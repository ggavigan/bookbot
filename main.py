def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        count = wordCount(file_contents)
        chars = uniqueChars(file_contents)
        report(file_contents, chars, count)

def wordCount(text):
    words = text.split()
    return len(words)

def uniqueChars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def report(text, chars, wordCount):
    print("--- Begin book report of books/frankenstein.txt ---")
    print(f"{wordCount} words found in the document")
    for c, num in chars.items():
        print(f"The '{c}' character was found {num} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()