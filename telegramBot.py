import requests
import time
import schedule

def telegram_bot_sendtext(bot_message):
    
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    
def sendMsg(): 
    message = "hello friend"
    telegram_bot_sendtext(message)
    print(message)

schedule.every(1).minutes.do(sendMsg)

while True:
    schedule.run_pending()
    time.sleep(1)