import hashlib

def crack_sha256(hash_to_crack, max_length=6):
    for i in range(1, max_length + 1):
        for guess in generate_guesses(i):
            if hashlib.sha256(guess.encode()).hexdigest() == hash_to_crack:
                return guess
    return None

def generate_guesses(length):
    for c in range(0, 128): #change 0 and 128 to desired range in ascii table 
        for i in range(0, 2 ** (7 * length)):
            guess = ''
            for j in range(0, length):
                guess += chr((i // (2 ** (7 * j))) % 128) #this number needs to be same as the one above 
            yield guess

# Example usage
hash_to_crack = 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb'#change this value
cracked = crack_sha256(hash_to_crack)
if cracked:
    print('Hash cracked! Original input was:', cracked)
else:
    print('Failed to crack hash.')


