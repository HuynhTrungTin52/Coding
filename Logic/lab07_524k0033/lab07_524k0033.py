import math,random

def findGCD(r0,r1):
    if r0==0:
        return r1
    return findGCD(r1 % r0,r0)

def extendedGCD(n,a):
    n0 = n
    a0 = a
    t0 = 0 #y
    t = 1
    s0 = 1 #x
    s = 0
    q = math.floor(n0 / a0)
    r = n0 - q * a0
    while r > 0:
        s_temp = s0 - q * s
        s0 = s
        s = s_temp
        temp = t0 - q * t
        # if temp >= 0:
        #     temp = temp % n
        # else:
        #     if temp < 0:
        #         temp = n - ((-temp) % n)
        t0 = t
        t = temp
        n0 = a0
        a0 = r
        q = math.floor(n0 / a0)
        r = n0 - q * a0
    if a0 != 1:
        print("a has no inverse in Z_n")
    else:
        aminus1 = t % n
        print("a has an inverse of", aminus1)
    return (a0,s,t)

# print(extendedGCD(1024,173))

def mod_inverse(a,n):
    n0 = n
    a0 = a
    t0 = 0
    t = 1
    q = math.floor(n0 / a0)
    r = n0 - q * a0
    while r > 0:
        temp = t0 - q * t
        if temp >= 0:
            temp = temp % n
        else:
            if temp < 0:
                temp = n - ((-temp) % n)
        t0 = t
        t = temp
        n0 = a0
        a0 = r
        q = math.floor(n0 / a0)
        r = n0 - q * a0
    if a0 != 1:
        return None
    else:
        aminus1 = t % n
        return aminus1

def find_mod_inverses(numbers,n):
    my_dict={}
    for num in numbers:
        my_dict[(num,n)]=mod_inverse(num,n)
    return my_dict

list=[random.randint(1, 100) for _ in range(10)]
# print(find_mod_inverses(list,10))

def coprimes_and_inverses(n):
    my_dict={}
    
    for num in [random.randint(1, 100) for _ in range(10)]:
        if(findGCD(num,n)==1):
            my_dict[(num,n)]=mod_inverse(num,n)
    return my_dict

# print(coprimes_and_inverses(5))

# def encrypt(plain_text, key):
#     cipher_text = ""
#     for char in plain_text:
#         if char.isalpha():
#             char = char.upper()
#             encrypted_char = chr(((ord(char) - ord('A')) * key) % 26 + ord('A'))
#             cipher_text += encrypted_char
#         else:
#             cipher_text += char
#     return cipher_text

# def decrypt(cipher_text, key):
#     plain_text = ""
#     key_inverse = pow(key, -1, 26)
#     for char in cipher_text:
#         if char.isalpha():
#             char = char.upper()
#             decrypted_char = chr(((ord(char) - ord('A')) * key_inverse) % 26 + ord('A'))
#             plain_text += decrypted_char
#         else:
#             plain_text += char
#     return plain_text


def bruteForceDecrypt(cipher_text, n):
    pos_key=[i for i in range(0,1001) if findGCD(i,n)==1]
    pos_res=[]
    # print(len(pos_key))
    for key in pos_key:
        plain_text=""
        for char in cipher_text:
            decrypted_char=chr(((ord(char)-ord('A')) * key) % n +ord('A') )
            # print(decrypted_char)
            plain_text+=decrypted_char
        pos_res.append(plain_text)
    return pos_res


# print(bruteForceDecrypt("QCCSWJUPQCCSW",26))

def affine_decryption_key(a, b, n):
    a_inverse = mod_inverse(a, n)
    if a_inverse is None:
        return None
    return (a_inverse, (-b * a_inverse) % n)

# print(affine_decryption_key(5,8,2))

def affine_encrypt(text, a, b, n):
    if mod_inverse(a, n) is None:
        raise ValueError("a has no inverse in Z_n")
    
    cipher_text = ""
    for char in text:
        if char.isalpha():
            char = char.upper()
            encrypted_char = chr(((ord(char) - ord('A')) * a + b) % n + ord('A'))
            cipher_text += encrypted_char
        else:
            cipher_text += char
    return cipher_text

def affine_decrypt(cipher_text, a, b, n):
    a_inverse = mod_inverse(a, n)
    if a_inverse is None:
        raise ValueError("a has no inverse in Z_n")
    
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            char = char.upper()
            decrypted_char = chr(((ord(char) - ord('A') - b) * a_inverse) % n + ord('A'))
            plain_text += decrypted_char
        else:
            plain_text += char
    return plain_text

def compute_private_key_exponent(p, q, b):

    phi_n = (p - 1) * (q - 1)
    
    a = mod_inverse(b, phi_n)
    
    return a

def generate_rsa_keys(p, q, e):
    n = p * q
    # d is the modular inverse of e modulo phi(n)
    d = compute_private_key_exponent(p, q, e) 
    
    if d is None:
        raise ValueError("The given public exponent 'e' does not have an inverse. Choose another 'e'.")
        
    return n, e, d

def rsa_encrypt(m, e, n):
    c = pow(m, e, n)
    return c

def rsa_decrypt(c, d, n):
    # m = c^d mod n
    m = pow(c, d, n)
    return m

