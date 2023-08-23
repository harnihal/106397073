x = input("Input: ")

print("Output: ", end="")

for vowels in x:
    if not vowels in ['a', 'A', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']:
        print(vowels, end="")

print()