text = input("Text: ")

# defining variables
letters = 0
words = 1
sentences = 0
for i in range(len(text)):
    # counting letters
    if text[i].isalpha():
        letters += 1

    # counting words
    if text[i] == " ":
        words += 1

    # counting sentences
    if text[i] == "!" or text[i] == "." or text[i] == "?":
        sentences += 1

# Identify level of readability with formula
num = 0.0588 * (100 * letters / words) - 0.296 *(100 * sentences / words) - 15.8
index = round(num)

# giving output to user
if index > 1 and index < 16:
    print(f"Grade {index}")
elif index == 16 or index > 16:
    print("Grade 16+")
else:
    print("Before Grade 1")
