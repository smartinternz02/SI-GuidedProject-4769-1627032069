import wiotp.sdk.device
import time
import random
import requests
myConfig = { 
    "identity": {
        "orgId": "xkdbgo",
        "typeId": "IOTDevice",
        "deviceId":"181016"
    },
    "auth": {
        "token": "147258369"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    print()      
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
while True:
    temp=random.randint(10,50)
    pH=random.randint(3,12)
    con=random.randint(400,1000)
    oxi=random.randint(500,900)
    tur=random.randint(0,8)
    if((6<=pH<=9)and(20<temp<40)and(500<con<1000)and(0<tur<5)and(650<oxi<800)):
        sms=1
        print("drink that water")
    else:
        sms=0
        print("not to drink that water")
    myData={'temperature':temp,'pH_Value':pH,'Conductivity':con,'sms':sms,'turbidity':tur,'Oxidation_reduction_potential':oxi}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
r = requests.get('https://www.fast2sms.com/dev/bulkV2?authorization=sxi3wHNID7tQ4Tjyu0SVUvEgZapbrzGAX9q85kPlfOFcKeBLhW5eqyvC8OoJrpXnWUjNhbzA3EgxaZRB&route=q&message=Prefer%20not%20to%20drink%20water&language=english&flash=0&numbers=8179521130')
print(r.status_code)
