
def iso_zone(v):

    if v < 2.8:
        return "Zone(Green) - Newly Commissioned Machinery"
    elif v < 4.5:
        return "Zone(Yellow) - Unrestricted Operation"
    elif v < 7.1:
        return "Zone(Orange) - Restricted Operation"
    else:
        return "Zone(Red) - Damage Occurs"
