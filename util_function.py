# xor two strings of different lengths
def strxor(str_a, str_b):     
    if len(str_a) > len(str_b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(str_a[:len(str_b)], str_b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(str_a, str_b[:len(str_a)])])


# print a hex string, two chars separated by separator
def print_hex(str, separator):
   if len(str) == 0 :
      return -1
   for char in str[:-1]:
      print("{:02x}".format(ord(char)), end = separator)
   print("{:02x}".format(ord(str[-1])))

# compute xor of chars [a-zA-Z] and space and store it in the dictionary
def compute_char_xor(xor_dict):
   chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
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