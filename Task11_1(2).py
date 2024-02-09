import calendar

for month in range(1, 13):
    cal = calendar.monthcalendar(2024, month)
    first_week = cal[0]
    second_week = cal[1]
    third_week = cal[2]
    fourth_week = cal[3]

    if first_week[calendar.THURSDAY]:
        free_day = third_week[calendar.THURSDAY]
    else:
        free_day = fourth_week[calendar.THURSDAY]

    print("%s : %s" % (calendar.month_abbr[month], free_day))