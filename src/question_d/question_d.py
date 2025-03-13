#write functions here, don't add input('') statements here!

def get_day_of_week(day):
    if day < 1 or day > 7:
        return "Invalid number"
    elif day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    elif day == 7:
        return "Sunday"

def test_get_day_of_week():
    assert get_day_of_week(0) == "Invalid number"
    assert get_day_of_week(1) == "Monday"
    assert get_day_of_week(2) == "Tuesday"
    assert get_day_of_week(3) == "Wednesday"
    assert get_day_of_week(8) == "Invalid number"

test_get_day_of_week()