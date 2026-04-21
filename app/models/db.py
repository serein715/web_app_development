import sqlite3
import os

# 預設以與此專案根目錄為基準點來定位 database
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DB_PATH = os.path.join(BASE_DIR, 'database', 'app.db')
SCHEMA_PATH = os.path.join(BASE_DIR, 'database', 'schema.sql')

def get_db_connection():
    """取得 SQLite 資料庫連線，並設定 row_factory 以利使用 dict 取值"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """初始化資料庫：如果資料庫不存在，就會去讀取 schema.sql 並建立對應資料表"""
    # 確保資料夾存在
    db_dir = os.path.dirname(DB_PATH)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
        
    conn = get_db_connection()
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # 允許單獨執行這個檔案來初始化資料庫
    init_db()
    print("資料庫初始化完成！")
