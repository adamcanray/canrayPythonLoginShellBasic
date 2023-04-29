import json

# read file
with open('user.json', 'r') as user_data:
    data = user_data.read()
# parse file
obj_user = json.loads(data)

# print(len(obj_user['user']))

# show values
# print("username : " + str(obj_user['user'][0]['username']))

# validation method
def validationFormLogin(username, password):
    #
    result = ""
    # looping
    # for i in obj_user:
    i = 0
    while ( len(obj_user['user']) > i ):
        # check username
        if ( username == obj_user['user'][i]['username'] ):
            # username correct
            # then check password
            if ( password == obj_user['user'][i]['password'] ):
                result = "Login berhasil! ID kamu %s" % obj_user['user'][i]['id']
                break
            else:
                result = "Password salah!"
                break
        else:
            result = "Username belum pernah dibuat."
        i += 1

    # jika di user.json masih kosong
    if ( obj_user['user'] == [] ):
        result = "object user masih kosong,\nsilahkan registrasi pada register.py!"

    return print(result)

# user input form
print("LOGIN")
username = input("Username : ")
password = input("Password : ")
# run validation method with argument from user input form
validationFormLogin(username, password)
