cycle_distance = 10
cycle_speed = 5
bullock_distance = 5
bullock_speed = 20 / 3.6
helicopter_distance = 20
helicopter_speed = 140

time_cycle = cycle_distance / cycle_speed
time_bullock = bullock_distance / bullock_speed
time_helicopter = helicopter_distance * 1000 / helicopter_speed

total_time_hours = time_cycle + time_bullock + (time_helicopter / 3600)
print("Total time taken in hours:", total_time_hours)