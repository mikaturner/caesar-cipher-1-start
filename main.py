alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
i= 0
mess_list_indexes = []
encry_list_indexes = []
encrypted_message = []
cipher = ""

def encrypt(text, shift):
  for character in text:
    if character in alphabet:
      i = alphabet.index(character)
    #creates a list with the index numbers of each letter in message according to the alphabet list
      mess_list_indexes.append(i)
    else: 
      mess_list_indexes.append(character)
  
    #creates a list with the index numbers of each letter in the encrypted/shifted message according to the alphabet list    
  for character in mess_list_indexes:
    if type(character) == int:
      #number_shift = (character + shift) % 26;
      number_shift = character + shift
      if number_shift <= 25:
        encry_list_indexes.append(number_shift)
      else:
        number_shift -= 26
        encry_list_indexes.append(number_shift)
    else: encry_list_indexes.append(character)
  
  #creates a list with the shifted message
  for character in encry_list_indexes:
    if type(character) == int:
      encrypted_message.append(alphabet[character])
    else: 
      encrypted_message.append(character)
  print(f"The encoded text is: {''.join(encrypted_message)}")
    
    
encrypt(text, shift)
    