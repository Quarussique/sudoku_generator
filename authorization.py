import pickle
import random
import sys

from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(self, name, password, status):
        self.name = name
        self.password = generate_password_hash(password)
        self.status = status # 2-superadmin 1-admin 0-user

    def change_password(self, new_password):
        self.password = generate_password_hash(new_password)


empty_file = False
while True:
    with open('data', 'rb') as file:
        try:
            data = pickle.load(file)
            # empty_file = True
            break
        except EOFError:
            with open('data', 'wb') as file:
                pickle.dump([], file)

inpud = ' '
while 1:
    inpud = input('>')
    if inpud == 'login':
        login_found = False
        name = input('Nickname: ')
        password = input('Password: ')
        personality = User(name, password, 0)
        for data_user in data:
            if data_user.name == personality.name:
                login_found = True
                # if i.password == personality.password:
                if check_password_hash(data_user.password, password):
                    print('LOGGED IN AS ', data_user.name)

                    # session cycle
                    while 1:
                        session_inpud = input('>')
                        if session_inpud == 'help':
                            if data_user.status == 2:
                                print('YOUR STATUS: SUPER-ADMIN\n'
                                      'formatdb\nedituserstatus\nremoveuser\nchangepassword\nlogout')
                            if data_user.status == 1:
                                print('YOUR STATUS: ADMIN\n'
                                      'edituserstatus\nchangepassword\nlogout')
                            if data_user.status == 0:
                                print('YOUR STATUS: USER\n'
                                      'changepassword\nlogout')
                        elif session_inpud == 'formatdb' and data_user.status == 2:
                            format_key = ''
                            for i in range(5):
                                format_key += chr(random.randint(48, 57))
                            print('TYPE', format_key, 'TO CONFIRM:', end=' ')
                            format_key1 = input()
                            if format_key == format_key1:
                                data = []
                                with open('data', 'wb') as file:
                                    pickle.dump(data, file)
                                sys.exit()
                        elif session_inpud == 'removeuser' and data_user.status == 2:
                            user_to_delete_name = input('USERNAME TO REMOVE: ')
                            for deletable_user in data:
                                if deletable_user.name == user_to_delete_name:
                                    break
                            if deletable_user:
                                data.remove(deletable_user)

                        elif session_inpud == 'edituserstatus' and data_user.status > 0:
                            user_to_edit_name = input('USERNAME TO CHANGE STATUS: ')
                            for editable_user in data:
                                if editable_user.name == user_to_edit_name:
                                    break
                            if editable_user:
                                print('CURRENT USER STATUS: ', editable_user.status)
                                try:
                                    new_status = int(input('CHANGE STATUS TO: '))
                                    if 0 <= new_status <= 1:
                                        editable_user.status = new_status
                                        print('SUCCESS')
                                    else:
                                        print('WRONG STATUS ID\nTRY AGAIN')
                                except ValueError:
                                    print('ERROR\nTRY AGAIN')

                        elif session_inpud == 'changepassword':
                            data_user.change_password(input('Type new password: '))
                            print('PASSWORD SUCCESSFULLY CHANGED')
                        elif session_inpud == 'logout' or session_inpud == 'exit':
                            print('LOGGED OUT')
                            break
                        else:
                            print('COMMAND NOT FOUND\n'
                                  'TYPE "help" FOR HELP')

                else:
                    print('WRONG PASSWORD')
        if not login_found:
            print('NOT FOUND')
    elif inpud == 'register':
        registration_error = False
        name = input('NICKNAME: ')
        password = input('PASSWORD: ')
        if len(data) == 0:
            personality = User(name, password, 2)
        else:
            personality = User(name, password, 0)
        for data_user in data:
            if data_user.name == personality.name:
                print('NAME ALREADY EXISTS')
                registration_error = True
        if not registration_error:
            data.append(personality)
            print('SUCCESSFULLY REGISTERED')
    elif inpud == 'showall':
        for data_user in data:
            print(data_user.name)
    elif inpud == 'exit':
        break
    elif inpud == 'help':
        print('login\nregister\nshowall\nhelp\nexit')

    else:
        print('COMMAND NOT FOUND\n'
              'TYPE "help" FOR HELP')

with open('data', 'wb') as file:
    pickle.dump(data, file)
