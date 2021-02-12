from RoomConditioning import RoomConditioning
import matplotlib.pyplot as plt

r = RoomConditioning()
temperature = []
tempmod = []
tempcond = []
tempcalc = []


for i in range(180):
    r.tempmodGen()
    r.tempcondGen()
    r.computeTempcalc()
    temperature.append(r.room.temperature)
    tempmod.append(r.tempmod)
    tempcond.append(r.tempcond)
    tempcalc.append(r.tempcalc)



r.room.addPerson()
r.sys.fan = 25

for i in range(180):
    r.tempmodGen()
    r.tempcondGen()
    r.computeTempcalc()
    temperature.append(r.room.temperature)
    tempmod.append(r.tempmod)
    tempcond.append(r.tempcond)
    tempcalc.append(r.tempcalc)

print(r.room.temperature)
print(r.tempcond)

r.room.addPerson()
r.room.addPerson()
r.sys.fan = 75
for i in range(180):
    r.tempmodGen()
    r.tempcondGen()
    r.computeTempcalc()
    temperature.append(r.room.temperature)
    tempmod.append(r.tempmod)
    tempcond.append(r.tempcond)
    tempcalc.append(r.tempcalc)

print(r.room.temperature)
print(r.tempcond)

r.room.addPerson()
r.room.addPerson()
r.sys.fan = 100
for i in range(180):
    r.tempmodGen()
    r.tempcondGen()
    r.computeTempcalc()
    temperature.append(r.room.temperature)
    tempmod.append(r.tempmod)
    tempcond.append(r.tempcond)
    tempcalc.append(r.tempcalc)

print(r.room.temperature)
print(r.tempcond)

fig, axs = plt.subplots(4)
axs[0].plot(temperature)
axs[0].set_title("Temperature")
axs[1].plot(tempmod)
axs[1].set_title("Tempmod")
axs[2].plot(tempcond)
axs[2].set_title("Tempcond")
axs[3].plot(tempcalc)
axs[3].set_title("Tempcalc")
plt.show()



    