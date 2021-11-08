import time
import RV_8803_RTC as RTClib

#i2c channel
i2c_ch = 1

#RV-8803 Address
RTC_Address = 0x32

#Initialize I2C (SMBus)
rtc_bus = RTClib.create_RTC(i2c_ch)

while True:
    print('Date is ', end="", flush=True)
    RTClib.print_date(rtc_bus,RTC_Address) 
    print(', Time is ', end="", flush=True)
    RTClib.print_time(rtc_bus,RTC_Address)
    time.sleep(1)




