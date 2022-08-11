from email import message
from flask import Flask, render_template
from flask import *
from linebot.models import *
from linebot import *
import json
import requests   



app = Flask(__name__)

# Channel access token and Channel secret 
line_bot_api = LineBotApi('KtzrTuJet6PYQfzQRQEnV6F6QrC8VQTH+hzLKTfpj99SxRp1vG00aidjuAHU/YLayESkb22eatO0SU/YoYxSYbpK1bEQOUITQ7o8M2yR2phcLSsiwsJxd6dnXp4s77eB1RFC1r/6nzedhhQb1uQkXwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('277fb1c0412709857645ac19242f7be7')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/callback", methods=['POST'])
def callback():
    fulfillmentText =''
    body = request.get_data(as_text=True)
    print(body)
    req = request.get_json(silent=True, force=True)
    intenttext = req["queryResult"]["intent"]["displayName"] 
    if "fulfillmentText" in req["queryResult"].keys():
        fulfillmentText = req["queryResult"]["fulfillmentText"] or 'xxx' 
    inputmessage = req['originalDetectIntentRequest']['payload']['data']['message']['text'] 
    reply_token = req['originalDetectIntentRequest']['payload']['data']['replyToken']
    id = req['originalDetectIntentRequest']['payload']['data']['source']['userId']
    disname = line_bot_api.get_profile(id).display_name

    retmessage = 'id = ' + id
    retmessage = retmessage + '\nname = ' + disname
    retmessage = retmessage + '\ntext = ' + inputmessage
    retmessage = retmessage + '\nintent = ' + intenttext
    retmessage = retmessage + '\nreply_token = ' + reply_token
    retmessage = retmessage + '\nfullfillment = ' + fulfillmentText
    retmessage = retmessage + '\n'


    if (len(inputmessage)):
        # reply(inputmessage,retmessage,reply_token,id,disname)
        # quit()
        if inputmessage == 'ReplyKIN':
            replyKIN(inputmessage,retmessage,reply_token,id,disname)
            quit()
        if inputmessage == 'ReplySDN':
            replySDN(inputmessage,retmessage,reply_token,id,disname)
            quit()
        if inputmessage == 'Vendor':
            reply(inputmessage,retmessage,reply_token,id,disname)
            quit()
        if inputmessage == 'Customer':
            reply(inputmessage,retmessage,reply_token,id,disname)
            quit()
        if inputmessage == 'Vendor - Description':
            replyVendor(inputmessage,retmessage,reply_token,id,disname)
            quit()
        if inputmessage == 'Customer - Description':
            replyCustomer(inputmessage,retmessage,reply_token,id,disname)
            quit()
        if inputmessage == 'requestCompanyName':
            reqCompanyName(inputmessage,retmessage,reply_token,id,disname)
            quit()
        if inputmessage == 'KIN':
            replyKIN(inputmessage,retmessage,reply_token,id,disname)
            quit()
        if inputmessage == 'SDN':
            replySDN(inputmessage,retmessage,reply_token,id,disname)
            quit()
        
    return 'OK'

def reply(inputmessage,retmessage,reply_token,id,disname):
    # print(intent)
    # text_message = StickerMessage(package_id=8525,sticker_id=16581292)
    # line_bot_api.reply_message(reply_token,text_message)
    text_message = TextSendMessage(text='สวัสดี คุณ ตอบว่า '+disname + ' ' +inputmessage + '\n' + retmessage)
    line_bot_api.reply_message(reply_token,text_message)

    if inputmessage == 'Vendor':
        text_message = TextSendMessage(text='สวัสดี คุณ ตอบว่า '+disname + ' ' +inputmessage + '\n' + retmessage)
        line_bot_api.reply_message(reply_token,text_message)
        
    if inputmessage == 'Customer':
        text_message =TextSendMessage(text='สวัสดี คุณ ตอบว่า '+disname + ' ' +inputmessage + '\n' + retmessage)
        line_bot_api.reply_message(reply_token,text_message)
        
def replyVendor(inputmessage,retmessage,reply_token,id,disname):
    if inputmessage == 'Vendor - Description':
        text_message = TextSendMessage(text='Vendor Description'+ '\n' + retmessage)
        line_bot_api.reply_message(reply_token,text_message)

def replyCustomer(inputmessage,retmessage,reply_token,id,disname):
    if inputmessage == 'Customer - Description':
        text_message = TextSendMessage(text='Customer Description'+ '\n' + retmessage)
        line_bot_api.reply_message(reply_token,text_message)       

def reqCompanyName(inputmessage,retmessage,reply_token,id,disname):
    if inputmessage == 'requestCompanyName':
        text_message = TextSendMessage(text='Please enter company code'+ '\n' + retmessage)
        line_bot_api.reply_message(reply_token,text_message)
    
def replySDN(inputmessage,retmessage,reply_token,id,disname):
    if inputmessage == 'SDN':
        access_Token_URL = 'https://login.microsoftonline.com/51cd216f-49b0-46d5-b6f2-dce309a29830/oauth2/v2.0/token'
        configure_New_Token= {'grant_type' : 'client_credentials',
                'scope' : 'https://api.businesscentral.dynamics.com/.default',
                'client_id' : '2bb54e51-334d-4848-94cc-e44c9cc3f54a',
                'client_secret' : 'Pg38Q~Ic5i2oJncaQs~SwRAPzmnjKSURqMynydjj'
            }

        response = requests.post(access_Token_URL, data=configure_New_Token)
        jsonResponse = json.loads(response.text)
        access_Token = jsonResponse['access_token']
        Display =''
        print(access_Token)

        api_URL = "https://api.businesscentral.dynamics.com/v2.0/51cd216f-49b0-46d5-b6f2-dce309a29830/SDNDEV2/api/AMCO/Item/v2.0/companies"

        headers = {'Authorization' : 'Bearer '+access_Token}

        resp = requests.get(api_URL , headers=headers)
        json_result = resp.json()
        print(json_result)
        for data in json_result['value']:
            if (data['name']) == inputmessage:
                Display = (data['displayName'])
        text_message = TextSendMessage(text="รายชื่อบริษัท : " + Display + '\n' + retmessage)
        line_bot_api.reply_message(reply_token,text_message)

def replyKIN(inputmessage,retmessage,reply_token,id,disname):
    if inputmessage == 'KIN':
        access_Token_URL = 'https://login.microsoftonline.com/51cd216f-49b0-46d5-b6f2-dce309a29830/oauth2/v2.0/token'
        configure_New_Token= {'grant_type' : 'client_credentials',
                'scope' : 'https://api.businesscentral.dynamics.com/.default',
                'client_id' : '2bb54e51-334d-4848-94cc-e44c9cc3f54a',
                'client_secret' : 'Pg38Q~Ic5i2oJncaQs~SwRAPzmnjKSURqMynydjj'
            }

        response = requests.post(access_Token_URL, data=configure_New_Token)
        jsonResponse = json.loads(response.text)
        access_Token = jsonResponse['access_token']
        Display =''
        print(access_Token)

        api_URL = "https://api.businesscentral.dynamics.com/v2.0/51cd216f-49b0-46d5-b6f2-dce309a29830/SDNDEV2/api/AMCO/Item/v2.0/companies"

        headers = {'Authorization' : 'Bearer '+access_Token}

        resp = requests.get(api_URL , headers=headers)
        json_result = resp.json()
        print(json_result)
        # Transform json input to python objects
        input_dict = json.loads(json.dumps(json_result))

        # Filter python objects with list comprehensions
        output_dict = [x for x in input_dict if x['2'] == inputmessage]

        # Transform python object back into json
        output_json = json.dumps(output_dict)

        # for data in json_result['value']:
        #     if (data['name']) == inputmessage:
        Display = (output_json['displayName'])

        text_message = TextSendMessage(text="รายชื่อบริษัท : " + Display+ '\n' + retmessage)
        line_bot_api.reply_message(reply_token,text_message)
    
if __name__ == '__main__': app.run(debug=True)