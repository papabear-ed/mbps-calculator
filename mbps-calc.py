import sys

# MBps -> Mbps

#Class for colors
class bcolors:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

# Print the Title and Rev Number
def banner():
    print(bcolors.green + '''
  _    _    _    _    _  
 / \  / \  / \  / \  / \ 
( K )( - )( N )( E )( T )
 \_/  \_/  \_/  \_/  \_/  Presents: ''')
    print(bcolors.blue + '''
              __                  __                              
|\ |  _ |_   (_   _   _  _  _|   /    _  |  _     |  _  |_  _   _ 
| \| (- |_   __) |_) (- (- (_|   \__ (_| | (_ |_| | (_| |_ (_) |  
                 |                          
                                            Rev: 1 
                                            By: K-Net                      
                                                            
''')

class Net_Calc_Bytes_Bits:
    count = 0

    def __init__(self):
        try:
            print(bcolors.lightred + '\n [+[+[ Initializing program ]+]+]+')
            print(bcolors.lightred + '\n ----------------------------------------------------------------------------------------')
            print(bcolors.lightred + '\n [+[+[ Welcome to KNets network speed calculator..... ]+]+]' )
            print(bcolors.lightred + '\n ----------------------------------------------------------------------------------------')
            print(bcolors.orange + '\n [+[+[ Things you will need are as follows: ]+]+]')
            print(bcolors.orange + '''     [ Total size of data transferred (GB, MB, KB, or B) ]''')
            print(bcolors.orange + '''     [ Total time data took to transfer (Hours, Minutes, and Seconds) ]''')
            print(bcolors.lightred + "\n ----------------------------------------------------------------------------------------")
            print("")
            self.datasize = float(input(bcolors.green + ' ========== Enter the data amount transferred >: '))
            self.datatype = int(input(bcolors.green + ' ========== Enter data type (1,2,3,4) 1:GB, 2:MB, 3:KB, 4:Bytes >:'))
            if int(self.datatype) > int(4) or int(self.datatype) <int(1):
                print('ERROR: Invalid Option........ Exiting.....')
                sys.exit(1)
            self.hrs = int(input(bcolors.green + ' ========== Enter how many hours did it take to transfer >:'))
            self.mins = int(input(bcolors.green + ' ========== Enter how many minutes did it take to transfer >:'))
            self.secs = int(input(bcolors.green + ' ========== Enter how many additional seconds did it take to transfer >:'))
            if int(self.secs) > int(60):
                print('ERROR: Invalid Option........ Exiting.....')
                sys.exit(1)

        except Exception as e:
            print(f'ERROR: {e}')

    def dataCalc(self):
        # convert GB, MB, or KB to Bytes
        if self.datatype == int(1):
            self.bytes = self.datasize * int(1000000000)
        elif self.datatype == int(2):
            self.bytes = int(self.datasize) * int(1000000)
        elif self.datatype == int(3):
            self.bytes = int(self.datasize) * int(1000)
        elif self.datatype == int(4):
            self.bytes = int(self.datasize)
        print(bcolors.yellow + f'      [  The total number of bytes transferred is: {self.bytes}  ]')
        # Convert bytes to Bits
        self.bits = self.bytes * int(8)
        print(bcolors.yellow + f'      [  The total number of bits transferred is: {self.bits}  ]')

    def timeCalc(self):
        # Add time up to seconds
        # Convert hours to minutes
        self.hrsMins = self.hrs * int(60)
        # Add up minutes 
        self.minsTotal = self.hrsMins + self.mins
        # Convert mins to secs
        self.minsSecs = self.minsTotal * int(60)
        # Add up secs
        self.secsTotal = self.minsSecs + self.secs
        print(bcolors.cyan + f'      [  The total seconds it took to transfer the data is: {self.secsTotal}  ]')

    def bps(self):
        self.bps = self.bits / self.secsTotal
        self.bpsRound = round(self.bps, 2)
        self.kbps = self.bps / int(1000)
        self.kbpsRound = round(self.kbps, 2)
        self.mbps = self.bps / int(1000000)
        self.mbpsRound = round(self.mbps, 2)
        self.gbps = self.bps / int(1000000000)
        self.gbpsRound = round(self.gbps, 2)
        print(bcolors.purple + f'      [  Your total transfer speed is: {self.bpsRound} bps  ]')
        print(bcolors.purple + f'      [  Your total transfer speed is: {self.kbpsRound} kbps  ]')
        print(bcolors.purple + f'      [  Your total transfer speed is: {self.mbpsRound} mbps  ]')
      #  print(bcolors.orange + f'      [ Your total transfer speed is: {self.gbps} gbps ]')

if __name__=='__main__':
    banner()
    calc = Net_Calc_Bytes_Bits()
    calc.dataCalc()
    calc.timeCalc()
    calc.bps()
