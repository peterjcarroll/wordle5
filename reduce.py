with open("wordle_answers.txt", "r") as f:
    words = f.readlines()

keep_words = []
for word in words:
    # keep words that have no duplicate letters and only one vowel
    if len(set(word)) == len(word) and len([c for c in word if c in "aeiou"]) == 1:
        keep_words.append(word.strip())

# with open("wordle_answers_reduced.txt", "w") as f:
#     f.write("".join(keep_words))

# Find 5 words that have no duplicate letters among the 5 words
unique_words = []
for start_word in keep_words:
    unique_words = [start_word]
    for word in keep_words:
        # print(set(word).intersection(set("".join(unique_words))))
        if word != start_word and len(set(word).intersection(set("".join(unique_words)))) == 0:
            unique_words.append(word)
        if len(unique_words) == 5:
            break
    if len(unique_words) == 5:
        break
    elif len(unique_words) == 4:
        # found 4 words, but not 5
        # find a 5th word that has only 2 duplicate letter with the 4 words
        for word in keep_words:
            if word not in unique_words and len(set(word).intersection(set("".join(unique_words)))) == 2:
                unique_words.append(word)
                print(" ".join(unique_words))
                break

if len(unique_words) == 5:
    print("Found 5 unique words!")
    print(" ".join(unique_words))
