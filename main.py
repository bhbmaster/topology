import sys
from topo import NetworkTopologyGenerator

if __name__ == "__main__":

    # print("Generating topology for", sys.argv[1], "servers", len(sys.argv))
    #sys.exit(0)
    if len(sys.argv) > 1:
        total_servers = int(sys.argv[1])
    else:
        total_servers = int(input("Enter the number of servers: "))
    
    topology_generator = NetworkTopologyGenerator()
    topology = topology_generator.generate_topology(total_servers)
    topology_generator.display_topology(topology)
    topology_generator.generate_mermaid_topology(topology, f"topology_{total_servers}.mmd")