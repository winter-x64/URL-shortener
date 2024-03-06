import uuid


def generate_event_id() -> str:
    event_id: str = str(uuid.uuid4().hex)
    event_id = f"{event_id}"
    return event_id


print(generate_event_id())
