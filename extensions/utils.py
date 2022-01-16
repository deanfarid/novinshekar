from . import jalali

def jalali_converter(time):
    time_to_str = "{},{},{}".format(time.year , time.month , time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)
    output = ("{} / {} / {}").format(
        time_to_list[2],
        time_to_list[1],
        time_to_list[0],

    )
    return output
