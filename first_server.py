from flask import Flask,request
from DB_find import *
from datetime import *
# import threading, time

thread_Count = 0

app = Flask(__name__)

@app.route('/')
def mach_UserName():

    temp = request.args.get('name', "")
    check_User = Find_Data(temp)

    return check_User

@app.route('/Log')
def Call_Log():

    AccountName = request.args.get('name', "")
    AccountBalance = request.args.get('balance', "")
    Make_Log(AccountName,AccountBalance)
    return "sds"

@app.route('/Deposit')
def Add_Deposit():

    AccountName = request.args.get('name', "")
    UNIX__Time = request.args.get('UNIX_Time', "")
    time = request.args.get('time', "")
    AccountBalance = request.args.get('Deposit', "")
    Make_Deposit(AccountName,UNIX__Time,time,AccountBalance)
    return "sds"

@app.route('/Find_Deposit')
def Finds_Deposit():

    AccountName = request.args.get('name', "")
    UNIX_Time = Find_Deposit(AccountName)
    return UNIX_Time

if __name__ == '__main__':
    # def getHtml():
        
    #     while True:
    #         time.sleep(5)
    #         print(date.today().isoformat())
    #         print(time.strftime("%H:%M:%S",time.localtime()))
            
    # threading.Thread(target=getHtml).start()
    app.run(debug=True,host='0.0.0.0', port=80)
    