# leds = (
#     6,
#     2,
#     5,
#     5,
#     4,
#     5,
#     6,
#     3,
#     7,
#     6,
# )

# test_case = int(input())
# while test_case > 0:
#     test_case -= 1

#     number = input()

#     number_leds = 0
#     for digit in number:
#         digit = int(digit)
#         number_leds += leds[digit]
#     print(number_leds, 'leds')

# SEGUNDA VERSAO
leds = {
    '0' : 6,
    '1' : 2,
    '2' : 5,
    '3' : 5,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 3,
    '8' : 7,
    '9' : 6,
}
test_cases = int(input())
for k in range(test_cases):
    number = input()
    
    for digit in number:
        number_leds += leds[digit]




