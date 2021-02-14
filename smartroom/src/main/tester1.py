from modules.SensorModule.TempHumModule.RoomConditioning import RoomConditioning
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



#r.room.addPerson()
r.sys.fan = 25

for i in range(180):
    r.tempmodGen()
    r.tempcondGen()
    r.computeTempcalc()
    temperature.append(r.room.temperature)
    tempmod.append(r.tempmod)
    tempcond.append(r.tempcond)
    tempcalc.append(r.tempcalc)


#r.room.addPerson()
#r.room.addPerson()
r.sys.fan = 25
for i in range(180):
    r.tempmodGen()
    r.tempcondGen()
    r.computeTempcalc()
    temperature.append(r.room.temperature)
    tempmod.append(r.tempmod)
    tempcond.append(r.tempcond)
    tempcalc.append(r.tempcalc)


#r.room.addPerson()
#r.room.addPerson()
r.sys.fan = 25
for i in range(180):
    r.tempmodGen()
    r.tempcondGen()
    r.computeTempcalc()
    temperature.append(r.room.temperature)
    tempmod.append(r.tempmod)
    tempcond.append(r.tempcond)
    tempcalc.append(r.tempcalc)


fig, axs = plt.subplots(4)
axs[0].plot(temperature)
axs[0].set_title("Evoluzione naturale")
axs[1].plot(tempmod)
axs[1].set_title("Temperatura modificata dalle persone")
axs[2].plot(tempcond)
axs[2].set_title("Temperatura modificata dalla persone e condizionata dalla ventola")
axs[3].plot(tempcalc)
axs[3].set_title("Temperatura calcolata a partire da quella modificata dalle persone")
plt.show()



    