naam = input("Wat is je naam? > ")
voornaam = input("wat is je voornaam? > ")
leeftijd = input("wat is je leeftijd? > ")
import time
import sys
from time import sleep
string = f"Leeftijd: {leeftijd} \nVoornaam: {voornaam} \nNaam: {naam}"

for letter in string:
  sleep(0.07) 
  sys.stdout.write(letter)
  sys.stdout.flush()


# print(f"Leeftijd: {leeftijd}")
# time.sleep(0.5)
# print(f"Voornaam: {voornaam}")
# time.sleep(0.5)
# print(f"naam: {naam}")