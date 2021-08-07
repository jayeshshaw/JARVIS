import pywhatkit
from pywhatkit.main import sendwhatmsg_to_group
# import sys
import json

contactList = {}       

def printContact():
    f = open('contactListPhone.json')
    data = json.load(f)
    print(data)
        
    # x = input("To Add New contact press C : or else press enter : ")
    # if x == 'C':
    #     addContact()



def addContact():
    name = input("Enter the name : ")
    num = input("Enter the phone number with ISD code : ")
    phone = {name:num}
    with open("contactListPhone.json","r+") as file:
        data = json.load(file)
        data.update(phone)
        file.seek(0)
        json.dump(data,file)
def whatIsTheMessage():
    x = input("Enter the message:") 
    return x
def selectContact():
    file = open("contactListPhone.json")
    contactList = json.load(file)
    print(contactList.keys())
    contact = input('Enter the contact to whome you want to send message \n')
    return contact

def sendMessage(contact,message):

    file = open("contactListPhone.json")
    contactList = json.load(file)
    
    # message = input('Enter the message\n')
    if contact in contactList.keys():
        print('Your message sending in progress')
        pywhatkit.sendwhatmsg_instantly(contactList[contact],message,20,browser=None)
    else:
        print('Contact not present')
        
def sendMessageToGroup():
    sendwhatmsg_to_group(group_id='https://chat.whatsapp.com/DayzmW6SfD5BNu1xL9B4vf',message='testing',time_hour=12,time_min=20,wait_time=20,print_wait_time=True)
    
if __name__ == '__main__':
    # sendMessage()
    printContact()
    name = selectContact()
    msg = whatIsTheMessage()
    sendMessage(name,msg)
    input('press enter to exit')
            
