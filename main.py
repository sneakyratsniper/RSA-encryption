import base64

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
    p = 7919
    q = 6719
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
    data = number.to_bytes(length, byteorder="big")
    if type == "b64":
        return base64.b64encode(data).decode("ascii")
    else:
        return data.decode("utf-8")


public_key,private_key = generate_rsa_keypair()

print("Public key : ",public_key,"\nPrivate key : ",private_key)

while True:
        choice = input("Would you like to \nEncrypt (1)\nDecrypt (2)\nExit (3)\n")
        if choice == '1': #Encrypt
            
            message = input("Enter your message:\n")
            message = str_to_int(message)
            code = int_to_str(encrypt(message, public_key),'b64')
            print("\nEncrypted message:\n",code)
            
            input("\nPress ENTER to continue...")
            
        elif choice == '2': #Decrypt
            
            code = input("Enter your code:\n").strip('')
            code = str_to_int(code,'b64')
            message = int_to_str(decrypt(code, private_key))
            print("\nDecrypted message:", message)
            
            input("\nPress ENTER to continue...")
            
        elif choice == '3':
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            input("\nPress ENTER to continue...")
            
#c = m^e mod(n)
#m = c^d mod(n)

#Generate two large random prime numbers
#Calculate d using mod inverse and euclidian algorithm
