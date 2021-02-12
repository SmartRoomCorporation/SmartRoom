from random import randrange

class RoomSimulation():
    day = 1339 # MAX
    count = 0 # MOMENTO CORRENTE
    temperature = 16.3
    humidity = 19.8
    morning = 719
    people = 0
    # range 0 - 719 GIORNO
    # range 720 - 1339 NOTTE

    def genTemperature(self):
        if(self.count <= self.morning): #16.3 - 20.0
            #GIORNO
            if(self.count <= self.morning):
                if(self.count > 0 and self.count <= 143): #16.3 - 17.8
                    if(self.count / 36 < 1): # primo pezzo
                        if(randrange(6) is 0): self.temperature = 16.4
                        if(randrange(6) is 1): self.temperature = 16.5
                        if(randrange(6) is 2): self.temperature = 16.7
                        if(randrange(6) is 3): self.temperature = 16.8
                        if(randrange(6) is 4): self.temperature = 16.6
                        if(randrange(6) is 5): self.temperature = 16.3
                    if(self.count / 36 >= 1): # secondo pezzo
                        if(randrange(6) is 0): self.temperature = 16.7
                        if(randrange(6) is 1): self.temperature = 17.1
                        if(randrange(6) is 2): self.temperature = 17.0
                        if(randrange(6) is 3): self.temperature = 16.9
                        if(randrange(6) is 4): self.temperature = 16.8
                        if(randrange(6) is 5): self.temperature = 16.7
                    if(self.count / 36 >= 2): # terzo pezzo
                        if(randrange(6) is 0): self.temperature = 17.0
                        if(randrange(6) is 1): self.temperature = 16.9
                        if(randrange(6) is 2): self.temperature = 17.3
                        if(randrange(6) is 3): self.temperature = 17.4
                        if(randrange(6) is 4): self.temperature = 16.9
                        if(randrange(6) is 5): self.temperature = 17.2
                    if(self.count / 36 >= 3): # quarto pezzo
                        if(randrange(6) is 0): self.temperature = 17.4
                        if(randrange(6) is 1): self.temperature = 17.5
                        if(randrange(6) is 2): self.temperature = 17.8
                        if(randrange(6) is 3): self.temperature = 17.6
                        if(randrange(6) is 4): self.temperature = 17.7
                        if(randrange(6) is 5): self.temperature = 17.4

                elif(self.count > 144 and self.count <= 287): #17.5 - 18.6
                    if(self.count / 36 >= 4): # primo pezzo
                        if(randrange(6) is 0): self.temperature = 17.5
                        if(randrange(6) is 1): self.temperature = 17.7
                        if(randrange(6) is 2): self.temperature = 17.9
                        if(randrange(6) is 3): self.temperature = 17.6
                        if(randrange(6) is 4): self.temperature = 17.7
                        if(randrange(6) is 5): self.temperature = 17.8
                    if(self.count / 36 >= 5): # secondo pezzo
                        if(randrange(6) is 0): self.temperature = 17.8
                        if(randrange(6) is 1): self.temperature = 17.7
                        if(randrange(6) is 2): self.temperature = 17.9
                        if(randrange(6) is 3): self.temperature = 18.0
                        if(randrange(6) is 4): self.temperature = 18.1
                        if(randrange(6) is 5): self.temperature = 18.0
                    if(self.count / 36 >= 6): # terzo pezzo
                        if(randrange(6) is 0): self.temperature = 18.0
                        if(randrange(6) is 1): self.temperature = 18.1
                        if(randrange(6) is 2): self.temperature = 18.2
                        if(randrange(6) is 3): self.temperature = 18.3
                        if(randrange(6) is 4): self.temperature = 18.4
                        if(randrange(6) is 5): self.temperature = 18.2
                    if(self.count / 36 >= 7): # quarto pezzo
                        if(randrange(6) is 0): self.temperature = 18.3
                        if(randrange(6) is 1): self.temperature = 18.4
                        if(randrange(6) is 2): self.temperature = 18.5
                        if(randrange(6) is 3): self.temperature = 18.6
                        if(randrange(6) is 4): self.temperature = 18.5
                        if(randrange(6) is 5): self.temperature = 18.4

                elif(self.count > 288 and self.count <= 431): #18.6 - 20
                    if(self.count / 36 >= 8): # primo pezzo
                        if(randrange(6) is 0): self.temperature = 18.8
                        if(randrange(6) is 1): self.temperature = 18.7
                        if(randrange(6) is 2): self.temperature = 18.9
                        if(randrange(6) is 3): self.temperature = 19.0
                        if(randrange(6) is 4): self.temperature = 19.1
                        if(randrange(6) is 5): self.temperature = 19.0
                    if(self.count / 36 >= 9): # secondo pezzo
                        if(randrange(6) is 0): self.temperature = 19.2
                        if(randrange(6) is 1): self.temperature = 19.3
                        if(randrange(6) is 2): self.temperature = 19.4
                        if(randrange(6) is 3): self.temperature = 19.6
                        if(randrange(6) is 4): self.temperature = 19.7
                        if(randrange(6) is 5): self.temperature = 19.5
                    if(self.count / 36 >= 10): # terzo pezzo
                        if(randrange(6) is 0): self.temperature = 20.0
                        if(randrange(6) is 1): self.temperature = 19.9
                        if(randrange(6) is 2): self.temperature = 19.8
                        if(randrange(6) is 3): self.temperature = 19.6
                        if(randrange(6) is 4): self.temperature = 19.7
                        if(randrange(6) is 5): self.temperature = 19.5
                    if(self.count / 36 >= 11): # quarto pezzo
                        if(randrange(6) is 0): self.temperature = 19.2
                        if(randrange(6) is 1): self.temperature = 19.3
                        if(randrange(6) is 2): self.temperature = 19.4
                        if(randrange(6) is 3): self.temperature = 19.6
                        if(randrange(6) is 4): self.temperature = 19.7
                        if(randrange(6) is 5): self.temperature = 19.5

                elif(self.count > 432 and self.count <= 575): #17.5 - 19.0
                    if(self.count / 36 >= 12): # primo pezzo
                        if(randrange(6) is 0): self.temperature = 19.0
                        if(randrange(6) is 1): self.temperature = 18.9
                        if(randrange(6) is 2): self.temperature = 18.7
                        if(randrange(6) is 3): self.temperature = 18.6
                        if(randrange(6) is 4): self.temperature = 18.7
                        if(randrange(6) is 5): self.temperature = 18.8
                    if(self.count / 36 >= 13): # secondo pezzo
                        if(randrange(6) is 0): self.temperature = 18.3
                        if(randrange(6) is 1): self.temperature = 18.5
                        if(randrange(6) is 2): self.temperature = 18.4
                        if(randrange(6) is 3): self.temperature = 18.3
                        if(randrange(6) is 4): self.temperature = 18.5
                        if(randrange(6) is 5): self.temperature = 18.2
                    if(self.count / 36 >= 14): # terzo pezzo
                        if(randrange(6) is 0): self.temperature = 18.0
                        if(randrange(6) is 1): self.temperature = 18.1
                        if(randrange(6) is 2): self.temperature = 17.9
                        if(randrange(6) is 3): self.temperature = 17.8
                        if(randrange(6) is 4): self.temperature = 18.0
                        if(randrange(6) is 5): self.temperature = 17.8
                    if(self.count / 36 >= 15): # quarto pezzo
                        if(randrange(6) is 0): self.temperature = 17.8
                        if(randrange(6) is 1): self.temperature = 17.7
                        if(randrange(6) is 2): self.temperature = 17.6
                        if(randrange(6) is 3): self.temperature = 17.5
                        if(randrange(6) is 4): self.temperature = 17.7
                        if(randrange(6) is 5): self.temperature = 17.5

                elif(self.count > 576 and self.count <= 719): #16.3 - 17.8
                    if(self.count / 36 >= 16): # primo pezzo
                        if(randrange(6) is 0): self.temperature = 17.6
                        if(randrange(6) is 1): self.temperature = 17.5
                        if(randrange(6) is 2): self.temperature = 17.6
                        if(randrange(6) is 3): self.temperature = 17.4
                        if(randrange(6) is 4): self.temperature = 17.7
                        if(randrange(6) is 5): self.temperature = 17.5
                    if(self.count / 36 >= 17): # secondo pezzo
                        if(randrange(6) is 0): self.temperature = 17.4
                        if(randrange(6) is 1): self.temperature = 17.3
                        if(randrange(6) is 2): self.temperature = 17.2
                        if(randrange(6) is 3): self.temperature = 17.2
                        if(randrange(6) is 4): self.temperature = 17.1
                        if(randrange(6) is 5): self.temperature = 17.3
                    if(self.count / 36 >= 18): # terzo pezzo
                        if(randrange(6) is 0): self.temperature = 16.8
                        if(randrange(6) is 1): self.temperature = 17.0
                        if(randrange(6) is 2): self.temperature = 17.1
                        if(randrange(6) is 3): self.temperature = 17.0
                        if(randrange(6) is 4): self.temperature = 16.8
                        if(randrange(6) is 5): self.temperature = 16.9
                    if(self.count / 36 >= 19): # quarto pezzo
                        if(randrange(6) is 0): self.temperature = 16.7
                        if(randrange(6) is 1): self.temperature = 16.4
                        if(randrange(6) is 2): self.temperature = 16.3
                        if(randrange(6) is 3): self.temperature = 16.5
                        if(randrange(6) is 4): self.temperature = 16.5
                        if(randrange(6) is 5): self.temperature = 16.6
            #NOTTE
            #elif(self.count > self.morning and self.count <= self.day):
            #    return False
            self.count += 1
        elif(self.count > self.morning):
            self.count = 0
            self.genTemperature()


    def genHumidity(self): 
        if(self.count <= self.morning): #18.8 - 24.0
            #GIORNO
            if(self.count <= self.morning):
                if(self.count > 0 and self.count <= 143): #19.8 - 22.5
                    if(self.count / 36 < 1): # primo pezzo
                        if(randrange(6) is 0): self.humidity = 18.9
                        if(randrange(6) is 1): self.humidity = 18.8
                        if(randrange(6) is 2): self.humidity = 18.9
                        if(randrange(6) is 3): self.humidity = 19.7
                        if(randrange(6) is 4): self.humidity = 19.5
                        if(randrange(6) is 5): self.humidity = 19.3
                    if(self.count / 36 >= 1): # secondo pezzo
                        if(randrange(6) is 0): self.humidity = 19.5
                        if(randrange(6) is 1): self.humidity = 19.6
                        if(randrange(6) is 2): self.humidity = 19.3
                        if(randrange(6) is 3): self.humidity = 19.5
                        if(randrange(6) is 4): self.humidity = 19.6
                        if(randrange(6) is 5): self.humidity = 19.7
                    if(self.count / 36 >= 2): # terzo pezzo
                        if(randrange(6) is 0): self.humidity = 20.0
                        if(randrange(6) is 1): self.humidity = 20.5
                        if(randrange(6) is 2): self.humidity = 20.3
                        if(randrange(6) is 3): self.humidity = 20.7
                        if(randrange(6) is 4): self.humidity = 20.9
                        if(randrange(6) is 5): self.humidity = 20.7
                    if(self.count / 36 >= 3): # quarto pezzo
                        if(randrange(6) is 0): self.humidity = 21.0
                        if(randrange(6) is 1): self.humidity = 20.9
                        if(randrange(6) is 2): self.humidity = 21.4
                        if(randrange(6) is 3): self.humidity = 21.5
                        if(randrange(6) is 4): self.humidity = 21.3
                        if(randrange(6) is 5): self.humidity = 21.1

                elif(self.count > 144 and self.count <= 287): #22.3 - 24.7
                    if(self.count / 36 >= 4): # primo pezzo
                        if(randrange(6) is 0): self.humidity = 21.3
                        if(randrange(6) is 1): self.humidity = 21.5
                        if(randrange(6) is 2): self.humidity = 21.4
                        if(randrange(6) is 3): self.humidity = 21.6
                        if(randrange(6) is 4): self.humidity = 21.7
                        if(randrange(6) is 5): self.humidity = 21.5
                    if(self.count / 36 >= 5): # secondo pezzo
                        if(randrange(6) is 0): self.humidity = 21.6
                        if(randrange(6) is 1): self.humidity = 21.7
                        if(randrange(6) is 2): self.humidity = 21.8
                        if(randrange(6) is 3): self.humidity = 21.6
                        if(randrange(6) is 4): self.humidity = 21.9
                        if(randrange(6) is 5): self.humidity = 22.1
                    if(self.count / 36 >= 6): # terzo pezzo
                        if(randrange(6) is 0): self.humidity = 22.6
                        if(randrange(6) is 1): self.humidity = 22.5
                        if(randrange(6) is 2): self.humidity = 22.4
                        if(randrange(6) is 3): self.humidity = 22.4
                        if(randrange(6) is 4): self.humidity = 22.8
                        if(randrange(6) is 5): self.humidity = 22.7
                    if(self.count / 36 >= 7): # quarto pezzo
                        if(randrange(6) is 0): self.humidity = 23.0
                        if(randrange(6) is 1): self.humidity = 23.1
                        if(randrange(6) is 2): self.humidity = 23.2
                        if(randrange(6) is 3): self.humidity = 23.4
                        if(randrange(6) is 4): self.humidity = 23.5
                        if(randrange(6) is 5): self.humidity = 23.7

                elif(self.count > 288 and self.count <= 431): #24.6 - 26
                    if(self.count / 36 >= 8): # primo pezzo
                        if(randrange(6) is 0): self.humidity = 23.8
                        if(randrange(6) is 1): self.humidity = 23.7
                        if(randrange(6) is 2): self.humidity = 23.9
                        if(randrange(6) is 3): self.humidity = 24.0
                        if(randrange(6) is 4): self.humidity = 24.1
                        if(randrange(6) is 5): self.humidity = 24.2
                    if(self.count / 36 >= 9): # secondo pezzo
                        if(randrange(6) is 0): self.humidity = 24.1
                        if(randrange(6) is 1): self.humidity = 24.3
                        if(randrange(6) is 2): self.humidity = 24.6
                        if(randrange(6) is 3): self.humidity = 24.7
                        if(randrange(6) is 4): self.humidity = 24.4
                        if(randrange(6) is 5): self.humidity = 24.9
                    if(self.count / 36 >= 10): # terzo pezzo
                        if(randrange(6) is 0): self.humidity = 25.0
                        if(randrange(6) is 1): self.humidity = 24.8
                        if(randrange(6) is 2): self.humidity = 24.9
                        if(randrange(6) is 3): self.humidity = 24.5
                        if(randrange(6) is 4): self.humidity = 24.6
                        if(randrange(6) is 5): self.humidity = 24.7
                    if(self.count / 36 >= 11): # quarto pezzo
                        if(randrange(6) is 0): self.humidity = 23.8
                        if(randrange(6) is 1): self.humidity = 23.7
                        if(randrange(6) is 2): self.humidity = 23.9
                        if(randrange(6) is 3): self.humidity = 24.0
                        if(randrange(6) is 4): self.humidity = 24.1
                        if(randrange(6) is 5): self.humidity = 24.2

                elif(self.count > 432 and self.count <= 575): #22.3 - 24.7
                    if(self.count / 36 >= 12): # primo pezzo
                        if(randrange(6) is 0): self.humidity = 23.0
                        if(randrange(6) is 1): self.humidity = 23.1
                        if(randrange(6) is 2): self.humidity = 23.2
                        if(randrange(6) is 3): self.humidity = 23.4
                        if(randrange(6) is 4): self.humidity = 23.5
                        if(randrange(6) is 5): self.humidity = 23.7
                    if(self.count / 36 >= 13): # secondo pezzo
                        if(randrange(6) is 0): self.humidity = 22.6
                        if(randrange(6) is 1): self.humidity = 22.5
                        if(randrange(6) is 2): self.humidity = 22.4
                        if(randrange(6) is 3): self.humidity = 22.4
                        if(randrange(6) is 4): self.humidity = 22.8
                        if(randrange(6) is 5): self.humidity = 22.7
                    if(self.count / 36 >= 14): # terzo pezzo
                        if(randrange(6) is 0): self.humidity = 21.6
                        if(randrange(6) is 1): self.humidity = 21.7
                        if(randrange(6) is 2): self.humidity = 21.8
                        if(randrange(6) is 3): self.humidity = 21.6
                        if(randrange(6) is 4): self.humidity = 21.9
                        if(randrange(6) is 5): self.humidity = 22.1
                    if(self.count / 36 >= 15): # quarto pezzo
                        if(randrange(6) is 0): self.humidity = 21.3
                        if(randrange(6) is 1): self.humidity = 21.5
                        if(randrange(6) is 2): self.humidity = 21.4
                        if(randrange(6) is 3): self.humidity = 21.6
                        if(randrange(6) is 4): self.humidity = 21.7
                        if(randrange(6) is 5): self.humidity = 21.5
                        

                elif(self.count > 576 and self.count <= 719): #19.8 - 22.5
                    if(self.count / 36 >= 16): # primo pezzo
                        if(randrange(6) is 0): self.humidity = 21.0
                        if(randrange(6) is 1): self.humidity = 20.9
                        if(randrange(6) is 2): self.humidity = 21.4
                        if(randrange(6) is 3): self.humidity = 21.5
                        if(randrange(6) is 4): self.humidity = 21.3
                        if(randrange(6) is 5): self.humidity = 21.1
                    if(self.count / 36 >= 17): # secondo pezzo
                        if(randrange(6) is 0): self.humidity = 20.0
                        if(randrange(6) is 1): self.humidity = 20.5
                        if(randrange(6) is 2): self.humidity = 20.3
                        if(randrange(6) is 3): self.humidity = 20.7
                        if(randrange(6) is 4): self.humidity = 20.9
                        if(randrange(6) is 5): self.humidity = 20.7
                    if(self.count / 36 >= 18): # terzo pezzo
                        if(randrange(6) is 0): self.humidity = 19.5
                        if(randrange(6) is 1): self.humidity = 19.6
                        if(randrange(6) is 2): self.humidity = 19.3
                        if(randrange(6) is 3): self.humidity = 19.5
                        if(randrange(6) is 4): self.humidity = 19.6
                        if(randrange(6) is 5): self.humidity = 19.7
                    if(self.count / 36 >= 19): # quarto pezzo
                        if(randrange(6) is 0): self.humidity = 18.9
                        if(randrange(6) is 1): self.humidity = 18.8
                        if(randrange(6) is 2): self.humidity = 18.9
                        if(randrange(6) is 3): self.humidity = 19.7
                        if(randrange(6) is 4): self.humidity = 19.5
                        if(randrange(6) is 5): self.humidity = 19.3
            #NOTTE
            #elif(self.count > self.morning and self.count <= self.day):
            #    return False
            self.count += 1
        elif(self.count > self.morning):
            self.count = 0
            self.genHumidity() 

    def addPerson(self):
        self.people += 1
    
    def removePerson(self):
        if(self.people > 0): self.people -= 1