import mysql.connector 

# Connect to MySQL server
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="d3_ti_2023"
)

# Create a cursor object
cursorObject = dataBase.cursor()

# Insert data into Mahasiswa table
sql = "INSERT INTO mataKuliah (Kode_Matkul, Nama_Matkul, Waktu, Ruangan, Jurusan) VALUES (%s, %s, %s, %s, %s)"
val = [
    ('MDI', 'Matematika Diskrit', '2022-08-01', 'L2R2', 'Teknik Informatika'),
    ('ADP', 'Algoritma dan Pemrograman', '2022-08-02', 'L2R3', 'Sistem Informasi'),
    ('SOP', 'Sistem Operasi', '2022-08-03', 'L2R4', 'Teknik Informatika'),
    ('JKO', 'Jaringan Komputer', '2022-08-04', 'L2R5', 'Sistem Informasi'),
    ('PEW', 'Pemrograman Web', '2022-08-05', 'L3R1', 'Teknik Informatika')
]

cursorObject.executemany(sql, val)

# Commit changes to the database
dataBase.commit()

# Close the cursor and database connection
cursorObject.close()
dataBase.close()