def test_substring(full_string, substring):
	assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"


def main():
	a = input()
	b = input()

	test_substring(a, b)


if __name__ == "__main__":
	main()
