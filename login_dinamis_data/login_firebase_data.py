import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
# serviceAccountKey -- adalah api key untuk access database firebase
# -- ini sesuai account dan project firebase masing-masing, jadi tidak sata upload ke repository
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'real.databaseURL'})

# input login
usernameInput = input("Masukan Username : ")
passwordInput = input("Masukan Password : ")
# buat variabel kosong untuk result
result = ''

# mengambil semua data
ref = db.reference("user/")
# simpan semua data hasil get() ke variabel data
data = ref.get()

# perulangan sebanyak data pada user
for u in data:
    # cek username
    if ( usernameInput == u['username'] ):
        # cek password
        if ( passwordInput == u['password'] ):
            result = "Berhasil login. hallo " + u['name'] + "."
            break
        else:
            result = "password tidak salah!"
            break
    else:
        result = "username tidak tersedia!"
# tampilkan result
print(result)