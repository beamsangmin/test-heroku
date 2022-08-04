from flask import *
from linebot.models import *
from linebot import *
import json
import requests   

app = Flask(__name__)

# Channel access token and Channel secret 
line_bot_api = LineBotApi('KtzrTuJet6PYQfzQRQEnV6F6QrC8VQTH+hzLKTfpj99SxRp1vG00aidjuAHU/YLayESkb22eatO0SU/YoYxSYbpK1bEQOUITQ7o8M2yR2phcLSsiwsJxd6dnXp4s77eB1RFC1r/6nzedhhQb1uQkXwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('277fb1c0412709857645ac19242f7be7')

@app.route("/", methods=['GET'])
def helloworld():
    return 'helloworld'
        
@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    print(body)
    return 'OK'
    
def reply(intent,text,reply_token,id,disname):
    if intent == 'Vendor':
        text_message = TextSendMessage(text='Vendor List')
        line_bot_api.reply_message(reply_token,text_message)
        
    if intent == 'Customer':
        text_message = TextSendMessage(text='Customer List')
        line_bot_api.reply_message(reply_token,text_message)
        
def replyVendor(intent,text,reply_token,id,disname):
    if intent == 'Vendor - Description':
        text_message = TextSendMessage(text='Vendor Description')
        line_bot_api.reply_message(reply_token,text_message)

def replyCustomer(intent,text,reply_token,id,disname):
    if intent == 'Customer - Description':
        text_message = TextSendMessage(text='Customer Description')
        line_bot_api.reply_message(reply_token,text_message)       

def reqCompanyName(intent,text,reply_token,id,disname):
    if intent == 'requestCompanyName':
        text_message = TextSendMessage(text='Please enter company code')
        line_bot_api.reply_message(reply_token,text_message)
    
def replySDN(intent,text,reply_token,id,disname):
    if intent == 'ReplySDN':
        access_Token_URL = 'https://login.microsoftonline.com/51cd216f-49b0-46d5-b6f2-dce309a29830/oauth2/v2.0/token'
        configure_New_Token= {'grant_type' : 'client_credentials',
                'scope' : 'https://api.businesscentral.dynamics.com/.default',
                'client_id' : '2bb54e51-334d-4848-94cc-e44c9cc3f54a',
                'client_secret' : 'Pg38Q~Ic5i2oJncaQs~SwRAPzmnjKSURqMynydjj'
            }

        response = requests.post(access_Token_URL, data=configure_New_Token)
        jsonResponse = json.loads(response.text)
        access_Token = jsonResponse['access_token']

        api_URL = "https://api.businesscentral.dynamics.com/v2.0/51cd216f-49b0-46d5-b6f2-dce309a29830/SDNDEV2/api/AMCO/Item/v2.0/companies"

        headers = {'Authorization' : 'Bearer '+access_Token}

        resp = requests.get(api_URL , headers=headers)
        json_result = resp.json()
        for data in json_result['value']:
            if (data['name']) == text:
                Display = (data['displayName'])
        text_message = TextSendMessage(text="รายชื่อบริษัท : {} ".format(Display))
        line_bot_api.reply_message(reply_token,text_message)

def replyKIN(intent,text,reply_token,id,disname):
    if intent == 'ReplyKIN':
        access_Token_URL = 'https://login.microsoftonline.com/51cd216f-49b0-46d5-b6f2-dce309a29830/oauth2/v2.0/token'
        configure_New_Token= {'grant_type' : 'client_credentials',
                'scope' : 'https://api.businesscentral.dynamics.com/.default',
                'client_id' : '2bb54e51-334d-4848-94cc-e44c9cc3f54a',
                'client_secret' : 'Pg38Q~Ic5i2oJncaQs~SwRAPzmnjKSURqMynydjj'
            }

        response = requests.post(access_Token_URL, data=configure_New_Token)
        jsonResponse = json.loads(response.text)
        access_Token = jsonResponse['access_token']

        api_URL = "https://api.businesscentral.dynamics.com/v2.0/51cd216f-49b0-46d5-b6f2-dce309a29830/SDNDEV2/api/AMCO/Item/v2.0/companies"

        headers = {'Authorization' : 'Bearer '+access_Token}

        resp = requests.get(api_URL , headers=headers)
        json_result = resp.json()
        for data in json_result['value']:
            if (data['name']) == text:
                Display = (data['displayName'])
        text_message = TextSendMessage(text="รายชื่อบริษัท : {} ".format(Display))
        line_bot_api.reply_message(reply_token,text_message)
    
if __name__ == "__main__":
    app.run()
