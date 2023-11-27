def convert_to_24_hour(hour, minute, period):
    # dict
    adjustments = {"am": 0, "pm": 12}

    if hour == 12:
        hour = 0

    hour += adjustments.get(period.lower(), 0)

    return f"{hour:02d}{minute:02d}"


hour_1, minute_1, period_1 = 12, 30, "am"
result_1 = convert_to_24_hour(hour_1, minute_1, period_1)
print(f"Midnight has arrived! {hour_1}:{minute_1} {period_1.upper()} transforms into {result_1} in 24-hour time.")