

import requests
from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import messagebox
from tkinter import ttk
from keyboard import *
import keyboard
import tkinter as tk
from pynput.keyboard import Key
import requests
import RPi.GPIO as GPIO
import time

from pynput.mouse import Controller

from io import BytesIO
LED_PIN = 17


class CustomerWin:
    def __init__(self, root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry("400x100+0+0")
        self.card_number = StringVar()
        self.imagaeUrl = StringVar()
        my_mouse = Controller()
    

        print (my_mouse.position,',,,,,,,,,,,,,,,,,,,,')

        # ============================== Tile =========================

        # lbl_title = Label(self.root, text="Card Details", font=(
        #     'times new roman', 10, 'bold'), bg='black', fg='gold', bd=4, relief=RIDGE)
        # lbl_title.place(x=0, y=0, width=900, height=30)

        # ============================== label frame  =========================

        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text='Cusomer Details ', font=(
            'times new roman', 6, 'bold'), padx=2)
        labelframeleft.place(x=5, y=5, width=400, height=100)

        # ============================== Cusomer Card Details =========================

        label_customer_name = Label(labelframeleft, text=' Card Number: ', font=(
            'times new roman', 9, 'bold'), padx=2, pady=6)
        label_customer_name.grid(row=1, column=0, sticky=W)
        entry_mother_name = ttk.Entry(
            labelframeleft, width=22,  textvariable=self.card_number, font=('times new roman', 12, 'bold'))
        entry_mother_name.bind('<Return>', self.add_data)
        entry_mother_name.grid(row=1, column=1)
        entry_mother_name.focus()

        # ============================== Search Button =========================
        add_button = Button(labelframeleft, command=self.add_data, text='Search', font=(
            'arial', 10, 'bold'), bg='black', fg='gold', width=8)
        add_button.grid(row=1, column=2, padx=1, pady=2)


        # image2 = Image.open(r'C:\Python\hotel\image\image5.jpg')
        # image2 = image2.resize((150, 200), Image.ANTIALIAS)
        # self.photoimage2 = ImageTk.PhotoImage(image2)
        # lblimage = Label(self.root, image=self.photoimage2,
        #                  bd=0, relief=RIDGE)
        # lblimage.place(x=50, y=130, width=150, height=200)

    def get_info(self):
        print (self.entry_mother_name.index(INSERT))
        

    def add_data(self, *args):
        self.card_number.get()
        card_number = self.card_number.get()
        payload = {'card_number': card_number}
        url = 'http://erp.superhostelbd.com/super_home/json/data-information-pi/select'

        # url = 'http://10.100.93.11/super_home_dummy/json/data-information-pi/select'
        r = requests.post(url, data=payload, headers={
                          "authorization": "api_pi_12345678!@#$%^&*"})
        self.card_number.set('')

        data = r.json()
        print (data)
        if data['message']=='Active Member!':
            if data["status"]:
                print ('ok')
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(LED_PIN, GPIO.OUT)
                GPIO.output(LED_PIN, GPIO.LOW)
                time.sleep(1)
                GPIO.output(LED_PIN, GPIO.HIGH)
                GPIO.cleanup
            else:

                print ('not ok ............ ')

        else:
            print ('not data')

        # self.imagaeUrl.set(data['image'])
        # img_url = data['image']
        # response = requests.get(img_url)
        # img_data = response.content
        # image2 = Image.open(BytesIO(img_data))
        # image2 = image2.resize((150, 200), Image.ANTIALIAS)
        # self.photoimage2 = ImageTk.PhotoImage(image2)
        # lblimage = Label(self.root, image=self.photoimage2,
                        #  bd=0, relief=RIDGE)
        # lblimage.place(x=20, y=100, width=150, height=200)


if __name__ == '__main__':
    root = Tk()
    obj = CustomerWin(root)
    root.mainloop()
