def validate(number):
	if number <= 100000:
		return False
	elif number >= 999999:
		return False

	return True