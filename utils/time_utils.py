from datetime import datetime, timezone


def utc_now():
    return datetime.now(timezone.utc)


def iso_timestamp():
    return utc_now().isoformat()


def human_time(dt: datetime):
    return dt.strftime("%H:%M:%S")


def meeting_duration(start_time: datetime, end_time: datetime):
    delta = end_time - start_time
    minutes = delta.total_seconds() / 60
    return round(minutes, 2)
