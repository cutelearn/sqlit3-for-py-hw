import sqlite3
from module import executeQuery

class SQLiteDB:
    def __init__(self, db_path):
        """ 初始化 SQLiteDB 類別，設置數據庫路徑。 """
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def connect(self):
        """ 建立數據庫連接。 """
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"連接數據庫時出錯: {e}")


    def close(self):
        """ 關閉數據庫連接和游標。 """
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()

# 使用範例
if __name__ == "__main__":
    database = '04weather.db'
    db = SQLiteDB(database)
    db.connect()

    query_exec = executeQuery(db)

    print("歡迎使用交互使用SQLite數據庫")
    while True:
        print("請選擇你要使用的操作類型CRUD")
        print("C = Create, R = Read, U = Update, D = Delete, S = Show Schema")
        operation_type = input("請輸入你要使用的操作類型: ").upper()
        if operation_type == 'S':
            table_name = input("請輸入要顯示結構的表名: ")
            query = f"PRAGMA table_info({table_name});"
            results = query_exec.read(query)
            for row in results:
                print(row)
            continue
        query = input("請輸入你要使用的SQL語句: ")
        params = input("請輸入SQL語句的參數（若無則留空），以逗號分隔: ")

        # 將參數字符串轉換為元組
        params = tuple(params.split(',')) if params else ()

        results = None
        if operation_type == 'C':
            query_exec.create(query, params)
        elif operation_type == 'R':
            results = query_exec.read(query, params)
            if not results:
                print("找不到任何資料。")
        elif operation_type == 'U':
            query_exec.update(query, params)
        elif operation_type == 'D':
            query_exec.delete(query, params)
        else:
            print("輸入錯誤，請重新輸入")

        if results:
            for row in results:
                print(row)

        if input("是否繼續？（Y/N）").upper() != 'Y':
            break

    db.close()