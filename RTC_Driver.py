import time
import RV_8803_RTC as RTClib

#i2c channel
i2c_ch = 1

#RV-8803 Address
RTC_Address = 0x32

#Initialize I2C (SMBus)
rtc_bus = RTClib.create_RTC(i2c_ch)

#Use the library to print date and time continuously
while True:
    RTClib.print_date(rtc_bus,RTC_Address) 
    RTClib.print_time(rtc_bus,RTC_Address)
    time.sleep(1)




