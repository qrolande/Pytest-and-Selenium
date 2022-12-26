def test_input_text(expected_result, actual_result):
	assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"


def main():
	a = input()
	b = input()

	test_input_text(a, b)


if __name__ == "__main__":
	main()
