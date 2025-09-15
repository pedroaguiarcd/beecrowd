# alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


test_cases = int(input())

while test_cases > 0:
    test_cases -= 1

    crypto = input()
    shift = int(input())

    a_code = ord('A')
    z_code = ord('Z')

    text = ''
    for char in crypto:
        index = ord(char) - ord('A') - shift
        if index < 0:
            index = 26 + index
            code  = ord('A') + index 
            text +=  chr(code)
    print(text)
           

        # index = alpha.index(char) - shift
        # text += alpha(index)
        

    print(text)

# no caso seria para diminuir e nao o contrario. inves de somar as letras tem que diminuir,
# ou seja, eles nunca vao passar do 25. mas sim ficar negativos
