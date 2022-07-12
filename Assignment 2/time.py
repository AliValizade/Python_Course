seconds = int(input("Plz enter seconds: "))
h = int(seconds / 3600)
m = int((seconds % 3600) / 60)
s = seconds % 60
print("time = ", h,":",m,":",s )
