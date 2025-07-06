import mysql.connector as m
con=m.connect(host="localhost",user="root",password="123456",charset="utf8")
cur=con.cursor()
#####Introduction function
def introduction():
    print("*******************************************************************")
    print("* \t\t\t CBSE  PROJECT 2025                                            *")
    print("* \t\t\tCLASS XII                                                                 *")
    print("*                                                                                                                                  *")
    print("*  PROJECT TITLE:   HOSTEL MANAGEMENT SYSTEM                                                                     *")
    print("*  PROJECT TEAM:                                                                                                 *")
    print("*                                                                                                                                  *")
    print("*                                                                                                                                  *")
    print("*  SUBMITTED TO:-                                    SUBMITTED BY:-                            *")
    print("*                                                                                                                                  *")
    print("*\t                               \t             *")
    print("*\tINTERNAL EXAMINER                        \tCBSE ROLL NO       *")
    print("*                                                                                                                                  *")
    print("*                                                                                                                                  *")
    print("*PRESS ANY KEY TO CONTINUE:-                                                                    *")
        
    print("*******************************************************************")
    input()
    print("*******************************************************************")
    print("*                           WELCOME TO HOSTEL MANAGEMENT SYSTEM                                        *")
    print("*                            PRESS ANY KEY TO CONTINUE                                           *")
    print("*******************************************************************")
    input()

def database():
    try:
        cur.execute("create database hostel_management")####change database name as per your software
    except:
        pass
    cur.execute("use hostel_management")####change database name as per your software
    try:
        cur.execute("create table user ( uname varchar(30) primary key, password varchar(30))")
    except:
        pass
    try:
        cur.execute("create table fees(department int primary key,fees int)")
    except:
        pass
    try:
        cur.execute("create table hostel_management(roll_no int primary key,name varchar(20),address varchar(100),room_no int,dept varchar(15),fees int,bal int")
    except:
        pass
        
     #   add all create table statement here

database()# call statement

def login():
    print("*******************************************************************")
    for i in range(3):
        u=input("enter username")
        cur.execute("select * from user where uname='{}'".format(u))
        x=cur.fetchone()
        if x==None:
            print("invalid user")
        else:
            p=input("password")
            if x[1]==p:
                print("welcome to  HOSTEL")
                return True
            else:
                print("invalid password")
    else:
        print("try later")
    print("*******************************************************************")        
    return False
def newuser():
    u=input("enter username")
    cur.execute("select * from user where uname='{}'".format(u))
    x=cur.fetchone()
    if x==None:
         p=input("password")
         cur.execute("insert into user values('{}','{}')".format(u,p))
    else:
        print("user exist")

def removeuser():
    print("*******************************************************************")
    u=input("enter username")
    cur.execute("select * from user where uname='{}'".format(u))
    x=cur.fetchone()
    if x==None:
         print("user not exist")
    else:
         cur.execute("delete from  user where uname='{}'".format(u))
         print("user deleted")
         print("*******************************************************************")

def changepassword():
    print("***************************")
    u=input("Enter Username")
    cur.execute("select * from user where uname='{}'".format(u))
    x=cur.fetchone()
    if x==None:
       print("User not exist")
         
    else:
        p=input("Enter present password")
        if p==x[1]:
            p=input("New password")
            cur.execute("update user set password='{}' where uname='{}'".format(p,u))
            print("Password changed")

#######################################################################################

def admform():
    v_roll=input("ENTER YOUR ROLL NUMBER")
    v_name=input("ENTER YOUR NAME")                    
    v_add=input("ENTER YOUR ADDRESS")
    v_room_no=input("ENTER YOUR ROOM NUMBER")
    v_dept=input("ENTER YOUR DEPARTMENT")
    v_fees=input("ENTER YOUR FEES")
    v_bal=input("ENTER YOUR BALANCE")
    
    abc=("insert into hostel_management values ("+v_roll+",'"+v_name+"','"+v_add+"',"+v_room_no+",'"+v_dept+"',"+v_fees+","+v_bal+")")
    print(abc)
    cur.execute(abc)
    con.commit()

def feecheck():
    
    # Assuming data is fetched from a database
    data = fetch_data_from_database()  # Replace with actual data-fetching code
    if data and len(data) > 0 and len(data[0]) > 1:
        print("Your fees is:", data[0][1])
    else:
        print("No fees data available.")


def modify():
    roll_no=int(input("enter your roll number"))
    mysql="select*from hostel_management where roll_no={}".format(roll_no)
    cur.execute(mysql)
    data=cur.fetchall()
    print("roll_no:",data[0][0])
    print("name:",data[0][1])
    print("address:",data[0][2])           
    print("room_no:",data[0][3])
    print("dept:",data[0][4])
    print("fees:",data[0][5])           
    print("bal:",data[0][6])

def authority():
    print( "SORRY,YOU ARE NOT AUTHORIZED TO USE THIS SITE  ")

def menu():
    c='yes'
    c=input("do you want to continue or not(yes or No):")
    while(c=='yes'):
    
        print("1.employee registeration")
        print("2.employee details")
        print("3.update salary")
        print("4.employees list")
        print("exiting")
        choice=int(input("      enter the choice:          "))
        
        if choice==1:
            admform()
        elif choice==2:
            feecheck()
        elif choice==3:
            modify()
        elif choice==4:
            authority()
        else:
            print ("exit")
            break
    else : print("Thank You")



#######################################################################################
#     add software code option menu

import time
print ("\t\t\t",time.ctime())


introduction()
while True:
    print("***************************")          
    print("*1 Login                                     *")
    print("*2:New user                               *")
    print("*3:Remove User                        *")
    print("*4:Change Password                *")
    print("*5:Exit                                       *")
    print("***************************")          
    try:
        print("* Enter your choice                   *\n*",end="")
        ch=int(input())
    except:
        print("*   Enter digit only                    *")
        continue
    if ch==1:
        if login():
            menu()
    elif ch==2:
        newuser()
    elif ch==3:
        removeuser()
    elif ch==4:
        changepassword()
    elif ch==5:
        print("Bye...................")
        break
    else:
        print("Enter choice 1-5 only")
        

                
            
