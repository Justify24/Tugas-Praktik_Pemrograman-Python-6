import mysql.connector 

# Hubungkan ke database
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="d3_ti_2023"
)

# 
cursorObject = dataBase.cursor()

# Buat Table Mahasiswa
cursorObject.execute("CREATE TABLE mahasiswa (    NIM VARCHAR(10) PRIMARY KEY,     Nama VARCHAR(30),     Alamat VARCHAR(255),     Matkul VARCHAR(10),     Jurusan VARCHAR(25) )")

# Buat Table Dosen
cursorObject.execute("CREATE TABLE dosen (    NIP VARCHAR(20) PRIMARY KEY,     Nama_Dosen VARCHAR(50),     Matkul VARCHAR(50),     Umur INT(3) )")

# Buat Table Matkul
cursorObject.execute("CREATE TABLE matakuliah (    Kode_Matkul VARCHAR(10) PRIMARY KEY,     Nama_Matkul VARCHAR(50),     Waktu DATE,     Ruangan VARCHAR(10),     Jurusan VARCHAR(25) )")

# Close the cursor and database connection
cursorObject.close()
dataBase.close()