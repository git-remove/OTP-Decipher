# Decipher of One Time Pad Cipher Algorithm


## One Time Pad Algorithm

One Time Pad Algorithm is a simple algorithm used to cipher some message. Given a key `k` and a message `m`, the algorithm will calculate the cipher text by `c = m xor k`.

Both sender and receiver will share the same key `k`. Therefore it is easy for the receiver to decipher the cipher text by `m = c xor k = m xor k xor k = m`.

For more information of One Time Pad algorithm, you can refer to this [link](https://en.wikipedia.org/wiki/One-time_pad).

## Decipher One Time Pad Algorithm
One Time Pad Algorithm is extremely safe if the key `k` is used only once and will be replaced by another key in next communication. If the convention is kept, it is generally impossible to decipher the plain text by [Ciphertext-only attack
](https://en.wikipedia.org/wiki/Ciphertext-only_attack).

However, if the key `k` is used more than once, the attackers can then observe some patterns from only the cipher texts. 

The way the attacker can do is to `xor` the cipher texts together and observe the result.

For example, consider three cipher texts `c1`, `c2` and `c3` which are generated with the same key `k`. That means `c1 = k xor m1`, `c2 = k xor m2` and `c3 = k xor m3`.

If we `xor` `c1`, `c2` and `c3` in pairs, we can get some information about the plaintext since `c1 xor c2 = k xor m1 xor k xor m2 = m1 xor m2`. 

Similarly, `c2 xor c3 = m2 xor m3` and `c1 xor c3 = m1 xor m3`.

If we have some previous knowledge about the message, for example all the messages contain only `[a-zA-Z]` and space, we can use the [ascii table](https://en.wikipedia.org/wiki/ASCII) to filter the result and limit the number of possible solutions.

This project will also adopt this method to decipher the cipher text.

## Usage Guide

### Generate Cipher Text

The `cipher.py` accepts a file that contains the message needed to be ciphered. The first line is the number of messages. I have provided an example message file `plain_text`. To use the cipher, you can simply run `cipher.py < plain_text > cipher_text` in the command line. The key is generated randomly with python inherit `random.randint()` function.

### Decipher Cipher Text

The `decipher.py` will accept a file that contains the cipher texts. The first line of the file is the number of cipher texts (in my example, 7).

Simply run `decipher.py < cipher_text > decipher_result` in the command line and the decipher result will be stored in the file `decipher_result`.

There is an argument `full` to `decipher.py`. If `full` is set to `0`, all the characters that cannot be determined (more than one possible characters or the character list not covering all character in the message) will be represent as `*`. If `full` is set to `1`, then the characters that cannot be determined exactly will be listed in curly braces. `full` is set to `0` by default. To set it to `1`, use `--full=1` in the command.

### Modify the set of possible characters

To modify the set of possible characters in messages, simply modify the variable `chars` on line 1 in the file `util_function.py`. Each character in the string represents a possible character.

## Contact
If you have any questions or better ways to solve this problem, you can raise an issue or send an email to Yiwen(yiw.che@gmail.com)