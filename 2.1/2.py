def same_parity(input: list[int]) -> list[int]:
    return list(filter(lambda x: x % 2 == input[0] % 2, input))


exec(open("../tester.py").read())
