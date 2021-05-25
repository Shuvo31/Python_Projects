import pywhatkit

try:
    pywhatkit.sendwhatmsg('+91 xxxxxxxxxx', 'something....', 23, 32)
    print('Sending message...')

except:
    print('Unexpected Error.')