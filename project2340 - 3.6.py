import pymysql
from Tkinter import messagebox
from Tkinter import *
import base64
import os
import requests
import random
import datetime
from matplotlib import pyplot as plt
import numpy as np
import gmplot
from tkinterhtml import HtmlFrame
import json
import webbrowser
import heapq


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
        self.frame1 = Frame(self.root)
        self.frame1.pack(side = TOP, fill = X)
        self.frame2 = Frame (self.root)
        self.frame2.pack(side = TOP, fill = X)

        #the labels
        self.userLabel = Label(self.frame1, text = "Username:")
        self.userLabel.grid(row = 1, column = 0, sticky = E)
        self.passwdLabel = Label(self.frame1, text = "Password:")
        self.passwdLabel.grid(row = 2, column = 0, sticky = E)
    
        #the entries 
        self.userEntry = Entry(self.frame1, width = 30, textvariable = self.sv1)
        self.userEntry.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.passwdEntry = Entry(self.frame1, width = 30, show="*")
        self.passwdEntry.grid(row = 2, column = 1, padx = 5, pady = 5)

        #the buttons
        self.loginButton = Button (self.frame2, text = "Login", command = self.loginCheck)
        self.loginButton.pack(fill = X, anchor = E, side = RIGHT)
        self.registerButton = Button(self.frame2, text= "Register", command = self.register)
        self.registerButton.pack(fill = X, anchor = E, side = RIGHT)

       
    def register (self):

        #show only the register
        self.root.withdraw ()
        self.register = Toplevel()
        self.register.title("New User Registration Page")

        #create the 2 frames
        self.frame1 = Frame(self.register)
        self.frame1.pack(side = TOP,fill = X)
        self.frame2 = Frame (self.register)
        self.frame2.pack(side = TOP, fill = X)
        self.frame3 = Frame (self.register)
        self.frame3.pack(side = TOP, fill = X)


        #all of the labels 
        self.nameLabel2 = Label(self.frame1, text = "Name:")
        self.nameLabel2.grid(row = 1, column = 0, sticky = E)
        self.userLabel2 = Label(self.frame1, text = "Username:")
        self.userLabel2.grid(row = 2,  column = 0, sticky = E)
        self.passwdLabel2 = Label(self.frame1, text = "Password:")
        self.passwdLabel2.grid(row = 3, column = 0, sticky = E)

        #all of the entries
        self.nameEntry2 = Entry(self.frame1, width = 30)
        self.nameEntry2.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.userEntry2 = Entry(self.frame1, width = 30)
        self.userEntry2.grid(row = 2, column = 1, padx = 5, pady = 5)
        self.passwdEntry2 = Entry(self.frame1, width = 30, show="*")
        self.passwdEntry2.grid(row = 3, column = 1, padx = 5, pady = 5)

        #all the buttons
        self.cancelButton2 = Button (self.frame2, text = "Cancel", command = self.login2)
        self.cancelButton2.pack(fill = X, anchor = E, side = RIGHT)
        self.registerButton2 = Button(self.frame2, text= "Register", command = self.registerCheck)
        self.registerButton2.pack(fill = X, anchor = E, side = RIGHT)

        #AdminCheckbox
        global registerVar
        registerVar = StringVar()
        self.adminCheckbox = Checkbutton(self.frame2, text = "Check if you are an admin", variable = registerVar)
        self.adminCheckbox.pack()                
        
    #function that gets called upon once you hit cancel that pulls up the login window again
    def login2 (self):
        
       self.register.withdraw()
       self.root.deiconify()
       
    def mainPage(self):

        self.mainPageView = Toplevel()
        self.mainPageView.title("Dashboard")

        #create the frame
        self.frame1 = Frame(self.mainPageView)
        self.frame1.pack(side = TOP, fill = X)
       
        #creating buttons
        self.submitButton = Button (self.frame1, text = "Submit Rat Report", command = self.submitReport)
        self.submitButton.grid(row = 1, column = 0)
        self.listButton = Button(self.frame1, text= "List of  recent rat sightings", command = self.ratSightings)
        self.listButton.grid(row = 2, column = 0)
        self.viewGraph = Button(self.frame1, text= "View Data Graphs", command = self.viewData)
        self.viewGraph.grid(row = 3, column = 0)
        self.viewMap = Button(self.frame1, text= "View Map", command = self.viewMap)
        self.viewMap.grid(row = 4, column = 0)
        self.logout = Button(self.frame1, text= "Logout", command = self.logout)
        self.logout.grid(row = 5, column = 0)


    def submitReport (self):
        self.mainPageView.withdraw()
        self.submitReportView = Toplevel()
        self.submitReportView.title("Submit a Rat Sighting")

        #create the frames
        self.frame1 = Frame(self.submitReportView)
        self.frame1.pack(side=TOP)
        self.frame2 = Frame(self.submitReportView)
        self.frame2.pack(side=TOP)

        #create the labels
        self.locationTypeLabel = Label(self.frame1, text = "Enter the Location Type")
        self.locationTypeLabel.grid(row = 1, column = 0, sticky = E)
        self.streetLabel = Label(self.frame1, text = "Street Name:")
        self.streetLabel.grid(row = 3,  column = 0, sticky = E)
        self.cityLabel = Label(self.frame1, text = "City:")
        self.cityLabel.grid(row = 5, column = 0, sticky = E)
        self.zipcodeLabel = Label(self.frame1, text = "Zip Code:")
        self.zipcodeLabel.grid(row = 7, column = 0, sticky = E)
        self.boroughLabel = Label(self.frame1, text = "Enter the Borough")
        self.boroughLabel.grid(row = 9, column = 0, sticky = E)

        #create the entries
        self.streetName = Entry(self.frame1, width = 30)
        self.streetName.grid(row = 4, column = 1, padx = 5, pady = 5)
        self.city = Entry(self.frame1, width = 30)
        self.city.grid(row = 6, column = 1, padx = 5, pady = 5)
        self.zipcode = Entry(self.frame1, width = 30)
        self.zipcode.grid(row = 8, column = 1, padx = 5, pady = 5)

        #create the dropdowns
        locationOptions = ["1-2 Family Dwelling", "3+ Family Apt. Building",
                           "3+ Family Mixed Use Building", "Commercial Building",
                           "Vacant Lot", "Construction Site", "Hospital", "Catch Basin/Sewer"]
        self.locationVar = StringVar(root)
        self.locationVar.set(locationOptions[0])
        self.locationType = OptionMenu(self.frame1, self.locationVar, *locationOptions)
        self.locationType.grid(row=2,column=1)


        boroughOptions = ["Manhattan", "Staten Island", "Queens", "Brooklyn",
                          "Bronx"]
        self.boroughVar = StringVar(root)
        self.boroughVar.set(boroughOptions[0])
        self.borough = OptionMenu(self.frame1, self.boroughVar, *boroughOptions)
        self.borough.grid(row=10,column=1)      


        #create the buttons 
        self.submit = Button(self.frame2, text= "Submit", command = self.submitReportCheck)
        self.submit.grid(row = 1, column = 1)
        self.cancel = Button(self.frame2, text= "Cancel", command = self.cancel)
        self.cancel.grid(row = 1, column = 2)

    def ratSightings (self):     
        
        self.ratSightingView = Toplevel()
        self.ratSightingView.title("List of recent rat sighting")
        
        self.frame1 = Frame(self.ratSightingView)
        self.frame1.pack(side=TOP)
        
        sightingRequest = requests.get('http://ec2-54-174-96-216.compute-1.amazonaws.com:9000/showRecords')
        data = sightingRequest.text
        dataList = data.split("},")
        dataDict = {}
        cityDict = {}
        breakCount =1
        for d in dataList:
            print("**************************************************************")
            key = d.split(": {")[0]
            value = d.split(": {")[1]
            cityString = value.split(",\n")[2]
            city = cityString.split(": ")[1]
            dataDict.update({key:value})
            print("KEY")
            print(key)
            print("VALUE")
            print(value)

            breakCount = breakCount + 1

            if breakCount == 6:
                break
            
        count2 = 1
        first1500 = [v for v in list(dataDict.values())[:5]]
        print(list(dataDict.values())[:5])
        for each in first1500:
            print("IN THE FOR LOOP")
            print("EACH")
            print(each)
            self.label = Label(self.frame1, text = each)
            self.label.grid(row = count2, column = 0, sticky = E)

            count2 = count2 + 1

            if count2 == 6:
                break
                        
   


    def viewData (self):
        self.viewDataView = Toplevel()
        self.viewDataView.title("List of recent rat sighting")
        
        self.frame1 = Frame(self.viewDataView)
        self.frame1.pack(side=TOP)
        
        slices = [20475, 34199, 26250,14574, 4867]
        activities = ["Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"]

        plt.pie(slices,labels=activities,startangle=90)
        plt.title("Rats by Borough")
        plt.show()
        
    def viewMap (self):
        #request rat sightings from API
        r = requests.get('http://ec2-54-174-96-216.compute-1.amazonaws.com:9000/showRecords')
        rtext = r.text
        rawdata = json.loads(rtext)
        
        latitudes = []
        longitudes = []
        for k, v in rawdata.items():
            if type(v['latitude']) == float:
                latitudes.append(v['latitude'])
            else:
                try:
                    latitudes.append(float(v['latitude']))
                except:
                    pass
            if type(v['longitude']) == float:
                longitudes.append(v['longitude'])
            else:
                try:
                    longitudes.append(float(v['longitude']))
                except:
                    pass


        gmap = gmplot.GoogleMapPlotter.from_geocode("New York")
        gmap.heatmap(latitudes, longitudes, threshold=20, radius=20)
        
        gmap.draw("mymap.html")
        webbrowser.open_new_tab('mymap.html')


    def logout (self):
        self.mainPageView.withdraw()
        self.root.deiconify()
        print("Log out successful")


    def registerCheck(self):
        #requesting API
        registerPayload = {"name": self.nameEntry2.get(), "username": self.userEntry2.get(),
                   "password":self.passwdEntry2.get(), "isAdmin": registerVar.get()}
        registerRequest = requests.post('http://ec2-54-174-96-216.compute-1.amazonaws.com:9000/addUser',
                                        data=registerPayload)

        requestStatus = json.loads(registerRequest.text)["status"]
        if requestStatus == 1:
            self.mainPageView.withdraw()
            self.root.deiconify()
        else:
            messagebox.showerror(
                "Registration Error",
                "No entries may be left blank. Please try again."
            )

    def loginCheck(self):
        #requesting API
        loginPayload = {"username": self.userEntry.get(), "password":self.passwdEntry.get()}
        loginRequest = requests.post('http://ec2-54-174-96-216.compute-1.amazonaws.com:9000/checkUser',
                                     data=loginPayload)
        
        requestStatus = loginRequest.status_code
        if requestStatus == 200:
            self.root.withdraw()
            self.mainPage()
        else:
            messagebox.showerror(
                "Login Error",
                "Username or password incorrect."
            )

    def submitReportCheck(self):
        rand = random.randint(1111,9999)

        #find latitude & longitude using current IP address
        d = datetime.datetime.now().strftime("%m/%d/%y %I:%M%p")
        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']

        submitPayload = {"key":rand, "date":d, "location_type": self.locationVar.get(),
                        "zip":self.zipcode.get(), "address": self.streetName.get(),
                        "city":self.city.get(), "borough":self.boroughVar.get(),
                        "latitude": lat, "logitude":lon}
        submitRequest = requests.post('http://ec2-54-174-96-216.compute-1.amazonaws.com:9000/addRecord',
                                     data=submitPayload)

        requestStatus = submitRequest.status_code
        print(requestStatus)
        if requestStatus == 200:
            self.submitReportView.destroy()
            self.mainPageView.deiconify()
        else:
            messagebox.showerror(
                "Submit Error",
                "No entries may be left blank. Please try again."
            )

    def cancel(self):
        self.submitReportView.destroy()
        self.mainPageView.deiconify()

        
    

                            

root = Tk()
app = project2340(root)
root.mainloop()
