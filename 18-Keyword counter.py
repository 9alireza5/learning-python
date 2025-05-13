text = input()
words = text.split()
keywords = []
word_index = 1
at_sentence_start = True

for word in words:
    clean_word = word.rstrip('.,')
    if clean_word and clean_word[0].isupper() and not clean_word.isnumeric():
        if not at_sentence_start:
            keywords.append(f"{word_index}:{clean_word}")
    at_sentence_start = word.endswith('.')
    word_index += 1
if keywords:
    for item in keywords:
        print(item)
else:
    print("None")