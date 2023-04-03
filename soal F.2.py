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
sql = "INSERT INTO dosen (NIP, Nama_Dosen, Matkul, Umur) VALUES (%s, %s, %s, %s)"
val = [
    ('732328428422', 'Tirta Hartono Hadiman', 'MDI', 35),
    ('238490289423', 'Yuda Hendri Oesman', 'ADP', 40),
    ('123012310131', 'Wiryono Chung', 'JKO', 50),
    ('834724927942', 'Neonardi Duyi', 'SOP', 45),
    ('204322000920', 'Gerard Pattikawa', 'PEW', 38)
]

cursorObject.executemany(sql, val)


dataBase.commit()

cursorObject.close()
dataBase.close()