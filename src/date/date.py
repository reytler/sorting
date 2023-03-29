from datetime import timezone

def timestamp(dt):
    return dt.replace(tzinfo=timezone.utc).timestamp() * 1000
