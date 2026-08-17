"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""
"""
This program demonstrates:
- Parent and child classes
- Inheritance
- Class and instance namespaces
- Shallow and deep copying
- A student-created extension
- Error handling in a server-management example
"""

from copy import copy, deepcopy


# TODO 1:

class Server:
    # Class variable
    server_type = "Linux Server"

    def __init__(self, hostname, ip_address):
        # Instance variables
        self.hostname = hostname
        self.ip_address = ip_address
        self.status = "OFF"
        self.logs = ["Server created"]

    def get_info(self):
        """Return information about the server."""
        return (
            f"Hostname: {self.hostname} | "
            f"IP Address: {self.ip_address} | "
            f"Status: {self.status}"
        )


# TODO 2:

class UbuntuServer(Server):
    # New class variable
    operating_system = "Ubuntu Linux"

    def __init__(self, hostname, ip_address, ubuntu_version, services):
        # Initialize the parent class
        super().__init__(hostname, ip_address)

        # New instance variables
        self.ubuntu_version = ubuntu_version
        self.services = services

    # New method
    def start_server(self):
        self.status = "ON"
        self.logs.append("Server started")
        print(f"{self.hostname} has been started.")

    # New method for stopping the server
    def stop_server(self):
        self.status = "OFF"
        self.logs.append("Server stopped")
        print(f"{self.hostname} has been stopped.")

    # Student-created extension
    def add_service(self, service):
        """Add a new service to the server."""
        if service not in self.services:
            self.services.append(service)
            self.logs.append(f"Added service: {service}")
            print(f"{service} was added to {self.hostname}.")
        else:
            print(f"{service} is already installed.")

    # Override the parent method
    def get_info(self):
        base_info = super().get_info()

        return (
            f"{base_info} | "
            f"OS: {self.operating_system} | "
            f"Ubuntu Version: {self.ubuntu_version} | "
            f"Services: {self.services}"
        )


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two objects from the child class.
    server1 = UbuntuServer(
        "Ubuntu-Web-01",
        "192.168.1.10",
        "24.04",
        ["SSH", "Apache"]
    )

    server2 = UbuntuServer(
        "Ubuntu-Database-01",
        "192.168.1.20",
        "24.04",
        ["SSH", "MySQL"]
    )

    # Access the class variable through the class itself.
    print(
        "Class variable through class:",
        UbuntuServer.operating_system
    )

    # Access the same class variable through an object.
    print(
        "Class variable through server1:",
        server1.operating_system
    )

    # Add an attribute to only one object after creation.
    server1.environment = "Production"

    # Display each object's namespace.
    print("\nserver1 instance namespace:")
    print(server1.__dict__)

    print("\nserver2 instance namespace:")
    print(server2.__dict__)

    # Display the class namespace.
    print("\nUbuntuServer class namespace:")
    print(UbuntuServer.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Create an Ubuntu server object.
    original = UbuntuServer(
        "Ubuntu-Web-01",
        "192.168.1.10",
        "24.04",
        ["SSH", "Apache"]
    )

    # Add nested mutable data to the server.
    original.configuration = {
        "firewall": ["22", "80", "443"],
        "backup": ["Monday", "Wednesday", "Friday"]
    }

    # A shallow copy creates a new outer object,
    # but nested mutable objects are still shared.
    shallow_server = copy(original)

    # A deep copy creates a completely independent copy,
    # including nested mutable objects.
    deep_server = deepcopy(original)

    # Modify nested data in the original server.
    original.configuration["firewall"].append("8080")

    # Display all three objects.
    print("\nOriginal server:")
    print(original.__dict__)

    print("\nShallow copy:")
    print(shallow_server.__dict__)

    print("\nDeep copy:")
    print(deep_server.__dict__)


# TODO 5:
# Complete the main function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create an object from the parent class.
    print("\n=== Parent Class Object ===")

    server = Server(
        "Basic-Server",
        "192.168.1.5"
    )

    print(server.get_info())

    # Create an object from the child class.
    print("\n=== Child Class Object ===")

    ubuntu_server = UbuntuServer(
        "Ubuntu-Web-01",
        "192.168.1.10",
        "24.04",
        ["SSH", "Apache"]
    )

    # Demonstrate inheritance and method overriding.
    print(ubuntu_server.get_info())

    # Call methods from the child class.
    ubuntu_server.start_server()

    # Demonstrate the student-created extension.
    ubuntu_server.add_service("Docker")

    print("\nUpdated server information:")
    print(ubuntu_server.get_info())

    # Demonstrate namespaces.
    demonstrate_namespaces()

    # Demonstrate shallow and deep copying.
    demonstrate_copying()

    # Demonstrate error handling.
    print("\n=== Error Handling Demonstration ===")

    try:
        # Simulate a configuration problem.
        port = int("not-a-number")
        print(f"Server port: {port}")

    except ValueError:
        print(
            "Error: Invalid port configuration. "
            "The server configuration was not changed."
        )


if __name__ == "__main__":
    main()