def hide_card(card: str) -> str:
    return f"{'*'*12}{card.replace(' ', '')[-4:]}"


exec(open("../tester.py").read())
