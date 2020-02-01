import subprocess
import shutil
import dc_results as dr
import os
import itertools

#list containing fault
fault_vectors = itertools.combinations(range(1,40),2)

#fault_dict
fault_dict = {1:('mnm12','SG'),2:('mnm12','DG'),3:('mnm12','SD'),4:('mnm11','SG'),5:('mnm11','SD'),6:('mnb02','SG'),7:('mnb02','SD'),8:('mnpd1','SG'),9:('mnpd1','DG'),10:('mnpd1','SD'),11:('mn001','SG'),12:('mn001','DG'),13:('mn001','SD'),14:('mnpd2','SG'),15:('mnpd2','DG'),16:('mnpd2','SD'),17:('mnc01','SG'),18:('mnc01','DG'),19:('mnc01','SD'),20:('mpb02','SG'),21:('mpb02','DG'),22:('mpb02','SD'),23:('mppd1','SG'),24:('mppd1','DG'),25:('mppd1','SD'),26:('mps11','SG'),27:('mps11','DG'),28:('mps11','SD'),29:('mpd11','SG'),30:('mpd11','DG'),31:('mpd11','SD'),32:('mp001','SG'),33:('mp001','DG'),34:('mp001','SD'),35:('mpd12','SG'),36:('mpd12','DG'),37:('mpd12','SD'),38:('mpb01','SG'),39:('mpb01','SD')}

transistor_map = {}
#drain gate source map
dgs_map = {'D':1,'G':2,'S':3}

with open("/home/research/aditya_btech/working_directory/analog_benchmark2017_v2.2/subcircuit_files/OPAMP1.sub","r") as file1:
    data = file1.readlines()
    
#create the transistor vs line map   
for no,lines in enumerate(data):
    transistor_map[lines.split(" ")[0]] = no 

for fn, fault_list in enumerate(fault_vectors):
    f = open("/home/research/aditya_btech/working_directory/analog_benchmark2017_v2.2/subcircuit_files/OPAMP1.sub","w")
    with open("/home/research/aditya_btech/working_directory/analog_benchmark2017_v2.2/subcircuit_files/OPAMP1.sub","a") as f:
        for line in data[0:34]:
            f.write(line)   

        for no,fault in enumerate(fault_list):
            line_no = transistor_map[fault_dict[fault][0]]

            dgs = data[line_no]
            fault_code = 'R' + str(no) + " " + dgs.split(" ")[dgs_map[fault_dict[fault][1][0]]] + " "+ dgs.split(" ")[dgs_map[fault_dict[fault][1][1]]] + " " + str(1) +'\n'
            f.write(fault_code)

        f.write('.ends\n')
    output = subprocess.check_output("spectre OPAMP1.circuit", shell=True)
    print(fault_list)
    dr.add_entry(fault_list)
    # shutil.copy('/home/research/aditya_btech/working_directory/analog_benchmark2017_v2.2/OPAMP1.print', '/home/research/aditya_btech/working_directory/analog_benchmark2017_v2.2/Print')
    # os.rename('/home/research/aditya_btech/working_directory/analog_benchmark2017_v2.2/Print/OPAMP1.print','/home/research/aditya_btech/working_directory/analog_benchmark2017_v2.2/Print/OPAMP' + str(fn) +'.print')

