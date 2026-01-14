name = input("Enter your name: ")
total_ascii = 0
for char in name:
    total_ascii += ord(char) 
print(f"The total ASCII value of '{name}' is: {total_ascii}")
