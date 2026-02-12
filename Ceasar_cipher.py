"""
Ceasar cipher program
Mitro Saunio
"""

ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
N_ALPHABETS = len(ALPHABETS)

# Cipher message: M: plaintext message, K: key
def E(K, M):
    K = K % N_ALPHABETS
    C = ''
    for char in M:
        charUpper = char.upper()
        if charUpper in ALPHABETS:
            charIndex = ALPHABETS.index(charUpper)
            charOutput = ALPHABETS[(charIndex + K) % N_ALPHABETS]
            C += charOutput
        else:
            C += char
    return C


# Decipher message: K: key, M: plaintext message
def D(K, C):
    K = K % N_ALPHABETS
    M = ''
    for char in C:
        charUpper = char.upper()
        if char in ALPHABETS:
            charIndex = ALPHABETS.index(charUpper)
            charOutput = ALPHABETS[(charIndex - K) % N_ALPHABETS]
            M += charOutput
        else:
            M += char
    return M

# Main
if __name__=="__main__":
    print("Welcome to Ceasar cipher machine!\nPlease enter your plain text message you want to encrypt and the cipher key.\n")
    M = input("Enter plain text: ")
    K = int(input("Enter cipher key (any number): "))
    C = E(K, M)
    print("\n***------***------***------***")
    print(f'\nCIPHER MESSAGE = "{C}"\n')
    print("***------***------***------***")
    while True:
        Q=input('\nDo you wish to decipher text?\n     Please enter "y" for "Yes", "n" for "No"\n     Your answer: ')
        if Q == "y":
            M_received=D(K, C)
            print(f'\nDecrypted message = "{M_received}"')
            break
        elif Q == "n":
            break
        else:
            print("Please insert correct answer.")
    print("\nThank you, see you soon!\nProgram ending...")
    