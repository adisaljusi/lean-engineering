from datetime import date

def eligible(captured_on: date | None, requested_on: date) -> bool:
    return captured_on is not None
