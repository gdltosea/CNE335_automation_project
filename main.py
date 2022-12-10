# This is the template code for the CNE335 Final Project
# Juan Flores
# CNE 335 Fall

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Juan Flores")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    #TODO - Create a Server object
    from Server import Server
    server_ip = '104.193.114.103'
    y = Server(server_ip)
    # TODO - Call Ping method and print the results
    y.ping()


    my_server_ip = '172.31.4.114'
    my_rsa_key_file = r"C:\Users\JuanFlores\.ssh\id_rsa"
    user_name = "ubuntu"
    my_upgrade_command = 'sudo apt update && sudo apt upgrade -y'
    my_server = Server(my_server_ip, my_rsa_key_file, user_name, my_upgrade_command)
    print(my_server.ping())
    print("Updating sever")
    ssh_result = my_server.upgrade()
    print(".join(ssh_result")




