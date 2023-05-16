#from logging import debug
#from flask import Flask, redirect, url_for, render_template
#import flask

import iota_client
import os
import hashlib



import time
import subprocess as s
import pyperclip


def rfid():
    import serial
    ser = serial.Serial()
    ser.baudrate = 9600
    try:
        ser.port = 'COM3'
    except:
        ser.port = 'COM6'

    ser.open()
    RFID_Data = ser.readline()
    if RFID_Data:
        RFID_Data = RFID_Data.decode()  # Decode arduino Serial
        RFID_Data = RFID_Data.strip()  # Strip Arduino Data to remove string
        RFID_Data = int(RFID_Data);  # Convert the Data to Int
        return (RFID_Data)


print("Please put your NFC card!! ")
while (True):
    data = rfid()
    if data == 1231072228:
        print("Congratulations Card Accepted. Please put your info in firefly and CTRL+V to paste in Send option")

        pyperclip.copy('atoi1qpuppl2nkrx2np8esnlet8fheq3hfg9ulslytvd3kd5063m0t7rnu2d7u2n')

        # IOTA
        client = iota_client.Client(nodes_name_password=[['https://api.lb-0.h.chrysalis-devnet.iota.cafe']])

        IOTA_SEED_SECRET = os.getenv('IOTA_SEED_SECRET')


        a = int(client.get_address_balance("atoi1qpuppl2nkrx2np8esnlet8fheq3hfg9ulslytvd3kd5063m0t7rnu2d7u2n")['balance'])
        print("Your Current balance is: ", a)
        print("Please wait!, Transaction is in process....")
        time.sleep(3)
        s.Popen('C:\\Users\\SHOVON\\AppData\\Local\\Programs\\desktop\\Firefly.exe')

        while True:
            b = int(
            client.get_address_balance("atoi1qpuppl2nkrx2np8esnlet8fheq3hfg9ulslytvd3kd5063m0t7rnu2d7u2n")['balance'])

            if (b > a):
                print("Congratulation!! Your Transaction is successful")
                print("Your balance after transaction is: ", b)
                break


        else:
            print("Transection is not completed.")
            print("Your balance after transaction is: ", b)
            break
    else:
        print("Access Denied")
        print("Please try agin with your NFC card")











