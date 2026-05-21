import json


def filter_users_by_name(name):
	with open("users.json", "r") as file:
		users = json.load(file)

	filtered_users = [user for user in users if user["name"].lower() == name.lower()]

	for user in filtered_users:
		print(user)


def filter_users_by_age(age: int) -> None:
	"""
	Filters and prints users based on the specified age. This function reads user data
	from a JSON file named 'users.json', processes it, and prints out users whose
	age matches the provided value.

	:param age: The age to filter the users by.
	:type age: int

	:return: None
	"""
	with open("users.json", "r") as file:
		users = json.load(file)
	filtered_users = [user for user in users if user["age"] == age]

	for user in filtered_users:
		print(user)


def filter_users_by_email(email: str) -> None:
	"""
	Filters user data by email from a JSON file and prints the matching users.

	This function reads a JSON file containing user data, filters the users
	whose email matches the provided email address, and prints the details of
	the filtered users.

	:param email: The email address to filter users by.
	:type email: str
	:return: None
	"""
	with open("users.json", "r") as file:
		users = json.load(file)

	filtered_users = [user for user in users if user["email"].lower().strip() == email.lower().strip()]

	for user in filtered_users:
		print(user)

if __name__ == "__main__":
	filter_option = input("What would you like to filter by? ('name', 'email' or 'age'): ").strip().lower()

	if filter_option == "name":
		name_to_search = input("Enter a name to filter users: ").strip()
		filter_users_by_name(name_to_search)
	elif filter_option == "age":
		while True:
			try:
				age_to_search = int(input("Enter an age to filter users: "))
				if age_to_search < 0 or age_to_search > 151:
					raise ValueError
				filter_users_by_age(age_to_search)
				break
			except ValueError:
				print("Invalid input. \n"
				      "Please enter a valid age between 0 and 150.")
	elif filter_option == "email":
		email_to_search = input("Enter an email to filter users: ").strip()
		filter_users_by_email(email_to_search)
	else:
		print("Filtering by that option is not yet supported.")
