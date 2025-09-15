original_text = input()

dancing_text = ""


# se ela for true eu pego o proximo e transformo em maiusculo se nao nao faço isso
to_upper = True

for char in original_text:
    if char .isalpha():
        if to_upper:
            char = char.upper
        else:
            char = char.lower()

        to_upper = not to_upper

        # if to_upper:           #o codigo de cima faz a mesma coisa
        #     to_upper = False
        # else:
        #     to_upper = True
    dancing_text = dancing_text + char
print(dancing_text)


# prob1234.py < prob1234.in
