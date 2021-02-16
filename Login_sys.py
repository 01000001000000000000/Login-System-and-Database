import json

start = input('Login or Sign up? ')
filename = 'userdata.json'


if start == 'Sign up':
    s_username = input('Enter a username: ')
    s_password = input('Enter a password: ')
    with open(filename, 'r') as file:
        userdata = json.load(file)
    if s_username not in userdata:
        userdata.update({s_username: s_password})
        with open(filename, 'w') as f:
            json.dump(userdata, f)
            print('Successfully signed up!')
    else:
        print('Username is taken.')
elif start == 'Login':
    l_username = input('Enter your username: ')
    l_password = input('Enter your password: ')
    with open(filename) as f:
        l_userdata = json.load(f)
    if l_username in l_userdata:
        if l_password == l_userdata[l_username]:
            print(f"Welcome back, {l_username}!")
    else:
        print('Username not found.')
else:
    print("Couldn't recognize. Please try again.")
