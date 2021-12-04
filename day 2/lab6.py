# You jog the first mile at 7mph; then run the next two at15mph; beforejogging the last at 7mph again.
# Will this be quicker or slower than the bus?
distance = 4
speed1 = 25
time = (4/speed1)*60
total_time=time+(10*2)
speed2=7
time1=(1/speed2)*60
speed3=15
time2=(2/ speed3)*60
speed4=7
time3=(1/speed4)*60
totaltime1=time1+time2+time3
print("the total time to reach to university by buss is : " , total_time)
print("the total time to reach to the university by walkikng : " , totaltime1)
if totaltime1>total_time:
    print("walking is faster to reach university")
else:
    print("going by the bus is fasterthan walking")
