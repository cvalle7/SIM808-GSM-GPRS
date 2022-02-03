# SIM808-GSM-GPRS
This library has been developed for a Raspberry Pi.
Python library that gets coordinates using a SIM808 module.


The library obtain coordinates through the SIM808 module, to start using this library just initialize it as follows:

## importing library
```python
import SIM808 as GPS
```
## Initializing listening port
```python
gps = GPS.GPS('/dev/ttyAMA0', 115200)
gps.setPowerOn()
```
## Getting coordinates
```python
coordinates =  gps.getLocation()
lat = coordinates[0]
lng = coordinates[1]
```
## Upcoming updates
GSM communication functionalities will be implemented in the future.
