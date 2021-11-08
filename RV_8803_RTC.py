import numpy as np
import smbus
import time

#Create SMBUS
def create_RTC(i2c_ch):
    return smbus.SMBus(i2c_ch)

#reads date from specified address
def read_date(rtc_bus,rtc_add): 
    Day = convert_day(rtc_bus.read_byte_data(rtc_add,0x04))#Read day
    Month = convert_month(rtc_bus.read_byte_data(rtc_add,0x05)) #Read month
    Year = convert_year(rtc_bus.read_byte_data(rtc_add,0x06)) #Read year
    return Day, Month, Year

#prints date from specified address
def print_date(rtc_bus,rtc_add): 
    Day, Month, Year = read_date(rtc_bus,rtc_add)
    print(Day,'-',Month,'-',Year)

def read_time(rtc_bus,rtc_add):
    sec_100 = convert_100_sec(rtc_bus.read_byte_data(rtc_add,0x10))#Read 100th seconds
    sec = convert_sec(rtc_bus.read_byte_data(rtc_add,0x00)) #Read sec
    min = convert_min(rtc_bus.read_byte_data(rtc_add,0x01)) #Read min
    hr = convert_hour(rtc_bus.read_byte_data(rtc_add,0x02)) #Read min

    return sec_100,sec,min,hr

def print_time(rtc_bus,rtc_add):
    sec_100,sec,min,hr = read_time(rtc_bus,rtc_add)
    print(hr,':',min,':',sec,'.',sec_100)

#Converts the read int value to 8-bit binary
def read_rtc_byte(int_byte):
    #convert int to binary str
    return format(int_byte,'08b')

###
## Date Conversion Functions
###

#This function will convert the reading from the RTC
#to a string containing the current year
def convert_year(year_int):

    year_bin = read_rtc_byte(year_int) #convert int to binary

    functionvalues = np.array([80 , 40, 20, 10, 8, 4, 2 ,1]) #array that holds function values from data sheet

    sum = 0 #initialize value for year
    #Circle through bits in address and add corresponding to values
    for b in range(8):
        if year_bin[b] == '1':
            sum += functionvalues[b]

    return '20' + str(sum) #return year in string form

#This function will convert the reading from the RTC
#to a string containing the current month
def convert_month(month_int):
    month_bin = read_rtc_byte(month_int) #convert int to binary

    functionvalues = np.array([0 , 0, 0, 10, 8, 4, 2 ,1]) #array that holds function values from data sheet

    sum = 0 #initialize value for year
    #Circle through bits in address and add corresponding to values
    for b in range(8):
        if month_bin[b] == '1':
            sum += functionvalues[b]

    return str(sum) #return year in string form

#This function will convert the reading from the RTC
#to a string containing the current month
def convert_day(day_int):
    day_bin = read_rtc_byte(day_int) #convert int to binary

    functionvalues = np.array([0 , 0, 20, 10, 8, 4, 2 ,1]) #array that holds function values from data sheet

    sum = 0 #initialize value for year
    #Circle through bits in address and add corresponding to values
    for b in range(8):
        if day_bin[b] == '1':
            sum += functionvalues[b]

    return str(sum) #return year in string form

###
## Time Conversion Functions
###

def convert_100_sec(sec_h_int):
    sec_h_bin = read_rtc_byte(sec_h_int) #convert int to binary

    functionvalues = np.array([80 , 40, 20, 10, 8, 4, 2 ,1]) #array that holds function values from data sheet

    sum = 0 #initialize value for year
    #Circle through bits in address and add corresponding to values
    for b in range(8):
        if sec_h_bin[b] == '1':
            sum += functionvalues[b]

    return str(sum) #return year in string form

def convert_sec(sec_int):
    sec_bin = read_rtc_byte(sec_int) #convert int to binary

    functionvalues = np.array([0 , 40, 20, 10, 8, 4, 2 ,1]) #array that holds function values from data sheet

    sum = 0 #initialize value for year
    #Circle through bits in address and add corresponding to values
    for b in range(8):
        if sec_bin[b] == '1':
            sum += functionvalues[b]

    return str(sum) #return year in string form

def convert_min(min_int):
    min_bin = read_rtc_byte(min_int) #convert int to binary

    functionvalues = np.array([0 , 40, 20, 10, 8, 4, 2 ,1]) #array that holds function values from data sheet

    sum = 0 #initialize value for year
    #Circle through bits in address and add corresponding to values
    for b in range(8):
        if min_bin[b] == '1':
            sum += functionvalues[b]

    return str(sum) #return year in string form   

def convert_hour(hour_int):
    hr_bin = read_rtc_byte(hour_int) #convert int to binary

    functionvalues = np.array([0 , 0, 20, 10, 8, 4, 2 ,1]) #array that holds function values from data sheet

    sum = 0 #initialize value for year
    #Circle through bits in address and add corresponding to values
    for b in range(8):
        if hr_bin[b] == '1':
            sum += functionvalues[b]

    return str(sum) #return year in string form
