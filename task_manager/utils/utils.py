from datetime import datetime
import uuid


def get_curr_time() -> str:
    now = datetime.now()
    return str(now.strftime("%Y-%m-%d %H:%M:%S"))


def get_uuid() -> str:
    return str(uuid.uuid4())