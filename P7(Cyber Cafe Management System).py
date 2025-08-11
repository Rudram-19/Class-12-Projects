import mysql.connector as m
con=m.connect(host="localhost",user="root",password="123456",charset="utf8")
cur=con.cursor()
#####Introduction function
def introduction():
    print("*******************************************************************")
    print("* \t\t\t CBSE  PROJECT 2025                                            *")
    print("* \t\t\tCLASS XII                                                                 *")
    print("*                                                                                                                                  *")
    print("*  PROJECT TITLE:                                                                                                *")
    print("*  PROJECT TEAM:                                                                                                 *")
    print("*                                                                                                                                  *")
    print("*                                                                                                                                  *")
    print("*  SUBMITTED TO:-                                    SUBMITTED BY:-                            *")
    print("*                                                                                                                                  *")
    print("*\t                                \t             *")
    print("*\tINTERNAL EXAMINER                        \tCBSE ROLL NO       *")
    print("*                                                                                                                                  *")
    print("*                                                                                                                                  *")
    print("*PRESS ANY KEY TO CONTINUE:-                                                                    *")
        
    print("*******************************************************************")
    input()
    print("*******************************************************************")
    print("*                           WELCOME TO SOFTWARE NAME                                        *")
    print("*                            PRESS ANY KEY TO CONTINUE                                           *")
    print("*******************************************************************")
    input()

def database():
    try:
        cur.execute("create database ccms")####change database name as per your software
    except:
        pass
    cur.execute("use ccms")####change database name as per your software
    try:
        cur.execute("create table user ( uname varchar(30) primary key, password varchar(30))")
    except:
        pass
    try:
        cur.execute('create table Add_new_customer(Customer_name varchar(20),Age int,Address varchar(100),Phone_no int(10),Email_ID varchar(30))')
    except:
        pass
    try:
        cur.execute('create table Bill(Customer_name varchar(20),Time_accessed_in_min int,Total_charges int)')
    except:
        pass
    try:
        cur.execute('create table Time_charges(Time varchar(30),Amount_charged int)')
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
                print("Welcome to CYBER CAFE MANAGEMENT SYSTEM")
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
            
##############################################################################################################################

def details():
    name=input("Enter your name :")
    age=int(input("Enter your age :"))
    address=input("Enter your residential address :")
    phone_no=int(input("Enter your phone number :"))
    email_id=input("Enter your Email ID :")
    ty="insert into Add_new_customer values('{}',{},'{}',{},'{}')".format(name,age,address,phone_no,email_id)
    cur.execute(ty)
    con.commit()    
    print("                                                THANK YOU VISIT AGAIN               ")
def charges():
    time=input("Enter the time :") 
    amount=int(input("Enter the amount :"))
    ss="insert into Time_charges values('{}',{})".format(time,amount)
    cur.execute(ss)
    con.commit()
    print("                                                THANK YOU VISIT AGAIN               ")
def em_bill():
    name=input("Enter your name :")
    time=int(input("Enter the time you accessed cyber cafe in minutes :"))
    total=time*30
    qw="insert into Bill values('{}',{},{})".format(name,time,total)
    cur.execute(qw)
    con.commit()
    print("Please pay Rs.",total)
    print("Type YES to pay your bill or NO to pay it later")
    b=input("Type YES or NO:")
    if b=="YES":
        print("Bill paid successfully")
        print("                                            THANK YOU VISIT AGAIN               ")
    else:
        print("Bill not paid,pay the bill to leave the place")
def em_list():
    phone_no=input("Enter the phone number of the customer you want to search :")
    ea="select * from Add_new_customer where Phone_no=" + str(phone_no)
    cur.execute(ea)
    data=cur.fetchall()
    for row in data:
        print("Name:",row[0])
        print("Age:",row[1])
        print("Address:",row[2])
        print("Phone number:",row[3])
        print("Email ID",row[4])
    print("                                                THANK YOU VISIT AGAIN               ")

    
def menu():
    c='yes'
    c=input("do you want to continue or not(yes or No):")
    while(c=='yes'):
        print("                             ****************AMARAVIAN CYBER CAFE WELCOMES YOU****************        ")
        print("                                               CYBER CAFE MANAGEMENT SYSTEM            ")
        print("1.Customer details")
        print("2.Time Charges")
        print("3.Bill")
        print("4.Customers detail view")
        print("5.Quit")
        choice=int(input("Enter your choice :"))

        if choice==1:
            details()
        elif choice==2:
            charges()
        elif choice==3:
            em_bill()
        elif choice==4:
            em_list()
        else:
            print ("exit")
            break
    else : print("Thank You")
        
##############################################################################################################################

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
        #     add software code option menu
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
        

                
            
