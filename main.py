"""
Usage: python main.py [total_servers] [output_directory]

Arguments:
  total_servers      (Optional) The total number of servers in the network. 
                     If not provided, the user will be prompted to enter it.
  output_directory   (Optional) The directory where the mermaid topology file 
                     will be saved. If not provided, the user will be prompted 
                     to enter it.

Description:
  This script generates a network topology based on the specified number of 
  servers and outputs a mermaid diagram to the specified directory.
"""

import sys
from topo import NetworkTopologyGenerator

if __name__ == "__main__":
    # Check if the total number of servers is provided as a command line argument
    if len(sys.argv) > 1:
        total_servers = int(sys.argv[1])
    else:
        # Prompt the user to enter the number of servers
        total_servers = int(input("Enter the number of servers: "))
    
    # Check if the output directory is provided as a command line argument
    if len(sys.argv) > 2:
        output_directory = sys.argv[2]
    else:
        # Prompt the user to enter the output directory
        output_directory = input("Enter the output directory: ")

    # Create an instance of the NetworkTopologyGenerator
    topology_generator = NetworkTopologyGenerator()
    
    # Generate the network topology based on the total number of servers
    topology = topology_generator.generate_topology(total_servers)
    
    # Display the generated topology details
    topology_generator.display_topology(topology, output_directory, f"topology_{total_servers}.json")
    
    # Generate and save the mermaid topology diagram to the specified directory
    topology_generator.generate_mermaid_topology(topology, output_directory, f"topology_{total_servers}.mmd")