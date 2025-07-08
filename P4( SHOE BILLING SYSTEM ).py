import mysql.connector as m
con=m.connect(host="localhost",user="root",password="123456",charset="utf8")
cur=con.cursor()
#####Introduction function
def introduction():
    print("*********************************************************************************")
    print("********************       CBSE  PROJECT 2025   *********************************")
    print("********************       CLASS XII            *********************************")
    print("*********************************************************************************")
    print()
    print("*********************************************************************************")                                                                                                                           
    print("*****                 PROJECT TOPIC :-  SHOE BILLING SYSTEM                 *****")
    print("*********************************************************************************")
    print()
    print()
    print("**  SUBMITTED TO:-                                    SUBMITTED BY:-           **")
    print()                                                                                                                                  
    print("**                                                                                         **")
    print("**INTERNAL EXAMINER                                   CBSE ROLL NO             **")
    print("*********************************************************************************")
    print()
    print("***             -------PRESS ANY KEY TO CONTINUE:-  ------                    ***")
    input()    
    print()
    print("*********************************************************************************")
    print("***         --------WELCOME TO SHOE BILLING SYSTEM -----                      ***")
    print("***         --------PRESS ANY KEY TO CONTINUE------                           ***")
    input()
    print("***         -------TELL ME WHAT CAN I DO FOR YOU------                        ***")

    
def shoe_billing():
    try:
        cur.execute("create database shoe_billing")####change database name as per your software
    except:
        pass
    cur.execute("use shoe_billing")####change database name as per your software
    try:
        cur.execute("create table user ( uname varchar(30) primary key , password varchar(30))")
    except:
        pass
    try:
        cur.execute('''CREATE TABLE shoe_details (
                    shoe_code NUMERIC(10) PRIMARY KEY,
                    brand_name VARCHAR(25),
                    customer_name VARCHAR(25),
                    customer_number NUMERIC(10),
                    customer_address VARCHAR(25),
                    amount NUMERIC(10)
                    )''')

    except:
        pass
    try:
        cur.execute("""ALTER TABLE shoe_details ADD COLUMN brand_name VARCHAR(255);""")
    except:
        pass
    try:
        cur.execute("""ALTER TABLE shoe_details ADD COLUMN customer_name VARCHAR(255);""")
    except:
        pass
    try:
        cur.execute("""ALTER TABLE shoe_details ADD COLUMN customer_number VARCHAR(255);""")
    except:
        pass
    try:
        cur.execute("""ALTER TABLE shoe_details ADD COLUMN customer_address VARCHAR(255);""")
    except:
        pass
    try:
        cur.execute("""ALTER TABLE shoe_details ADD COLUMN amount VARCHAR(255);""")
    except:
        pass
    

     #   add all create table statement
shoe_billing()# call statement


def login():
    print("*")
    for i in range(3):
        u=input("enter username")
        cur.execute("select * from user where uname='{}'".format(u))
        x=cur.fetchone()
        if x==None:
            print("opps!!....invalid user")
        else:
            p=input("enter your password")
            if x[1]==p:
                print("****           -----WELCOME TO SHOE BILLING SYSTEM-----          ****")
                break
            else:
                print("invalid password")
    else:
        print("try later")
        
 
def newuser():
    u=input("enter username")
    cur.execute("select * from user where uname='{}'".format(u))
    x=cur.fetchone()
    if x==None:
        p=input("password")
        cur.execute("insert into user values('{}','{}')".format(u,p))
    else:
        print("user already  exist")
        

def removeuser():
    print("*")
    u=input("enter username")
    cur.execute("select * from user where uname='{}'".format(u))
    x=cur.fetchone()
    if x==None:
        print("user not exist")
    else:
        cur.execute("delete from  user where uname='{}'".format(u))
        print("user deleted")
        print("*")

        
def changepassword():
    print("*")
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
        else:
            print("enter correct password")

            
def checkint(s,l):
    try:
        x=int(input(s))
        if len(str(x))<=l:
            return x
        else:
            print("you can enter a length of",l,"only")
    except:
        print("please enter digit only")
        

def checkstring(s,l):
    x=input(s)
    if len(x)<=l:
        return x
    else:
        print("you can enter a length of",l,"only")
        
    
def menu():
    while True:
        print("*****           ------WELCOME TO SHOE_BILLING SYSTEM------              *****")  
        print()
        print("*****                 -----HERE ARE SOME QUERIES--------                *****")
        print("                  ****************************************                   ")
        print("1:-                     enter customer details                               ")             
        print()
        print("2:-                      show customer details                               ")
        print()
        print("3:-                     change customer details                              ")
        print()
        print("4:-                     delete customer details                              ")
        print()
        print("5:-                     calculate total amount                               ")
        print()
        print("6:-                     calculate average amount                             ")
        print()
        print("7:-                        find maximum amount                               ")
        print()
        print("8:-                        find minimum amount                               ")
        print()
        print("9:-                        to show all records                               ")
        print()
        print("10:-                           to exit                                       ")
        print()
        print("11:-             to calculate total amount of a particular brand             ")
        print()
        print("12:-             to calculate average amount of a particular brand           ")
        print()
        print("13:-              to calculate maximum amoount of a particular brand         ")
        print()
        print("14:-              to calculate minimum amount  of a particular brand         ")
        print()
        
        v_choice=checkint("enter your choice = ",2)

        
        if v_choice == 1:
            code = checkint("Enter code for which you want to enter detail=", 10)
            cur.execute("SELECT * FROM shoe_details WHERE shoe_code=%s", (code,))
            data = cur.fetchone()
            if data is None:
                brand = checkstring("Enter brand=", 25)
                name = checkstring("Enter customer name=", 25)
                number = checkint("Enter phone no=", 10)
                details = checkstring("Enter address=", 25)
                amount = checkint("Enter amount=", 10)
                cur.execute(
                    "INSERT INTO shoe_details (shoe_code, brand_name, customer_name, customer_number, customer_address, amount) VALUES (%s, %s, %s, %s, %s, %s)",
                    (code, brand, name, number, details, amount)
                )
                con.commit()
            else:
                print("This code already exists")
                print("Enter any other code")

            
            
            
        elif v_choice==2:
            v_code=checkint("enter code no. whose data you want to see",10)
            cur.execute("select * from shoe_details where shoe_code={}".format(v_code))
            data=cur.fetchall()
            if data==[]:
                print("no record for this code")
            else:
                for i in data:
                    print("shoe_code;",i[0])
                    print("brand_name;",i[1])
                    print("customer_name.;",i[2])
                    print("customer_no;", i[3])
                    print("customer_address;", i[4])
                    print("amount;",i[5])
            
            
        elif v_choice==3:
            print("3a:-                    to change brandname                              ")
            print()
            print("3b:-                   to change customer name                           ")
            print()
            print("3c:-                   to change customer number                         ")
            print()
            print("3d:-                   to change customer address                        ")
            print()
            print("3e:-                        to change amount                             ")
            print()
            print("3f:-                             to exit                                 ")
            print()
            while True:
                v_choice1=checkstring("what you want to change",2)
                print()
                if v_choice1=="3a":
                    v_code=checkint("enter the code whose brandname you want to change",10)
                    cur.execute("select * from shoe_details where shoe_code={} " .format(v_code))
                    data=cur.fetchone()
                    if data==None:
                        print("this code does not exist")
                    else:
                        newb=checkstring("enter new brandname",25)
                        cur.execute('''update shoe_details 
                                 set brand_name='{}' where shoe_code={}'''.format(newb,v_code))
                        con.commit()
                elif v_choice1=="3b":
                    v_code=checkint("enter the code whose customer name you want to change",10)
                    cur.execute("select * from shoe_details where shoe_code={} " .format(v_code))
                    data=cur.fetchone()
                    if data==None:
                        print("this code does not exist")
                    else: 
                        newc=checkstring("enter new customer name",25)
                        cur.execute(''' update shoe_details
                                set customer_name='{}' where shoe_code={}'''.format(newc,v_code))
                        con.commit()
                elif v_choice1=="3c":
                    v_code=checkint("enter the code whose customer number you want to change",10)
                    cur.execute("select * from shoe_details where shoe_code={} " .format(v_code))
                    data=cur.fetchone()
                    if data==None:
                        print("this code does not exist")
                    else:
                        newn=checkint("enter new customer number",10)
                        cur.execute('''update shoe_details
                                set customer_number={} where shoe_code={} '''.format(newn,v_code))
                        con.commit()
                elif v_choice1=="3d":
                    v_code=checkint("enter the code whose address you want to change",10)
                    cur.execute("select * from shoe_details where shoe_code={} " .format(v_code))
                    data=cur.fetchone()
                    if data==None:
                        print("this code does not exist")
                    else: 
                        newa=checkstring("enter new customer address",25)
                        cur.execute('''update shoe_details
                                set customer_address='{}' where shoe_code={}'''.format(newa,v_code))
                        con.commit()
                elif v_choice1=="3e":
                    v_code=checkint("enter the code whose amount you want to change",10)
                    cur.execute("select * from shoe_details where shoe_code={} " .format(v_code))
                    data=cur.fetchone()
                    if data==None:
                        print("this code does not exist")
                    else:    
                        newam=checkint("enter new amount",10)
                        cur.execute('''update shoe_details
                                set amount={} where shoe_code={}'''.format(newam,v_code))
                        con.commit()
                elif v_choice1=="3f":
                    print("***         -----THANK YOU FOR COMING-----               ***")
                    break
                else:
                    print("you can enter only from 3a to 3f")

                    
        elif v_choice==4:
            while True:
                v_code=checkint("enter the code whose details you want to delete ",10)
                cur.execute("select * from shoe_details where shoe_code={} " .format(v_code))
                data=cur.fetchone()
                if data==None:
                    print("this code does not exist")
                else: 
                                
                    cur.execute(''' delete from shoe_details
                                 where shoe_code={}'''.format(v_code))
                    con.commit()
                    print("deleted successfully")
                    x=cur.fetchone()
                    if x==None:
                        print("all details for this code  are deleted")
                        break
                    else:
                        continue

                    
        elif v_choice==5:
            cur.execute(''' select * from shoe_details ''')
            z=cur.fetchall()
            c=0
            if z==[]:
                print("there is no record in your table")
            else:
                for i in z:
                    try:
                        c=c+int(i[5])
                    except ValueError:
                        print("total amount is: ",c)

                
        elif v_choice==6:
            cur.execute('''select * from shoe_details''')
            z=cur.fetchall()
            n=len(z)
            c=0
            if z==[]:
                print("there is no record in your table")
            else:
                for i in z:
                    try:
                        c=(c+int(i[5]))/n
                    except ValueError:
                        print("average amount is: ",c)

                
        elif v_choice==7:
            cur.execute('''select * from shoe_details''')
            z=cur.fetchall()
            c=z[0][5]
            q=z[0][5]
            for i in z:
                if i[5]>c:
                    q=i[5]
                else:
                    q=c
            print("maximum amount is: ",q)

            
        elif v_choice==8:
            cur.execute('''select * from shoe_details''')
            z=cur.fetchall()
            c=z[0][5]
            q=z[0][5]
            for i in z:
                if i[5]<c:
                    q=i[5]
                else:
                    q=c
            print("minimum amount is: ",q)

            
        elif v_choice==9:
            cur.execute("select * from shoe_details")
            data=cur.fetchall()
            for i in data:
                print(str(i))
                

        elif v_choice==10:
            print("bye bye")
            print("***                 ----THANK YOU FOR VISITING-----                   ***")
            break

        
        elif v_choice==11:
            b=checkstring("enter brand name for which you want to calculate the total amount",25)
            cur.execute("select * from shoe_details where brand_name='{}' ".format(b))
            c=0
            data=cur.fetchall()
            if data==[]:
                print("sorry this brand name is not valid")
            else:
                for i in data:
                    try:
                        c=c+int(i[5])
                    except ValueError:
                        print("total amount for",b ," brandname is ",c)


        elif v_choice==12:
            b=checkstring("enter brand name for which you want to calculate the average amount",25)
            cur.execute("select * from shoe_details where brand_name='{}' ".format(b))
            c=0
            data=cur.fetchall()
            d=len(data)
            if data==[]:
                print("sorry this brand name is not valid")
            else:
                for i in data:
                    try:
                        if i[5].isdigit():
                            c=c+int(i[5])
                        else:
                            print(f"Skipping non-numeric value: {i[5]}")
                            continue
                    
                        avg=c/d
                    except ValueError:
                        print("average amount for",b ,"brandname is ",avg)

        elif v_choice==13:
            b=checkstring("enter brand name for which you want to calculate the maximum amount",25)
            cur.execute("select * from shoe_details where brand_name='{}' ".format(b))
            data=cur.fetchall()
            if data==[]:
                print("sorry this brand name is not valid")
            else:
                z=data[0][5]
                y=data[0][5]
                for i in data:
                    if z<=i[5]:
                        y=i[5]
                    else:
                        y=data[0][5] 
                print("maximum amount for",b, "brandname is ",y)

        elif v_choice==14:
            b=checkstring("enter brand name for which you want to calculate the minimum amount",25)
            cur.execute("select * from shoe_details where brand_name='{}' ".format(b))
            data=cur.fetchall()
            if data==[]:
                print("sorry this brand name is not valid")
            else:
                z=data[0][5]
                y=data[0][5]
                for i in data:
                    if z>=i[5]:
                        y=i[5]
                    else:
                        y=data[0][5]
                print("minimum amount for",b,"brandname is ",y)
                   

        
def menu1():
    while True:
        print("***               -----WELCOME TO SHOE_BILLING SYSTEM-----                ***")
        print()
        print("1:-                       enter customer details                             ")
        print()
        print("2:-                       show customer details                              ")
        print()
        print("3:-                            to exit                                       ")
        print()
        v_choice2=checkint("enter your choice = ",1)
        print()

        
        if v_choice2==1:
            code=checkint("enter code for which you want to enter detail=",10)
            cur.execute("select * from shoe_details where shoe_code={} ".format(code))
            data=cur.fetchone()
            if data==None:
                brand=checkstring("enter brand=",25)
                name= checkstring("enter customer name=",25)
                number=checkint("enter phone no=",10)
                details=checkstring("enter address=",25)
                amount=checkint("enter amount=",10)
                cur.execute("insert into shoe_details values({},'{}','{}',{},'{}',{})".format(code,brand,name,number,details,amount))
                con.commit()
            else:
                print(" this code already exist")
                print()
                print("enter any other code")

                
        elif v_choice2==2:
            v_code=checkint("enter code no. whose data you want to see",10)
            cur.execute("select * from shoe_details where shoe_code={}".format(v_code))
            data=cur.fetchall()
            if data==[]:
                print("no record for this code")
            else:
                for i in data:
                    print("shoe_code;",i[0])
                    print("brand_name;",i[1])
                    print("customer_name.;",i[2])
                    print("customer_no;", i[3])
                    print("customer_address;", i[4])
                    print("amount;",i[5])
         
            
        elif v_choice2==3:
            print("bye byeeee")
            print()
            print("***                      -----VISIT AGAIN-----                        ***")
            break
        else:
            print("invalidddd choiceee")
            
def user():
    N=checkstring(" please enter username again",25)
    cur.execute("select * from user where uname='{}' ".format(N))
    x=cur.fetchone()
    if N=="raghavan" and x[1]=="leo":
        menu1()
    else:
        menu()
            
        
introduction()


while True:
    print("*-------------------------------*")          
    print("*** 1:      Login             ***")
    print("*** 2:        New user        ***")
    print("*** 3:         Remove User    ***")
    print("*** 4:     Change Password    ***")
    print("*** 5:       Exit             ***")
    print("*-------------------------------*")
    try:
        print("* Enter your choice                   \n",end="")
        ch=int(input())
    except:
        print("*   Enter digit only                    *")
        continue
    if ch==1:
        login()
        user()
        
        #     add software code option menu
        
            
        
    elif ch==2:
        newuser()
        menu()
    elif ch==3:
        removeuser()
    elif ch==4:
        changepassword()
    elif ch==5:
        print("                         Bye... HAVE A NICE DAYY!...                         ")
        break
    else:
        break
else:
    print("***             I HOPE IT WAS HELPFUL FOR YOU........                                    ***")
    
