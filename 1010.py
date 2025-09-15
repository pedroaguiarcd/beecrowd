c1, q1, v1 = input().split()
c2, q2, v2 = input().split()
print(f"VALOR A PAGAR: R$ {int(q1)*float(v1) + int(q2)*float(v2):.2f}")
