#how to start machine 
#if power supply is available=true
#safety door is closed=true
power=True
door=True
if power and door:
    print("Machine is starter")
else:
    print("Machine is not started")