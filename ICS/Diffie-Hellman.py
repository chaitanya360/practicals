

# global keys
P = 23
G = 9


def power(a, b, c):
    return (a**b) % c


# private keys
a = 4
b = 3


# generated keys
A = power(G, a, P)
B = power(G, b, P)

# decripted keys
Ka = power(B, a, P)
Kb = power(A, b, P)

print(Ka, Kb)

if Ka == Kb:
    print("Secret key", Ka)
else:
    print("Not Secret Key")
