from util_function import *

# Read input cipher text needed to decipher
def read_input(ciphertext_set):
    ciphertext_num = int(input())
    for _ in range(ciphertext_num):
        ciphertext_set.append(input())
    return ciphertext_num


# initialize plain text, set all character of plain text to 'x' (unknown)
# initialize plain text possible chars sets
def initialize_plaintext_set(ciphertext_num, ciphertext_set, plaintext_set, plaintext_possible_char):
    for i in range(ciphertext_num):
        ciphertext = ciphertext_set[i]
        ciphertext_len = len(ciphertext)
        if ciphertext_len % 2 != 0:
            raise Exception("All ciphertext mod 2 should be 0!")
        plaintext = '*' * int(ciphertext_len / 2) 
        plaintext_set.append(plaintext)
        plaintext_possible_char.append([])
        
        
# detect if we can confirm some text in the xor result
def detect_flaw(ciphertext_num, xor_result, plaintext_set, xor_dict, plaintext_possible_char):
    pass

# main function of the program
def main():
    ciphertext_set = []
    plaintext_set = []
    plaintext_possible_char = []
    xor_dict = {}
    ciphertext_num = read_input(ciphertext_set)
    initialize_plaintext_set(ciphertext_num, ciphertext_set, plaintext_set, plaintext_possible_char)
    compute_char_xor(xor_dict)
    if ciphertext_num < 2:
        raise Exception("OPT is secure if only one ciphertext is observed!")
    for i in range(ciphertext_num):
        for j in range(i + 1, ciphertext_num):
            xor_result = strxor(ciphertext_set[i], ciphertext_set[j])
            detect_flaw(ciphertext_num, xor_result, plaintext_set, xor_dict, plaintext_possible_char)
       


if __name__ == "__main__":
    main()