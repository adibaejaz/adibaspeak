import math
import numpy

# this is an edit

print("Welcome to Adiba's custom language. I do not have a name for it yet. Ad interim, let's call it AdibaSpeak.")
print("You will start the challenge with e^πi + 1 points. If you don't understand what that means, google Euler's identity.")

username = str(input("What is your name?"))
username = username.replace(" ", "")
username = username.lower()
outsenas = []
a = 0
if username == "wittgenstein" or username == "ludwig_wittgenstein":  
    print("You are the coolest person on the planet.")
    a = a + 1
    print("You now have " + str(a) + " point.")
elif username == "adibaejaz" or username == "adiba":
    print("You are a human.")
    print("You now have ∞ points. However, that's weird in Python, so we'll make that a 1.")
    a = a + 1
else:
    print("You are an alien. Let's move on to the language.")
    a = a - 1
    print("You now have " + str(a) + " point(s?).")  # code written by adiba

for i in range(0, 5):
    outsamas = []
    inword = input("Enter a word in EnglishScript and I will translate it into AdibaSpeak.")
    inword = str(inword)
    inword = list(inword)
    for character in inword:
        x = ord(character)
        if x in range(32, 127):
            outsamnum = 12 * x ** 3 + 8 * x ** 2 + 2 * x + 12  # code written by adiba
            outsamnum = str(outsamnum)
            outsamas.append(outsamnum)
        else:
            print(
                "You may only translate EnglishScript, which consists of characters with ASCII codes from 32 to 126, to AdibaSpeak.")
    outsamas = "-".join(outsamas)
    inword = "".join(inword)
    a = a + 1
    print("The word " + str(inword) + " is " + outsamas + " in AdibaSpeak.")

print("Congratulations on sampling AdibaSpeak. You now have %s points." % str(a))

print("EnglishScript to AdibaSpeak translator")
insenen = input("Enter the text that you would like to translate from EnglishScript to AdibaSpeak.")
insenen = str(insenen)
insenen = list(insenen)
for garbage in insenen:
    z = ord(garbage)
    if z in range(32, 127):
        outnumas = 12 * z ** 3 + 8 * z ** 2 + 2 * z + 12  # code written by adiba
        outnumas = str(outnumas)
        outsenas.append(outnumas)
    else:
        print(
            "You may only translate EnglishScript, which consists of characters with ASCII codes from 32 to 126, to AdibaSpeak.")
outsenas = "-".join(outsenas)
print("The text you have entered in EnglishScript translates to " + outsenas + " in AdibaSpeak")
print("You have translated to a superior language. Well done. You now have %s points." % str(a + 10))

print("AdibaSpeak to English translator")
insenas = input("Enter the text that you would like to translate from AdibaSpeak to English Script.")
insenas = str(insenas)
insenas = insenas.split("-")
roots = []
outsenen = []
for wordas in insenas:
    wordas = int(wordas)
    coeffs = [12, 8, 2, 12 - wordas]  # code written by adiba
    r = numpy.roots(coeffs)
    rootslist = r.tolist()
    roots.append(rootslist)
for root in roots:
    rootstring = str(root[2])
    rootstring = rootstring.replace("+0j", "")
    rootstring = rootstring.replace("(", "")
    rootstring = rootstring.replace(")", "")
    rootstring = rootstring[0:5]
    rootstring = float(rootstring)
    rootstring = numpy.rint(rootstring)
    rootstring = str(rootstring)  # code written by adiba
    dotin = rootstring.find(".")
    y = rootstring[0:dotin]
    y = int(y)
    outsenen.append(chr(y))
outsenen = "".join(outsenen)
print("The text you have entered in AdibaSpeak translates to " + outsenen + " in EnglishScript.")
print("You have translated to an inferior language. Terrible. You now have %s points." % str(a - 100))
print(
    "The end. I think I'll stick with the name AdibaSpeak. Changing it now would require too much effort and time. Because creating this language did not need any of that.")  # python 3.5.2


