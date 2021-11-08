# qwiic_RV8803_RTC

This repository holds the code to use a SparkFun RV8803-RTC with a Rasperberry Pi through I2C

It currently is only able to read time and date using the read_time() and read_date() functions which returns strings corresponding to the 100th seconds, seconds, minutes, and hours & day, month, and year

Future releases would support syncing with GPS

The helper functions, convert_xxx() use arrays with values directly from the RTC's data sheet: https://www.microcrystal.com/fileadmin/Media/Products/RTC/App.Manual/RV-8803-C7_App-Manual.pdf
see pages 13-15 for this information.


