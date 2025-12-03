import math
float_nb = 3.14
int_nb = math.ceil(float_nb)  # `int_nb` est égal à 4

filled_time = 80/(12-1)
filled_time_int = math.ceil(filled_time)
water_vol=0

for n in range(filled_time_int):
    water_vol = water_vol +(12-1)
    print(water_vol)
    