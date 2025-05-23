from datetime import datetime
import uuid


def get_curr_time() -> str:
    """
    get current time
    :return: string of the current time formatted as 'YYYY-MM-DD HH:MM:SS'
    """
    now = datetime.now()
    return str(now.strftime("%Y-%m-%d %H:%M:%S"))


def get_uuid() -> str:
    """
    generate uuid for task
    :return: uuid, as string
    """
    return str(uuid.uuid4())
