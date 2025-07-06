import mysql.connector as m
con=m.connect(host="localhost",user="root",password="123456",charset="utf8")
cur=con.cursor()
#####Introduction function
def introduction():
    print("*******************************************************************")
    print("* \t\t\t CBSE  PROJECT 2025                                            *")
    print("* \t\t\tCLASS XII                                                                 *")
    print("*                                                                                                                                  *")
    print("*  PROJECT TITLE:      MARRIAGE BUREAU MANAGEMENT                                                                                          *")
    print("*                                                                                                                                  *")
    print("*                                                                                                                                  *")
    print("*  SUBMITTED TO:-                                    SUBMITTED BY:-                            *")
    print("*                                                                                                                                  *")
    print("*\Teacher Name                                \t Student Name             *")
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
        cur.execute("create database marriage_bureaw_management")####change database name as per your software
    except:
        pass
    cur.execute("use marriage_bureaw_management")####change database name as per your software
    try:
        cur.execute("create table user ( uname varchar(30) primary key, password varchar(30))")
    except:
        pass
    try:
        cur.execute('create table legends_details(name varchar (200),address varchar(20),caste varchar (100),appearence varchar(100),age bigint(55),profession varchar (255),phone_no  bigint(200)')
    except:
        pass
    try:
        cur.execute('create girls_details(name varchar(100),address varchar(100),caste varchar(50),appearence varchar(25),age int(4),profession varchar(65),phone_no varchar(15)')
    except:
        pass
    try:
        cur.execute('create table user_id(user_name varchar(55),password varchar(55)')
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
                print("Welcome to MARRIAGE BUREAW MANAGEMENT")
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



def register():
     name=input('Enter your  User name:')
     passwd=int(input('Enter  your  Password(only numbers):'))
     print()
     V_SQLInsert="INSERT  INTO user_id (password,user_name) values (" +  str (passwd) + ",' " + name + " ') "
     cur.execute(V_SQLInsert)
     con.commit()
     print()
     print('USER created succesfully')

def existuser() :
     name=input('Enter your Username=')
     print()
     passwd=int(input('Enter your  Password='))
     V_Sql_Sel="select * from user_id where password='"+str (passwd)+"' and user_name=  ' " +name+ " ' "
     cur.execute(V_Sql_Sel)
     if cur.fetchone() is  None:
          print()
          print('Invalid username or password')
     else:
          print()

def male():
     a=(input('enter the name:'))
     b=(input('enter the address:'))
     c=(input('enter the caste:'))
     d=(input('enter the appreance:'))
     e=(input('enter the age:'))
     f=(input('enter the profession:'))
     g=(input('enter the phone_no:'))
     cur=con.cursor()
     sql_insert="insert into legends_details values( '{}','{}','{}','{}','{}','{}','{}')".format(a,b,c,d,e,f,g)
     cur.execute(sql_insert)
     con.commit()
     print ('Data inserted')
     c=input('do you want to continue (y/[n]:)')

def female():
     h=(input('enter the name:'))
     i=(input('enter the address:'))
     j=(input('enter the caste:'))
     k=(input('enter the appreance:'))
     l=(input('enter the age:'))
     m=(input('enter the profession:'))
     n=(input('enter the phone_no:'))
     cur=con.cursor()
     sql_insert="insert into girls_details values( '{}','{}','{}','{}','{}','{}','{}')".format(h,i,j,k,l,m,n)
     cur.execute(sql_insert) 
     con.commit()
     print("Details are successfully inserted")


def Bride():
     prof=(input('Enter the profession:'))
     cur.execute("select* from legends_details where profession='{}'". format(prof))
     data= cur.fetchall()
     print("name\t\t address\t\t caste\t\t  appreance\t\t  age\t\t  profession\t\t phone_no \t\t ")
     for i in data:
         print (data [0][0],'\t\t',data[0][1],'\t\t',data[0][2],'\t\t',data [0][3],'\t\t',data[0][4],'\t\t',data[0][5],'\t\t',data[0][6],'\t\t')
         c=input('do you want to continue (y/[n]:)')
         if c =='y' :
             continue
         else:
                 print('THANK  YOU  FOR  VISITING  OUR   WEBSITE' )
                 print('VISIT  AGAIN')

def Groom():
     appearance=(input('Enter the appearence:'))
     cur.execute("select* from girls_details where appearance='{}'". format(appearance))
     data= cur.fetchall()
     print("name\t\t address\t\t caste\t\t  appeance\t\t  age\t\t  profession\t\t phone_no \t\t ")
     for i in data:
         print (data [0][0],'\t\t',data[0][1],'\t\t',data[0][2],'\t\t',data [0][3],'\t\t',data[0][4],'\t\t',data[0][5],'\t\t',data[0][6],'\t\t')
         c=input('do you want to continue (y/[n]:)')
         if c =='y' :
             continue
         else:
                 print('THANK  YOU  FOR  VISITING  OUR   WEBSITE' )
                 print('VISIT  AGAIN')

def menu():
    c='yes'
    c=input("do you want to continue or not(yes or No):")
    while(c=='yes'):
    
        print("1.Registeration")
        print("2.Login")
        print('3.Male customer details')
        print('4.Female customer details')
        print('5. Handsome Groom ')
        print('6. Beautiful Bride')
        print("exiting")
        choice=int(input("      enter the choice:          "))
        
        if choice==1:
            register()
        elif choice==2:
            existuser()
        elif choice==4:
            female()
        elif choice==3:
            male()
        elif choice==5:
            Bride()
        elif choice==6:
            Groom()
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
        

                
            
