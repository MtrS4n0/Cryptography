"""
Ceasar cipher decryption code
Mitro Saunio
"""
N_ALPHABETS=26

#Your code here

def D(K, C):
    K = K % N_ALPHABETS
    M = ''
    for char in C:
        if char.isalpha():
            shifted = ord(char) - K
            if shifted < ord('A'):
                shifted += N_ALPHABETS
            M += chr(shifted)
        else:
            M += char
    return M

if __name__=="__main__":
    print("Welcome to Ceasar cipher decryption machine!\n")
    print("This program will iterate through all possible keys and show you the decrypted message for each key.\n")
    print("Please enter your cipher text message you want to decrypt.\n")
    C = input("Enter cipher text: ")
    print("\n***------***------***------***\n")
    for K in range(1, N_ALPHABETS + 1):
        M_received = D(K, C)
        print(f"Key {K}: {M_received}")
    print("\n***------***------***------***")
    print("\nThank you, see you soon!\nProgram ending...")
