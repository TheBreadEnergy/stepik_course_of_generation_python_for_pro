def is_valid(pin: str) -> str:
    return str(pin.isdigit() and len(pin) in (4, 5, 6))


exec(open("../tester.py").read())
