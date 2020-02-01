# ================= Working =================

# output_file = "/home/research/aditya_btech/working_directory/analog_benchmark2017_v2.2/dc_ports.csv"

# from os import listdir
# from os.path import isfile, join
# mypath = '/home/research/aditya_btech/working_directory/analog_benchmark2017_v2.2/OPAMP1.print'
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


# bad_words = ['* * Disclaimer:\n', ' ******  DC Analysis ( dcrun1 )  tnom= 27.0 temp= 27.0\n', '******\n','x\n', 'y\n', 'freq' ]

# for file in onlyfiles:
# lst = []
# for i in range(14):
#     lst.append(0)
# x = file.split('MP')[1].split('.')[0]
# x1,x2 = int(x[0:2])-20,int(x[2:4])-20
# lst[x1] = 1
# lst[x2] = 1
def add_entry(fault_list):
    output_file = "/home/research/aditya_btech/working_directory/analog_benchmark2017_v2.2/dc_ports.csv"
    mypath = '/home/research/aditya_btech/working_directory/analog_benchmark2017_v2.2/OPAMP1.print'
    bad_words = ['* * Disclaimer:\n', ' ******  DC Analysis ( dcrun1 )  tnom= 27.0 temp= 27.0\n', '******\n','x\n', 'y\n', 'freq' ]

    with open(mypath) as oldfile, open('temp.txt', 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                line = line.replace(' m','m')
                line = line.replace(' n','n')
                line = line.replace(' k','k')
                line = line.replace(' u','u')
                line = line.replace(' p','p')
                line = line.replace(' f','f')
                newfile.write(line)

    oldfile.close()
    newfile.close()


    input_file = open("temp.txt")
    out_string = ''
    line_no = 0
    line = input_file.readline()
    for line in input_file:
        line_no += 1
        y = line.split()
        line = input_file.readline()
        
        # print(y)
        
        for i in range(1,len(y)):           # discard the 1st 0 under dc column
            out_string = out_string + ',' + y[i]
    fault_str = str(fault_list)
    out_string = fault_str[1:len(fault_str)-1]+ ','+ out_string  + ';\n'

    # print(line_no)

    f=open(output_file, "a+")
    f.write(out_string)

    f.close()
