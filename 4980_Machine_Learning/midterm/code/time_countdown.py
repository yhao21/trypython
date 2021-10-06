import math,time


def workload_time_left(round_time,sleep_time,remain_workload):
    """
    estimate finishing time according to the workload being left over.
    """

    left_time = remain_workload * (round_time + sleep_time)
    if  left_time < 3600:
        time_estimation = str(math.modf(left_time/60)[1])
        seconds = str(round(math.modf(math.modf(left_time/60)[0])[0]*60,3))
        print('This section will finish in [ ' + time_estimation + ' ] minutes [ ' + seconds + ' ] seconds...')

    elif left_time >= 3600 and left_time < 86400:
        time_estimation = str(math.modf(left_time/60/60)[1])
        mins = str(math.modf(math.modf(left_time/60/60)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(left_time/60/60)[0]*60)[0]*60,2))
        print('This section will finish in [ ' + time_estimation + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...')

    elif left_time >= 86400 and left_time < 172800:
        time_estimation = str(math.modf(left_time/60/60/24)[1])
        hours = str(math.modf(math.modf(left_time/60/60/24)[0]*24)[1])
        mins = str(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[0]*60,2))
        print('This section will finish in [ ' + time_estimation + ' ] day ' + '[ ' + hours + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...')

    elif left_time >= 172800:
        time_estimation = str(math.modf(left_time/60/60/24)[1])
        hours = str(math.modf(math.modf(left_time/60/60/24)[0]*24)[1])
        mins = str(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[0]*60,2))
        print('This section will finish in [ ' + time_estimation + ' ] days ' + '[ ' + hours + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...')


def clock_time_left(total_time):
    """
    transfer total time (in seconds) to the form of 00:00:00 (hour:min:second)

    total time = 3001 ---->  00:50:01
    total time = 5221 ---->  01:27:01
    """

    if  total_time < 3600:
        time_estimation = str(int(math.modf(total_time/60)[1]))
        seconds = str(int(round(math.modf(math.modf(total_time/60)[0])[0]*60,3)))
        if int(time_estimation) < 10:
            time_estimation = add_zero(time_estimation)
        if int(seconds) < 10:
            seconds = add_zero(seconds)
        print('%s:%s:%s' % ('00', time_estimation, seconds))

    elif total_time >= 3600:
        time_estimation = str(int(math.modf(total_time/60/60)[1]))
        mins = str(int(math.modf(math.modf(total_time/60/60)[0]*60)[1]))
        seconds = str(int(round(math.modf(math.modf(total_time/60/60)[0]*60)[0]*60,2)))
        if int(time_estimation) < 10:
            time_estimation = add_zero(time_estimation)
        if int(mins) < 10:
            mins = add_zero(mins)
        if int(seconds) < 10:
            seconds = add_zero(seconds)

        print('%s:%s:%s' % (time_estimation, mins, seconds))

def add_zero(n):
    standard_form = '0' + n
    return standard_form

if __name__ == '__main__':
    # workload_time_left(15,3,10)
    clock_time_left(1000000)
