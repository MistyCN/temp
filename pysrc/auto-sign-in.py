import sqlite3

def Sign():
    name = input("输入你的姓名或使用号码")
    
def CheckPerson():
    pass
def CheckAll():
    pass
def DataBase(indb):
    db = indb
    dbSelect = int(input("1.初始化数据库"))
    if dbSelect==1:
        print("初始化执行")
        try:
            db.execute("""CREATE TABLE students( 
                    id INT PRIMARY KEY,  
                    name VARCHAR(50) NOT NULL
                    
        
                    
                    );""")
        except Exception as any:
            print("初始化错误："+str(any))
        

def About():
    print("本项目用于学习数据库操作")
    print("github - https://github.com/MistyCN/temp")
def init():
    conn = sqlite3.connect("sqlite.db")
    global db
    db = conn.cursor

#菜单 MENU

print("=====签到 ver9.26=====")
try:
    init()
except Exception as any:
    print("数据库连接失败"+str(any))

#run直接控制菜单循环
run = True
#quit用于输入错误第二次后退出程序
quit = 0
while run:
    select = int(input("""1 > 今日签到 2 > 查询历史(个人) 3 > 查询历史(全局) 4 > 数据库相关 5 > 关于"""))
    if select ==1:
        Sign()
    elif select == 2:
        CheckPerson()
    elif select == 3:
        CheckAll()
    elif select == 4:
        DataBase(db)
    elif select == 5:
        About()
    else:
        print("无效输入,输入任意键关闭程序")
        quit += 1

    if quit == 2:
        run = False