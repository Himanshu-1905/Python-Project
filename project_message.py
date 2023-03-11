# This code automatically send messages
# using Exception Handling to avoid unprecedented errors
try:
    import pywhatkit 
    pywhatkit.sendwhatmsg("+91930618XXXX","Hello from Himanshu Rajput", 21, 5)
    print("Successfully Sent!")

except Exception as e:
    print(e)
    
