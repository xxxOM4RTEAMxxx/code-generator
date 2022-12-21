print("🄺🄾🄳 🅈🄰🅁🄰🄳🄰🄽")

import string

import random
 
# Getting password length

length = int(input("kodun uzunlugu "))
 

print('''asagdaki variantlardan sec kod yaratmaq ucun : 

         1. Nömələr

         2. Hərflər

         3. xüsusi isarələr

         4. yarat''')
 

characterList = ""
 
# Getting character set for password

while(True):

    choice = int(input("yuxardaki variantlardan sec "))

    if(choice == 1):

         

        # Adding letters to possible characters

        characterList += string.ascii_letters

    elif(choice == 2):

         

        # Adding digits to possible characters

        characterList += string.digits

    elif(choice == 3):

         

        # Adding special characters to possible

        # characters

        characterList += string.punctuation

    elif(choice == 4):

        break

    else:

        print("Zəhmət olmasa düzgün variant secin")
 

password = []
 

for i in range(length):

   

    # Picking a random character from our 

    # character list

    randomchar = random.choice(characterList)

     

    # appending a random character to password

    password.append(randomchar)
 
# printing password as a string

print("sənin kodun: " + "".join(password))