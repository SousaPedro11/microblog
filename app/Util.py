from datetime import datetime


def timestamp_to_string(timestamp, formato='%H:%M:%S %d/%m/%Y'):
    return datetime.strftime(timestamp, formato)
