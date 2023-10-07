import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Vineeth@123",database="BANK_MANAGEMENT")

def OpenAcc():
    n=input("Enter The Name:")
    ac=input("Enter Account No:")
    db=input('Enter The DOB:')
    add=input("Enter Address:")
    cn=int(input("Enter Contact No:"))
    ob=int(input("Enter Opening Balance:"))
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,ob)
    sql1=("insert into account values (%s,%s,%s,%s,%s,%s)")
    sql2=("insert into amount values (%s,%s,%s)")
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("Data Enter Sucessfully........")
    main()


def DepoAmo():
    ac=input("Enter Account No:")
    amount=int(input("Enter Amount To Deposit:"))
    a="select balance from amount where accno=%s"
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[-1]+amount
    sql1 = ("update amount set balance=%s where Accno=%s")

    d=(t,ac)
    x.execute(sql1,d)

    mydb.commit()
    print("Amount deposited successfully")
    main()


def withdrawAmount():
    ac=input("Enter Account No:")
    amount=int(input("Enter Amount To Withdraw:"))
    a="select balance from amount where accno=%s"
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[-1]-amount
    sql1=("update amount set balance=%s where Accno=%s")

    d=(t,ac)
    x.execute(sql1,d)

    mydb.commit()
    print("Amount withdrawn succesfully")
    main()

def balEnq():
    ac=input("Enter Account No:")
    a="select * from amount where AccNo=%s"
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print("Balance for account:",ac,"is",result[-1])
    main()

def DisDetails():
    ac=input("Enter Account No:")
    a="select * from account where AccNo=%s"
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    for i in result:
        print(i)
    main()

def closeAcc():
    ac=input("Enter Account No:")
    sql1="delete from account where accno=%s"
    sql2="delete from amount where accno=%s"
    data=(ac,)
    x=mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    print("Account closed successfully")
    main()



def main():
    print(''' 
          1.Open New Account
          2.Deposit Amount
          3.Withdraw
          4.Balance Enquiry
          5.Display Customer Details
          6.Close An Account
               ''')
    choice=input("Enter Task You Want To Perform:")
    if(choice=='1'):
        OpenAcc()
    elif(choice=="2"):
        DepoAmo()
    elif(choice=="3"):
        withdrawAmount()
    elif(choice=="4"):
        balEnq()
    elif(choice=="5"):
        DisDetails()
    elif(choice=="6"):
        closeAcc()
    else:
        print("Your Choice Is Wrong")
        main()

main()


