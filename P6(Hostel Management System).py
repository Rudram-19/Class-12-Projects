import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",password="123456",charset="utf8")
conn.autocommit=True
c1=conn.cursor()
#####Introduction function
def introduction():
    print('''*************************************************************************************
* 			 CBSE PROJECT 2025                                                   *
* 			CLASS XII                                                                         *
*                                                                                                                                            *
*  PROJECT TITLE:   HOSTEL MANAGEMENT SYSTEM                                              *
*  PROJECT TEAM:                                                                                                            *
*                                                                                                                                            *
*                                                                                                                                            *
*  SUBMITTED TO: -                                    SUBMITTED BY: -                                        *
*                                                                                                                                            *
*	                                	                                          *
*	INTERNAL EXAMINER                        	CBSE ROLL NO                             *
*                                                                                                                                             *
*                                                                                                                                             *
*PRESS ANY KEY TO CONTINUE: -                                                                                  *
************************************************************************************************''')
    input()

introduction()
def database():
    try:
        c1.execute("create database hostel_management")
    except:
        pass
    c1.execute("use hostel_management")
    try:
        c1.execute("create table fees(department varchar(25) primary key,fees int)")
    except:
        pass
    try :
        c1.execute("create table hostel_management(roll_no int primary key,name varchar(20),address varchar(100),room_no int,dept varchar(15),fees int,bal int)")
    except:
        pass

    
database()# call statement


def new_department():
    try:
            v_department=input("Enter your department :- ")
            v_fees=int(input("Enter your fee :- ") )
            try :
                c1.execute("insert into fees values ('{}',{})".format(v_department,v_fees))
                conn.commit()
            except:
                print('Please do not repeat departments')
            except:
                print('Invalid parameters please enter valid entries')
                print()
    



    
def admission_form():
    try:
        v_roll=int(input("Enter YOUR ROLL NUMBER :- "))
        v_name=input("Enter YOUR NAME :- ")                    
        v_add=input("Enter YOUR ADDRESS")
        v_room_no=int(input("Enter YOUR ROOM NUMBER :- "))
        v_dept=input("Enter YOUR DEPARTMENT :- ")
        v_fees=int(input("Enter YOUR FEES :- "))
        v_bal=int(input("Enter YOUR BALANCE :- "))
        try:
            c1.execute("insert into hostel_management values ({},'{}','{}',{},'{}',{},{})".format(v_roll,v_name,v_add,v_room_no,v_dept,v_fees,v_bal))
            conn.commit()
        except:
            print('Please do not repeat roll no')
            
    except:
        print('Invalid parameters please enter valid entries')
    

#######################
def modify_data():
    try:
        roll_no=int(input("Enter your roll number"))
        try:
            c1.execute("select*from hostel_management where roll_no={}".format(roll_no))
            data=c1.fetchall()
        except:
            
    print("roll_no:",data[0][0])
    print("name:",data[0][1])
    print("address:",data[0][2])           
    print("room_no:",data[0][3])
    print("dept:",data[0][4])
    print("fees:",data[0][5])           
    print("bal:",data[0][6])


########################
def fee_checking():
    try:
        print("AVAILABLE DEPARTMENTS AS FOLLOWS")
        print("1.COMPUTER")
        print("2.BIO")
        print("3.TECH")
        print("4.PHYSICS")
        print("5.ECO")
        print("6.ENG")
        department=input("Enter YOUR DEPARTMENT")
        try:
            c1.execute("select*from fees where department='{}'".format(department))
            data=c1.fetchall()
        except:
            print('Department does not exists')
            c=input('Enter 1 to add new department')
            if c==1:
                new_department()
                c1.execute("select*from fees where department='{}'".format(department))
                data=c1.fetchall()
        print("your fees is:",data[0][1])

while True:
    print(" \t\t\t WELCOME TO  HOSTEL MANAGEMENT \n\n\n")

    print(" 1.ADMISSION FORM")

    print(" 2.FEE CHECKING")

    print(" 3.MODIFY DATA")

    print(" 4.AUTHORITIES ONLY")

    print(" 5.QUIT")
    choice=int(input('Enter YOUR CHOICE'))

    if choice==1:
        admission_form()
######################################################
    elif choice==2:
        fee_checking()

######################################################

    elif choice==4:
        modify_data()

######################################################
    elif choice==4:
        print( "SORRY,YOU ARE NOT AUTHORIZED TO USE THIS SITE  ")                       

    else:
         print("QUITTING!!!!!!!!!")
