import sys, os, code
os.system("clear")
import pyfiglet
banner=pyfiglet.figlet_format("Phone Spy Minimum", font="standard")
print(banner)
import phonenumbers
from phonenumbers import geocoder, carrier
print("Hello, welcome to PhoneSpy Minimum created by Srijan Mishra")
print("Use this program only for good purposes,not evil")
print("Options :-")
print("e = Enter/specify the number in +xx xxxxxxxxxx format")
print("c = Get the carrier or ISP for the number (works only after entering the number)")
print("g = Get the country details for the number (works only after entering the number)")
print("q = Exit/Quit the program.")
a=input("Select and enter the option>")
if a == "e":
 n=input("Enter/specify the phone number>")
 pn = phonenumbers.parse(n)
elif a == "q":
 os.system("exit")
 os.system("clear")
else:
 print("Enter a valid option or first specify the number")
a=input("Select and enter the option>")
if a == "c":
 i=carrier.name_for_number(pn, 'en')
 print("Carrier or ISP for the number =", i)
elif a == "q":
 os.system("exit")
 os.system("clear")
else:
 print("Enter a valid option or first specify the number")
a=input("Select and enter the option>")
if a == "g":
 geo=geocoder.description_for_number(pn, 'en')
 print("Country the number is located =", geo)
elif a == "q":
 os.system("exit")
 os.system("clear")
else:
 print("Enter a valid option or first specify the number")
a=input("Select and enter the option>")
if a == "q":
 os.system("exit")
 os.system("clear")
