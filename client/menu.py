



# Choose your G8 country for relations
def main_menu():
	print("[1] United States")
	print("[2] France")
	print("[3] Germany")
	print("[4] Italy")
	print("[5] United Kingdom")
	print("[6] Japan")
	print("[7] Russia")
	print("[8] Canada")

main_menu()
option = int(input("Choose your G8 country: "))

# Main menu options 
while option != 0:
	if option == 1:
		# do things ...........
		print("United states") 
	print()
	menu()
	option = int(input("Choose your G8 country: "))


print("Test run") 