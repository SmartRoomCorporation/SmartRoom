from RoomSimulation import RoomSimulation
from TempHumSystem import TempHumSystem

class RoomConditioning():
    tempmod = 0     # modificata dalla presenza delle persone
    tempcond = 0    # modificata dalle persone e dalla ventola
    tempcalc = 0
    hummod = 0     # modificata dalla presenza delle persone
    humcond = 0    # modificata dalle persone e dalla ventola
    humcalc = 0
    room = RoomSimulation()
    sys = TempHumSystem()
    fanerror = 0
    humidity_increment_per_person = 16.77180531
    temperature_increment_per_person = 9.887985059

    def tempmodGen(self):
        self.room.genTemperature()
        self.tempmod = self.room.temperature
        p = self.room.people
        for i in range(p):
            self.tempmod += (self.tempmod*self.temperature_increment_per_person)/100

    def hummodGen(self):
        self.room.genHumidity()
        self.hummod = self.room.humidity
        p = self.room.people
        for i in range(p):
            self.hummod += (self.hummod*self.humidity_increment_per_person)/100

    def computeTempFanerror(self): # crea tempcond
        fan = self.sys.fan
        if(fan == 0): self.fanerror = 0
        if(fan == 25): self.fanerror = 10 
        if(fan == 50): self.fanerror = 18 
        if(fan == 75): self.fanerror = 25 
        if(fan == 100): self.fanerror = 35 
        return self.fanerror

    def computeHumFanerror(self): # crea humcond
        fan = self.sys.fan
        if(fan == 0): self.fanerror = 0
        if(fan == 25): self.fanerror = 15 
        if(fan == 50): self.fanerror = 25 
        if(fan == 75): self.fanerror = 35 
        if(fan == 100): self.fanerror = 45 
        return self.fanerror
    
    def computeTemperror(self): # da cond a mod
        fan = self.sys.fan
        if(fan == 0): return 0
        if(fan == 25): return 15
        if(fan == 50): return 20
        if(fan == 75): return 35
        if(fan == 100): return 55
    
    def computeHumerror(self): # da cond a mod
        fan = self.sys.fan
        if(fan == 0): return 0
        if(fan == 25): return 18
        if(fan == 50): return 35
        if(fan == 75): return 55
        if(fan == 100): return 80

    def computeTempcalc(self):
        self.tempcalc = self.tempcond + (self.tempcond*self.computeTemperror())/100

    def computeHumcalc(self):
        self.humcalc = self.humcond + (self.humcond*self.computeHumerror())/100

    def tempcondGen(self):
        self.tempcond = self.tempmod - (self.computeTempFanerror()*self.tempmod)/100
    
    def humcondGen(self):
        self.humcond = self.hummod - (self.computeHumFanerror()*self.hummod)/100

    def activateReading(self):
        self.sys.setHumidity(self.humcalc)
        self.sys.setTemperature(self.tempcalc)
        return self.sys.computePeople()
