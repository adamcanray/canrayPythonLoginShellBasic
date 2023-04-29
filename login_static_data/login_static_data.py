# static data
user = {
    1 : { "username" : "ujang", "password" : "ujang123"},
    2 : { "username" : "maman", "password" : "maman12" },
    3 : { "username" : "unih", "password" : "unih123"},
}

# validation
def validationLogin(username, password):
    result = ""
    # proccess
    for u in user:
        # cek username jika sesuai
        if ( username == user[u]['username'] ):
            # cek jika password-nya sesuai
            if ( password == user[u]['password'] ):
                result = "login berhasil! ID kamu %s" % u
                break
            else:
                result = "password salah!"
                break
        else:
            result = "username tidak pernah dibuat!"
            # jika username tidak sesuai, lanjutkan tetap perulangan dengan cek ke index lain.
            # tidak menggunkan continue juga tetap berjalan.
            continue
    return print(result)
# form
username = input("Username : ")
password = input("Password : ")

validationLogin(username, password)
