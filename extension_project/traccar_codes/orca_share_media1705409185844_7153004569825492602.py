from threading import Thread
from send_sms1 import send_message
import websocket
import requests
import urllib
import json
import time
import API_Traccar

# CHANGE HOST HERE
host = "13.229.69.46:8082"
# --------------------------- #

ws_url = "ws://" + host + "/api/socket"
http_url = 'http://' + host + '/api/session'

###################### AUTHENTICATION ######################################
# CHANGE EMAIL AND PASSWORD HERE
email    = 'admin'
password = 'admin'

# ------------------------------------------- #

headers = {'content-type': 'application/x-www-form-urlencoded',
           'accept': 'application/json'}
session = requests.Session()
params = urllib.parse.urlencode({'email': email, 'password': password})
response = session.post(http_url,
                        data=params,
                        headers=headers)

cookies = session.cookies.get_dict()
token = cookies['JSESSIONID']
############################################################################

event_list = []

def on_open(ws):
    print('Websocket opened!')


def on_error(ws, error):
    print(f"error: {error}")


def on_message(ws, message):
    try:  # try if there's an event happened in the websocket
        event = ''
        event_data = json.loads(message)['events']

        dev_id = event_data[0]['deviceId']
        vehicle_name = devices[dev_id]  # name of vehicle must be: <Brgy>"T"<Truck code> , example: OOiTa which means Poblacion 1 for 'OOi', 'T' for Truck, 'a' as truck code

        event = event_data[0]['type']
        if event == "geofenceEnter":
            event = "E"  # ENTER
        elif event == "geofenceExit":
            event = "X"  # EXIT
        else:
            # raise an error here
            pass

        geof_id = event_data[0]['geofenceId']
        cluster_name = geof[geof_id]  # name of cluster/geofence must be: <Brgy>C<Cluster #> , example: OiiCc which means Oii for Poblacion 2, Cc - Cluster 3
        
        # event_time = event_data[0]['eventTime']
        message = str(vehicle_name + cluster_name + event)  # sample: TOiiCc - (Poblacion 2) Truck will now ENTER the vicinity of Cluster 3  >>> can add the truck code for truck identification
        # msg = event_data[0]['attributes']['message']  # just get the message that shows in the traccar web interface
        if message in event_list:
            print(">>> Ignoring duplicate events!")
            pass
        else:
            event_list.append(message)
            #send_messages(msg, receiver)
            send_message(phone_number, message, authorization_token)
            print(f">>> Event caught (code): {message}")
    except:
        # print(">>> No event data")
        pass


def on_close(ws):
    print("Websocket closed!")
        

def ws_start():
    ws = websocket.WebSocketApp(ws_url, 
                on_message = on_message,
                on_error =   on_error,
                on_close =   on_close,
                on_open =    on_open,
                header={"Cookie: JSESSIONID=" + token}) 

    ws_thread = Thread(target=ws.run_forever)
    ws_thread.start()
    ws_thread.join()


# Main code - Proccess starts here

tracker = API_Traccar.API_Traccar(host)
r = tracker.credential_auth(email, password)
print(">>> Log in successful!")

# get devices id in dictionary structure
ret = tracker.get_all_devs()
devices = tracker.get_dev_id(ret)  # returned a dictionary with {"name of device": id, ...}
print(">>> Devices data collection started...")

# get geofences id in dictionary structure
geofs = tracker.get_all_geof()
geof = tracker.get_geof_id(geofs)  # returned a dictionary with {"name of geofence": id, ...}
print(">>> Geofences data collection started...")

phone_number = input(">>> Input the receiver's number: ")  # or you can embed the number here for fix
print(">>> Catching Live Events started...")


ws_start()

#Possible Combination ng Text 
#GPS1C01E - unang pasok sa cluster 1
#T01C01X - unang labas sa cluster 1
#T01C02E|
#T01C02X
#T01C03E
#T01C03X