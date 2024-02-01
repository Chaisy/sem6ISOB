eng_alf = 'abcdefghijklmnopqrstuvwxyz'


def caesar(text, alf, shift):
    def get_new_char(x):
        if x.isalpha():
            new_index = (alf.index(x.lower()) + shift) % len(alf)
            return alf[new_index].upper() if x.isupper() else alf[new_index]
        return x

    return ''.join(map(get_new_char, text))


def caesar_decrypt(text, alf, shift):
    return caesar(text, alf, -shift)


if __name__ == '__main__':
    try:
        with open('input_caesar.txt', 'r') as f:
            text = f.read()

        if len(text) == 0:
            raise Exception("Empty file")
        # for i in text:
        #     if not i.isalpha():
        #         raise Exception("text have not just a letters")

        print(f'Text: {text}')
        sh = int(input('Enter shift: '))

        if type(sh) is not int:
            raise ValueError("you enter bad shift")

        print(f'Encrypted message: {caesar(text, eng_alf, sh)}')
        print(f'Decrypted message: {caesar_decrypt(caesar(text, eng_alf, sh), eng_alf, sh)}')

    except ValueError as e:
        print(f'Number mistake: {e}')

    except Exception as e:
        print(f'Mistake: {e}')

    except FileNotFoundError:
        print(f"file is not found.")
