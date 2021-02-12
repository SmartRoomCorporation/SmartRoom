
class TempHumSystem():
    N = 5
    fan = 0
    FAN0 = 0
    FAN25 = 25
    FAN50 = 50
    FAN75 = 75
    FAN100 = 100
    hum_theta = 0.08569
    temp_theta = 0.19987
    inter_theta = -4.816
    humidity = 0
    temperature = 0
    peoplecalc = 0

    def setHumidity(self, hum):
        self.humidity = hum

    def setTemperature(self, temp):
        self.temperature = temp

    def computePeople(self):
        self.peoplecalc = self.temperature*self.temp_theta + self.humidity*self.hum_theta + self.inter_theta
        self.changeState()
        return self.peoplecalc

    def changeState(self):
        if(self.peoplecalc < 1): self.fan = self.FAN0
        if(self.peoplecalc >= 1): self.fan = self.FAN25
        if(self.peoplecalc >= self.N/4): self.fan = self.FAN50
        if(self.peoplecalc >= self.N/2): self.fan = self.FAN75
        if(self.peoplecalc >= self.N*3/4): self.fan = self.FAN100
        if(self.peoplecalc >= self.N): 
            self.fan = self.FAN100
            self.alarm()

    def alaram(self):
        print("ALARM")