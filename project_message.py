# This code automatically send messages
# using Exception Handling to avoid unprecedented errors
try:
    import pywhatkit 
    pywhatkit.sendwhatmsg("+918307919250","Hello from Himanshu Rajput", 21, 5)
    print("Successfully Sent!")

except Exception as e:
    print(e)
    