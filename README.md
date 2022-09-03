# Wind+Hydrogen storage simulation

A crude símulation of how big stable output wind power backed by hydrogen power plant could provide in Finland
based on Fingrid open data.

Hydrogen power storage round trip efficiency of 40% based on 
https://pv-magazine-usa.com/2020/07/03/nrel-study-backs-hydrogen-for-long-duration-storage/

NOTE: Do get API key from Fingrid

Data fetching brutally ripped from. 
https://github.com/aHertsberg/Fingrid_requests_python

This is not a clean fork, do not merge back :)

-----
## Example command and output
```
#Fetch raw data, which is stored in data.json
$ python3 fetch.py

#Run simulation
python3 simulate_battery.py
```

Output with 360 days data fetched at 3.9.2022

Maximum continuous output found

Hydrogen plant size: 585MW

Excess hydrogen at end of the year: 1699GWh