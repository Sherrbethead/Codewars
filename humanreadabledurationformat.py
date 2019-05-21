'''Description

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds,
in a human-friendly way. The function must accept a non-negative integer. If it is zero, it just returns "now".
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
Note that spaces are important.
Detailed rules:
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of
the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.
The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ",
just like it would be written in English. A more significant units of time will occur before than a least significant
one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is. Different components have different
unit of times. So there is not repeated units like in 5 seconds and 1 second. A component will not appear at all if its
value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute. A unit of time
must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second
instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit
of time.'''


def format_duration(seconds):
    humanread = list()
    years = seconds//31536000
    yearsmod = seconds%31536000
    if years == 1:
        humanread.append('1 year')
    if years > 1:
        humanread.append(str(years)+' years')
    days = yearsmod//86400
    daysmod = yearsmod%86400
    if days == 1:
        humanread.append('1 day')
    if days > 1:
        humanread.append(str(days)+' days')
    hours = daysmod//3600
    hoursmod = daysmod%3600
    if hours == 1:
        humanread.append('1 hour')
    if hours > 1:
        humanread.append(str(hours)+' hours')
    minutes = hoursmod//60
    minutesmod = hoursmod%60
    if minutes == 1:
        humanread.append('1 minute')
    if minutes > 1:
        humanread.append(str(minutes)+' minutes')
    secs = minutesmod
    if secs == 1:
        humanread.append('1 second')
    if secs > 1:
        humanread.append(str(secs)+' seconds')
    if not humanread:
        return 'now'
    end = humanread.pop()
    return end if len(humanread) == 0 else ', '.join(humanread) + ' and ' + end

print(format_duration(3662))  # 1 hour, 1 minute and 2 seconds
print(format_duration(31708800))  # 1 year and 2 days