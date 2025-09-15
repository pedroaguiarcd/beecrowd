while True:
    correct_password = 2002
    try:
        password = int(input())
        if password == correct_password:
            print("Acesso Permitido")
            break
        else:
            print("Senha Invalida")
    except:
        print("Senha Invalida")
