n = int(input())
translate_dict = {}

for _ in range(n):
    original, en, fr, de = input().split()
    translate_dict[en] = original
    translate_dict[fr] = original
    translate_dict[de] = original
sentence = input().split()

translated_sentence = []
for word in sentence:
    if word in translate_dict:
        translated_sentence.append(translate_dict[word])
    else:
        translated_sentence.append(word)

print(" ".join(translated_sentence))