import json

# # read file
with open('user.json', 'r') as feedsjson:
    feeds = json.load(feedsjson)

# untuk menambah id setiap data baru(agar berbeda)
# print(feeds['user'][-1]['id'] + 1)

# validation method
def validationFormRegister(username,password):
    # string kosong untuk hasil
    result = ""
    # jika object 'user' masih kosong []
    if (feeds['user'] == []):
        # save username dan passwordnya
        with open('user.json', 'w') as feedsjson:
            # siapkan data
            # beri id(id-nya adalah id index terakhir +1)
            entry = { 'id': 1, 'username': username, 'password': password }
            # append data ke user.json dengan key['user']
            feeds['user'].append(entry)
            # jalankan method json.dump
            # kita ingin append data yang ada di feeds ke feedjson(nama alias yang kita berikan untuk open('user.json','r'))
            json.dump(feeds, feedsjson)
        result  = "Berhasil Registrasi!\ndata ditambahkan."
        # keluar dari function
        return print(result)

    # jika tidak kosong
    # untuk wadah yang menjadi acuan sudah tersedia atau tidak username
    ready_exists = 0
    """looping for check username already exits"""
    i = 0
    for id in feeds['user']:
        # username already exists
        if ( username in feeds['user'][i]['username'] ):
            ready_exists += 1
        i += 1
    # cek ready_exists(jika lebih dari 0 maka username sudah tersedia, return False)
    if ( ready_exists > 0 ):
        result = "Username sudah tersedia.\ndata tidak ditambahkan."
    else:
        # save username dan passwordnya
        with open('user.json', 'w') as feedsjson:
            # siapkan data
            # beri id(id-nya adalah id index terakhir +1)
            entry = { 'id': feeds['user'][-1]['id']+1, 'username': username, 'password': password }
            # append data ke user.json dengan key['user']
            feeds['user'].append(entry)
            # jalankan method json.dump
            # kita ingin append data yang ada di feeds ke feedjson(nama alias yang kita berikan untuk open('user.json','r'))
            json.dump(feeds, feedsjson)
        result = "Berhasil Registrasi!\ndata ditambahkan."

    # kembalikan nilai
    return print(result)


# input user
print("REGISTER")
username = input("Username : ")
password = input("Password : ")

# run method
validationFormRegister(username,password)
