#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score_sum = 0
    weight_sum = 0
    for val in my_list:
        score_sum += val[0] * val[1]
        weight_sum += val[1]
    return (score_sum/weight_sum)
