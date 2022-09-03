import json
import time

import numpy

def simulate_battery(events, specs):
  print("Simulating with plant size %d"%specs["plant_size"])

  #Process each 3 minute slice, adding or subtracting from storage, so that plant maximum output is reached
  #Bail out if storage goes negative
  for generated_power in events:
    specs["storage"]=specs["storage"]+(generated_power*0.4 - specs["plant_size"])
    if specs["storage"]<0:
      return specs["storage"]
  else:
    #Return the surplus at end of the year
    return specs["storage"]

events=list()

with open("data.json") as input_data:

  for line in input_data:
    event=json.loads(line)
    events.append(event["value"])

print(numpy.average(events))
print(numpy.median(events))

specs=dict()

#Initial plant size, increase if result is found in first round
specs["plant_size"]=1000
#Events are in 3 minute pulses, so multiply initial storage by 20
#Assume that we have a sizeable storage or use other sources until storage has built up
specs["storage"]=24000*20

end_of_the_year=-1

while end_of_the_year<0:
  end_of_the_year=simulate_battery(events, specs)
  #print(end_of_the_year)
  if end_of_the_year<0:
    specs["plant_size"] = specs["plant_size"]-5
    #Reset storage
    specs["storage"]=24000*20

print("Maximum continuous output found")
print("Hydrogen plant size: %dMW"%specs["plant_size"])
print("Excess hydrogen at end of the year: %dGWh"%(specs["storage"]/20000))