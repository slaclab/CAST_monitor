# import pyvisa
import vxi11
import time
from epics import caget, caput, cainfo


visa_address = 'TCPIP::172.21.161.39::INSTR'

# rm = pyvisa.ResourceManager()
#print(rm.list_resources())
# scope = rm.open_resource(visa_address)
instr =  vxi11.Instrument(visa_address)

## Measurement setup 
# instr.write('CH1:SCALE 2.0E-1')
# instr.write('CH2:SCALE 2.0E-1')
# instr.write('CH3:SCALE 2.0E-1')
# instr.write('MEASUREMENT:MEAS3:STATE ON')
# instr.write('MEASUREMENT:MEAS3:TYPE DELAY CH1:CH2')
# instr.write('MEASUREMENT:MEAS4:TYPE DELAY CH1:CH3')

run = 1
while run == 1:
    caput("LAS:CAST:FLOAT:01",instr.ask('MEASUREMENT:MEAS1:VALUE?')) #QUERY SCOPE FOR MEAS 1 - PHASE DIFFERENCE BETWEEN S29 - NEH
    caput("LAS:CAST:FLOAT:02",instr.ask('MEASUREMENT:MEAS3:VALUE?')) #QUERY SCOPE FOR MEAS 2 - PHASE DIFFERENCE BETWEEN S29 - FEH
    # caput("LAS:CAST:FLOAT:03",instr.ask('MEASUREMENT:MEAS3:VALUE?')) #QUERY SCOPE FOR MEAS 3 - AMPLITUDE OF S29 REF RF, ASSIGN TO PV
    # caput("LAS:CAST:FLOAT:04",instr.ask('MEASUREMENT:MEAS4:VALUE?')) #QUERY SCOPE FOR MEAS 4 - AMPLITUDE OF NEH CAST REF RF, ASSIGN TO PV

    time.sleep(0.1) # update rate to 10 Hz 
