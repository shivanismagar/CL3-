import Pyro4
def main():
	#read the server URI from the file
	with open("server_uri.txt", "r") as f:
		uri= f.read().strip()

# connect to remote server
	server = Pyro4.Proxy(uri)
	str1= input("Enter first string: ")
	str2= input("Enter second string: ")
	result= server.concatenate_strings(str1, str2)
	print("Concatenated string:", result)

if __name__ == "__main__":
	main()
