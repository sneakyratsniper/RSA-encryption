import base64
import sys
import random

def egcd(a, b): #Extended Euclidiean Algorithm
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

def is_prime(n,a):
    #Check small primes
    if n % 2 == 0 : return False
    for x in range(3,min(10001,n),2):
        if n % x == 0 : return False

    if n < 3 : raise ValueError("arg must be greater than or equal to 3")
   
    #Miller Rabin
    #Step 1 : Solve n - 1 = d*2**s
    d = n-1
    s = 0 
    while d % 2 == 0:
        d = d // 2
        s += 1 

    #Step 2 : x = a**d mod n
    x = pow(a,d,n)
    if x == 1 or x == n-1:
        return True
    else:
        #Step 3 : a**d*2**r mod n
        for i in range(0,s):
            x1 = pow(x,2,n)
            if x1 == n-1:
                return True
            x = x1
    return False

def gen_prime(size, rounds = 10):
    n = random.randint(10**(size-1),10**size)
    
    for x in range(rounds):
        a = random.randrange(2, n-1)
        if is_prime(n,a) is False:
            return gen_prime(size)
  
    return n


def generate_rsa_keypair():
    p = gen_prime(100)
    q = gen_prime(100)

    n = p*q
    phi = (p-1)*(q-1)
    
    e = 65537

    d = mod_inverse(e, phi) 

    return (e,n),(d,n)

def encrypt(message, public_key):
    e, n = public_key
    if message > n:
        raise ValueError("Message is too long!")
    return pow(message, e, n)

def decrypt(cipher, private_key):
    d, n = private_key
    return pow(cipher, d, n)

    
def str_to_int(text, type = "utf-8"):
    if type == "b64":
        data = base64.b64decode(text.encode("ascii"))
    else:
        data = text.encode("utf-8")
    return int.from_bytes(data, byteorder="big")

def int_to_str(number, type = "utf-8"):
    length = (number.bit_length() + 7) // 8
    print(length)
    data = number.to_bytes(length, byteorder="big")
    if type == "b64":
        return base64.b64encode(data).decode("ascii")
    else:
        return data.decode("utf-8")


#public_key,private_key = generate_rsa_keypair()


while True:
        choice = input("Would you like to \nEncrypt (1)\nDecrypt (2)\nExit (3)\nKeys (0)\n")
        if choice == '1': #Encrypt
            
            message = input("Enter your message:\n")
            message = str_to_int(message)
            try:
                code = int_to_str(encrypt(message, public_key),'b64')
                print("\nEncrypted message:\n",code)
            except NameError:
                print("No key!")
            input("\nPress ENTER to continue...")
            
        elif choice == '2': #Decrypt
            
            code = input("Enter your code:\n").strip('')
            code = str_to_int(code,'b64')
            try:
                message = int_to_str(decrypt(code, private_key))
                print("\nDecrypted message:", message)
            except NameError:
                print("No key!")
            input("\nPress ENTER to continue...")
            
        elif choice == '3':
            break
        elif choice == '0':
            try:
                print("Public key : ",public_key, "\nPrivate key : ",private_key)
            except NameError:
                print("No keys")
                
            choice = input("\nExit (1) \nStore Keys (2) \nGenerate keys (0)")
            if choice == "0":
                public_key,private_key = generate_rsa_keypair()
                print(print("Public key : ",public_key, "\n\nPrivate key : ",private_key))
            elif choice == "2":
                f = open('keys.txt', 'w')
                f.write('Public key: ('+str(public_key[0])+','+str(public_key[1])+')\n'+'Private key: ('+str(private_key[0])+','+str(private_key[1])+')')
                f.close()
            
            input("\nPress ENTER to continue...")

        elif choice == '':
            sys.stdout.flush()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            input("\nPress ENTER to continue...")




#c = m^e mod(n)
#m = c^d mod(n)

#Generate two large random prime numbers
#Calculate d using mod inverse and euclidian algorithm
