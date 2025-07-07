import mysql.connector as m
import random
import datetime as dt

con=m.connect(host="localhost",user="root",password="123456",charset="utf8")
cur=con.cursor()
#####Introduction function
def introduction():
    print("***********************")
    print("* \t\t\t CBSE  PROJECT 2025                                            *")
    print("* \t\t\tCLASS XII                                                                 *")
    print("*                                                                                                                                  *")
    print("*  PROJECT TITLE:                                                                                                *")
    print("*  PROJECT TEAM:   ELECTRICITY BILLING SYSTEM                                                                     *")
    print("*                                                                                                                                  *")
    print("*                                                                                                                                  *")
    print("*  SUBMITTED TO:-                                    SUBMITTED BY:-                            *")
    print("*                                                                                                                                  *")
    print("*\tMRS.                                \t              *")
    print("*\tINTERNAL EXAMINER                        \tCBSE ROLL NO       *")
    print("*                                                                                                                                  *")
    print("*                                                                                                                                  *")
    print("*PRESS ANY KEY TO CONTINUE:-                                                                    *")
        
    print("***********************")
    input()
    print("***********************")
    print("*                           WELCOME TO SOFTWARE NAME                                        *")
    print("*                            PRESS ANY KEY TO CONTINUE                                           *")
    print("***********************")
    input()

def database():
    try:
        cur.execute("create database EBS")####change database name as per your software
    except:
        pass
    cur.execute("use EBS")####change database name as per your software
    try:
        cur.execute("create table USER ( uname varchar(30) primary key, password varchar(30))")
        
    except:
        pass
    try:
        cur.execute('create table AddNewCustomer(accountno int primary key,bankname VARCHAR(25),bankbranch VARCHAR(25),name VARCHAR(25),address VARCHAR(100),areacode INT(6),phoneno INT(15),email VARCHAR(25),boxid VARCHAR(25))')
    except:
        pass
    try:
        cur.execute('create table Transaction(accountno INT(10) ,unit INT(10),toda VARCHAR(25),totamt INT(10),GST INT(10),totalamt INT(10),p VARCHAR(25) , foreign key(accountno) references AddNewCustomer(accountno))')          
    except:
        pass
    
     #   add all create table statement here

database()# call statement

def login():
    print("***********************")
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
    print("***********************")

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
    print("***********************")
    u=input("enter username")
    try:
        cur.execute("select * from user where uname='{}'".format(u))
        x=cur.fetchone()
    except:
        print("error")
    if x==None:
         print("user not exist")
    else:
         print(x)
         cur.execute("delete from  user where uname='{}'".format(u))
         print("user deleted")
         con.commit()
         print("***********************")

def changepassword():
        username=input("Enter your username number :")
        password=input("Enter your password:")
        confirmpasswd=input("Confirm  your password:")
        if password==confirmpasswd:
            info1="insert into newuser values('{}','{}','{}')".format(username,password,confirmpasswd)
            cur.execute(info1)
            con.commit()
            c=input("do you want to continue?(yes or no)")
        else:
            print('your confirm password is incorrect')
            print('Try again')
            c=input("do you want to continue?(yes or no)")
def addnewcustomer():
    accountno=random.randrange(1000000,9999999,10)
    print("your accountno is",accountno)
    boxid=input("enter your mete box ID:")
    bankname=input('Enter your BANK NAME  :')
    bankbranch=input('Enter your BANK BRANCH  :')
    name=input('Enter your name  :')
    address=input('Enter your address  :')
    areacode=int(input('Enter your area PIN CODE  :'))
    phoneno=int(input('Enter your PHONE NUMBER  :'))
    email=input('Enter your email  :')
    info2="insert into AddNewCustomer values({},'{}','{}','{}','{}',{},{},'{}','{}')".format(accountno,bankname,bankbranch,name,address,areacode,phoneno,email,boxid)
    cur.execute(info2)
    con.commit()
def delaccount():
    acc=input("ENTER YOUR ACCOUNT NUMBER:")
    use=input("ENTER YOUR USERNAME:")
    info6=cur.execute("delete from Transaction where accountno='{}'".format(acc))
    info7=cur.execute("delete from AddNewCustomer where accountno='{}'".format(acc))
    info8=cur.execute("delete from newuser where username='{}'".format(use))
    cur.execute(info6)
    cur.execute(info7)
    cur.execute(info8)
    con.commit()
############################################################3
            ############################################################3

##############################################            
introduction()
while True:
    print("*********")          
    print("*1 Login                                     *")
    print("*2:New user                               *")
    print("*3:Remove User                        *")
    print("*4:Change Password                *")
    print("*5:Exit                                       *")
    print("*********")          
    try:
        print("* Enter your choice                   \n",end="")
        ch=int(input())
    except:
        print("*   Enter digit only                    *")
        continue
    V="yes"
    if ch==1:
        if login():
            while V=='YES' or "yes" or 'Yes':
                
                    print('*********WELCOME TO ELECTRICITY BILLING SYSTEM*********')
                    print("1.ACCOUNT SETTINGS")
                    print("2.TRANSACTION")
                    print("3.VIEW CUSTOMER DETAILS")
                    print("4.GRAPHICAL REPRESENTATION")
                    print('5.EXIT')
                    choice2=int(input('ENTER YOUR CHOICE'))
                    if choice2==1:
                        print('1.NEW CUSTOMER')
                        print('2.DELETE EXISTING ACCOUNT')
                        choice12=int(input('ENTER YOUR CHOICE:'))
                        if choice12==1:
                            accountno=random.randrange(1000000,9999999,10)
                            print("your accountno is",accountno)
                            boxid=input("enter your mete box ID:")
                            bankname=input('Enter your BANK NAME  :')
                            bankbranch=input('Enter your BANK BRANCH  :')
                            name=input('Enter your name  :')
                            address=input('Enter your address  :')
                            areacode=int(input('Enter your area PIN CODE  :'))
                            phoneno=int(input('Enter your PHONE NUMBER  :'))
                            email=input('Enter your email  :')
                            info2="insert into AddNewCustomer values({},'{}','{}','{}','{}',{},{},'{}','{}')".format(accountno,bankname,bankbranch,name,address,areacode,phoneno,email,boxid)
                            cur.execute(info2)
                            con.commit()
                            V=input("do you want to continue?(yes or no)")
                            if V=='yes':
                                continue
                            else:
                                break
                        elif choice12==2:
                            acc=input("ENTER YOUR ACCOUNT NUMBER:")
                            use=input("ENTER YOUR USERNAME:")
                            info6=cur.execute("delete from Transaction where accountno='{}'".format(acc))
                            info7=cur.execute("delete from AddNewCustomer where accountno='{}'".format(acc))
                            info8=cur.execute("delete from newuser where username='{}'".format(use))
                            cur.execute(info6)
                            cur.execute(info7)
                            cur.execute(info8)
                            con.commit()
                            print("THANK YOU FOR USING OUR SOFTWARE,YOUR ACCOUNT IS SUCCESFULLY DELETED")
                            V=input("do you want to continue?(yes or no)")
                            if V=='yes':
                                continue
                            else:
                                break

                    elif choice2==2:
                        accountno=int(input('Enter your account number  :'))
                        info10="select * from Transaction where accountno="+str(accountno)
                        cur.execute(info10)
                        data3=cur.fetchall()
                        if len(data3)!=0:
                            for row in data3:
                                paid=row[6]
                                if paid=='yes':
                                    print('you have already paid the bill')
                                    break
                                else:
                                    unit=random.randint(0,101)
                                    print('Dear customer, you have used ',unit,'units of electricity.')
                                    print('One unit of curent is 150 ruppees')
                                    amount=150*unit
                                    toda=dt.date.today()
                                    deadline=dt.date(2020,1,30)
                                    if deadline<toda:
                                        fine=(toda-deadline)*30
                                        totamt=amount+fine
                                        print('you have dealyed for ',toda-deadline,'days.The fine per day is 30 rupees.')
                                        GST=(15/100)*totamt
                                        totalamt=totamt+GST
                                        print('Pleae payup ',totalamt,'rupees inclding GST')
                                        p=input("Please Enter YES to transact")
                                        if p=="YES"or 'Yes'or'yes':
                                            print("Transaction successful")
                                            print("You have paid the bill")
                                        else:
                                            print('plz pay the bill sooner')
                                    else:
                                        totamt=0
                                        GST=(15/100)*amount
                                        totalamt=amount+GST
                                        print('Pleae payup ',totalamt,'rupees inclding GST')
                                        p=input("Please Enter YES to transact")
                                        if p=="YES":
                                            print("Transaction successful")
                                            print("You have paid the bill")
                                        else:
                                            print('plz pay the bill sooner')
                                info3="insert into Transaction values({},{},'{}',{},{},{},'{}')".format(accountno,unit,toda,totamt,GST,totalamt,p)
                                cur.execute(info3)
                                con.commit()
                                V=input("do you want to continue?(yes or no)")
                                if V=='yes':
                                    continue
                                else:
                                    break
                            else:
                                pass
                    elif choice2==2:
                        accountno=int(input('Enter your account number  :'))
                        info10="select * from Transaction where accountno="+str(accountno)
                        cur.execute(info10)
                        data3=cur.fetchall()
                        print(data3)
                        if data3!=[]:
                            print(data3)
                            for row in data3:
                                print(row)
                                paid=row[6]
                            if paid=='yes':
                                print('you have already paid the bill')
                                break
                            else:
                                unit=random.randint(0,101)
                                print('Dear customer, you have used ',unit,'units of electricity.')
                                print('One unit of curent is 150 ruppees')
                                amount=150*unit
                                toda=dt.date.today()
                                deadline=dt.date(2020,1,30)
                                if deadline<toda:
                                    fine=(toda-deadline)*30
                                    totamt=amount+fine
                                    print('you have dealyed for ',toda-deadline,'days.The fine per day is 30 rupees.')
                                    GST=(15/100)*totamt
                                    totalamt=totamt+GST
                                    print('Pleae payup ',totalamt,'rupees inclding GST')
                                    p=input("Please Enter YES to transact")
                                    if p=="YES"or 'Yes'or'yes':
                                        print("Transaction successful")
                                        print("You have paid the bill")
                                    else:
                                        print('plz pay the bill sooner')
                                else:
                                    totamt=0
                                    GST=(15/100)*amount
                                    totalamt=amount+GST
                                    print('Pleae payup ',totalamt,'rupees inclding GST')
                                    p=input("Please Enter YES to transact")
                                    if p=="YES":
                                        print("Transaction successful")
                                        print("You have paid the bill")
                                    else:
                                        print('plz pay the bill sooner')
                                info3="insert into Transaction values({},{},'{}',{},{},{},'{}')".format(accountno,unit,toda,totamt,GST,totalamt,p)
                                cur.execute(info3)
                                con.commit()
                        else:
                                pass
                        V=input("do you want to continue?(yes or no)")
                        if V=='yes':
                                continue
                        else:
                                break

                    elif choice2==3:
            
                        accountno=int(input('Enter your account number  :'))
                        info4="select * from AddNewCustomer where accountno=" + str(accountno)
                        cur.execute(info4)
                        data1=cur.fetchall()
                        for row in data1:
                            print(" Account Number: ", row[0])
                            print("bankname:",row[1])
                            print("bankbranch:",row[2])
                            print("Person name:",row[3])
                            print("Your meter device ID=",row[8])
                            print("Residential address:",row[4])
                            print("area code:",row[5])
                            print("phone number:",row[6])
                            print("email:",row[7])
                            info5="select * from Transaction where accountno=" + str(accountno)
                            cur.execute(info5)
                            data2=cur.fetchall()
                        for row in data2:
                
                            print(" Unit : ",row[1])
                            print(" paid on:",row[2])
                            print("amount to be paid without GST:",row[3])
                            print("GST=",row[4])
                            print("amount to be paid including GST:",row[5])
                        V=input("do you want to continue?(yes or no)")
                        if V=='yes':
                            continue
                        else:
                            break

                    elif choice2==4:
                        info9="select accountno,totalamt from Transaction"
                        cur.execute(info9)
                        L1,L2,=[],[]
                        for i in cur.fetchall():
                            L1.append(i[0])
                            L2.append(i[1])
                        plt.plot(L1,L2)
                        plt.title("GRAPH")
                        plt.show()
                        V=input("do you want to continue?(yes or no)")
                        if V=='yes':
                            continue
                        else:
                            break

                    elif choice2==5:
                        print(                                  "THANK  YOU!!!!  VISIT AGAIN!!!!")
                        break
                        c='yes'

            
        #     add software code option menu
    elif ch==2:
            u=input("enter username")
            cur.execute("select * from user where uname='{}'".format(u))
            x=cur.fetchone()
            if x==None:
                 p=input("password")
                 cur.execute("insert into user values('{}','{}')".format(u,p))
            else:
                print("user exist")

    elif ch==3:
            print("***********************")
            u=input("enter username")
            cur.execute("select * from user where uname='{}'".format(u))
            x=cur.fetchone()
            if x==None:
                 print("user not exist")
            else:
                 cur.execute("delete from  user where uname='{}'".format(u))
                 print("user deleted")
                 print("***********************")

    elif ch==4:
            username=input("Enter your username number :")
            password=input("Enter your password:")
            confirmpasswd=input("Confirm  your password:")
            if password==confirmpasswd:
                info1="insert into newuser values('{}','{}','{}')".format(username,password,confirmpasswd)
                cur.execute(info1)
                con.commit()
                c=input("do you want to continue?(yes or no)")
            else:
                print('your confirm password is incorrect')
                print('Try again')
                c=input("do you want to continue?(yes or no)")
                
    elif ch==5:
            print("Bye...................")
            break
    else:
            print("Enter choice 1-5 only")
