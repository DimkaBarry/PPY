from math import ceil

#zad1
def panel_calc(f_length, f_width, p_length, p_width, pack):
    floor = f_length * f_width + f_length * f_width / 10
    panel = p_length * p_width
    panels_needed = floor / panel
    return ceil(panels_needed / pack)

print("Need: " + str(panel_calc(4, 4, 0.20, 1, 10)))

#zad2
def prime(*num):
    for i in num:
        is_prime = True
        if(num[i] == 0 or num[i] == 1):
            print(f"{num[i]} is not prime")
        else:
            for j in range(2, num[i]):
                if num[i] % j == 0 and j != num[i]:
                    is_prime = False
            if is_prime:
                print(f"{num[i]} is prime")
            else:
                print(f"{num[i]} is not prime")

prime(0, 1, 2, 3, 4, 5)

#zad3
def caesar_cipher(data, shift):
    data.lower()
    #print(data)
    new_data = ""
    for elem in data:
        if(elem != " "):
            character = ord(elem) - shift
            new_data = new_data + chr(character)
        else:
            new_data = new_data + elem
    return new_data

print(caesar_cipher("asd zx", 3))