import mysql.connector

class DatabaseConnection:
    def connection(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="blog_pf"
        )

        if self.db.is_connected():
            print("Berhasil terhubung ke database")


class Crud:
    def insert(self):
        db_connect = DatabaseConnection()
        db_connect.connection()
        cursor = db_connect.db.cursor()
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        values = ("Putra", "Cendikia")
        cursor.execute(sql, values)
        db_connect.db.commit()
        print("{} data ditambahkan".format(cursor.rowcount))


if __name__ == "__main__":
    crud = Crud()
    crud.insert()
