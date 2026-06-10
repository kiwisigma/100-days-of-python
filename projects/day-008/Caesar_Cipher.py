alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(f"Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = "" # j

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet) # 0-25
        cipher_text += alphabet[shifted_position] # j

    print(f"Here is the encoded result: {cipher_text}")

#TODO-2 decrypt function

def decrypt(original_text, shift_amount):
    output_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {output_text}")

decrypt(original_text=text, shift_amount=shift)
# encrypt(original_text=text, shift_amount=shift)
