# This is the template code for the CNE335 Final Project
# Justin Ellis
# CNE 335 Fall

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Juan Flores")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    from Server import Server
    server_ip = '172.31.4.114'
    y = Server(server_ip)
    # TODO - Call Ping method and print the results
    y.ping()


