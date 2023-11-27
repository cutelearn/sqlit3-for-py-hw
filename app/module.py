import sqlite3

class executeQuery:
    def __init__(self, db_instance):
        self.db = db_instance

    def create(self, query, params=None):
        """ 執行插入操作。 """
        self._execute(query, params)

    def read(self, query, params=None):
        """ 執行讀取操作。 """
        return self._execute(query, params, fetch=True)

    def update(self, query, params=None):
        """ 執行更新操作。 """
        self._execute(query, params)

    def delete(self, query, params=None):
        """ 執行刪除操作。 """
        self._execute(query, params)

    def _execute(self, query, params=None, fetch=False):
        """ 內部方法，用於執行 SQL 命令。 """
        try:
            if self.db.cursor is not None:
                self.db.cursor.execute(query, params or ())
                if fetch:
                    return self.db.cursor.fetchall()
                else:
                    self.db.conn.commit()
            else:
                print("尚未建立數據庫連接。")
        except sqlite3.Error as e:
            print(f"執行 SQL 時出錯: {e}")
