import pyvisa
import time
from epics import caget, caput, cainfo


visa_address = 'TCPIP::172.21.161.49::INSTR'

rm = pyvisa.ResourceManager()
#print(rm.list_resources())
scope = rm.open_resource(visa_address)

run = 1

while run == 1:

    caput("LAS:CAST:FLOAT:01",scope.query('MEASUREMENT:MEAS1:VALUE?')) #QUERY SCOPE FOR MEAS 1 - PHASE DIFFERENCE BETWEEN S29 - NEH
    caput("LAS:CAST:FLOAT:02",scope.query('MEASUREMENT:MEAS2:VALUE?')) #QUERY SCOPE FOR MEAS 2 - PHASE DIFFERENCE BETWEEN S29 - FEH
    caput("LAS:CAST:FLOAT:03",scope.query('MEASUREMENT:MEAS3:VALUE?')) #QUERY SCOPE FOR MEAS 3 - AMPLITUDE OF S29 REF RF, ASSIGN TO PV
    caput("LAS:CAST:FLOAT:04",scope.query('MEASUREMENT:MEAS4:VALUE?')) #QUERY SCOPE FOR MEAS 4 - AMPLITUDE OF NEH CAST REF RF, ASSIGN TO PV

    time.sleep(5)
    
# use bash command "nohup python run.py" to keep it running in the background
    
















































































































