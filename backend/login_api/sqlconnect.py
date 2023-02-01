#进行数据库连接
import pymysql

mydb = pymysql.connect(host='182.16.13.70', port=3306, user='sqlyanshujuku', password='zwj798261', db='sqlsqlyanshujuku', charset='utf8')

def getmessage(a,b): #a用户名 b密码
    mydb.ping(reconnect=True)
    #建立数据库游标
    cursor = mydb.cursor()
    sql = "select * from admin where name = '{}' and password = '{}'". format(a,b)
    cursor.execute(sql)
    #存储结果
    ret = cursor.fetchall()
    data = []
    #json数据转换 前端需要json数据格式 1存在 0不存在
    for k in ret:
        target = {}
        for j in range(len(cursor.description)):
            target[cursor.description[j][0]] = k[j]
        data.append(target)
    mydb.commit()
    cursor.close()
    mydb.close()
    if len(data)!= 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    ret = getmessage()