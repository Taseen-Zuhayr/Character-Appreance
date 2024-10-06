word = input("Enter a word : ")
letter = input("Enter a letter : ")
i = 0
count = 0

while i<len(word):
    if word[i] == letter:
        count += 1
    i += 1
print("The letter has occured ",count,"times.")