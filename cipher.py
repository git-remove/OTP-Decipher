from util_function import *
import random

# read input
def read_input(message_set):
    message_num = int(input())
    for _ in range(message_num):
        message_set.append(input())
    return message_num

# entrypy the message with given key
def encrypt(key, message):
    cipher_text = strxor(key, message)
    return cipher_text

# print a single encrypted message
def print_single_encrypted(cipher_text):
    cipher_text_hex = ""
    for char in cipher_text:
        cipher_text_hex = cipher_text_hex + "{:02x}".format(ord(char))
    print(cipher_text_hex)

# main function
def main():
    message_set = []
    message_num = read_input(message_set)
    max_size = 2 * len(max(message_set, key = len))
    random_ascii = [hex(random.randint(0, 15)).split('x')[-1] for _ in  range(max_size)]
    key = ''.join(random_ascii)
    print(message_num)
    for message in message_set:
        cipher_text = encrypt(key, message)
        print_single_encrypted(cipher_text)
        
    

if __name__ == "__main__":
    main()