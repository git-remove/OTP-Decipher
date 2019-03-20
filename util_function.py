chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
undetermined_char = '*' 

# xor two strings of different lengths
def strxor(str_a, str_b):     
    if len(str_a) > len(str_b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(str_a[:len(str_b)], str_b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(str_a, str_b[:len(str_a)])])

# xor two hex strings of different lengths
def hexxor(hex_a, hex_b):     
    if len(hex_a) > len(hex_b):
       return "".join([chr(int(x, 16) ^ int(y, 16)) for (x, y) in zip(hex_a[:len(hex_b)], hex_b)])
    else:
       return "".join([chr(int(x, 16) ^ int(y, 16)) for (x, y) in zip(hex_a, hex_b[:len(hex_a)])])

# print a hex string, two chars separated by separator
def print_hex(str, separator):
   if len(str) == 0 :
      return -1
   for char in str[:-1]:
      print("{:02x}".format(ord(char)), end = separator)
   print("{:02x}".format(ord(str[-1])))

# compute xor of chars [a-zA-Z] and space and store it in the dictionary
def compute_char_xor(xor_dict):
   for char1 in range(len(chars)):
      for char2 in range(char1, len(chars)):
         xor_result = strxor(chars[char1], chars[char2])
         if xor_result in xor_dict:
            possible_list = xor_dict[xor_result]
            if chars[char1] not in possible_list:
               possible_list.append(chars[char1])
            if chars[char2] not in possible_list:
               possible_list.append(chars[char2])
         else:
            if chars[char1] == chars[char2]:
               xor_dict[xor_result] = [chars[char1]]
            else:
               xor_dict[xor_result] = [chars[char1], chars[char2]]

# compute the intersection of two lists
# for example, listA = ['a', 'b'], listB = ['A', 'b'], result = ['b']
def list_intersection(listA, listB):
   result_list = [val for val in listA if val in listB]
   return result_list


# output the result of decipher
def print_result(plaintext_possible_char, full_output):
   for i in range(len(plaintext_possible_char)):
         print('The decipher result of message ', i, ' is >>> ')
         print_single(plaintext_possible_char[i], full_output)
         print()

# output a single result message
def print_single(plaintext_set, full_output):
   output = ""
   for single_char_set in plaintext_set:
      if len(single_char_set) == 0:
         if full_output == 0:
            output = output + undetermined_char
         else:
            output = output + '{}'
      elif len(single_char_set) == 1:
         output = output + single_char_set[0]
      else:
         if full_output == 0:
            output = output + undetermined_char
         else:
            output = output + '{'
            for i in range(len(single_char_set)):
               output = output + single_char_set[i]
               if i != len(single_char_set) - 1:
                  output = output + ', '
            output = output + '}'
   print(output)
