name = input("Enter your name: ").strip() 
length = len(name)
middle_index = length // 2  
middle_char = name[middle_index]
vowels = "AEIOUaeiou"

if middle_char.isalpha():  
    if middle_char in vowels:
        print(f"The middle character '{middle_char}' is a vowel.")
    else:
        print(f"The middle character '{middle_char}' is a consonant.")
else:
    print(f"The middle character '{middle_char}' is not an alphabet character.")
