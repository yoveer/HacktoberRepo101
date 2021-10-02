import random
import math
prime_num = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 
    71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 
    151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 
    233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 
    317, 331, 337, 347, 349]

def  primalityTest(n): 
    while True:
        number = random.randrange(2**(n-1)+1, 2**n - 1)
        for i in prime_num:
            if number % i == 0 and i**2 <= number: break
        else: return number

def MillerRabinPassed(num):
    d = num-1
    count = 0
    while d % 2 == 0:
        d >>= 1
        count += 1
    def trials(round_tester):
        if pow(round_tester, d, num) == 1:
            return False
        for i in range(count):
            if pow(round_tester, 2**i * d, num) == num-1:
                return False
        return True
    for _ in range (20):
        if trials(random.randrange(2, num)): return False
    return True

def power(x, y, p):
    # fast exponentiation for large numbers
	res = 1
	x = x % p
	while (y > 0):
		if (y & 1): res = (res * x) % p
		y = y >> 1 
		x = (x * x) % p
	return res

def findPrimefactors(s, n) :
	while (n % 2 == 0) :
		s.add(2)
		n = n // 2
	for i in range(3, int(math.sqrt(n)), 2):
            while (n % i == 0):
                s.add(i)
                n = n // i
	if (n > 2) :
		s.add(n)

def findPrimitive(n) :
	s = set()
	phi = n - 1
	findPrimefactors(s, phi)
	for r in range(2, phi + 1):
		flag = False
		for it in s:
			if (power(r, phi // it, n) == 1):
				flag = True
				break
		if (flag == False):
			return r
	return -1

def extendedEuclidean(a, b):
    if a == 0: return (b, 0, 1)
    else:
        g, y, x = extendedEuclidean(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = extendedEuclidean(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else: return x % m

if __name__ == "__main__" : 
    while True:
        bits = 20
        prime = primalityTest(bits)
        if not MillerRabinPassed(prime): continue
        else:
            p = prime
            break
    alpha = findPrimitive(p)
    d = random.randint(2,p-2)
    beta = pow(alpha,d,p)
    print("Public key : ",[alpha,beta,p])
    print("Private key : ",d)
    r = random.randint(2,p-2)

    plain_txt = input("Enter plain text : ")
    encrypted_list = []
    decrypted_text = ""
    c1 = pow(alpha, r, p)
    for i in plain_txt:
        c2 = pow((pow(beta,r)*ord(i)),1,p) 
        encrypted_list.append(c2)
    print("Encrypted list : ",encrypted_list)

    print("--Decrypting this sequence--")
    for i in encrypted_list:
        decrypted_text += chr(pow((modinv(pow(c1,d),p)*i),1,p))
    print("Decrypted text : ", decrypted_text)

#Example :
# Public key :  [3, 140135, 639487]
# Private key :  184357
# Enter plain text : cryptography   
# Encrypted list :  [419262, 308381, 299269, 493695, 123067, 586352, 48634, 308381, 604576, 493695, 595464, 299269]
# --Decrypting this sequence--
# Decrypted text :  cryptography