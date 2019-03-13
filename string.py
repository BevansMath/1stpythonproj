an_letters = "aefhilmnorsxAEFHILMNORSX"

word = input("I WILL CHEER FOR YOU! Enter a word: ")

times = int(input("Enter Enthusiasum level (1-10): "))

i = 0
for char in word:
    char = word[i]
    if char in an_letters:
        print ("Give me an" + char + "!" + char)

    else:
        print("Give me an" + char + "!" + char)

    i+=1
print("What does that spell?")
for i in range(times):
    print(word,"!!!")
