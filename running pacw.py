# def running_pace(distance, time):
#     # if distance == 1:
#     #     return time
#     a = ''
#     b = 0
#     c = []
#     for i in time.split(':'):
#         c.append(int(i))
#
#
#     b = (c[0]*60 +c[1]) // distance
#     minute = int(b//60)
#     seconds = int(b%60)
#     a = "{}:{}".format(minute,seconds)
#     if seconds < 10:
#         return a + "0"
#     else:
#         return a
#
#
#
# print(running_pace(4.99,'22:32'))
# print(250%60)
sec_to_hr = 1/3600 # 3600 seconds in 1 hour
min_to_hr = 1/60 # 60 minutes in 1 hour

time_hrs = (5*min_to_hr)+ (42*sec_to_hr) # Total time in hours
dist_km = 1 # Total time in miles

av_speed = dist_km/time_hrs # Average Speed in miles/hour

answer1 = "Average speed = {} miles per hour".format(round(av_speed,2))

print(answer1)

"""
If you understood the calculation above, see if you can
understand the code below. 
Hint: "Pace" is how much time in 1 mile. Time = Distance / Speed 
Also, Do you know what the function "round()" is doing?
"""
pace_dist = 1 # In 1 mile

pace_time_hr = round(pace_dist/av_speed, 2)
pace_time_min = round(pace_time_hr * 60, 2)
pace_time_sec = round(pace_time_min % 1,2) * 60

answer2 = "Average pace per mile = {} minutes and {} seconds".format(int(pace_time_min), int(pace_time_sec))
print(answer2)



def running_pace(distance,time):
    c = []
    for i in time.split(":"):
        c.append(int(i))
    b = (c[0]*60 +c[1]) // distance
    minute = int(b//60)
    seconds = int(b%60)
    av_speed =  distance//sum(c)
    return av_speed

print(running_pace(1,"4:00"))