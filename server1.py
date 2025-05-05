import Pyro4
@Pyro4.expose


class StringConcatenationServer:
	def concatenate_strings(self, str1, str2):
		return str1+ str2

def main():
	daemon= Pyro4.Daemon()
	ns= Pyro4.locateNS()


	server = StringConcatenationServer()
	uri = daemon.register(server)
	ns.register("string.concatenation", uri)
	print("Server URI:", uri)

	# Save the URI to a file for client access
	with open("server_uri.txt", "w") as f:
		f.write(str(uri))

	print("String Concatenation Server is running")
	daemon.requestLoop()

if __name__ == "__main__":
	main()