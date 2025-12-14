def mod_inverse(a, m):
    return 0 

def generate_rsa_keypair():
    p = 5
    q = 11
    n = p*q
    phi = (p-1)*(q-1)
    
    e = 65537
    d = mod_inverse(e, phi) 

    return (e,n),(d,n)

public_key,private_key = generate_rsa_keypair()

print("Public key : ",public_key,"\nPrivate key : ",private_key)

x = 1 % 7
y = 1178%116
print(x)
print(y)

#Generate two large random prime numbers
#Calculate d using mod inverse and euclidian algorithm
