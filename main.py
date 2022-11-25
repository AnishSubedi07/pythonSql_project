from dbhelper import DBHelper

def main():
    db=DBHelper()
    while True:
        print()
        print("****Employee Data Management System****")
        print()
        print("Press 1 to Insert New Data")
        print("Press 2 to Display all Data")
        print("Press 3 to Display a Data")
        print("Press 4 to Delete a Data")
        print("Press 5 to Update a Data")
        print("Press 6 to Exit")
        print()
        try:
            choice=int(input())
            if(choice==1):
                #insert user
                uid=int(input("Enter Employee ID: "))
                username=input("Enter Employee Name: ")
                useraddress=input("Enter Address: ")
                userage=input("Enter Age: ")
                userphone=input("Enter Phone: ")
                userposition=input("Enter Position: ")
                db.insert_user(uid,username,useraddress,userage,userphone,userposition)
            elif choice==2:
                #display all user
                db.fetch_all()
            elif choice==3:
                #display a user
                userID=int(input("Enter Employee Id which you want to Display: "))
                print()
                db.fetch_id(userID)
            elif choice==4:
                #delete user
                userid=int(input("Enter Employee Id which you want to Delete: "))
                db.delete_user(userid)
            elif choice==5:
                #update user
                uid=int(input("Enter Employee ID: "))
                username=input("Enter New Employee Name: ")
                useraddress=input("Enter New Address: ")
                userage=input("Enter New Age: ")
                userphone=input("Enter New Phone: ")
                userposition=input("Enter New Position: ")
                db.update_user(uid,username,useraddress,userage,userphone,userposition)
            elif choice==6:
                #exit
                break
            else:
                print("Invalid Input!, Please Try Again")
        except Exception as e:
            print(e)
            print("Invalid Details!, Try Again")
            
if __name__ == "__main__":
    main()
