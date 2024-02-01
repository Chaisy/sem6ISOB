def encrypt_ceasar(word, key):
    result = ''
    for lett, k in zip(word, key):
        shift = dct[k.lower()]
        if lett.isupper():
            nev_lett = (ord(lett) - ord('A') + shift) % 26 + ord('A')
        else:
            nev_lett = (ord(lett) - ord('a') + shift) % 26 + ord('a')
        result += chr(nev_lett)
    return result

def decrypt_ceasar(word, key):
    result = ''
    for lett, k in zip(word, key):
        shift = dct[k.lower()]
        if lett.isupper():
            nev_lett = (ord(lett) - ord('A') - shift) % 26 + ord('A')
        else:
            nev_lett = (ord(lett) - ord('a') - shift) % 26 + ord('a')
        result += chr(nev_lett)
    return result

def adeq(word, key):
    size_word = len(word)
    while len(key) < size_word:
        key += key
    return key

dct = {}
start, end = ord('a'), ord('z') + 1
for i in range(start, end):
    dct[chr(i)] = i - start

if __name__ == '__main__':
    try:
        with open('input_vigenere.txt', 'r') as f:
            text = f.read()

        if len(text) == 0:
            raise Exception("Empty file")
        # for i in text:
        #     if not i.isalpha():
        #         raise Exception("text have not just a letters")

        print(f'Text: {text}')

        key = input('Key: ')
        for i in key:
            if not i.isalpha():
                raise Exception("text have not just a letters")

        print('Encrypted word:', encrypt_ceasar(text, adeq(text, key)))
        print('Decrypted word:', decrypt_ceasar(encrypt_ceasar(text, adeq(text, key)), adeq(text, key)))

    except ValueError as e:
        print(f'Number mistake: {e}')

    except Exception as e:
        print(f'Mistake: {e}')

    except FileNotFoundError:
        print(f"file is not found.")



#
# def encrypt_ceasar(word, key):
#     result = ''
#     key_index = 0
#
#     for lett in word:
#         if lett.isalpha():
#             shift = dct[key[key_index].lower()]
#             if lett.isupper():
#                 nev_lett = (ord(lett) - ord('A') + shift) % 26 + ord('A')
#             else:
#                 nev_lett = (ord(lett) - ord('a') + shift) % 26 + ord('a')
#             result += chr(nev_lett)
#             key_index = (key_index + 1) % len(key)
#         else:
#             result += lett
#
#     return result
#
#
# def decrypt_ceasar(word, key):
#     result = ''
#     key_index = 0
#
#     for lett in word:
#         if lett.isalpha():
#             shift = dct[key[key_index].lower()]
#             if lett.isupper():
#                 nev_lett = (ord(lett) - ord('A') - shift) % 26 + ord('A')
#             else:
#                 nev_lett = (ord(lett) - ord('a') - shift) % 26 + ord('a')
#             result += chr(nev_lett)
#             key_index = (key_index + 1) % len(key)
#         else:
#             result += lett
#
#     return result
#
#
# def adeq(word, key):
#     size_word = len(word)
#     while len(key) < size_word:
#         key += key
#     return key
#
#
# dct = {}
# start, end = ord('a'), ord('z') + 1
# for i in range(start, end):
#     dct[chr(i)] = i - start
#
# if __name__ == '__main__':
#     try:
#         filename = 'input_vigenere.txt'
#         with open(filename, 'r') as f:
#             text = f.read()
#
#         if len(text) == 0:
#             raise Exception("Empty file")
#
#         print(f'Text: {text}')
#
#         key = input('Key: ')
#         for i in key:
#             if not i.isalpha():
#                 raise Exception("Key should consist only of letters")
#
#         encrypted_text = encrypt_ceasar(text, adeq(text, key))
#         decrypted_text = decrypt_ceasar(encrypted_text, adeq(text, key))
#
#         print('Encrypted text:', encrypted_text)
#         print('Decrypted text:', decrypted_text)
#
#     except ValueError as e:
#         print(f'Number mistake: {e}')
#
#     except Exception as e:
#         print(f'Mistake: {e}')
#
#     except FileNotFoundError:
#         print(f"File '{filename}' is not found.")
#


