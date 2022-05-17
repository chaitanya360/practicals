# original msg
m = 12
print("original ", m)


# power function
def power(a, b, c):
    return (a**b) % c


# gcd function

def GCD(x, y):

    if x > y:
        small = y
    else:
        small = x

    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd


# step 1
p = 7
q = 3


# step 2
n = p*q


# step 3 (find fi_n)
fi_n = (p-1)*(q-1)

# step 4 (find e)
e = 2
while e < fi_n:
    if GCD(e, fi_n) == 1:
        break
    else:
        e = e + 1

# step 5 (find d)
k = 2  # constant k
d = (1 + (k*fi_n))//e


# public key  (e,n)
# private key (d,n)


# step 6
# original -> ciphertext


c = power(m, e, n)

# step 7
# ciphertext -> original


m = power(c, d, n)


print("cipher ", c)
print("decrypted ", m)
