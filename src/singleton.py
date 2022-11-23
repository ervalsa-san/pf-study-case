from typing import Dict

import mysql.connector as mysql

class MySQLConnection:
    __instance = None

    def __init__(self, host: str, user: str, password: str, name: str, port: str) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.name = name
        self.port = port

        connection = MySQLConnection.__instance

        if connection is None:
            connection = mysql.connect(host=self.host, user=self.user, passwd=self.password, database=self.name, port=self.port)
            
            # Connection Cursor Berhasil
            cursor = connection.cursor()
            sql = """
                CREATE TABLE customers (
                customer_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                address Varchar(255))
            """
            cursor.execute(sql)
        else:
            raise Exception('You cannot create another MySQL connection')
        
    @staticmethod
    def get_instance(credentials: Dict[str, str]) -> object:
        if not MySQLConnection.__instance:
            MySQLConnection(credentials['DB_HOST'], credentials['DB_USER'], credentials['DB_PASS'], credentials['DB_NAME'], credentials['DB_PORT'])
        return MySQLConnection.__instance
        
    @staticmethod
    def close_instance() -> None:
        MySQLConnection.__instance.close()

    # Connection Gagal
    # def create_table_customers(self):
    #     connection = MySQLConnection.__instance
    #     cursor = connection.cursor()
    #     sql = """
    #         CREATE TABLE customers (
    #         customer_id INT AUTO_INCREMENT PRIMARY KEY,
    #         name VARCHAR(255),
    #         address Varchar(255))
    #     """
    #     msyql_cursor.execute(sql)
    #     print("tabel berhasil dibuat")