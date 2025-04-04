import pathlib
import io
import sys

def run_tests():
    import __main__
    current_file = pathlib.Path(__main__.__file__).resolve()
    test_dir = current_file.parent / f"tests_{current_file.stem}"

    if not test_dir.exists():
        print(f"❗ No test dir for {current_file.name}")
        return

    test_files = sorted(f for f in test_dir.iterdir() if f.is_file() and not f.name.endswith('.clue'))

    for test_file in test_files:
        clue_file = test_file.with_suffix(test_file.suffix + '.clue')
        if not clue_file.exists():
            print(f"⚠️ No clue for {test_file.name}")
            continue

        input_code = test_file.read_text()
        expected_output = clue_file.read_text().strip()

        try:
            # Захватываем stdout
            old_stdout = sys.stdout
            sys.stdout = io.StringIO()

            # Выполняем код с доступом к определённой функции из __main__
            exec(input_code, __main__.__dict__)

            actual_output = sys.stdout.getvalue().strip()
            sys.stdout = old_stdout

            assert actual_output == expected_output, (
                f"❌ {test_file.name} failed\nExpected: {expected_output!r}\nGot: {actual_output!r}"
            )
            print(f"✅ {test_file.name} passed")

        except Exception as e:
            sys.stdout = old_stdout
            print(f"💥 {test_file.name} crashed: {e}")

run_tests()
