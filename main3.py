s=str(input("Enter a text: "))
word=""
if len(s.split(" ")) >= 2:
    for i in s.split(" "):
        word+=i.replace(i[0],i[0].upper())+" "
else:
    print("Must provide a str of length >= 2 words")
print(word)
