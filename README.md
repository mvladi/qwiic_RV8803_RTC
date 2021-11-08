# qwiic_RV8803_RTC

This repository holds the code to use a SparkFun RV8803-RTC with a Rasperberry Pi through I2C

It currently is only able to read time and date using the read_time() and read_date() functions which returns strings corresponding to the 100th seconds, seconds, minutes, and hours & day, month, and year

Future releases would support syncing with GPS
