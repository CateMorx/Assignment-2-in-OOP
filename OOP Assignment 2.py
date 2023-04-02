#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 2 (Item 2:Decryption)

#Imports necessary elements
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

#Asks for user input
string=input(str("Please Input your statement:"))

#Converts the following characters: 'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !
new_string= (string.replace("*","a").replace("&","e").replace("#","i").replace("+","o").replace("!","u"))

#Prints and animates the final output
def input(screen):
    final_string=new_string
    effects = [
        Cycle(screen,
              FigletText(final_string, font= 'avatar'),
              int(screen.height / 2-8)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects,500)])
Screen.wrapper(input)