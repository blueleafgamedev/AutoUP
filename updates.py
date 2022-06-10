import os
import datetime as dt
import emoji

today = dt.datetime.today().day
print(emoji.emojize('Let me do a quick check to see if there are any updates :grinning_face_with_big_eyes:\n'))
checkup = os.popen('dnf updateinfo').read()

while True:

    if 'available' not in checkup:
        print(emoji.emojize('It looks like all is well! Have a wonderful day! :beaming_face_with_smiling_eyes:\n'))
        break

    elif today == 1 and 'available' in checkup:
        answer = input(emoji.emojize('Would you like me to perform your monthly maintenance? '
                                     ':thinking_face: [Y/n] ')).lower().strip()

        if answer == 'y' or answer == 'yes':
            print(emoji.emojize("Please Enter Your Password and I'll get you up to speed! "
                                ":beaming_face_with_smiling_eyes:\n"))
            os.system('sudo dnf -y up')
            os.system('sudo dnf -y autoremove')
            os.system('sudo dnf clean all')

            restart = os.popen('dnf needs-restarting -r').read()
            if 'not' in restart:
                print(emoji.emojize("\nYou're good to go partner! :cowboy_hat_face:\n"))
                break

            else:
                print(restart)
                answer = input(emoji.emojize('It looks like some updates require a restart. Would you like me to do this? '
                                  ':thinking_face: [Y/n] ')).lower().strip()
                if answer == 'y' or answer == 'yes':
                    os.system('sudo shutdown -r 1')
                    print(
                        emoji.emojize('System will reboot in 1 Minute. See you soon! :grinning_face_with_big_eyes:\n'))
                    break

                elif answer == 'n' or answer == 'no':
                    print(emoji.emojize('\nAlright! You have a great day! :grinning_face_with_big_eyes:'))
                    break

                else:
                    print(emoji.emojize('Please give me a valid input. :pouting_face:\n'))

            break

        elif answer == 'n' or answer == 'no':
            print(emoji.emojize('No problem. Have a great day! :beaming_face_with_smiling_eyes:\n'))
            break

        else:
            print(emoji.emojize('Please give me a valid input. :pouting_face:\n'))

    elif 'available' in checkup:
        print(checkup)
        answer = input(emoji.emojize('The above updates are available. Would you like me to run them? :thinking_face: '
                                     '[Y/n] ')).lower().strip()

        if answer == 'y' or answer == 'yes':
            print(emoji.emojize("Please Enter Your Password and I'll get you up to speed! "
                                ":beaming_face_with_smiling_eyes:\n"))
            os.system('sudo dnf -y up')

            restart = os.popen('dnf needs-restarting -r').read()
            if 'not' in restart:
                print(emoji.emojize("\nYou're good to go partner! :cowboy_hat_face:\n"))
                break

            else:
                print(restart)
                answer = input(emoji.emojize('It looks like some updates require a restart. Would you like me to do this? '
                                  ':thinking_face: [Y/n] ')).lower().strip()
                if answer == 'y' or answer == 'yes':
                    os.system('sudo shutdown -r 1')
                    print(emoji.emojize('System will reboot in 1 Minute. See you soon! :grinning_face_with_big_eyes:\n'))
                    break

                elif answer == 'n' or answer == 'no':
                    print(emoji.emojize('\nAlrighty! You have a great day! :grinning_face_with_big_eyes:'))
                    break
                else:
                    print(emoji.emojize('Please give me a valid input. :pouting_face:\n'))

            break

        elif answer == 'n' or answer == 'no':
            print(emoji.emojize('No problem. Have a great day! :beaming_face_with_smiling_eyes:\n'))
            break

        else:
            print(emoji.emojize('Please give me a valid input. :pouting_face:\n'))

    else:
        break
