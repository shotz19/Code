##MAIN 
from element import Element
from PeriodicTable import PeriodicTable
import os
import sys
import time

def clear(): #function to clear the terminal 
		os.system('clear')

def delay_print(s): #function that pauses a little between each letter so that it makes the sentences look like it's being typed out.
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

def main () :
	pt = PeriodicTable('elements.csv')
	clear ()
	delay_print ("\nWelcome to the periodic element dictionary! \nYou could choose to display information about an element, calculate the weight for a molecule, calculate mols for a certain weight of an element, find the element with nearest atomic weight. ")
	
	while True :
		choice = input ("\nEnter display, compound, moles, nearest, or quit: ")
		if str.lower(choice) == "display" :
			clear ()
			info = input ("\nEnter an element name, number, symbol, or weight: ")
			print (pt.display(info))

		elif str.lower(choice) == "compound":
			clear ()
			compound = input ("Enter a compound: ")
			print (pt.calcWeight(compound))

		elif str.lower(choice) == "moles" :
			clear ()
			compound, grams = input ("Enter a compound and its weight in grams, split by a space: ").split()
			print (pt.calcMoles(compound, grams))

		elif str.lower(choice) == "nearest":
			clear ()
			weight = input ("Enter a weight: ")
			print(pt.nearestWeight(float(weight)))

		elif str.lower(choice)  == "quit" :
			clear
			delay_print ("See you later! Bye!       ")
			exit ()
main()
    




