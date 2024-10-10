#Variable
timeSinceMidnight = 0

def run(hours: int, minutes: int, seconds: int) -> float:
    # TODO
    global timeSinceMidnight 
    timeSinceMidnight = (hours * 3600000) + (minutes * 60000) + (seconds * 1000)
    return timeSinceMidnight


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(timeSinceMidnight)
