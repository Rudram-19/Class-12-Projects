import mysql.connector as m
con=m.connect(host="localhost",user="root",password="123456",charset="utf8")
cur=con.cursor()
#####Introduction function
def introduction():
    print("*******************************************************************")
    print("* \t\t\t CBSE  PROJECT 2025                                            *")
    print("* \t\t\tCLASS XII                                                                 *")
    print("*                                                                                                                                  *")
    print("*  PROJECT TITLE:                             COURIER SERVICE SYSTEM                                            *")
    print("*  PROJECT TEAM:                                                                                                 *")
    print("*                                                                                                                                  *")
    print("*                                                                                                                                  *")
    print("*  SUBMITTED TO:-                                    SUBMITTED BY:-                            *")
    print("*                                                                                                                                  *")
    print("*\t                                \t              *")
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
        cur.execute("create database courier_service_system2")####change database name as per your software
    except:
        pass
    try:
        cur.execute("use courier_service_system2")####change database name as per your software
    except:
        pass
    try:
        cur.execute("create table user ( uname varchar(30) primary key, password varchar(30))")
    except:
        pass
    try:
        cur.execute("CREATE TABLE login ( user_name VARCHAR(50) PRIMARY KEY, password VARCHAR(50))")
    except:
        pass
    try:
        cur.execute('create table courier(customer_name varchar(99) ,customer_mobile_number varchar(789),customer_address text(789),receiver_name varchar(99) ,receiver_mobile_number varchar(789),receiver_address text(789))')
    except:
        pass
    try:
        cur.execute('create table couriers2(Weight_in_kgs varchar(789),Cost_in_rupees varchar(789));')
    except:
        pass
    try:
        cur.execute('create table couriers3(city varchar(99),courier_boys varchar(99),courier_service_boys_mob_number varchar(99));')
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
                print("welcome to rao man singh school")
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

###############################################################################################################################

def menu():
    c='yes'
    c=input("do you want to continue or not(yes or No):")
    while(c=='yes'):
            
        print('WELCOME TO COURIER SERVICE SYSTEM:')
        print('Hi')
        o=input('Press enter to begin your courier surfing')
        print('1.CREATE YOUR COURIER SERVICE ACCOUNT')
        print('2.LOGIN')
        print('3.EXIT')
        
        choose=int(input('ENTER (1) FOR NEW ACCOUNT OR (2) FOR LOGIN:'))
        if choose==1:
             name=input('Enter your user-name:')
             passwd=input('Set your password here:')
             passwd1=input('Confirm password:')
             cur.execute("INSERT INTO login VALUES(' "+name+" ',' "+passwd+" ')")
             con.commit()
             print('ACCOUNT CREATED CONGRATULATIONS')
             move_in=input('press enter to login:')
             for i in range(0,76):
                 print('WELCOME TO BATMAN COURIER SERVICE:')
                 print('1.Courier_order and customer_details')
                 print('2.billing_procedure')
                 print('3.courier_service_boys')
                 print('4.exit')
                 choice=int(input('enter the section you want to access:....(1,2,3or4)........:'))
                 if choice==1:
                    print('A.courier placement')
                    print('B.courier order list')
                    sect=str(input('enter the section that you want to access:'))
                    if sect=="A":
                       print('COURIER-ORDER')
                       a=(input('enter the customer name:'))
                       b=int(input('enter the customer mobile number:'))
                       c=(input('enter the customer address:'))
                       d=(input('enter the receiver name:'))
                       e=int(input('enter the receiver mobile number:'))
                       f=(input('enter the receiver address:'))
                       cur.execute("INSERT INTO couriers VALUES(' "+a+" ',"+str(b)+",' "+c+" ',' "+d+" ',"+str(e)+",' "+f+" ')")
                       con.commit()
                       print(cur.rowcount,'courier (s) placed')
                       print('===============================================================================================================')
                    elif sect=="B":
                       S=str(input('do you want to see your courier_order''(yes...\\..no):'))
                       if S=="yes":
                         a=input('enter the customer mob number:')
                         cur.execute('select * from couriers where customer_mobile_number="{}" '.format(a))
                         order=cur.fetchall()
                         print('customer name,','customer mob no,','customer address,','receiver name,','receiver mob no,','receiver address:')
                         for j in order:
                              print(j)
                         print('===============================================================================================================')
                       else:
                            print('Thank you')
                            print('==============================================================================================================')
                 elif choice==2:
                      print('BILLING PROCEDURE:[weight_in_kgs......AND.......cost_in_rupees]')
                      cur.execute("select * from couriers2")
                      bill=cur.fetchall()
                      for x in bill:
                           print(x)
                      print('===============================================================================================================')
                 if choice==3:
                      city1=input('enter your city name:')
                      cur.execute("select * from couriers3 where city='{}' ".format(city1))
                      boys=cur.fetchall()
                      print(' City                 courier_boy     mobile no:')
                      for y in boys:
                             print(y)
                      print('===============================================================================================================')
                 elif choice==4:
                            quit()
        elif choose==2:
             email=input('Enter your user_name')
             passd=input('Enter your PASSWORD:')
             cur.execute('select * from login where user_name=" '+email+' " and password=" '+passd+' " ')
             if cur.fetchone() is None:
                  print(' sorry your password in wrong')
             else:
                 for i in range(0,76):
                  print('WELCOME TO BATMAN COURIER SERVICE:')
                  print('1.Courier_order and customer_details')
                  print('2.billing_procedure')
                  print('3.courier_service_boys')
                  print('4.exit')
                  choice=int(input('enter the section you want to access:....(1,2,3or4)........:'))
                  if choice==1:
                     print('A.courier placement')
                     print('B.courier order list')
                     sect=str(input('enter the section that you want to access:'))
                     if sect=="A":
                        print('COURIER-ORDER')
                        a=(input('enter the customer name:'))
                        b=int(input('enter the customer mobile number:'))
                        c=(input('enter the customer address:'))
                        d=(input('enter the receiver name:'))
                        e=int(input('enter the receiver mobile number:'))
                        f=(input('enter the receiver address:'))
                        cur.execute("INSERT INTO couriers VALUES(' "+a+" ',"+str(b)+",' "+c+" ',' "+d+" ',"+str(e)+",' "+f+" ')")
                        con.commit()
                        print(cur.rowcount,'courier (s) placed')
                        print('===============================================================================================================')
                     elif sect=="B":
                        S=str(input('do you want to see your courier_order''(yes...\\..no):'))
                        if S=="yes":
                          a=input('enter the customer mob number:')
                          cur.execute('select * from couriers where customer_mobile_number="{}" '.format(a))
                          order=cur.fetchall()
                          print('customer name,','customer mob no,','customer address,','receiver name,','receiver mob no,','receiver address:')
                          for j in order:
                               print(j)
                          print('===============================================================================================================')
                        else:
                             print('Thank you')
                             print('==============================================================================================================')
                  elif choice==2:
                       print('BILLING PROCEDURE:[weight_in_kgs......AND.......cost_in_rupees]')
                       cur.execute("select * from couriers2")
                       bill=cur.fetchall()
                       for x in bill:
                            print(x)
                       print('===============================================================================================================')
                  if choice==3:
                       city1=input('enter your city name:')
                       cur.execute("select * from couriers3 where city='{}' ".format(city1))
                       boys=cur.fetchall()
                       print(' City                 courier_boy     mobile no:')
                       for y in boys:
                              print(y)
                       print('===============================================================================================================')
                  elif choice==4:
                      print("Exiting. Goodbye!")
                      break  
                  else:
                      print("Invalid choice, please try again.")
        elif choose==3:
            print("Bye...................")
            break
        else:
            print("Invalid choice, please try again.")


                        


###############################################################################################################################

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
        

                
