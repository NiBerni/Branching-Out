import json


def filter_users_by_name(name):
	with open("users.json", "r") as file:
		users = json.load(file)

	filtered_users = [user for user in users if user["name"].lower() == name.lower()]

	for user in filtered_users:
		print(user)


def filter_user_by_age(age):
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

if __name__ == "__main__":
	filter_option = input("What would you like to filter by? (Currently, only 'name' is supported): ").strip().lower()

	if filter_option == "name":
		name_to_search = input("Enter a name to filter users: ").strip()
		filter_users_by_name(name_to_search)
	elif filter_option == "age":
		while True:
			try:
				age_to_search = int(input("Enter an age to filter users: "))
				if age_to_search < 0 or age_to_search > 151:
					raise ValueError
				filter_user_by_age(age_to_search)
				break
			except ValueError:
				print("Invalid input. \n"
				      "Please enter a valid age between 0 and 150.")

	else:
		print("Filtering by that option is not yet supported.")
