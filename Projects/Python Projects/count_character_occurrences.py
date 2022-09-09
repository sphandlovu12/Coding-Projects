def count_chars(s):
    count = {}
    for i in s:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
    print(count)

word=input("Enter string: ")
count_chars(word)