#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Date Client
#
# name: Sarah Larbi
# email: slarbi@bu.edu
#
# Partner's Name: Sheryn Chung
# Partner's Emial: sherync@bu.edu

from ps9pr1 import Date

def print_birthdays(filename):
    ''' accepts a string filename as a parameter. The function should then open the file that corresponds to that filename, read through the file, and print some information derived from that file.
    '''
    
    file = open(filename, 'r')
    for line in file:
        line = line[:-1]
        
        fields = line.split(',')
        name = fields[0]
        new_month = int(fields[1])
        new_day = int(fields[2])
        new_year = int(fields[3])
        d = Date(new_month, new_day, new_year)
        day = d.day_of_week()


        print(name + ' ' + '(' + str(d) + ')' + ' ' + '(' + day + ')')
        
    file.close()
