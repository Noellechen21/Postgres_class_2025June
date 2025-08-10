#由9_3修改
import psycopg2

##以下這部分不需要執行也可得到結果
#def execute_query(connection, query):
#   cursor = connection.cursor()
#  cursor.execute(query)
# result = cursopyr.fetchall()
#cursor.close()
#return result

def create_connection():
    conn = psycopg2.connect(
        host="host.docker.internal",
        database="postgres",
        user="postgres",
        password="raspberry",
        port="5432"
    )
    return conn

##修改的部分在這
#建立一個function,功能是取得所有台鐵車站資訊的站點名稱
def get_station_names():
    """
    取得所有台鐵車站的名稱。

    此函式會連接至資料庫，查詢「台鐵車站資訊」資料表中的所有車站名稱，並以列表形式回傳查詢結果。

    回傳值:
        list: 包含所有車站名稱的查詢結果，每個元素為一個元組(tuple)。
    """
    conn = create_connection()
    #老師想要在function內建一個實體
    cursor = conn.cursor()
    query = """
    SELECT "name" FROM "台鐵車站資訊";
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

#執行SQL的通常不會是主執行檔 =>本檔案改名為db.py (我複製一個)(他是自訂的module), 主執行檔命名為index.py
def main():
 stations= get_station_names()
 print("所有台鐵車站資訊的站點名稱：", stations)

if __name__ == "__main__":
    main()