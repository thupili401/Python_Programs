a={
    "car": "i10",
    "price":"3.75l",
    "colour": "red",
    "milage": "18km"

}

print(a["car"])
print(a.keys()) #to print all the dict
print(a.values()) #to print all the values
a["colour"]="green"  #update the value
print(a.values()) #to print all the values

key=["Sree",'Kranthi','Lee']
values=['Alekhya','Prashanthi','Sravanthi']
data=dict(zip(key,values))
print(data)
data['Sreekanth']="Amma & Nanna"
print(data)
print(data.keys())
print(data.values())