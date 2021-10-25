6# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("contribution---ignore")
import mysql.connector as s
connection=s.connect(host="localhost",user="root",database="mybank",passwd="shania123")
if connection.is_connected():
    print("Database MyBank Access Successful")
else:
    print("Database MyBank Access Failed.")
    
def main():
    print("""
          1.OPEN NEW ACCOUNT
          2.DEPOSIT AMOUNT
          3.WITHDRAW AMOUNT
          4.BALANCE ENQUIRY
          5.DISPLAY CUSTOMER DETAILS
          6.CLOSE ACCOUNT
          """)
    choice=input("Enter Your Choice : ")
    while True:
        if (choice=='1'):
            openAcc()
        elif (choice=='2'):
            deposAmt()
        elif (choice=='3'):
            wdAmt()
        elif (choice=='4'):
            balEnq()
        elif (choice=='5'):
            dispCustDetails()
        elif (choice=='6'):
            closeAcc()
        else:
            print("ERROR!!USER ENTERED INVALID CHOICE.")
            main()
            
def openAcc():
    name=input("Enter Customer Name : ")
    accNo=int(input("Enter Account Number : "))
    dob=input("Enter Customer D.O.B : ")
    ph=int(input("Enter Customer Phone Number : ")) 
    add=input("Enter Customer Address : ")
    obal=int(input("Enter Opening Balance : "))
    data1=(name,accNo,dob,ph,add,obal) 
    data2=(name,accNo,obal)
    sql1='insert into account values(%s,%s,%s,%s,%s,%s)'
    sql2='insert into amount values(%s,%s,%s)'
    cursor=connection.cursor()
    cursor.execute(sql1,data1)
    cursor.execute(sql2,data2) 
    connection.commit()
    print("Data Entered Successfully") 
    main()
    
def deposAmt():
    amt=int(input("Enter Amount To Be Deposited : "))
    accNo=int(input("Enter Account Number : "))
    sql3='select balance from amount where ACCOUNT_NUMBER = %s'
    data3=(accNo,)
    cursor=connection.cursor()
    cursor.execute(sql3,data3)
    prevbal=cursor.fetchone()
    totAmt=prevbal[0]+amt
    sql4='update amount set balance = %s where ACCOUNT_NUMBER = %s'
    data4=(totAmt,accNo)
    cursor.execute(sql4,data4)
    connection.commit()
    print("CASH DEPOSIT SUCCESSFUL.")
    main()
    
def wdAmt():
    amt=int(input("Enter Amount To Be Withdrawn : "))
    accNo=input("Enter Account Number : ")
    sql5="select balance from amount where account_number = %s"
    data5=(accNo,)
    cursor=connection.cursor()
    cursor.execute(sql5,data5)
    prevbal=cursor.fetchone()
    totAmt=prevbal[0]-amt
    sql6="update amount set balance = %s where account_number = %s"
    data6=(totAmt,accNo)
    cursor.execute(sql6,data6) 
    connection.commit()
    print("CASH WITHDRAWAL SUCCESSFUL.")
    main()
    
def balEnq():
    accNo=input("Enter Account Number : ")
    sql7="select balance from AMOUNT WHERE ACCOUNT_NUMBER = %s"
    data7 = (accNo,)
    cursor=connection.cursor() 
    cursor.execute(sql7,data7)
    current_bal=cursor.fetchone()
    print("\n\n\nBALANCE FOR ACCOUNT NUMBER : ", accNo, " is ", current_bal[0])
    print("\nBALANCE ENQUIRY OVER.")
    main()
    
def dispCustDetails():
    accNo=input("Enter Account Number : ")
    sql8='select * from account where ACCOUNT_NUMBER = %s'
    data8=(accNo,)
    cursor=connection.cursor()
    cursor.execute(sql8,data8)
    result_detail=cursor.fetchone()
    for i in result_detail:
        print(i,end="    ")
    print("\n\nCUSTOMERS DETAILS DISPLAYED.")
    main()
    
def closeAcc():
    accNo=input("Enter Account Number : ")
    sql9="delete from ACCOUNT WHERE ACCOUNT_NUMBER = %s"
    sql10="DELETE FROM AMOUNT WHERE ACCOUNT_NUMBER = %s" 
    data_910=(accNo,)
    cursor=connection.cursor()
    cursor.execute(sql9,data_910)
    cursor.execute(sql10,data_910)
    connection.commit()
    print("\n\nACCOUNT CLOSURE SUCCESSFUL")
    connection.commit()
    main()

main()