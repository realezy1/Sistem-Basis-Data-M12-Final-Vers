import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

abc = Tk()
abc.geometry('500x500')
abc.title('Database Sekolah')

def siswa():
    efg = Toplevel(abc)
    efg.geometry('850x500')
    efg.title('Data Siswa')

    Label(efg, text = 'DATA DIRI SISWA', fg = 'black', font = (None, 30)).place(x = 300, y = 5)
    Label(efg, text = 'NISN').place(x = 20, y = 70)
    Label(efg, text = 'Nama').place(x = 20, y = 100)
    Label(efg, text = 'Alamat').place(x = 20, y = 130)
    Label(efg, text = 'NIP').place(x = 20, y = 160)

    e1 = Entry(efg)
    e1.place(x = 140, y = 70)

    e2 = Entry(efg)
    e2.place(x = 140, y = 100)

    e3 = Entry(efg)
    e3.place(x = 140, y = 130)

    e4 = Entry(efg)
    e4.place(x = 140, y = 160)

    def kosong():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    def Add():
        nisn = e1.get()
        nama = e2.get()
        alamat = e3.get()
        nip = e4.get()
        mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'coba')
        mycursor = mysqldb.cursor()
        try:
            sql = "INSERT INTO siswa (nisn, nama_siswa, alamat_siswa, nip_guruFK) VALUES (%s, %s, %s, %s)"
            val = (nisn, nama, alamat, nip)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo('Information', 'Data Siswa Berhasil Diinput')
            kosong()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def Update():
        nisn = e1.get()
        nama = e2.get()
        alamat = e3.get()
        nip = e4.get()
        mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'coba')
        mycursor = mysqldb.cursor()
        try:
            sql = "UPDATE siswa set nama_siswa = %s, alamat_siswa = %s, nip_guruFK = %s  WHERE nisn = %s"
            val = (nama, alamat, nip, nisn)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo('Information', 'Data Siswa Berhasil Diperbarui')
            kosong()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def delete():
        nisn = e1.get()
        mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'coba')
        mycursor = mysqldb.cursor()
        try:
            sql = "DELETE FROM siswa WHERE nisn = %s"
            val = (nisn,)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo('Information', 'Data Siswa Berhasil Dihapus')
            kosong()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def select():
        mydb = mysql.connector.connect(user="root",host="localhost",password="",database="coba")
        cursor = mydb.cursor()

        sql = "SELECT * FROM siswa"
        cursor.execute(sql)
        rows = cursor.fetchall()
        total = cursor.rowcount
        print("Total Data Entries: "+str(total))

        for i, (nisn, nama_siswa, alamat_siswa, nipFK) in enumerate(rows, start = 1):
                listBox.insert("", 'end', values = (nisn, nama_siswa, alamat_siswa, nipFK))
                mydb.close()

    cols = ('NISN', 'Nama Siswa', 'Alamat Siswa', 'NIP')
    listBox = ttk.Treeview(efg, columns = cols, show = 'headings')

    for col in cols:
        listBox.heading(col, text = col)
        listBox.grid(row = 1, column = 50, columnspan = 500)
        listBox.place(x = 10, y = 250)      

    Button(efg, text = 'Add', command = Add, height = 3, width = 13).place(x = 30, y = 190)
    Button(efg, text = 'Update', command = Update, height = 3, width = 13).place(x = 140, y = 190)
    Button(efg, text = 'Delete', command = delete, height = 3, width = 13).place(x = 250, y = 190)
    Button(efg, text = 'Select', command = select, height = 3, width = 13).place(x = 360, y = 190)

def guru():
    hij = Toplevel(abc)
    hij.geometry('650x500')
    hij.title('Data Guru')
    Label(hij, text = 'DATA DIRI GURU', fg = 'black', font = (None, 30)).place(x = 175, y = 5)
    Label(hij, text = 'NIP').place(x = 20, y = 70)
    Label(hij, text = 'Nama').place(x = 20, y = 100)
    Label(hij, text = 'Alamat').place(x = 20, y = 130)

    e1 = Entry(hij)
    e1.place(x = 140, y = 70)

    e2 = Entry(hij)
    e2.place(x = 140, y = 100)

    e3 = Entry(hij)
    e3.place(x = 140, y = 130)

    def kosong():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e1.focus_set()

    def Add():
        nip = e1.get()
        nama = e2.get()
        alamat = e3.get()
        mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'coba')
        mycursor = mysqldb.cursor()
        try:
            sql = "INSERT INTO guru (nip_guru, nama_guru, alamat_guru) VALUES (%s, %s, %s)"
            val = (nip, nama, alamat)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo('Information', 'Data Guru Berhasil Diinput')
            kosong()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def Update():
        nip = e1.get()
        nama = e2.get()
        alamat = e3.get()
        mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'coba')
        mycursor = mysqldb.cursor()
        try:
            sql = "UPDATE guru set nama_guru = %s, alamat_guru = %s  WHERE nip_guru = %s"
            val = (nama, alamat, nip)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo('Information', 'Data Guru Berhasil Diperbarui')
            kosong()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def delete():
        nip = e1.get()
        mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'coba')
        mycursor = mysqldb.cursor()
        try:
            sql = "DELETE FROM guru WHERE nip_guru = %s"
            val = (nip,)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo('Information', 'Data Guru Berhasil Dihapus')
            kosong()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def select():
        mydb = mysql.connector.connect(user="root",host="localhost",password="",database="coba")
        cursor = mydb.cursor()

        sql = "SELECT * FROM guru"
        cursor.execute(sql)
        rows = cursor.fetchall()
        total = cursor.rowcount
        print("Total Data Entries: "+str(total))
        for i, (nip, nama_guru, alamat_guru) in enumerate(rows, start = 1):
            listBox.insert("", 'end', values = (nip, nama_guru, alamat_guru))
            mydb.close()

    cols = ('NIP', 'Nama Guru', 'Alamat Guru')
    listBox = ttk.Treeview(hij, columns = cols, show = 'headings')

    for col in cols:
        listBox.heading(col, text = col)
        listBox.grid(row = 1, column = 0, columnspan = 1)
        listBox.place(x = 10, y = 250)


    Button(hij, text = 'Add', command = Add, height = 3, width = 13).place(x = 30, y = 190)
    Button(hij, text = 'Update', command = Update, height = 3, width = 13).place(x = 140, y = 190)
    Button(hij, text = 'Delete', command = delete, height = 3, width = 13).place(x = 250, y = 190)
    Button(hij, text = 'Select', command = select, height = 3, width = 13).place(x = 360, y = 190)

def mapel():
    klm = Toplevel(abc)
    klm.geometry('850x500')
    klm.title('Data Mapel')

    Label(klm, text = 'DATA MAPEL', fg = 'black', font = (None, 30)).place(x = 300, y = 5)
    Label(klm, text = 'Kode Mapel').place(x = 20, y = 70)
    Label(klm, text = 'Kode Ruang').place(x = 20, y = 100)
    Label(klm, text = 'NIP').place(x = 20, y = 130)
    Label(klm, text = 'Nama Mapel').place(x = 20, y = 160)

    e1 = Entry(klm)
    e1.place(x = 140, y = 70)

    e2 = Entry(klm)
    e2.place(x = 140, y = 100)

    e3 = Entry(klm)
    e3.place(x = 140, y = 130)

    e4 = Entry(klm)
    e4.place(x = 140, y = 160)

    def kosong():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    def Add():
        kodemapel = e1.get()
        koderuang = e2.get()
        nip = e3.get()
        nama = e4.get()
        mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'coba')
        mycursor = mysqldb.cursor()
        try:
            sql = "INSERT INTO mapel (kode_mapel, kode_ruangFK, nip_guruFK, nama_mapel) VALUES (%s, %s, %s, %s)"
            val = (kodemapel, koderuang, nip, nama)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo('Information', 'Data Mapel Berhasil Diinput')
            kosong()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def Update():
        kode = e1.get()
        koderuang = e2.get()
        nip = e3.get()
        nama = e4.get()
        mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'coba')
        mycursor = mysqldb.cursor()
        try:
            sql = "UPDATE mapel set kode_ruangFK = %s, nip_guruFK = %s, nama_mapel = %s  WHERE kode_mapel = %s"
            val = (koderuang, nip, nama, kode)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo('Information', 'Data Mapel Berhasil Diperbarui')
            kosong()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def delete():
        kode = e1.get()
        mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'coba')
        mycursor = mysqldb.cursor()
        try:
            sql = "DELETE FROM mapel WHERE kode_mapel = %s"
            val = (kode,)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo('Information', 'Data Mapel Berhasil Dihapus')
            kosong()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def select():
        mydb = mysql.connector.connect(user="root",host="localhost",password="",database="coba")
        cursor = mydb.cursor()

        sql = "SELECT * FROM mapel"
        cursor.execute(sql)
        rows = cursor.fetchall()
        total = cursor.rowcount
        print("Total Data Entries: "+str(total))
        for i, (kode_mapel, kode_ruangFK, nip_guruFK, nama_mapel) in enumerate(rows, start = 1):
            listBox.insert("", 'end', values = (kode_mapel, kode_ruangFK, nip_guruFK, nama_mapel))
            mydb.close()

    cols = ('Kode Mapel', 'Kode Ruang', 'NIP', 'Nama Mapel')
    listBox = ttk.Treeview(klm, columns = cols, show = 'headings')

    for col in cols:
        listBox.heading(col, text = col)
        listBox.grid(row = 1, column = 0, columnspan = 1)
        listBox.place(x = 10, y = 250)

    Button(klm, text = 'Add', command = Add, height = 3, width = 13).place(x = 30, y = 190)
    Button(klm, text = 'Update', command = Update, height = 3, width = 13).place(x = 140, y = 190)
    Button(klm, text = 'Delete', command = delete, height = 3, width = 13).place(x = 250, y = 190)
    Button(klm, text = 'Select', command = select, height = 3, width = 13).place(x = 360, y = 190)

def kelas():
    nop = Toplevel(abc)
    nop.geometry('650x500')
    nop.title('Data Kelas')

    Label(nop, text = 'DATA KELAS', fg = 'black', font = (None, 30)).place(x = 175, y = 5)
    Label(nop, text = 'Kode Ruang').place(x = 20, y = 70)
    Label(nop, text = 'NIP').place(x = 20, y = 100)
    Label(nop, text = 'Kapasitas').place(x = 20, y = 130)

    e1 = Entry(nop)
    e1.place(x = 140, y = 70)

    e2 = Entry(nop)
    e2.place(x = 140, y = 100)

    e3 = Entry(nop)
    e3.place(x = 140, y = 130)

    def kosong():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e1.focus_set()

    def Add():
        kode = e1.get()
        nip = e2.get()
        kap = e3.get()
        mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'coba')
        mycursor = mysqldb.cursor()
        try:
            sql = "INSERT INTO kelas (kode_ruang, nip_guruFK, kapasitas) VALUES (%s, %s, %s)"
            val = (kode, nip, kap)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo('Information', 'Data Kelas Berhasil Diinput')
            kosong()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def Update():
        kode = e1.get()
        nip = e2.get()
        kap = e3.get()
        mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'coba')
        mycursor = mysqldb.cursor()
        try:
            sql = "UPDATE kelas set nip_guruFK = %s, kapasitas = %s  WHERE kode_ruang = %s"
            val = (nip, kap, kode)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo('Information', 'Data Kelas Berhasil Diperbarui')
            kosong()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def delete():
        kode = e1.get()
        mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'coba')
        mycursor = mysqldb.cursor()
        try:
            sql = "DELETE FROM kelas WHERE kode_ruang = %s"
            val = (kode,)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo('Information', 'Data Kelas Berhasil Dihapus')
            kosong()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def select():
        mydb = mysql.connector.connect(user="root",host="localhost",password="",database="coba")
        cursor = mydb.cursor()

        sql = "SELECT * FROM kelas"
        cursor.execute(sql)
        rows = cursor.fetchall()
        total = cursor.rowcount
        print("Total Data Entries: "+str(total))
        for i, (kode_ruang, nip_guruFK, kapasitas) in enumerate(rows, start = 1):
            listBox.insert("", 'end', values = (kode_ruang, nip_guruFK, kapasitas))
            mydb.close()

    cols = ('Kode Ruang', 'NIP', 'Kapasitas')
    listBox = ttk.Treeview(nop, columns = cols, show = 'headings')

    for col in cols:
        listBox.heading(col, text = col)
        listBox.grid(row = 1, column = 0, columnspan = 1)
        listBox.place(x = 10, y = 250)

    Button(nop, text = 'Add', command = Add, height = 3, width = 13).place(x = 30, y = 190)
    Button(nop, text = 'Update', command = Update, height = 3, width = 13).place(x = 140, y = 190)
    Button(nop, text = 'Delete', command = delete, height = 3, width = 13).place(x = 250, y = 190)
    Button(nop, text = 'Select', command = select, height = 3, width = 13).place(x = 360, y = 190)

def siswa_has_mapel():
    qrs = Toplevel(abc)
    qrs.geometry('500x500')
    qrs.title('Data Mapel yang diambil Siswa')

    Label(qrs, text = 'DATA MAPEL YANG DIAMBIL SISWA', fg = 'black', font = (None, 30)).place(x = 10, y = 5)
    Label(qrs, text = 'NISN').place(x = 20, y = 70)
    Label(qrs, text = 'Kode Mapel').place(x = 20, y = 100)

    e1 = Entry(qrs)
    e1.place(x = 140, y = 70)

    e2 = Entry(qrs)
    e2.place(x = 140, y = 100)


    def kosong():
        e1.delete(0, END)
        e2.delete(0, END)
        e1.focus_set()

    def Add():
        nisn = e1.get()
        kode = e2.get()
        mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'coba')
        mycursor = mysqldb.cursor()
        try:
            sql = "INSERT INTO siswa_has_mapel (nisnFK, kode_mapelFK) VALUES (%s, %s)"
            val = (nisn, kode)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo('Information', 'Data Mapel yang Diambil Siswa Berhasil Diinput')
            kosong()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()


    def delete():
        nisn = e1.get()
        mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'coba')
        mycursor = mysqldb.cursor()
        try:
            sql = "DELETE FROM siswa_has_mapel WHERE nisnFK = %s"
            val = (nisn,)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo('Information', 'Data Mapel yang Diambil Siswa Berhasil Dihapus')
            kosong()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def select():
        mydb = mysql.connector.connect(user="root",host="localhost",password="",database="coba")
        cursor = mydb.cursor()

        sql = "SELECT * FROM siswa_has_mapel"
        cursor.execute(sql)
        rows = cursor.fetchall()
        total = cursor.rowcount
        print("Total Data Entries: "+str(total))
        for i, (nisnFK, kode_mapelFK) in enumerate(rows, start = 1):
            listBox.insert("", 'end', values = (nisnFK, kode_mapelFK))
            mydb.close()

    cols = ('NISN', 'Kode Mapel')
    listBox = ttk.Treeview(qrs, columns = cols, show = 'headings')

    for col in cols:
        listBox.heading(col, text = col)
        listBox.grid(row = 1, column = 0, columnspan = 1)
        listBox.place(x = 10, y = 250)

    Button(qrs, text = 'Add', command = Add, height = 3, width = 13).place(x = 30, y = 130)
    Button(qrs, text = 'Delete', command = delete, height = 3, width = 13).place(x = 140, y = 130)
    Button(qrs, text = 'Select', command = select, height = 3, width = 13).place(x = 250, y = 130)

Label(abc, text = 'SEKOLAH', fg = 'black', font = (None, 30)).place(x = 150, y = 5)
Button(abc, text = 'SISWA', command = siswa, height = 3, width = 20).place(x = 80, y = 100)
Button(abc, text = 'GURU', command = guru, height = 3, width = 20).place(x = 250, y = 100)
Button(abc, text = 'MATA PELAJARAN', command = mapel, height = 3, width = 20).place(x = 80, y = 210)
Button(abc, text = 'KELAS', height = 3, command = kelas, width = 20).place(x = 250, y = 210)
Button(abc, text = 'MAPEL YANG DIAMBIL SISWA', command = siswa_has_mapel, height = 3, width = 40).place(x = 95, y = 320)

abc.mainloop()