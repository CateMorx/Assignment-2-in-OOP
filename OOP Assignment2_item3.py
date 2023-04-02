#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 2 (Item 3:The Vigenère Cipher)

#Imports necessary elements
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

#Prompts user input for message and key
message = input(str('Write your message: ')).lower()
key = input(str('Write your key: ')).lower()

#instantiates list for conversion
output_1=[]
output_2=[]

#Asks user to re-enter the key if the key is less than the length of the message
while len(key) < len(message):
    key_2 = input("Enter the key again: ").lower()
    key += key_2
    key = key[:len(message)]

#converts the message into numbers and added to a list
for i in (message):
    number= ord(i)-97
    output_1.append(number)

#converts the key into numbers and added to a list
for i in (key):
    number_2= ord(i)-97
    output_2.append(number_2)

#adds the two list together
add=[]
for i in range(max(len(output_1), len(output_2))):
    add.append((output_1[i] if i < len(output_1) else 0) + (output_2[i] if i < len(output_2) else 0))

#Computes the mod 26 from the result
mod=[]
for i in (add):
    number_3= i % 26
    mod.append(number_3)

#Converts into ciphertext
cipher_text=[]
for i in (mod):
    number_4= i + 97
    number_4= chr(number_4)
    cipher_text.append(number_4.upper())

#Prints and animates the final output
my_string= ''.join(cipher_text)
def input(screen):
    effects = [
        Cycle(screen,
              FigletText(my_string, font= 'big'),
              int(screen.height / 2-8)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects,500)])
Screen.wrapper(input)