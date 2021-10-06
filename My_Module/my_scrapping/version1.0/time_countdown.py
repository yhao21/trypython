import math,time


def left_time_estimation(round_time,sleep_time,remain_workload):
    left_time = remain_workload * (round_time + sleep_time)
    if  left_time < 3600:
        time_estimation = str(math.modf(left_time/60)[1])
        seconds = str(round(math.modf(math.modf(left_time/60)[0])[0]*60,3))
        print('This section will be finished in [ ' + time_estimation + ' ] minutes [ ' + seconds + ' ] seconds...')
    elif left_time >= 3600 and left_time < 86400:
        time_estimation = str(math.modf(left_time/60/60)[1])
        mins = str(math.modf(math.modf(left_time/60/60)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(left_time/60/60)[0]*60)[0]*60,2))
        print('This section will be finished in [ ' + time_estimation + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...')
    elif left_time >= 86400 and left_time < 172800:
        time_estimation = str(math.modf(left_time/60/60/24)[1])
        hours = str(math.modf(math.modf(left_time/60/60/24)[0]*24)[1])
        mins = str(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[0]*60,2))
        print('This section will be finished in [ ' + time_estimation + ' ] day ' + '[ ' + hours + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...')
    elif left_time >= 172800:
        time_estimation = str(math.modf(left_time/60/60/24)[1])
        hours = str(math.modf(math.modf(left_time/60/60/24)[0]*24)[1])
        mins = str(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[0]*60,2))
        print('This section will be finished in [ ' + time_estimation + ' ] days ' + '[ ' + hours + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...')


if __name__ == '__main__':
    left_time_estimation(15,3,10)
