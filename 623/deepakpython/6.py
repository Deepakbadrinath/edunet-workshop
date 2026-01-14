name = input("Enter your name: ").strip()
name_list = list(name)

if len(name_list) < 2:
    print("Name is too short to swap characters.")
else:
    name_list[1], name_list[-2] = name_list[-2], name_list[1]
    swapped_name = "".join(name_list)
    print("Name after swapping:", swapped_name)