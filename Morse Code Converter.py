# working and developing on python 3.8.6
 
from tkinter import Tk
from tkinter import *
from tkinter import messagebox
import sys

# database packages
import mysql.connector

#regex package for validation
import re

tapetom = None
tapmtoe = None

registered = False
loginedUserData = None

countEtoM = 0
countMtoE = 0


# morse code table for info to the user 
def morseCodeWin():

    windowIndex2 = Tk()

    windowIndex2.geometry("620x420")
    windowIndex2.maxsize(620,420)
    windowIndex2.minsize(620,420)
    windowIndex2.title("Morse Code")

    l1 = Label(windowIndex2, text = "International Morse Code", font = "Verdana 14", bg = "black", fg = "white")
    l1.grid(row = 0, column = 0, padx = 190, pady = 0, columnspan = 2)

    Label(windowIndex2, text = "A = .-",font = "verdana 9").grid(row = 1, column = 0,sticky = W, padx = (210,0))
    Label(windowIndex2, text = "B = -...",font = "verdana 9").grid(row = 2, column = 0,sticky = W, padx = (210,0))
    Label(windowIndex2, text = "C = -.-.",font = "verdana 9").grid(row = 3, column = 0, sticky = W, padx = (210,0))
    Label(windowIndex2, text = "D = -..",font = "verdana 9").grid(row = 4, column = 0, sticky = W, padx = (210,0))
    Label(windowIndex2, text = "E = .",font = "verdana 9").grid(row = 5, column = 0, sticky = W, padx = (210,0))
    Label(windowIndex2, text = "F = ..-.",font = "verdana 9").grid(row =6 , column = 0, sticky = W, padx = (210,0))
    Label(windowIndex2, text = "G = --.",font = "verdana 9").grid(row = 7, column = 0, sticky = W, padx = (210,0))
    Label(windowIndex2, text = "H = ....",font = "verdana 9").grid(row = 8, column = 0, sticky = W, padx = (210,0))
    Label(windowIndex2, text = "I = ..",font = "verdana 9").grid(row = 9, column = 0, sticky = W, padx = (210,0))
    Label(windowIndex2, text = "J = .---",font = "verdana 9").grid(row = 10, column = 0, sticky = W, padx = (210,0))
    Label(windowIndex2, text = "K = -.-",font = "verdana 9").grid(row = 11, column = 0, sticky = W, padx = (210,0))
    Label(windowIndex2, text = "L = .-..",font = "verdana 9").grid(row = 12, column = 0, sticky = W, padx = (210,0))
    Label(windowIndex2, text = "M = --",font = "verdana 9").grid(row = 13, column = 0, sticky = W, padx = (210,0))
    Label(windowIndex2, text = "N = -.",font = "verdana 9").grid(row = 14, column = 0, sticky = W, padx = (210,0))
    Label(windowIndex2, text = "O = ---",font = "verdana 9").grid(row = 15, column = 0, sticky = W, padx = (210,0))
    Label(windowIndex2, text = "P = .--.",font = "verdana 9").grid(row = 16, column = 0, sticky = W, padx = (210,0))
    Label(windowIndex2, text = "Q = --.-",font = "verdana 9").grid(row = 17, column = 0, sticky = W, padx = (210,0))
    Label(windowIndex2, text = "R = .-.",font = "verdana 9").grid(row = 18, column = 0, sticky = W, padx = (210,0))

    Label(windowIndex2, text = "S = ...",font = "verdana 9").grid(row = 1, column = 1,sticky = W, padx = (0,90))
    Label(windowIndex2, text = "T = -",font = "verdana 9").grid(row = 2, column = 1, sticky = W, padx = (0,90))
    Label(windowIndex2, text = "U = ..-",font = "verdana 9").grid(row = 3, column = 1,sticky = W, padx = (0,90))
    Label(windowIndex2, text = "V = ...-",font = "verdana 9").grid(row = 4, column = 1,sticky = W, padx = (0,90))
    Label(windowIndex2, text = "W = .--",font = "verdana 9").grid(row = 5, column = 1,sticky = W, padx = (0,90))
    Label(windowIndex2, text = "X = -..-",font = "verdana 9").grid(row = 6, column = 1,sticky = W, padx = (0,90))
    Label(windowIndex2, text = "Y = -.--",font = "verdana 9").grid(row = 7, column = 1,sticky = W, padx = (0,90))
    Label(windowIndex2, text = "Z = --..",font = "verdana 9").grid(row = 8, column = 1,sticky = W, padx = (0,90))
    Label(windowIndex2, text = "1 = .----",font = "verdana 9").grid(row = 9, column = 1,sticky = W, padx = (0,90))
    Label(windowIndex2, text = "2 = ..---",font = "verdana 9").grid(row = 10, column = 1,sticky = W, padx = (0,90))
    Label(windowIndex2, text = "3 = ...--",font = "verdana 9").grid(row = 11, column = 1,sticky = W, padx = (0,90))
    Label(windowIndex2, text = "4 = ....-",font = "verdana 9").grid(row = 12, column = 1,sticky = W, padx = (0,90))
    Label(windowIndex2, text = "5 = .....",font = "verdana 9").grid(row = 13, column = 1,sticky = W, padx = (0,90))
    Label(windowIndex2, text = "6 = -....",font = "verdana 9").grid(row = 14, column = 1,sticky = W, padx = (0,90))
    Label(windowIndex2, text = "7 = --...",font = "verdana 9").grid(row = 15, column = 1,sticky = W, padx = (0,90))
    Label(windowIndex2, text = "8 = ---..",font = "verdana 9").grid(row = 16, column = 1,sticky = W, padx = (0,90))
    Label(windowIndex2, text = "9 = ----.",font = "verdana 9").grid(row = 17, column = 1,sticky = W, padx = (0,90))
    Label(windowIndex2, text = "0 = -----",font = "verdana 9").grid(row = 18, column = 1,sticky = W, padx = (0,90))

    windowIndex2.mainloop()

# if user not want to login or register 
# this will be also used for logged-in user to move to converter options
def guest(): #guests do not have access to History
    head.grid_remove()
    loginButton.grid_remove()
    signupButton.grid_remove()
    guestButton.grid_remove()
    bottomFrame.grid_remove()
    logoutButton.grid_remove()
    converterButton.grid_remove()
    historyButton.grid_remove()

    global buttonFrame2

    buttonFrame2 = Frame(windowIndex)
    buttonFrame2.grid(row = 0, column = 0, columnspan = 2, padx = 125, pady = (50,0))

    mtoeButton = Button(buttonFrame2, text = "Morse to Text", font = "10", bg = '#000000', fg = '#fff', command = Morse_to_English)
    mtoeButton.grid(row = 0, column = 0, padx = 50)

    etomButton = Button(buttonFrame2, text = "Text to Morse", font = "10", bg = '#000000', fg = '#fff', command = English_to_Morse)
    etomButton.grid(row = 0, column = 1)

# converter 
def English_to_Morse():
    #logic
    def convertion():
        if(entry.get() == ''):
            messagebox.showwarning("Warning","Please fill all the fields!!")
        else:
            data = {
                "A" : ".-",
                "B" : "-...",
                "C" : "-.-.",
                "D" : "-..",
                "E" : ".",
                "F" : "..-.",
                "G" : "--.",
                "H" : "....",
                "I" : "..",
                "J" : ".---",
                "K" : "-.-",
                "L" : ".-..",
                "M" : "--",
                "N" : "-.",
                "O":"---",
                "P":".--.",
                "Q":"--.-",
                "R":".-.",
                "S":"...",
                "T":"-",
                "U":"..-",
                "V":"...-",
                "W":".--",
                "X":"-..-",
                "Y":"-.--",
                "Z":"--..",
                "1":".----",
                "2":"..---",
                "3":"...--",
                "4":"....-",
                "5":".....",
                "6":"-....",
                "7":"--...",
                "8":"---..",
                "9":"----.",
                "0":"-----",
            }
            error = 0
            text = ''
            for i in entry.get():
                if i == ' ':
                    text = text + i
                else:
                    try:
                        text = text + data[i.capitalize()] + ' '
                    except KeyError:
                        messagebox.showwarning("Warning","special characters are not allowed")
                        error = 1
                        break
            if error == 0:
                label3.grid()
                getvalue.grid()
                get.set(text)
                if registered == True:
                    #connect databse first
                    db = mysql.connector.connect(host='localhost',user='root',password='<your_myssql_password>',database='pythonproject')#databse credentials depends on a User
                    #checking if databse is connected or not
                    if(db):
                        myCursor = db.cursor()
                        #create table if it not exists
                        tableSql = r"CREATE TABLE IF NOT EXISTS texttomorsehistory( id int(255) PRIMARY KEY AUTO_INCREMENT, text varchar(255) NOT NULL, morseCode varchar(255) NOT NULL, userid int(255) NOT NULL)"
                        myCursor.execute(tableSql)

                        #inserting data to texttomorsehistory table to store the history
                        storeHistorySql = "INSERT INTO texttomorsehistory(text, morseCode, userid) VALUES(%s,%s,%s)"
                        myCursor.execute(storeHistorySql, (entry.get(),text,loginedUserData[0]))
                        db.commit()
                        resultExecution = myCursor.rowcount
                        if(resultExecution == 1):
                            myCursor.close()
                            db.close()
                            messagebox.showinfo("Success","Conversion completed!!")
                        else:
                            myCursor.close()
                            db.close()
                            messagebox.showwarning("Warning","Something went wrong while adding to history!!")
                    else:
                        messagebox.showwarning("Warning","Database is not connected!!")
                else:
                    messagebox.showinfo("Info","If you want to save this in your history please try conversion again after login, to this application!!")
            else:
                entry.set("")

    # GUI
    # fixed to remove overlaping bug
    global tapetom
    tapetom = True
    global countEtoM
    countEtoM += 1
    
    if(tapmtoe == True):
        global countMtoE
        mtoeFrame.grid_remove()
        #updating countMtoE and making it zero to start over when morse_to_english was call tap-morse-to-english(tapmtoe) becomes true and this condition execute
        countMtoE = 0
    #fix end

    global etomFrame

    if(countEtoM == 1):
        etomFrame = Frame(windowIndex)
        etomFrame.grid(row = 1, column = 0, columnspan = 2)

        label2 = Label(etomFrame, text = "Text")
        label2.grid(row = 1, column = 0, pady = (50,0))

        label3 = Label(etomFrame, text = "Morse")
        label3.grid(row = 2, column = 0, pady = (10,0))
        label3.grid_remove()

        entry = StringVar()
        get = StringVar()

        value = Entry(etomFrame, textvariable = entry )
        value.grid(row = 1, column = 1, pady = (50,0))

        getvalue = Entry(etomFrame, textvariable=get)#getting the text value
        getvalue.grid(row = 2, column = 1, pady = (10,0))
        getvalue.grid_remove()

        Convert = Button(etomFrame, text = "Convert", bg = '#000000', fg = '#fff', command = convertion)
        Convert.grid( row  =  3, column = 1, pady = (30,0))

        def goBack():
            global countEtoM
            buttonFrame2.grid_remove()
            etomFrame.grid_remove()
            #updating countMtoE and making it zero to start over after go back is press
            countEtoM = 0
            if registered == True:
                head.grid()
                logoutButton.grid()
                converterButton.grid()
                historyButton.grid()
            else:
                head.grid()
                loginButton.grid()
                signupButton.grid()
                guestButton.grid()
                bottomFrame.grid()

        gobackButton = Button(etomFrame, text = "Go Back", font = "10", bg = '#000000', fg = '#fff', command = goBack)
        gobackButton.grid(row = 5, column = 1, pady = (10,0))

        code = Button(etomFrame, text = "Morse Code Table", bg = '#000000', fg = '#fff', command = morseCodeWin)
        code.grid(row = 4, column = 1, pady = (10,0))
    

def Morse_to_English():

    messagebox.showinfo("Info","Please add space after morse code value of each character to get correct result!!")
    def convertion():
        if(entry.get() == ''):
            messagebox.showwarning("Warning","Please fill all the fields!!")
        elif entry.get().find(" ") == -1:
            messagebox.showwarning("Warning","Please add space after each morse code value!!")
        else:
            data = {
                "A" : ".-",
                "B" : "-...",
                "C" : "-.-.",
                "D" : "-..",
                "E" : ".",
                "F" : "..-.",
                "G" : "--.",
                "H" : "....",
                "I" : "..",
                "J" : ".---",
                "K" : "-.-",
                "L" : ".-..",
                "M" : "--",
                "N" : "-.",
                "O" : "---",
                "P" : ".--.",
                "Q" : "--.-",
                "R" : ".-.",
                "S" : "...",
                "T" : "-",
                "U" : "..-",
                "V" : "...-",
                "W" : ".--",
                "X" : "-..-",
                "Y" : "-.--",
                "Z" : "--..",
                "1" : ".----",
                "2" : "..---",
                "3" : "...--",
                "4" : "....-",
                "5" : ".....",
                "6" : "-....",
                "7" : "--...",
                "8" : "---..",
                "9" : "----.",
                "0" : "-----",
            }
            error = 0
            text = ''
            for i in entry.get().split():
                try:
                    text = text + list(data.keys())[list(data.values()).index(i)] #conversion
                except ValueError:
                    messagebox.showwarning("Warning","Please enter the valid morse code")
                    error = 1
                    break
            if error == 0:
                label3.grid()
                getvalue.grid()
                # setting the value of text in get entry
                get.set(text)
                if registered == True:
                    #connect databse first
                    db = mysql.connector.connect(host='localhost',user='root',password='<your_myssql_password>',database='pythonproject')#database credentials depends on user
                    #checking if databse is connected or not
                    if(db):
                        myCursor = db.cursor()
                        #create table if it not exists
                        tableSql = r"CREATE TABLE IF NOT EXISTS morsetotexthistory( id int(255) PRIMARY KEY AUTO_INCREMENT, text varchar(255) NOT NULL, morseCode varchar(255) NOT NULL, userid int(255) NOT NULL)"
                        myCursor.execute(tableSql)

                        #inserting data to texttomorsehistory table to store the history
                        storeHistorySql = "INSERT INTO morsetotexthistory(text, morseCode, userid) VALUES(%s,%s,%s)"
                        myCursor.execute(storeHistorySql, (entry.get(),text,loginedUserData[0]))
                        db.commit()
                        resultExecution = myCursor.rowcount
                        if(resultExecution == 1):
                            myCursor.close()
                            db.close()
                            messagebox.showinfo("Success","Conversion completed!!")
                        else:
                            myCursor.close()
                            db.close()
                            messagebox.showwarning("Warning","Something went wrong while adding history!!")
                    else:
                        messagebox.showwarning("Warning","Database is not connected!!")
                else:
                    messagebox.showinfo("Info","If you want to save this in your history, please try conversion again after login, to this application!!")
            else:
                entry.set("")

    # GUI
    # fixed to remove overlaping bug
    global tapmtoe
    tapmtoe = True
    
    global countMtoE
    countMtoE += 1
    
    if(tapetom == True):
        global countEtoM
        etomFrame.grid_remove()
        #updating countMtoE and making it zero to start over when english_to_morse was call tap-english-to-morse(tapetom) becomes true and this condition execute
        countEtoM = 0
    #fix end
    
    global mtoeFrame
    if(countMtoE == 1): 
        mtoeFrame = Frame(windowIndex)
        mtoeFrame.grid(row = 1, column = 0, columnspan = 2)

        label2 = Label(mtoeFrame, text = "Morse")
        label2.grid(row = 1, column = 0, pady = (50,0))

        label3 = Label(mtoeFrame, text = "Text")
        label3.grid(row = 2, column = 0, pady = (10,0))
        label3.grid_remove()

        entry = StringVar()
        get = StringVar()

        value = Entry(mtoeFrame, textvariable = entry)
        value.grid(row = 1, column = 1, pady = (50,0))

        getvalue = Entry(mtoeFrame, textvariable = get)#showing the converted code to get variable
        getvalue.grid(row = 2, column = 1, pady = (10,0))
        getvalue.grid_remove()
        
        Convert = Button(mtoeFrame, text = "Convert", bg = '#000000', fg = '#fff', command = convertion)
        Convert.grid( row  =  3, column = 1, pady = (30,0))

        def goBack():
            global countMtoE
            buttonFrame2.grid_remove()
            mtoeFrame.grid_remove()
            #updating countMtoE and making it zero to start over after go back is press
            countMtoE = 0 
            if registered == True:
                head.grid()
                logoutButton.grid()
                converterButton.grid()
                historyButton.grid()
            else:
                head.grid()
                loginButton.grid()
                signupButton.grid()
                guestButton.grid()
                bottomFrame.grid()

        gobackButton = Button(mtoeFrame, text = "Go Back", font = "10", bg = '#000000', fg = '#fff', command = goBack)
        gobackButton.grid(row = 5, column = 1, pady = (10,0))

        code = Button(mtoeFrame, text = "Morse Code Table", bg = '#000000', fg = '#fff', command = morseCodeWin)
        code.grid(row = 4, column = 1, pady = (10,0))

# login form 
def loginForm():
    head.grid_remove()
    loginButton.grid_remove()
    signupButton.grid_remove()
    guestButton.grid_remove()
    logoutButton.grid_remove()
    converterButton.grid_remove()
    historyButton.grid_remove()
    bottomFrame.grid_remove()

    #new login form frame created here

    loginHead = Label(windowIndex, text = "Login Form", font = "Verdana 25 bold")
    loginHead.grid(row = 0, column = 0, columnspan = 2, padx = 205, pady = (100,0))

    loginFrame = Frame()
    loginFrame.grid(row = 1, column = 0, columnspan = 2)

    usernamevalue = StringVar()
    passwordvalue = StringVar()

    username = Label(loginFrame, text = "Email", font = "12")
    username.grid(row = 1, column = 0, pady = (15,5))
    usernameEntry = Entry(loginFrame, textvariable = usernamevalue)
    usernameEntry.grid(row = 1, column = 1, pady = (15,5))

    password = Label(loginFrame, text = "Password", font = "12")
    password.grid(row = 2, column = 0, pady = 5)
    passwordEntry = Entry(loginFrame, show = "*", textvariable = passwordvalue)
    passwordEntry.grid(row = 2, column = 1, pady = 5)

    def goBack():
        loginHead.grid_remove()
        loginFrame.grid_remove()
        head.grid()
        loginButton.grid()
        signupButton.grid()
        guestButton.grid()
        bottomFrame.grid()
    
    # login user 
    def loginUser():
        global registered
        global loginedUserData
        # validate the user 
        if(usernamevalue.get() == '' or passwordvalue.get() == ''):
            messagebox.showwarning('Warning','Please fill all the fields!!')
        else:
            errors = 0
            #validating email
            if(not re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",usernamevalue.get().lower())):
                messagebox.showwarning("Warning", "Please enter valid email")
                errors = errors + 1
            if(errors == 0):
                # if there is no error connect to the database
                db = mysql.connector.connect(host='localhost',user='root',password='<your_myssql_password>',database='pythonproject')#database credentials depends on user
                # checking if database is connected or not
                if(db):
                    # creating database cursor 
                    myCursor = db.cursor()
                    # creating database first if it is not created
                    myCursor.execute("CREATE TABLE IF NOT EXISTS users(userId int(255) PRIMARY KEY AUTO_INCREMENT,name varchar(255) NOT NULL,email TINYTEXT NOT NULL,phonenumber int(11) NOT NULL,pass varchar(255) NOT NULL)")
                    # checking if the email is already present or not 
                    emailCheckSql = r"SELECT * FROM users WHERE email='"+usernamevalue.get()+"'"
                    myCursor.execute(emailCheckSql)
                    result = myCursor.fetchone()
                    if(myCursor.rowcount > 0):
                        # here email is present then verify the user password
                        if(passwordvalue.get() == result[-1]):
                            # setting login varible true
                            registered = True
                            # saving the logined user information to loginedUserData variable
                            loginedUserData = result
                            myCursor.close()
                            db.close()
                            #send user back to home screen and show to logout and converter and history button
                            loginHead.grid_remove()
                            loginFrame.grid_remove()
                            head.grid()
                            logoutButton.grid()
                            converterButton.grid()
                            historyButton.grid()
                            bottomFrame.grid()
                            messagebox.showinfo("Success","You are successfully logged in!!")
                        else:
                            myCursor.close()
                            db.close()
                            messagebox.showwarning("Warning","Wrong password or email!!")
                    else:
                        myCursor.close()
                        db.close()
                        messagebox.showwarning("Warning","Please register first!!")
                else:
                    messagebox.showwarning("Warning","Database is not connected!")  

    
    loginButton1 = Button(loginFrame, text = "Login", font = "10", bg = '#000000', fg = '#fff', command = loginUser)
    loginButton1.grid(row = 3, column = 0, columnspan = 2, pady = (15,0))

    gobackButton = Button(loginFrame, text = "Go Back", font = "10", bg = '#000000', fg = '#fff', command = goBack)
    gobackButton.grid(row = 4, column = 0, columnspan = 2, pady = (10,0))



# registration form 
def signupForm():
    head.grid_remove()
    loginButton.grid_remove()
    signupButton.grid_remove()
    guestButton.grid_remove()
    logoutButton.grid_remove()
    converterButton.grid_remove()
    historyButton.grid_remove()
    bottomFrame.grid_remove()

    #new frame for signup
    signupHead = Label(windowIndex, text = "Registration Form", font = "Verdana 25 bold")
    signupHead.grid(row = 0, column = 0, columnspan = 2, padx = 145, pady = (25,0))

    signupFrame = Frame()
    signupFrame.grid(row = 1, column = 0, columnspan = 2, pady = (20,0))

    #validation and register a user
    def validation():
        errors = 0
        if(namevalue.get() == '' or emailvalue.get() == '' or phonenumbervalue.get() == '' or passwordvalue.get() == '' or confirmpassvalue.get() == ''):
            messagebox.showwarning("Warning", "Please enter all fields")
            errors = errors + 1
        else:
            #validating name field
            if(not re.search("^[a-zA-Z].*",namevalue.get()) or re.search("[0-9]",namevalue.get())):
                messagebox.showwarning("Warning", "Name Should be in alphabets only")
                errors = errors + 1
            #validating email
            if(not re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",emailvalue.get().lower())):
                messagebox.showwarning("Warning", "Please enter valid email")
                errors = errors + 1
            #validating phone number
            if(not re.search("^[0-9].*$",phonenumbervalue.get()) or len(phonenumbervalue.get()) < 10):
                messagebox.showwarning("Warning", "Please enter valid phone number")
                errors = errors + 1
            #validating password
            if( passwordvalue.get() == '' or len(passwordvalue.get()) < 6 ):
                messagebox.showwarning("Warning", "Password should be atleast of 6 characters")
                errors = errors + 1
            #confirming password
            if(passwordvalue.get() != confirmpassvalue.get()):
                messagebox.showwarning("Warning", "Password is not matching")
                errors = errors + 1
            #checking if errors are there or not
            if(errors == 0):
                # if there is no error connect to the database
                db = mysql.connector.connect(host='localhost',user='root',password='<your_myssql_password>',database='pythonproject')#database credentials depends on user
                # checking if database is connected or not
                if(db):
                    # creating database cursor 
                    myCursor = db.cursor()
                    # creating database first if it is not created
                    myCursor.execute("CREATE TABLE IF NOT EXISTS users(userId int(255) PRIMARY KEY AUTO_INCREMENT,name varchar(255) NOT NULL,email TINYTEXT NOT NULL,phonenumber int(11) NOT NULL,pass varchar(255) NOT NULL)")
                    # checking if the email is already present or not 
                    emailCheckSql = r"SELECT * FROM users WHERE email='"+emailvalue.get()+"'"
                    myCursor.execute(emailCheckSql)
                    myCursor.fetchall()
                    if(myCursor.rowcount < 1):
                        # here email is not present then inserting the data and register the user
                        insertionSql = "INSERT INTO users(email,phonenumber,name,pass) VALUES(%s,%s,%s,%s)"
                        myCursor.execute(insertionSql,(emailvalue.get(), phonenumbervalue.get(),namevalue.get(),passwordvalue.get()))
                        db.commit()
                        if(myCursor.rowcount == 1):
                            myCursor.close()
                            db.close()
                            signupHead.grid_remove()
                            signupFrame.grid_remove()
                            head.grid()
                            loginButton.grid()
                            signupButton.grid()
                            guestButton.grid()
                            bottomFrame.grid()
                            messagebox.showinfo("Success", "You are registered successfully!!")
                        else:
                            messagebox.showwarning("Warning","Something went wrong while inserting the data!!")
                    else:
                        myCursor.close()
                        db.close()
                        messagebox.showwarning("Warning","This Email is already registered!!")
                else:
                    messagebox.showwarning("Warning","Database is not connected!")                

               

    #declaration
    name = Label(signupFrame, text = "Name", font = "12")
    email = Label(signupFrame, text = "Email", font = "12")
    phonenumber = Label(signupFrame, text = "Phone No.", font = "12")
    password = Label(signupFrame, text = "Password", font = "12")
    confirmpass = Label(signupFrame, text = "Confirm Password", font = "12")
    

    #packing declarations
    name.grid(row = 1,column = 0, pady = (0,5))
    email.grid(row = 2, column = 0, pady = (0,5))
    phonenumber.grid(row = 3, column = 0, pady = (0,5))
    password.grid(row = 4, column = 0, pady = (0,5))
    confirmpass.grid(row = 5, column = 0, pady = (0,5))

    #variables
    namevalue = StringVar()
    emailvalue = StringVar()
    phonenumbervalue = StringVar()
    passwordvalue = StringVar()
    confirmpassvalue = StringVar()

    #Entries
    nameentry = Entry(signupFrame, textvariable = namevalue)
    emailentry = Entry(signupFrame, textvariable = emailvalue)
    phonenumberentry = Entry(signupFrame, textvariable = phonenumbervalue)
    passwordentry = Entry(signupFrame,show = "*", textvariable = passwordvalue) 
    confirmpassentry = Entry(signupFrame, show = "*", textvariable = confirmpassvalue)

    #packing entries
    nameentry.grid(row = 1, column = 1, pady = (0,5))
    emailentry.grid(row = 2, column = 1, pady = (0,5))
    phonenumberentry.grid(row = 3, column = 1, pady = (0,5))
    passwordentry.grid(row = 4, column = 1, pady = (0,5))
    confirmpassentry.grid(row = 5, column = 1, pady = (0,5))


    def goBack():
        signupHead.grid_remove()
        signupFrame.grid_remove()
        head.grid()
        loginButton.grid()
        signupButton.grid()
        guestButton.grid()
        bottomFrame.grid()

    
    submit = Button(signupFrame, text = "Submit", font = "10", bg = '#000000', fg = '#fff', command = validation)
    submit.grid(row = 6, column = 0, columnspan = 2, ipadx = 8, ipady = 2, pady = (20,0))
    goBack = Button(signupFrame, text = "Go back", font = "10", bg = '#000000', fg = '#fff', command = goBack)
    goBack.grid(row = 7, column = 0, columnspan = 2, ipadx = 6, ipady = 2, pady = (10,0))


# logout the user 
def logout():
    global registered 
    registered = False
    logoutButton.grid_remove()
    converterButton.grid_remove()
    historyButton.grid_remove()
    loginButton.grid()
    signupButton.grid()
    guestButton.grid()    

# watch history for logined user
def history():
    # connecting to database 
    db = mysql.connector.connect(host='localhost',user='root',password='<your_myssql_password>',database='pythonproject')#database credentials depends on user
    if(db):
        # creating cursor 
        myCursor = db.cursor()
        #sql statements for texttomorsehistory and morsetotexthistory
        # loginedUserData[0]
        texttomorsehistorySql = r"SELECT * FROM texttomorsehistory WHERE userid = '"+str(loginedUserData[0])+"'"
        morsetotexthistorySql = r"SELECT * FROM morsetotexthistory WHERE userid = '"+str(loginedUserData[0])+"'"

        myCursor.execute(texttomorsehistorySql)
        result1 = myCursor.fetchall()
        
        # print("this is list of tuples",result1)

        texttomorsehistorylist = list()
        for i in result1:
            texttomorsehistorylist.append(i)
        # print(texttomorsehistorylist)

        myCursor.execute(morsetotexthistorySql)
        result2 = myCursor.fetchall()

        morsetotexthistorylist = list()
        for i in result2:
            morsetotexthistorylist.append(i)
        
        # making frames
        windowindex3 = Tk()

        windowindex3.geometry("1366x1280")
        windowindex3.maxsize(1920,1280)
        windowindex3.minsize(1366,1280)
        windowindex3.title("Conversion history")

        l1 = Label(windowindex3, text = "Morse Code History", font = "Verdana 14", bg = "black", fg = "white")
        l1.grid(row = 0, column = 1,columnspan = 2,  pady = 50)


        l2 = Label(windowindex3, text="Morse to Text conversion", font="Verdana 14 bold",width=50)
        l2.grid(row=1, column=0,columnspan=2)

        l3 = Label(windowindex3, text="Text to Morse conversion", font="Verdana 14 bold",width=50)
        l3.grid(row=1, column=2,columnspan=2)

        global row
        row = 3 
        if len(morsetotexthistorylist) != 0: #if the list is not empty then it will print the data in given format
            for i in morsetotexthistorylist:
                Label(windowindex3, text=str(i[1])+'=> '+str(i[2]), font='Verdana 12', fg="grey").grid(row=row+1,column=0,columnspan=2)
                row = row+1
        else:
            Label(windowindex3, text="No data Found", font='Verdana 12', fg="grey").grid(row=4,column=0,columnspan=2)

        # l3 = Label(windowindex3, text="Text to Morse conversion", font="Verdana 14 bold",width=50)
        # l3.grid(row=3, column=4,columnspan=3)
        row = 3
        if len(texttomorsehistorylist) != 0:
            for i in texttomorsehistorylist:
                Label(windowindex3, text=str(i[1])+'=> '+str(i[2]), font='Verdana 12', fg="grey").grid(row=row+1,column=2,columnspan=2)
                row = row+1
        else:
            Label(windowindex3, text="No data Found", font='Verdana 12', fg="grey").grid(row=4,column=4,columnspan=3)

        windowindex3.mainloop()
    else:
        messagebox.showwarning("Warning","Database is not connected!!")

# main window 
def mainWindow():
    global windowIndex
    global headFrame, head
    global buttonFrame, loginButton, signupButton, guestButton
    global bottomFrame
    global logoutButton,converterButton,historyButton
    
    
    
    windowIndex = Tk()
    windowIndex.geometry('620x420')
    windowIndex.maxsize(620,420)
    windowIndex.minsize(620,420)

    windowIndex.title('Morse Code Converter')

    headFrame = Frame()
    headFrame.grid(row = 0, column = 0)

    head = Label(windowIndex, text="Morse Code Converter", font = "Verdana 30 bold")
    head.grid(row = 0, column = 0, padx = 60, pady = (90,0))


    buttonFrame = Frame()
    buttonFrame.grid(row = 1, column = 0, pady = 40)

    # as bg not work on mac so "highlightbackground='#141313' "
    # if the use is not logined then this will happen
    logoutButton = Button(buttonFrame, text='Logout', font = "15", height = 2, width = 8, bg = '#000000', fg = '#fff', command=logout)
    logoutButton.grid(row = 2, column = 0, padx = 10, pady = 10)
    # go to converter 
    converterButton = Button(buttonFrame, text='Converter', font = "15", height = 2, width = 8, highlightbackground='#000000', bg = '#000000', fg = '#fff', command=guest)
    converterButton.grid(row = 2, column = 1, padx = 10, pady = 10)
    # if user is logined he can watch history 
    historyButton = Button(buttonFrame, text='History', font = "15", height = 2, width = 8, highlightbackground='#000000', bg = '#000000', fg = '#fff', command=history)
    historyButton.grid(row = 2, column = 2, padx = 10, pady = 10)

    
    loginButton = Button(buttonFrame, text='Login', font = "15", height = 2, width = 8, bg = '#000000', fg = '#fff', command=loginForm)
    loginButton.grid(row = 2, column = 0, padx = 10, pady = 10)

    signupButton = Button(buttonFrame, text='Signup', font = "15", height = 2, width = 8, highlightbackground='#000000', bg = '#000000', fg = '#fff', command=signupForm)
    signupButton.grid(row = 2, column = 1, padx = 10, pady = 10)

    guestButton = Button(buttonFrame, text='Guest', font = "15", height = 2, width = 8, highlightbackground='#000000', bg = '#000000', fg = '#fff', command=guest)
    guestButton.grid(row = 2, column = 2, padx = 10, pady = 10)


    bottomFrame = Frame()
    bottomFrame.grid(row = 3, column = 0, pady = (90,0))

    foot = Label(bottomFrame, text = "Morse Code Converter by Akash Singh Panwar, Aman Kumar, Raman Sharma")
    foot.grid(row = 3, column = 0)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            windowIndex.destroy()

    windowIndex.protocol("WM_DELETE_WINDOW", on_closing)
    windowIndex.mainloop()
    
mainWindow()
