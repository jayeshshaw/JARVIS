import requests
import datetime
import sys

# from requests.models import Response


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }

def getState():
    
    url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"

    payload={}

    response = requests.request("GET", url, headers=headers, data=payload).json()

    states = response["states"]
    for i in states:
        print(f"{i['state_name']} : {i['state_id']} ")
    # print()
    state_id = input('Enter the respective state id\n')
    return state_id
def getDistrict(state_id):
    url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/"+str(state_id);
    # print(url) 
    payload={}
    response = requests.request("GET", url, headers=headers, data=payload).json()  
    district = response['districts']
    for i in district:
        print(f"{i['district_name']} : {i['district_id']}")

    district_id = input("Enter the respective district id \n")
    return district_id
def sessions(pin,district_id,date):
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(district_id)+"&date="+date
    pin_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+str(pin)+"&date="+date
    # https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=730&date=18-06-2021
    payload={}
    if pin!=0:
        url = pin_url
    response = requests.request("GET", url, headers=headers, data=payload).json()
    centers = response['centers']
    found = 0
    for i in centers:
        for j in i['sessions']:
            if j["available_capacity"] >0 and j["min_age_limit"]==18 :
                found+=1
                print(f"{i['name']}")
                print(f"Avability : {j['available_capacity']} \tDate : {j['date']}")

    if found == 0:
        print('No Slots available')      
def getVaccine():
    
    today = str(datetime.date.today())
    date = datetime.datetime.strptime(today,"%Y-%m-%d").strftime("%d-%m-%Y")
    t = input('Do you want vaccination by district then enter d if pincode then enter p : ')
    if(t== 'p'):
        pin = input("Enter the pincode : ")
        sessions(pin,0,date)
    else:
        state_id = getState()    
        district_id=getDistrict(state_id)
        sessions(0,district_id,date)


if __name__ == "__main__":
    getVaccine()
    k = input('Enter any key to exit')
    if k != '':
        sys.exit()




