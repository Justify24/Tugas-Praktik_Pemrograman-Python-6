import mysql.connector 

# hubungkan ke db
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="d3_ti_2023"
)


cursorObject = dataBase.cursor()

# masukkan data ke table mahasiswa
sql = "INSERT INTO mahasiswa (NIM, Nama, Alamat, Matkul, Jurusan) VALUES (%s, %s, %s, %s, %s)"
val = [
    ('V392203311', 'Adam Kurniawan', 'Jl. Merdeka No. 1', 'SOP', 'Teknik Informatika'),
    ('V392204412', 'Bambang Kurniawan', 'Jl. Sudirman No. 2', 'ADP', 'Sistem Informasi'),
    ('V392205513', 'Agung Wicaksono', 'Jl. Ahmad Yani No. 3', 'JKO', 'Teknik Informatika'),
    ('V392201115', 'Wahyu Wicaksono', 'Jl. Gajah Mada No. 4', 'PEW', 'Teknik Informatika'),
    ('V392200075', 'Megy Kurniawati', 'Jl. Pahlawan No. 5', 'MDI', 'Sistem Informasi')
]

cursorObject.executemany(sql, val)


dataBase.commit()


cursorObject.close()
dataBase.close()