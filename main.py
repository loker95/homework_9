with open('my_file_1.txt', "w") as file:
    words = ["banana", "gun", "vegetables", "microwave", "vacuumcleaner", "salad", "potato", "apricot"]
    for word in words:
        file.write(word + "\n")


with open('my_file_1.txt', "r") as my_file_1:
    with open('my_file_2.txt', 'w') as my_file_2:
        for line in my_file_1:
            word = line.strip()
            if len(word) >= 7:
                my_file_2.write(word + "\n")
                



######## task 2


with open('my_file_3.txt', "w") as file:
    words = ["самолет", "пистолет", "облачко", "корова", "носорог", "картофель", "орангутанг", "носок"]
    words_counter = 0
    for word in words:
        file.write(word + "\n")
        words_counter += 1

print(words_counter)