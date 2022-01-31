# Word Count

def word_count(string):

    li = string.split(" ")
    count = 0
    for i in li:
        if i.__contains__("/"):
            count+=1
        if i.__contains__("-"):
            count+=1

    total = int(len(li)) + count
    print(total)

word_count(input("Enter a string to be counted: "))