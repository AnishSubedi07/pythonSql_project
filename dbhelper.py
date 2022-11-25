import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port = '3306',
                                     user='root',
                                     password='123456789',
                                     database = 'maindb')
        query = 'create table if not exists user(userId int primary key,userName varchar(200),address varchar(150),age varchar(4),phone varchar(12),position varchar(50))'
        cur = self.con.cursor()
        cur.execute(query)
        print()
        
    #Insert
    def insert_user(self,userid,username,address,age,phone,position):
        query="insert into user(userId,userName,address,age,phone,position) values({},'{}','{}','{}','{}','{}')".format(userid,username,address,age,phone,position)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print()
        print("Data is Saved")
 
    #Fetch All
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Employee Id : ",row[0])
            print("Employee Name : ",row[1])
            print("Address : ",row[2])
            print("Age : ",row[3])
            print("Phone : ",row[4])
            print("Position : ",row[5])
            print()
    
    #Fetch Single data
    def fetch_id(self,userId):
        query = "select * from user where userid= {}".format(userId)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Employee Id : ",row[0])
            print("Employee Name : ",row[1])
            print("Address : ",row[2])
            print("Age : ",row[3])
            print("Phone : ",row[4])
            print("Position : ",row[5])
            print()
     
    #Delete User  
    def delete_user(self,userId):
        query="Delete from user where userId= {}".format(userId)
        cur =self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print()
        print("Data is Deleted")
        
    #Update
    def update_user(self,userId,newName,newAddress,newAge,newPhone,newPosition):
        query="Update user set userName='{}',address='{}',age='{}',phone='{}',position='{}' where userId={}".format(newName,newAddress,newAge,newPhone,newPosition,userId)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print()
        print("Data is Updated")    
    