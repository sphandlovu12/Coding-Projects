def palidrome(sentence):
    for i in (",.'?/><}{{}};"):
        sentence = sentence.replace(i, "")
    palidrome = []
    words = sentence.split(' ')
    for word in words:
        words = words.lower()
        if word == word[::-1]:
            palidrome.append(word)
    return palidrome

sentence = input("Enter a sentence: ")
print(palidrome(sentence))