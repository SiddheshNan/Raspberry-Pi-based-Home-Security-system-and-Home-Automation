from twilio.rest import Client

account_sid = ''
auth_token = ''


def send_text(num, text):
    print("trying to send whatsapp text msg..")
    global t, sid
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=text,
            from_='whatsapp:+14155238886',
            to='whatsapp:+91' + str(num)
        )
        sid = message.sid
        print(message.sid)
        t = True
    except Exception as e:
        t = False
        print("Failed to Send WhatsApp text due to : " + str(e))
    if t:
        return sid
    else:
        return 0


def send_image(num, text, media):
    print("trying to send whatsapp media msg..")
    global t, sid
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            media_url=media,
            from_='whatsapp:+14155238886',
            body=text,
            to='whatsapp:+91' + str(num)
        )
        sid = message.sid
        print(message.sid)
        t = True
    except Exception as e:
        t = False
        print("Failed to Send WhatsApp media due to : " + str(e))

    if t:
        return sid
    else:
        return 0
