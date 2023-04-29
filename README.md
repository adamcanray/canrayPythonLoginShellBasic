## Basic Login dan Register dengan data JSON(static) dan Realtime Database(dinamis) di Python3

Versi Python: **3.7.0**

imported module: **json** -- learn **json** module: https://docs.python.org/3/library/json.html

Structure Files:

- intro/
  - **login.py** -- login menggunakan object/dictionary yang sangat sederhana(Basic).
- login_static_data/
  - **login_static_data.py** -- login menggunakan object/dictionary yang memiliki lebih dari 1 user.
- login_dinamis_data/
  - **login_firebase_data.py** -- login menggunakan data yang **user** dari Realtime Database Firebase.
  - **serviceAccountKey.json** -- adalah `service_account` kofigurasi dasar yang **RAHASIA** untuk mengakses Database pada Firebase.
- reg_log_static/
  - **user.json** -- file JSON yang akan menjadi wadah untuk user. menggunakan JSON dikarenakan pada umum-nya REST-SERVER akan memberikan response data berupa JSON ketika kita Request data sebagai REST-CLIENT. **Note: default-nya file ini tidak boleh kosong, harus berisi key "user" dari object JSON** contoh: `{"user":[]}` -- karena key **"user"** akan menjadi object untuk dibaca(read) isi-nya dan ditulis/tambahkan(write, tetapi dengan hanya menambahkan **data yang baru, tidak meniban.**) -- `{"user":[]}` list pada key **"user"** akan di **append()** dengan **data baru**.
  - **register.py** -- kamu bisa register ketika me-run file ini, maka data Username dan Passsword kamu otomatis masuk ke file **user.JSON**. file ini juga sudah mendukung validasi yang lumayan kompleks.
  - **login.py** -- di file ini kamu bisa login berdasarkan Username dan Password yang sudah tersedia/didaftarkan pada **user.JSON**
