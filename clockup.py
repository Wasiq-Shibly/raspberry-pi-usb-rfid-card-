import mysql.connector
import mysql
import requests
import json
import socket
from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import messagebox
from tkinter import ttk
from keyboard import *
import keyboard
import tkinter as tk
from pynput.keyboard import Key, Controller
import requests
import pyautogui
import RPi.GPIO as GPIO
import time
import asyncio
from evdev import InputDevice, categorize, ecodes

from pynput.mouse import Controller


from io import BytesIO
LED_PIN = 17
LED_PIN1=27
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.HIGH)
GPIO.output(LED_PIN1, GPIO.HIGH)

data1=False






mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="super_home"
)

mycursor = mydb.cursor()



class CustomerWin:
    def __init__(self, root):
        self.root = root
        self.root.title('Hostel Management System')
        self.root.attributes('-fullscreen', False)
        
        
        self.card_number = StringVar()
        
        self.imagaeUrl = StringVar()
        


        # ============================== Tile =========================

        # lbl_title = Label(self.root, text="Card Details", font=(
        #     'times new roman', 10, 'bold'), bg='black', fg='gold', bd=4, relief=RIDGE)
        # lbl_title.place(x=0, y=0, width=1500, height=30)

        # ============================== label frame  =========================

        labelframeleft = LabelFrame(self.root, bd=5, relief=RIDGE, text='Guest Details ', font=(
            'times new roman', 20, 'bold'), padx=10)
        labelframeleft.place(x=0, y=0, width=1024, height=768)
        print("2st")


        # ============================== Cusomer Card Details =========================

        label_customer_name = Label(labelframeleft, text='Guest  Card Number: ', font=(
            'times new roman', 10, 'bold'), padx=0, pady=0)
        label_customer_name.grid(row=1, column=0, sticky=W)
        
        
        entry_mother_name = ttk.Entry(
        labelframeleft, width=16, textvariable=self.card_number, font=('times new roman', 10, 'bold'))
        entry_mother_name.bind('<Return>', self.add_data)
        entry_mother_name.grid(row=1, column=1)
        entry_mother_name.focus_set()
        
        print("3st")
        
        
        
        


        
        

        # ============================== Search Button =========================
        
        add_button = Button(labelframeleft, command=self.add_data, text='Search', font=(
            'arial', 10, 'bold'), bg='black', fg='gold', width=15)
        add_button.grid(row=1, column=2, padx=5, pady=0)
        print("4st")
        


    def add_data(self, *args):
        
        global data1,data5
        global member_name,member_branch,member_status
        global img_url
        
       
        
        dev = InputDevice('/dev/input/event1')
        
        
        data=(dev.active_keys())
        print(len(data))
        
        print(data)
        
        if not data:
            data1=False
            print('nai')
        else:
            data1=True
            print('paichi')

        self.card_number.get()
        print("6st")
        card_number = self.card_number.get()
        print("7st")
        
        print(socket.gethostbyname(socket.gethostname()))
        
        sql = "SELECT * FROM members WHERE card_number = '"+card_number+"' AND status = '1'"
        
        
        
        result=mycursor.execute(sql)

        myresult = mycursor.fetchall()

        print(myresult)
        
        
        if len(myresult)==True:
            
            
            for x in myresult:

                print("got data")
                
               
                member_branch=(x[3])
                member_status="Active"
                member_name=(x[2])
                img_url = "http://localhost/members_card/image/defult.jpeg"
                
              
                print(member_branch)
                print(member_status)
                print(member_name)
                
                
                if data1==True:
                    
                    print ('ok')
                    print(data1)

                    GPIO.output(LED_PIN, GPIO.LOW)
                    time.sleep(1)
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    GPIO.cleanup
                    print ('gate one............ ')
                else:
                    
                    GPIO.output(LED_PIN1, GPIO.LOW)
                    time.sleep(1)
                    GPIO.output(LED_PIN1, GPIO.HIGH)
                    GPIO.cleanup

                    print ('gate Two ............ ')
    
            
        else:
            
            
            payload = {'card_number': card_number, 'ip_address': card_number}
            url = 'http://erp.superhostelbd.com/super_home/json/data-information-pi/select'
            r = requests.post(url, data=payload, headers={
                              "authorization": "api_pi_12345678!@#$%^&*"})
            data = r.json()
            
            print("you are not register check to api for over confirmation ")
            
            
            
            if (data['status']==True):
                
                print("api found data")
                
                
                data6="you are not register"
                
                member_branch=data['branch_name']
                member_status="Active"
                member_name=data['name']
                data15=data['status']
                img_url = "http://localhost/members_card/image/defult.jpeg"
                
                sql = "INSERT INTO members (card_number, name,branch,status) VALUES (%s, %s,%s, %s )"
                val = (card_number,member_name,member_branch,data15)
                mycursor.execute(sql, val)

                mydb.commit()
            else:
                
                
                member_branch="NOT FOUND"
                member_status="NOT FOUND"
                member_name="NOT FOUND"
                img_url = "http://localhost/members_card/image/defult.jpeg"
                

                

                
               
         
         
            
            
            
        
        data5="Welcome to Neways International"        

        self.card_number.set('')
        
        response = requests.get(img_url)
        img_data = response.content
        image2 = Image.open(BytesIO(img_data))
        image2 = image2.resize((550, 750), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(image2)
        lblimage = Label(self.root, image=self.photoimage2,
                        bd=5, relief=RIDGE)
        lblimage.place(x=500, y=50, width=500, height=700)
        
        status0= Label(self.root, text=data5, font=(
        'times new roman', 15, 'bold'), padx=5, pady=5,relief=RAISED)
        status0.place(x=5, y=290, width=450, height=100)
        
        
        status1= Label(self.root, text='Name:   '+member_name, font=(
        'times new roman', 15, 'bold'), padx=5, pady=5,relief=SUNKEN)
        status1.place(x=10, y=390, width=450, height=100)            
        
        
        status2= Label(self.root, text='Branch Name:   '+member_branch, font=(
        'times new roman', 15, 'bold'), padx=5, pady=5,relief=GROOVE)
        status2.place(x=10, y=490, width=450, height=100)
        
        
        status3= Label(self.root, text='Status:   '+member_status, font=(
        'times new roman', 10, 'bold'), padx=5, pady=5,relief=RIDGE)
        status3.place(x=10, y=590, width=450, height=100)



if __name__ == '__main__':
    root = Tk()    
    obj = CustomerWin(root)
    root.mainloop()



