Temp_input = float(input("enter temprature:"))
Temp_unit = input("enter its unit :")
if ("c" in Temp_unit or "C" in Temp_unit):
     print("temprature in farenheit : ",(Temp_input*(9/5) + 32) ,"°F")
elif("f" in Temp_unit or "F" in Temp_unit):
      print("temprature in celcius :",( (Temp_input -32)*5/9),"°C")     
else:
     print("invalid unit!,please enter unit in (c or f)")
   