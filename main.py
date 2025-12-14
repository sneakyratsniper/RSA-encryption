def egcd(a, b):
    if b == 0:
        #ax + 0y = GCD(a,0) => x=1 GCD = a
        return a, 1, 0
    gcd, x1, y1 = egcd(b, a % b)
    #Recursive GCD until Bézouts Identity is achieved

    x = y1
    
    # Same as a mod b 
    y = x1 - (a//b) * y1
  
    return gcd, x, y 

def mod_inverse(e, m):
    gcd, x, y = egcd(e, m)
    if gcd != 1:
        #Mod inverse only works if gcd(a,b) = 1
        return None

    #ex + my = GCD(e,m)
    #my % m = 0 so 1 = ex
    # x = x % m 
    
    return x % m
 

def generate_rsa_keypair():
    p = 67
    q = 37
    n = p*q
    phi = (p-1)*(q-1)
    
    e = 65537
    d = mod_inverse(e, phi) 

    return (e,n),(d,n)

def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)

def decrypt(cipher, private_key):
    d, n = private_key
    return pow(cipher, d, n)

def str_to_int(text):
    data = text.encode("utf-8")
    return int.from_bytes(data, byteorder="big")

def int_to_str(number):
    length = (number.bit_length() + 7) // 8
    data = number.to_bytes(length, byteorder="big")
    return data.decode("utf-8")

public_key,private_key = generate_rsa_keypair()

print("Public key : ",public_key,"\nPrivate key : ",private_key)



#c = m^e mod(n)
#m = c^d mod(n)

#Generate two large random prime numbers
#Calculate d using mod inverse and euclidian algorithm
