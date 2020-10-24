# working and developing on python 3.8.6
 
from tkinter import Tk
from tkinter import *
import sys

tapetom = None
tapmtoe = None

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

def guest():
    head.grid_remove()
    loginButton.grid_remove()
    signupButton.grid_remove()
    guestButton.grid_remove()
    bottomFrame.grid_remove()

    global buttonFrame2

    buttonFrame2 = Frame(windowIndex)
    buttonFrame2.grid(row = 0, column = 0, columnspan = 2, padx = 100, pady = (50,0))

    mtoeButton = Button(buttonFrame2, text = "Morse to English", font = "10", bg = '#000000', fg = '#fff', command = Morse_to_English)
    mtoeButton.grid(row = 0, column = 0, padx = 50)

    etomButton = Button(buttonFrame2, text = "English to Morse", font = "10", bg = '#000000', fg = '#fff', command = English_to_Morse)
    etomButton.grid(row = 0, column = 1)


def English_to_Morse():

    global tapetom
    tapetom = True
    
    if(tapmtoe == True):
        mtoeFrame.grid_remove()
        tapmtoe == False

    global etomFrame
    etomFrame = Frame(windowIndex)
    etomFrame.grid(row = 1, column = 0, columnspan = 2)

    label2 = Label(etomFrame, text = "English")
    label2.grid(row = 1, column = 0, pady = (50,0))

    label3 = Label(etomFrame, text = "Morse")
    label3.grid(row = 2, column = 0, pady = (10,0))

    entry = StringVar()
    get = StringVar()

    value = Entry(etomFrame, textvariable = entry )
    value.grid(row = 1, column = 1, pady = (50,0))

    getvalue = Entry(etomFrame, textvariable = get)########################################
    getvalue.grid(row = 2, column = 1, pady = (10,0))

    Convert = Button(etomFrame, text = "Convert", bg = '#000000', fg = '#fff', command = sys.exit)
    Convert.grid( row  =  3, column = 1, pady = (30,0))

    def goBack():
        buttonFrame2.grid_remove()
        etomFrame.grid_remove()
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

    global tapmtoe
    tapmtoe = True
    
    if(tapetom == True):
        etomFrame.grid_remove()
        tapetom == False

    global mtoeFrame
    mtoeFrame = Frame(windowIndex)
    mtoeFrame.grid(row = 1, column = 0, columnspan = 2)

    label2 = Label(mtoeFrame, text = "Morse")
    label2.grid(row = 1, column = 0, pady = (50,0))

    label3 = Label(mtoeFrame, text = "English")
    label3.grid(row = 2, column = 0, pady = (10,0))

    entry = StringVar()
    get = StringVar()

    value = Entry(mtoeFrame, textvariable = entry)
    value.grid(row = 1, column = 1, pady = (50,0))

    getvalue = Entry(mtoeFrame, textvariable = get)########################################
    getvalue.grid(row = 2, column = 1, pady = (10,0))
    
    Convert = Button(mtoeFrame, text = "Convert", bg = '#000000', fg = '#fff', command = sys.exit)
    Convert.grid( row  =  3, column = 1, pady = (30,0))

    def goBack():
        buttonFrame2.grid_remove()
        mtoeFrame.grid_remove()
        head.grid()
        loginButton.grid()
        signupButton.grid()
        guestButton.grid()
        bottomFrame.grid()

    gobackButton = Button(mtoeFrame, text = "Go Back", font = "10", bg = '#000000', fg = '#fff', command = goBack)
    gobackButton.grid(row = 5, column = 1, pady = (10,0))

    code = Button(mtoeFrame, text = "Morse Code Table", bg = '#000000', fg = '#fff', command = morseCodeWin)
    code.grid(row = 4, column = 1, pady = (10,0))

def loginForm():
    head.grid_remove()
    loginButton.grid_remove()
    signupButton.grid_remove()
    guestButton.grid_remove()
    bottomFrame.grid_remove()

    #new login form frame created here

    loginHead = Label(windowIndex, text = "Login Form", font = "Verdana 25 bold")
    loginHead.grid(row = 0, column = 0, columnspan = 2, padx = 205, pady = (100,0))

    loginFrame = Frame()
    loginFrame.grid(row = 1, column = 0, columnspan = 2)

    usernamevalue = StringVar()
    passwordvalue = StringVar()

    username = Label(loginFrame, text = "Username", font = "12")
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
    
    loginButton1 = Button(loginFrame, text = "Login", font = "10", bg = '#000000', fg = '#fff', command = sys.exit)
    loginButton1.grid(row = 3, column = 0, columnspan = 2, pady = (15,0))

    gobackButton = Button(loginFrame, text = "Go Back", font = "10", bg = '#000000', fg = '#fff', command = goBack)
    gobackButton.grid(row = 4, column = 0, columnspan = 2, pady = (10,0))


def signupForm():
    head.grid_remove()
    loginButton.grid_remove()
    signupButton.grid_remove()
    guestButton.grid_remove()
    bottomFrame.grid_remove()

    
    #new frame for signup

    #signupHeadFont = font.Font(family = "Verdana", weight = "bold", size = 25)
    signupHead = Label(windowIndex, text = "Registration Form", font = "Verdana 25 bold")
    signupHead.grid(row = 0, column = 0, columnspan = 2, padx = 145, pady = (25,0))

    signupFrame = Frame()
    signupFrame.grid(row = 1, column = 0, columnspan = 2, pady = (20,0))

    #validation
    # def validation():
    #     if(namevalue.get().isalpha() == False):
    #         namevalue.set("Alphabet")
    #         messagebox.showwarning("Warning", "Name Should be alphabet only")

    #labelFont = font.Font(size = 12)
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
    phonenumbervalue = IntVar()
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

    #     f.write(f"{namevalue.get(), phonenumbervalue.get(), emailvalue.get(), passwordvalue.get(), termsvalue.get()}\n")

    def goBack():
        signupHead.grid_remove()
        signupFrame.grid_remove()
        head.grid()
        loginButton.grid()
        signupButton.grid()
        guestButton.grid()
        bottomFrame.grid()

    
    #buttonFont = font.Font(size=10)
    submit = Button(signupFrame, text = "Submit", font = "10", bg = '#000000', fg = '#fff', command = goBack)
    submit.grid(row = 6, column = 0, columnspan = 2, ipadx = 8, ipady = 2, pady = (20,0))
    goBack = Button(signupFrame, text = "Go back", font = "10", bg = '#000000', fg = '#fff', command = goBack)
    goBack.grid(row = 7, column = 0, columnspan = 2, ipadx = 6, ipady = 2, pady = (10,0))



def mainWindow():
    global windowIndex
    global headFrame, head
    global buttonFrame, loginButton, signupButton, guestButton
    global bottomFrame
    
    windowIndex = Tk()
    windowIndex.geometry('620x420')
    windowIndex.maxsize(620,420)
    windowIndex.minsize(620,420)

    windowIndex.title('Morse Code Converter')

    #windowInnerFrame = Frame(windowIndex)
    #windowInnerFrame.grid(row = 1, column = 2)
    #windowInnerFrame.config(bg='dark green')

    headFrame = Frame()
    headFrame.grid(row = 0, column = 0)
    #headFrame.place(x=70, y=80)

    #headFont = font.Font(family = "Verdana", weight = 'bold', size = 30)
    head = Label(windowIndex, text="Morse Code Converter", font = "Verdana 30 bold")
    head.grid(row = 0, column = 0, padx = 60, pady = (90,0))
    #headFrame.place(x=75, y=150)


    buttonFrame = Frame()
    buttonFrame.grid(row = 1, column = 0, pady = 40)
    #buttonFrame.place(x=225, y=280)

    #loginFont = font.Font(size = 15)
    # as bg not work on mac so "highlightbackground='#141313' "
    loginButton = Button(buttonFrame, text='Login', font = "15", height = 2, width = 8, bg = '#000000', fg = '#fff', command=loginForm)
    loginButton.grid(row = 2, column = 0, padx = 10, pady = 10)

    signupButton = Button(buttonFrame, text='Signup', font = "15", height = 2, width = 8, highlightbackground='#000000', bg = '#000000', fg = '#fff', command=signupForm)
    signupButton.grid(row = 2, column = 1, padx = 10, pady = 10)

    guestButton = Button(buttonFrame, text='Guest', font = "15", height = 2, width = 8, highlightbackground='#000000', bg = '#000000', fg = '#fff', command=guest)
    guestButton.grid(row = 2, column = 2, padx = 10, pady = 10)

    #for aligning buttons in center
    #windowIndex.grid_rowconfigure(1, weight = 1) # aligning buttons vertically
    #windowIndex.grid_columnconfigure(0, weight=1) # this will align both buttons and label horizontally center

    bottomFrame = Frame()
    bottomFrame.grid(row = 3, column = 0, pady = (90,0))
    #bottomFrame.place(x=240, y=580)

    foot = Label(bottomFrame, text = "Morse Coverter by Akash Singh Panwar, Aman Kumar, Raman Sharma")
    foot.grid(row = 3, column = 0)

    windowIndex.mainloop()

mainWindow()