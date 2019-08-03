def main():

	data="this is where I wan to break"

	for char in data:
		if char=='b': break
		print(char,sep=" ")

main()