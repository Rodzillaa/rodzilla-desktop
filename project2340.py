import pymysql
from Tkinter import *
import base64
import os
import requests
import random


class project2340:
    ## initialize and create the root window
    def __init__(self, root):
        self.root = root
        self.root.title ("New York Rat Report")
        #self.root.configure (background = "blue")
        self.login()

    #function which creates the login window 
    def login (self):

        self.sv1 = StringVar()
        
        #create the 2 frames
        self.frame1 = Frame(self.root, bg = "gold")
        self.frame1.pack(side = TOP, fill = X)
        self.frame2 = Frame (self.root, bg = "gold")
        self.frame2.pack(side = TOP, fill = X)

        #the labels
        self.userLabel = Label(self.frame1, text = "Username:",bg = "gold")
        self.userLabel.grid(row = 1, column = 0, sticky = E)
        self.passwdLabel = Label(self.frame1, text = "Password:", bg = "gold")
        self.passwdLabel.grid(row = 2, column = 0, sticky = E)
    

        #the entries 
        self.userEntry = Entry(self.frame1, width = 30, textvariable = self.sv1)
        self.userEntry.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.passwdEntry = Entry(self.frame1, width = 30)
        self.passwdEntry.grid(row = 2, column = 1, padx = 5, pady = 5)

        #the buttons
        self.loginButton = Button (self.frame2, text = "Login", command = self.loginCheck)
        self.loginButton.pack(fill = X, anchor = E, side = RIGHT)
        self.registerButton = Button(self.frame2, text= "Register", command = self.register)
        self.registerButton.pack(fill = X, anchor = E, side = RIGHT)

    #function that gets called upon once you hit cancel that pulls up the login window again
    def login2 (self):
        
       self.register.withdraw()
       self.root.deiconify()
       
    def register (self):

        #show only the register
        self.root.withdraw ()
        self.register = Toplevel()
        self.register.title("New User Registration Page")

        #create the 2 frames
        self.frame1 = Frame(self.register, bg = "gold")
        self.frame1.pack(side = TOP,fill = X)
        self.frame2 = Frame (self.register, bg = "gold")
        self.frame2.pack(side = TOP, fill = X)
        self.frame3 = Frame (self.register, bg = "gold")
        self.frame3.pack(side = TOP, fill = X)


        #all of the labels 
        self.nameLabel2 = Label(self.frame1, text = "Name:",bg = "gold")
        self.nameLabel2.grid(row = 1, column = 0, sticky = E)
        self.userLabel2 = Label(self.frame1, text = "Username:", bg = "gold")
        self.userLabel2.grid(row = 2,  column = 0, sticky = E)
        self.passwdLabel2 = Label(self.frame1, text = "Password:",bg = "gold")
        self.passwdLabel2.grid(row = 3, column = 0, sticky = E)

        #all of the entries
        self.nameEntry2 = Entry(self.frame1, width = 30)
        self.nameEntry2.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.userEntry2 = Entry(self.frame1, width = 30)
        self.userEntry2.grid(row = 2, column = 1, padx = 5, pady = 5)
        self.passwdEntry2 = Entry(self.frame1, width = 30)
        self.passwdEntry2.grid(row = 3, column = 1, padx = 5, pady = 5)

        #all the buttons
        self.cancelButton2 = Button (self.frame2, text = "Cancel", command = self.login2)
        self.cancelButton2.pack(fill = X, anchor = E, side = RIGHT)
        self.registerButton2 = Button(self.frame2, text= "Register", command = self.registerCheck)
        self.registerButton2.pack(fill = X, anchor = E, side = RIGHT)

        #AdminCheckbox
        global registerVar
        var = StringVar()
        self.adminCheckbox = Checkbutton(self.frame2, text = "Check if you are an admin", variable = registerVar)
        self.adminCheckbox.pack()                
        


    def mainPage(self):
        #submit a rat sightings
        #list of recent rat sightings
        #view data graphs
        #view map
        #logout
        #show only the main page
        self.root.withdraw ()
        self.mainPage = Toplevel()
        self.mainPage.title("Dashboard")

        #create the 2 frames
        self.frame1 = Frame(self.mainPage, bg = "gold")
        self.frame1.pack(side = TOP, fill = X)
        self.frame2 = Frame (self.mainPage, bg = "gold")
        self.frame2.pack(side = TOP, fill = X)

        #creating buttons
        self.submitButton = Button (self.frame2, text = "Submit Rat Report", command = self.submitReport)
        self.submitButton.grid(row = 1, column = 0)
        self.listButton = Button(self.frame2, text= "List of  recent rat sightings", command = self.ratSightings)
        self.listButton.grid(row = 2, column = 0)
        self.viewGraph = Button(self.frame2, text= "View Data Graphs", command = self.viewData)
        self.viewGraph.grid(row = 3, column = 0)
        self.viewMap = Button(self.frame2, text= "View Map", command = self.viewMap)
        self.viewMap.grid(row = 4, column = 0)
        self.logout = Button(self.frame2, text= "Logout", command = self.logout)
        self.logout.grid(row = 5, column = 0)


    def submitReport (self):
        print "submit reports"

    def ratSightings (self):
        print "Searching"

    def viewData (self):
        print "some stuff will happen"

    def viewMap (self):
        print "some stuff will happen"

    def logout (self):
        print "log out" 

    def connect (self):
        try:
            self.db = pymysql.connect(user = "",
                                 passwd = "",
                                 host = "",
                                 db = "")
            return self.db
            
        except:
            messagebox.showerror("Error", "There was an error connecting with the database.")

    def loginCheck(self):
        #try to match the given user name and password

        #self.connect()
        #self.c = self.db.cursor()
        userEntry = self.userEntry.get()
        passwordEntry = self.passwdEntry.get()
        num = self.c.execute(sql,(userEntry,passwordEntry))  # number of rows it grabs
        if num != 0:
            self.c.close ()
            self.db.commit ()
            ##close the connection object????
            self.db.close ()
            messagebox.showinfo("Success!","You have logged in to GTMarketPlace.")
            self.root.destroy()
        #if you can't match it, then display this error
        else:
            messagebox.showerror("Error", "There was an error connecting with the database.")

       
    def registerCheck(self):
        #requesting API
        registerPayload = {"name": self.nameEntry2.get(), "username": self.userEntry2.get(),
                   "password":self.passwdEntry2.get(), "isAdmin": var.get()}
        registerRequest = requests.post('http://ec2-54-174-96-216.compute-1.amazonaws.com:9000/addUser',
                                        data=registerPayload);
        print (registerRequest.text)


    def loginCheck(self):
        #requesting API
        loginPayload = {"username": self.userEntry.get(), "password":self.passwdEntry.get()}
        loginRequest = requests.post('http://ec2-54-174-96-216.compute-1.amazonaws.com:9000/addUser', data=loginPayload);
        print (loginRequest.text)
        self.mainPage()
        

                            

root = Tk ()
app = project2340(root)
root.mainloop ()
