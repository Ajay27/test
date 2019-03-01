def get_invalid_ip():
    ip = ["256.256.256.256", "235.256.234.253", "asad", "-23.-23.-12.-34", "224.0.0.0", "239.255.255.255"]
    return ip


def get_valid_ip():
    ip = ["0.0.0.0", '223.255.255.255', '240.0.0.0', '255.255.255.255']
    return ip


def get_invalid_int(min, max=999999):
    mn = int(min)
    mx = int(max)
    data = [mn - 1, mx + 1, "qw", "1+1", "$", "+"]
    return data


def get_valid_int(min, max):
    mn = int(min)
    mx = int(max)
    data = [mn, mx, int(((mn+mx)/2))]
    return data