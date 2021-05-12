from RoomConditioning import RoomConditioning

r = RoomConditioning()

# start simulation
r.room.addPerson()
for i in range(180):
    r.tempmodGen() #temp
    r.tempcondGen() #tempcond
    r.computeTempcalc() #tempcalc
    r.hummodGen() #hum
    r.humcondGen() #humcond
    r.computeHumcalc() #humcalc
    r.activateReading() #people
    print(r.room.people)
    print(r.activateReading())
    print(r.sys.fan)

print(r.room.people)
print(r.activateReading())
print(r.sys.fan)

#r.room.addPerson()
#r.sys.fan = 25

for i in range(180):
    r.tempmodGen()
    r.tempcondGen()
    r.computeTempcalc()
    r.hummodGen()
    r.humcondGen()
    r.computeHumcalc()
    r.activateReading()

print(r.room.people)
print(r.activateReading())
print(r.sys.fan)

#r.room.addPerson()
#r.room.addPerson()
#r.sys.fan = 75
for i in range(180):
    r.tempmodGen()
    r.tempcondGen()
    r.computeTempcalc()
    r.hummodGen()
    r.humcondGen()
    r.computeHumcalc()
    r.activateReading()

print(r.room.people)
print(r.activateReading())
print(r.sys.fan)

#r.room.addPerson()
#r.room.addPerson()
#r.sys.fan = 100
for i in range(180):
    r.tempmodGen()
    r.tempcondGen()
    r.computeTempcalc()
    r.hummodGen()
    r.humcondGen()
    r.computeHumcalc()
    r.activateReading()

print(r.room.people)
print(r.activateReading())
print(r.sys.fan)