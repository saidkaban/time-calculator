def add_time(start, duration, starting_day = ""):
    start_split = start.split()
    start_hour = start_split[0].split(":")[0].strip()
    start_minute = start_split[0].split(":")[1].strip()
    am_pm_list = ["AM", "PM"]
    days_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    am_pm = start_split[1].strip()
    duration_split = duration.split(sep = ":")
    duration_hour = duration_split[0].strip()
    duration_minute = duration_split[1].strip()
    new_hour = int(start_hour) + int(duration_hour)
    new_minute = int(start_minute) + int(duration_minute)
    remainder_minute = new_minute // 60
    remainder_hour = new_hour // 12
    current_am_pm_index = am_pm_list.index(am_pm)
    day_reminder = ""
    if remainder_minute > 0:
        new_hour = new_hour + remainder_minute
        new_minute = new_minute % 60
    if am_pm == "AM":
        hours_passed = int(new_hour)
    else:
        hours_passed = new_hour + 12
    if starting_day != "":
        starting_day = starting_day.lower()
        day_index = days_list.index(starting_day)
        days_passed = hours_passed // 24
        new_index = (day_index + days_passed) % 7
        starting_day = days_list[new_index]
        starting_day = ", " + starting_day.capitalize()
    if remainder_hour > 0:
        if hours_passed // 24 > 0 and hours_passed // 24 < 2:
            day_reminder = " (next day)"
        elif hours_passed // 24 >= 2:
            day_reminder = " ({} days later)".format(hours_passed // 24)
    am_pm = am_pm_list[(current_am_pm_index + (remainder_hour % 2)) % 2]
    if new_hour % 12 == 0:
        new_hour = new_hour % 24
        if am_pm == "AM":
            am_pm = "PM"
        else:
            am_pm = "AM"
    else:
        new_hour = new_hour % 12   
    new_hour, new_minute = str(new_hour), str(new_minute)
    if len(new_minute) == 1:
        new_minute = "0" + new_minute
    new_time = new_hour + ":" + new_minute + " " + am_pm + starting_day + day_reminder
    return new_time