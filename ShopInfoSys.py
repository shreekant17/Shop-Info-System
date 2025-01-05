import mysql.connector as sql
while True:
    passw=input("Enter Mysql Password: ")
    try:
        c=sql.connect(host="localhost", user="root", passwd=passw)#password
        break
    except:
        print("Incorrect Password")
c1=c.cursor()
c1.execute("create database if not exists shop")
c1.execute("use Shop")
try:
    c1.execute("create table stocks(S_No int primary key, Name_of_Item varchar(30), Price_in_Rs int, Quantity_Available int)")
    c1.execute("insert into stocks values(1,'Photostat Paper',500,150)")
    c1.execute("insert into stocks values(2,'Calculator', 375, 20)")
    c1.execute("insert into stocks values(3,'Glue Stick', 20, 50)")
    c1.execute("insert into stocks values(4,'Permanent Marker', 20, 150)")
    c1.execute("insert into stocks values(5,'Officers Pen', 50, 200)")
    c1.execute("insert into stocks values(6,'Correction Pen', 30, 125)")
    c1.execute("insert into stocks values(7,'Eraser', 5, 525)")
    c1.execute("insert into stocks values(8,'Spiral Notebook', 30, 70)")
    c1.execute("insert into stocks values(9,'Colour', 80, 46)")
    c1.execute("insert into stocks values(10,'Diary Register', 175, 75)")
    c1.execute("insert into stocks values(11,'Chart Paper', 5, 200)")
    c1.execute("insert into stocks values(12,'Punching Machine', 150, 40)")
    c.commit()
except:
    print()
c1.execute("Create table if not exists custdtls(CNAME VARCHAR(30), PHONE BIGINT PRIMARY KEY, ITEMS INT, AMOUNT FLOAT)")
zk='-'*70
zkk="#"*70
print('+'+zk+'+')
print('|'+zkk+'|')
print("|\\\\\\\\\\\\\\\\\*******WELCOME TO THE SHOP IFORMATION SYSTEM*******//////////|")
print('|'+zkk+'|')
print('+'+zk+'+')
from time import gmtime,strftime
a=strftime("%a, %d %b %y",gmtime())
print(a)
print("")
print("WELCOME TO OUR STATIONERY SHOP")
try:
    c1.execute("create table Account(Name Varchar(30), Phone bigint primary key, Account_Type varchar(10), Pin int)")
except:
    print()
ch23='jk'
while ch23.lower()!='y':
    print("1. Customer Login/Register")
    print("2. Staff Login/Register")
    print('')
    ch22=input("Enter your choice: ")
    if ch22=='1':
        print("1. Login")
        print("2. Register")
        ch14=input("Enter Your Choice: ")
        if ch14=='1':
            while 7==7:
                lst=[]
                phn=int(input("Please Enter Your Phone Number: "))
                c1.execute("select Phone from account")
                for ph in c1.fetchall():
                    lst.append(ph[0])
                if phn in lst:
                    c1.execute("select Name from account where phone={}".format(phn))
                    for acname in c1.fetchall():
                        print("Welcome: ",acname[0])
                    break
                else:
                    print("Account Doesn't Exists")
            while 1==1:
                psd=int(input("Enter your pin: "))
                c1.execute("select pin from account where phone='{}' and Account_Type='Customer'".format(phn))
                for xm in c1:
                    xm=xm[0]
                if xm==psd:
                    break
                else:
                    print("Incorrect Pin! Try Again")
        elif ch14=='2':
            name=input("Please Enter Your Name: ")
            while 1==1:
                phn=(input("Please Enter Your Phone No.: "))
                if len(phn)==10:
                    break
                else:
                    print("Enter Valid Phone Number")
            pincode=int(input("Set 4 Digit pin"))
            actype="Customer"
            c1.execute("insert into Account values('{}',{},'{}',{})".format(name,phn,actype,pincode))
            c.commit()
        print()
        c1.execute("select name from account where phone={}".format(phn))
        for asd in c1:
             asd=asd[0]
        print("WELCOME ", asd.upper())
        ch1=(input("PRESS ANY KEY TO VIEW AVAILABLE ITEMS: "))
        c1.execute("select * from stocks")
        pl='-'*66
        print(pl+'+')
        print("%5s"%"ICode"+'|',"%30s"%"Item_Name"+'|',"%15s"%"Amount(in Rs)"+'|',"%10s"%"Qty_Avl"+'|')
        for i in c1.fetchall():
            print("%5s"%i[0]+'|',"%30s"%i[1]+'|',"%15s"%i[2]+'|',"%10s"%i[3]+'|')
        print(pl+'+')
        try:
            c1.execute("create table pur6(S_NO INT, Name_of_Item varchar(50), QUANTITY INT, AMT FLOAT, AmtGst float)")
        except:
            print('')
        while 1==1:
            ch2=input("Enter the ICode of the item to buy: ")
            ch3=input("Enter the quantity to buy: ")
            r="select (Price_in_Rs)*{} from stocks where S_No={}".format(ch3,ch2)
            amt=c1.execute(r)
            for j in c1:
                j=float(j[0])
                tax=((18/100)*j)*float(ch3)
                ji=j+tax
            c1.execute("select Name_of_item from stocks where S_No={}".format(ch2))
            for qwe in c1:
                qwe=qwe[0]
            m="insert into pur6 values({},'{}', {}, {}, {})".format(ch2,qwe,ch3,j,ji)
            c1.execute(m)
            c.commit()
            print("\nYou have selected these items to Buy")
            c1.execute("select Name_of_Item, (Price_in_Rs)*{} from stocks where S_No = {}".format(ch3,ch2))
            plu='-'*42
            print(plu+'+')
            print("%20s"%"Name_of_Item"+'|',"%20s"%"Total_Price"+'|')
            for z in c1.fetchall():
                print("%20s"%z[0]+'|',"%20s"%float(z[1])+'|')
            print(plu+'+')
            c1.execute("select Quantity_Available from stocks where S_No={}".format(ch2))
            for e in c1:
                e=e[0]
            c1.execute("Update stocks set Quantity_Available = {} - {} where S_No={}".format(e,ch3,ch2))
            c.commit()
            print("Press (E) if you dont wish to buy more : ")
            print("Press any key to continue shopping")
            ch4=input("Enter Your Choice: ")
            if ch4.lower()=="e":
                c1.execute("select sum(amt), sum(AmtGst) from pur6")
                for k in c1:
                    ki=k[0]
                    amgst=k[1]
                    ds='-'*39
                    print(ds+'+')
                    print("%10s"%"Amount"+'|', "%10s"%"Tax(GST)"+'|',"%15s"%"Total Amount"+'|')
                    print("%10s"%ki+'|',"%10s"%tax+'|',"%15s"%amgst+'|')
                    print(ds+'+')
                ck=input("Press (C) Proceed to checkout: ")
                if ck.lower()=="c":
                    print("Press (P) to proceed: ")
                    print("Press (X) to cancel purchase: ")
                    ch5=input("Enter Your Choice: ")
                    if ch5.lower()=="x":
                        c1.execute("select Quantity_Available from stocks where S_No={}".format(ch2))
                        for w in c1:
                            w=w[0]
                        c1.execute("Update stocks set Quantity_Available = {} + {} where S_No={}".format(w,ch3,ch2))
                        c.commit()
                        print("Thanks For Visiting")
                        break
                    elif ch5.lower()=="p":
                        c1.execute("select sum(Quantity)from pur6")
                        for d in c1:
                            d=d[0]
                        try:
                            c1.execute("insert into custdtls values('{}',{},{},{})".format(asd,phn,d,amgst))
                        except:
                            c1.execute("select items, amount from custdtls where phone={}".format(phn))
                            for itm in c1:
                                it=itm[0]
                                amu=itm[1]
                            c1.execute("update custdtls set items={}+{},amount={}+{} where phone={}".format(it,d,amu,amgst,phn))
                            c.commit()
                        c1.execute("select * from pur6")
                        plus='-'*78
                        print(plus+'+')
                        print("%7s"%"I_Code"+'|',"%20s"%"Item_Name"+'|',"%5s"%"Qty"+'|',"%12s"%"Amount"+'|',"%12s"%"Tax"+'|',"%12s"%"Total_Amt"+'|')
                        for t in c1.fetchall():
                            print("%7s"%t[0]+'|',"%20s"%t[1]+'|',"%5s"%t[2]+'|',"%12s"%t[3]+'|',"%12s"%tax+'|',"%12s"%t[4]+'|')
                        print(plus+'+')
                        c.commit()
                        print("SELECT PAYMENT METHOD")
                        print("Press 1 for Debit/Credit Card")
                        print("Press 2 for Cash")
                        ch7=int(input("Enter Your Choice: "))
                        print("PAYMENT ACCEPTED")
                        print("x"*82)
                        print(' '*29,"#####***INVOICE***#####")
                        print(" ")
                        print(a)
                        print("NAME: ",asd.upper())
                        print("PHONE No: ",phn)
                        print("\nITEMS BOUGHT: ")
                        c1.execute("select * from pur6")
                        print(plus+'+')
                        print("%7s"%"I_Code"+'|',"%20s"%"Item_Name"+'|',"%5s"%"Qty"+'|',"%12s"%"Amount"+'|',"%12s"%"Tax"+'|',"%12s"%"Total_Amt"+'|')
                        for t in c1.fetchall():
                            print("%7s"%t[0]+'|',"%20s"%t[1]+'|',"%5s"%t[2]+'|',"%12s"%t[3]+'|',"%12s"%tax+'|',"%12s"%t[4]+'|')
                        print(plus+'+')
                        
                        print("PAYMENT STATUS: SUCCESSFULL")
                        print("Total Amount Paid:",amgst) 
                        if ch7==1:
                            print("\nPAYMENT METHOD: DEBIT/CREDIT CARD")
                        elif ch7==2:
                            print("\nPAYMENT METHOD: CASH")
                        print('x'*82)
                        print("\n*******Thanks For Visiting! Have a great day*******")
                        print('')
                        ch21=input("PRESS (X) TO LOGOUT: ")
                        if ch21.lower()=="x":
                            print("\nTHANK YOU")
                        print()
                        c1.execute("drop table pur6")
                        c.commit()
                        break
                        c.close()
    elif ch22=="2":
        print("1. Login as staff")
        print("2. Register as staff")
        ch14=input("Enter Your Choice: ")
        if ch14=='1':
            while 7==7:
                lst=[]
                phn=int(input("Please Enter Your Phone Number: "))
                c1.execute("select Phone from account")
                for ph in c1.fetchall():
                    lst.append(ph[0])
                if phn in lst:
                    c1.execute("select Name from account where phone={}".format(phn))
                    for acname in c1.fetchall():
                        print("Welcome: ",acname[0])
                    break
                else:
                    print("Account Doesn't Exists")
            while 1==1:
                psd=int(input("Enter your pin: "))
                c1.execute("select pin from account where phone='{}' and Account_Type='staff'".format(phn))
                for xm in c1:
                    xm=xm[0]
                if xm==psd:
                    break
                else:
                   print("Incorrect Pin! Try Again")
        elif ch14=='2':
            shpin="0192"
            while 5==5:
                shpin=(input("Enter Shop Pin: "))
                if shpin in "0192":
                    break
                else:
                    print("Invalid Shop Pin: ")
            name=input("Please Enter Your Name: ")
            while 1==1:
                phn=(input("Please Enter Your Phone No.: "))
                if len(phn)==10:
                    break
                else:
                    print("Enter Valid Phone Number")
            pincode=int(input("Set 4 Digit pin: "))
            actype="Staff"
            c1.execute("insert into Account values('{}',{},'{}',{})".format(name,phn,actype,pincode))
            c.commit()
        else:
            print("Enter Valid Choice")
            continue
        ch21='s'
        while ch21.lower()!='x':
            print("If you want to update stocks PRESS(1), else PRESS(2)")
            ch18=input("Enter Choice: ")
            if ch18=="1":
                print("1. Update Quantity")
                print("2. Update Price")
                ch20=int(input("Enter Choice: "))
                if ch20==1:
                    c1.execute("select * from stocks")
                    pl='-'*66
                    print(pl+'+')
                    print("%5s"%"S_No"+'|',"%30s"%"Item_Name"+'|',"%15s"%"Amount"+'|',"%10s"%"Qty_Avl"+'|')
                    for v in c1.fetchall():
                        print("%5s"%v[0]+'|',"%30s"%v[1]+'|',"%15s"%v[2]+'|',"%10s"%v[3]+'|')
                    print(pl+'+')
                    ser=int(input("Enter S_No to update: "))
                    qt=int(input("Enter New Qty: "))
                    c1.execute("update stocks set Quantity_Available={} where S_No={}".format(qt,ser))
                    c.commit()
                    print("##STOCK UPDATED##")
                    continue
                elif ch20==2:
                    import mysql.connector as sql
                    c=sql.connect(host="localhost", user="root", passwd='asdf')#pass
                    c1=c.cursor()
                    c1.execute("use Shop")
                    c1.execute("select * from stocks")
                    pl='-'*66
                    print(pl+'+')
                    print("%5s"%"S_No"+'|',"%30s"%"Item_Name"+'|',"%15s"%"Price"+'|',"%10s"%"Qty_Avl"+'|')
                    for v in c1.fetchall():
                        print("%5s"%v[0]+'|',"%30s"%v[1]+'|',"%15s"%v[2]+'|',"%10s"%v[3]+'|')
                    print(pl+'+')
                    ser=int(input("Enter S_No to update: "))
                    am=int(input("New Amt: "))
                    c1.execute("update stocks set Price_in_Rs={} where S_No={}".format(am,ser))
                    c.commit()
                    print("##STOCK UPDATED##")
                    continue
            elif ch18=='2':
                print()
                print("If You Want to See Customer/sales Info PRESS (Y) else PRESS (N)")
                ch22=input("Enter Choice: ")
                if ch22.lower()=="y":
                    c1.execute("select * from custdtls")
                    res=c1.fetchall()
                    pluss='-'*66
                    print(pluss+'+')
                    print("%20s"%"CUS_NAME"+'|', "%20s"%"PHONE"+'|',"%10s"%"QTY"+'|',"%10s"%"AMT"+'|')
                    for gh in res:
                        print("%20s"%gh[0]+'|', "%20s"%gh[1]+'|',"%10s"%gh[2]+'|',"%10s"%gh[3]+'|')
                    print(pluss+'+')
                elif ch22.lower()=="n":
                    print()
                    ch21=input("PRESS (X) TO LOGOUT: ")
                    if ch21.lower()=="x":
                        c.close()
                    print("THANK YOU")
                    print()
    print("TO EXIT PRESS(Y)")
    print("PRESS ENTER TO CONTINUE")
    ch23=input("Enter Your Choice: ")
    print()
    if ch23.lower()=='y':
        print("###BYE###")
        break
    
    
                

        
        


    
                
                        
                        
                        
                        
                        
  
                        
                    

                    




            



    
