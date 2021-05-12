from modules.SensorModule.TempHumModule.RoomConditioning import RoomConditioning
import matplotlib.pyplot as plt

r = RoomConditioning()
humidity = []
hummod = []
humcond = []
humcalc = []


for i in range(180):
    r.hummodGen()
    r.humcondGen()
    r.computeHumcalc()
    humidity.append(r.room.humidity)
    hummod.append(r.hummod)
    humcond.append(r.humcond)
    humcalc.append(r.humcalc)



r.room.addPerson()
r.sys.fan = 25


for i in range(180):
    r.hummodGen()
    r.humcondGen()
    r.computeHumcalc()
    humidity.append(r.room.humidity)
    hummod.append(r.hummod)
    humcond.append(r.humcond)
    humcalc.append(r.humcalc)


r.room.addPerson()
r.room.addPerson()
r.sys.fan = 75

for i in range(180):
    r.hummodGen()
    r.humcondGen()
    r.computeHumcalc()
    humidity.append(r.room.humidity)
    hummod.append(r.hummod)
    humcond.append(r.humcond)
    humcalc.append(r.humcalc)



r.room.addPerson()
r.room.addPerson()
r.sys.fan = 100

for i in range(180):
    r.hummodGen()
    r.humcondGen()
    r.computeHumcalc()
    humidity.append(r.room.humidity)
    hummod.append(r.hummod)
    humcond.append(r.humcond)
    humcalc.append(r.humcalc)



fig, axs = plt.subplots(4)
axs[0].plot(humidity)
axs[0].set_title("Evoluzione Naturale")
axs[1].plot(hummod)
axs[1].set_title("Umidità modificata dalle persone")
axs[2].plot(humcond)
axs[2].set_title("Umidità modificata dalla persone e condizionata dalla ventola")
axs[3].plot(humcalc)
axs[3].set_title("Umidità calcolata a partire da quella modificata dalle persone")
plt.show()
