from util_function import *
import util_function
import argparse

# Read input cipher text needed to decipher
def read_input(ciphertext_set):
    ciphertext_num = int(input())
    for _ in range(ciphertext_num):
        ciphertext_set.append(input())
    return ciphertext_num


# initialize plain text, set all character of plain text to 'x' (unknown)
# initialize plain text possible chars sets
def initialize_plaintext_set(ciphertext_num, ciphertext_set, plaintext_set, plaintext_possible_char):
    all_char_list = [char for char in chars]
    for i in range(ciphertext_num):
        ciphertext = ciphertext_set[i]
        ciphertext_len = len(ciphertext)
        if ciphertext_len % 2 != 0:
            raise Exception("All ciphertext mod 2 should be 0!")
        plaintext = '*' * int(ciphertext_len / 2) 
        plaintext_set.append(plaintext)
        plaintext_possible_char.append([all_char_list for _ in range(int(ciphertext_len / 2))])
        
        
        
# detect if we can confirm some text in the xor result
def detect_flaw(text_index1, text_index2, xor_result, plaintext_set, xor_dict, plaintext_possible_char):
    for i in range(int(len(xor_result)/2)):
        xor_char = chr(ord(xor_result[2 * i]) * 16 + ord(xor_result[2 * i + 1]))
        if xor_char in xor_dict:
            possible_chars = xor_dict[xor_char]
            plaintext_possible_char[text_index1][i] = list_intersection(plaintext_possible_char[text_index1][i], possible_chars)
            plaintext_possible_char[text_index2][i] = list_intersection(plaintext_possible_char[text_index2][i], possible_chars)

# main function of the program
def main():
    parser = argparse.ArgumentParser(description='Process argument full.')
    parser.add_argument('--full', type = int, help = 'whether display all possible characters or not, default is 0')
    args = parser.parse_args()
    if args.full != None:
        full_output = int(args.full)
    else:
        full_output = 0
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
            xor_result = hexxor(ciphertext_set[i], ciphertext_set[j])
            detect_flaw(i, j, xor_result, plaintext_set, xor_dict, plaintext_possible_char)
    print_result(plaintext_possible_char, full_output)

if __name__ == "__main__":
    main()
