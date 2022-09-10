#MAIN.PY

import mysql.connector as sql
conn = sql.connect(host='localhost', user='root', passwd='1234', database='bank')
cur = conn.cursor()
# cur.execute('create table user_table(username varchar(25) primary key,passwrd varchar(25) not null )')
print('=========================WELCOME TO STARK BANK============================================================')
import datetime as dt
print(dt.datetime.now())
print('1.REGISTER')
print()
print('2.LOGIN')
print()


n = int(input('enter your choice='))
print()

if n == 1:
name = input('Enter a Username=')
print()
passwd = int(input('Enter a 4 DIGIT Password='))
print()
V_SQLInsert = "INSERT  INTOuser_table (passwrd,username) values (" + str(passwd) + ",' " + name + " ') "
cur.execute(V_SQLInsert)
conn.commit()
print()
print('USER created succesfully')
import menu

if n == 2:
name = input('Enter your Username=')
print()
passwd = int(input('Enter your 4 DIGIT Password='))
V_Sql_Sel = "select * from user_table where passwrd='"+str(passwd)+"' and username=  ' " + name+ " ' "
cur.execute(V_Sql_Sel)
ifcur.fetchone() is  None:
print()
print('Invalid username or password')
else:
print()
import menu


#MENU.PY

importdatetime as dt
importmysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='1234', database='bank')
cur = conn.cursor()

conn.autocommit = True
c = 'y'
while c == 'y':

print()
print('1.CREATE BANK ACCOUNT')
print()
print('2.TRANSACTION')
print()
print('3.CUSTOMER DETAILS')
print()
print('4.TRANSACTION DETAILS')
print()
print('5.DELETE ACCOUNT')
print()
print('6.QUIT')

print()
    n = int(input('Enter your CHOICE='))
print()

if n == 1:
acc_no = int(input('Enter your ACCOUNT NUMBER='))
print()
acc_name = input('Enter your ACCOUNT NAME=')
print()
ph_no = int(input('Enter your PHONE NUMBER='))
print()
add = (input('Enter your place='))
print()
cr_amt = int(input('Enter your credit amount='))
        #import table
V_SQLInsert = "INSERT  INTOcustomer_details values (" + str(acc_no) + ",' " + acc_name + " '," + str(
ph_no) + ",' " + add + " '," + str(cr_amt) + " ) "
cur.execute(V_SQLInsert)
print()
print('Account Created Succesfully!!!!!')
conn.commit()

if n == 2:
acct_no = int(input('Enter Your Account Number='))
cur.execute('select * from customer_details where acct_no=' + str(acct_no))
data = cur.fetchall()
count = cur.rowcount
conn.commit()
if count == 0:
print()
print('Account Number Invalid Sorry Try Again Later')
print()
else:
print()
print('1.WITHDRAW AMOUNT')
print()
print('2.ADD AMOUNT')
print()

print()
            x = int(input('Enter your CHOICE='))
print()
if x == 1:
amt = int(input('Enter withdrawl amount='))
cr_amt = 0
cur.execute(
                    'update customer_details set   cr_amt=cr_amt-' + str(amt) + ' where acct_no=' + str(acct_no))
V_SQLInsert = "INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,
dt.datetime.today(), amt,
cr_amt)
cur.execute(V_SQLInsert)
conn.commit()
print()
print('Account Updated Succesfully!!!!!')

if x == 2:
amt = int(input('Enter amount to be added='))
cr_amt = 0
cur.execute('update customer_details set  cr_amt=cr_amt+' + str(amt) + ' where acct_no=' + str(acct_no))
V_SQLInsert = "INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,
dt.datetime.today(),
cr_amt, amt)
cur.execute(V_SQLInsert)
conn.commit()
print()
print('Account Updated Succesfully!!!!!')

if n == 3:
acct_no = int(input('Enter your account number='))
print()
cur.execute('select * from customer_details where acct_no=' + str(acct_no))
ifcur.fetchone() is None:
print()
print('Invalid Account number')
else:
cur.execute('select * from customer_details where acct_no=' + str(acct_no))
data = cur.fetchall()
for row in data:
print('ACCOUNT NO=', acct_no)
print()
print('ACCOUNT NAME=', row[1])
print()
print(' PHONE NUMBER=', row[2])
print()
print('ADDRESS=', row[3])
print()
print('cr_amt=', row[4])
if n == 4:
        #import transcation_table
acct_no = int(input('Enter your account number='))
print()
cur.execute('select * from customer_details where acct_no=' + str(acct_no))
ifcur.fetchone() is None:
print()
print('Invalid Account number')
else:
cur.execute('select * from transactions where acct_no=' + str(acct_no))
data = cur.fetchall()
for row in data:
print('ACCOUNT NO=', acct_no)
print()
print('DATE=', row[1])
print()
print(' WITHDRAWAL AMOUNT=', row[2])
print()
print('AMOUNT ADDED=', row[3])
print()

if n == 5:
print('DELETE YOUR ACCOUNT')
acct_no = int(input('Enter your account number='))

cur.execute('delete from customer_details where acct_no=' + str(acct_no))
print('ACCOUNT DELETED SUCCESFULLY')

if n == 6:
print('DO YO WANT TO EXIT(y/n)')
        c = input('enter your choice=')
quit()

#TABLE.PY

import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='1234', database='bank')
ifconn.is_connected():
print('connected succesfully')
cur = conn.cursor()
cur.execute('create table customer_details(acct_noint primary key,acct_name varchar(25) ,phone_nobigint(25) check(phone_no>11),address varchar(25),cr_amt float )')
#TRANSACTION.PY

importmysql.connector as sql
conn = sql.connect(host='localhost', user='root', passwd='1234', database='bank')
cur = conn.cursor()
cur.execute('create table transactions(acct_noint(11),date date ,withdrawal_amtbigint(20),amount_addedbigint(20) )')



#USER TABLE.PY

importmysql.connector as sql
conn = sql.connect(host='localhost', user='root', passwd='1234', database='bank')
cur = conn.cursor()
cur.execute('create table user_table(username varchar(25) primary key,passwrd varchar(25) not null )')
