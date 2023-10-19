from datetime import datetime
    return "Hello ! Il est {}.".format(datetime.now().strftime("%H:%M:%S"))
