# data from database(MISALKAN)
adam = {
    "username" : "ujang",
    "password" : "ujang123",
}
# print(adam["username"])

# input
# username
username = input("Username : ")
# password
password = input("Password : ")

# check
if ( username != adam['username'] ):
    print("username salah!")
    print(False)
elif ( password != adam['password'] ):
    print("password salah!")
    print(False)
else:
    print("login seccess!")
    print(True)

