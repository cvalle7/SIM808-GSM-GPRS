import serial
import time 

class GPS():
    def __init__(self, port, baudrate):
        self.power = False
        self.ready = False
        self.ser = serial.Serial(port , baudrate, timeout = 0.5)

    def getPower(self):
        return self.power

    def __getReady(self):
        self.ser.write('AT+CGPSSTATUS?\r\n')
        self.ser.readline()    
        data = self.ser.readline().strip()
        self.ser.flush()
        if(data == '+CGPSSTATUS: Location Not Fix' or data == '+CGPSSTATUS: Location Unknown'):
            print data
            self.ready = False
            return self.ready
        else:
            print data
            self.ready = True
            return self.ready
        

    def setPowerOn(self):
        if(self.power == False):
            self.ser.write('AT+CGPSPWR=1\r\n')
            self.ser.readline()
            data = self.ser.readline().strip()
            self.ser.flush()
            if(data == 'OK'):
                self.power = True

    def setPowerOff(self):
        self.ser.write('AT+CGPSPWR=0\r\n')
        print self.ser.readline()
        data = self.ser.readline().strip()
        self.ser.flush()
        if(data == 'OK'):
            self.power = False

    def getLocation(self):
        if(self.power == True):
            i=False
            self.__getReady()
            if(self.ready == False):
                self.ser.readline()
                self.ser.readline()
                print('GPS module is not ready yet, please wait')
                while(i==False):
                    print('waiting...')
                    time.sleep(30)
                    self.__getReady()
                    self.ser.readline()
                    self.ser.readline()
                    if(self.ready == True):
                        print('GPS module is ready!')
                        i=True

            latlon = ''
            self.ser.write('AT+CGNSINF\r\n')

            if(i == False):
                self.ser.readline()
                self.ser.readline()
                self.ser.readline()
                latlon =  self.ser.readline()
            else:      
                self.ser.readline()
                latlon =  self.ser.readline()
            
            self.ser.readline()
            self.ser.readline()
            self.ser.flush()
            coordinates = parseLocation(latlon)
            return coordinates                    
        else:
            print ("please turn on de GPS")    
        

def parseLocation(data):

    coordinates = data.split(",")
    lat = coordinates[3]
    lng = coordinates[4]

    coord = []
    coord.append(lat)
    coord.append(lng)

    return coord





