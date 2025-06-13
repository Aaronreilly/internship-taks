def word_count(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower().split()

        words = {}
        for word in text:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

        for word in sorted(words):
            print(word + ":", words[word])

    except FileNotFoundError:
        print("File not found.")

# Example
word_count("sample.txt")
