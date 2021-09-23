import os
import distro
import datetime as dt
import emoji

today = dt.datetime.today().day
userOS = distro.id().lower().strip()

while True:
    
    if today == 1 and userOS == 'fedora':
        answer = input('Would you like me to perform your monthly maintenance? [Y/n] ').lower().strip()
            
        if answer == 'y' or answer == 'yes':
            print(emoji.emojize("Please Enter Your Password and I'll get you up to speed! :beaming_face_with_smiling_eyes:\n"))
            os.system('sudo dnf -y up')
            os.system('sudo dnf -y autoremove')
            os.system('sudo dnf clean all')
            print(emoji.emojize("\nYou're good to go partner! :cowboy_hat_face:\n"))
            break

        elif answer == 'n' or answer == 'no':
            print(emoji.emojize('No problem. Have a great day! :beaming_face_with_smiling_eyes:\n'))
            break
                
        else:
            print(emoji.emojize('Please give me a valid input. :pouting_face:\n'))

    elif today == 1 and userOS == 'ubuntu':
        answer = input('Would you like me to perform your monthly maintenance? [Y/n] ').lower().strip()
            
        if answer == 'y' or answer == 'yes':
            print(emoji.emojize("Please Enter Your Password and I'll get you up to speed! :beaming_face_with_smiling_eyes:\n"))
            os.system('sudo apt-get update')
            os.system('sudo apt-get upgrade')
            os.system('sudo apt-get autoremove')
            os.system('sudo apt-get clean')
            print(emoji.emojize("\nYou're good to go partner! :cowboy_hat_face:\n"))
            break

        elif answer == 'n' or answer == 'no':
            print(emoji.emojize('No problem. Have a great day! :beaming_face_with_smiling_eyes:\n'))
            break
                
        else:
                print(emoji.emojize('Please give me a valid input. :pouting_face:\n'))
    
    else:
        break