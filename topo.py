import os

class NetworkTopologyGenerator:
    def __init__(self, servers_per_tor=30, tors_per_aggregate=4, aggregates_per_spine=2):
        # Initialize the topology parameters
        self.servers_per_tor = servers_per_tor
        self.tors_per_aggregate = tors_per_aggregate
        self.aggregates_per_spine = aggregates_per_spine

    def generate_topology(self, total_servers):
        # Calculate the number of Top-of-Rack (ToR) switches required using ceiling division
        num_tor_switches = (total_servers // self.servers_per_tor) + 1

        # Calculate the number of Aggregate switches required using ceiling division
        num_aggregate_switches = (num_tor_switches // self.tors_per_aggregate) + 1 if num_tor_switches > 1 else 0

        # Calculate the number of Spine switches required using ceiling division
        num_spine_switches = (num_aggregate_switches // self.aggregates_per_spine) + 1 if num_aggregate_switches > 1 else 0

        # Return a dictionary containing the topology details
        return {
            "total_servers": total_servers,
            "num_tor_switches": num_tor_switches,
            "num_aggregate_switches": num_aggregate_switches,
            "num_spine_switches": num_spine_switches
        }

    def display_topology(self, topology, directory, filename):
        # Print the topology details
        print(f"Total Servers: {topology['total_servers']}")
        print(f"Top-of-Rack Switches: {topology['num_tor_switches']}")
        print(f"Aggregate Switches: {topology['num_aggregate_switches']}")
        print(f"Spine Switches: {topology['num_spine_switches']}")

        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)

        # save the topology to a file
        with open(os.path.join(directory, filename), 'w') as f:
            f.write(str(topology))

    def generate_mermaid_topology(self, topology, directory, filename):
        # Start the mermaid graph definition
        mermaid = "graph TD\n"

        # Generate Top-of-Rack Switches and Servers
        for tor in range(topology['num_tor_switches']):
            # Define each ToR switch
            mermaid += f"  A{tor}([ToR Switch {tor + 1}])\n"
            for server in range(self.servers_per_tor):
                # Calculate server ID and check if it exceeds total servers
                server_id = tor * self.servers_per_tor + server + 1
                if server_id > topology['total_servers']:
                    break
                # Define connection from ToR switch to server
                mermaid += f"  A{tor} --> S{server_id}([Server {server_id}])\n"

        # Generate Aggregate Switches
        for agg in range(topology['num_aggregate_switches']):
            # Define each Aggregate switch
            mermaid += f"  B{agg}([Aggregate Switch {agg + 1}])\n"
            for tor in range(topology['num_tor_switches']):
                # Connect Aggregate switch to ToR switch based on configuration
                if tor // self.tors_per_aggregate == agg % max(1, (topology['num_aggregate_switches'] // self.tors_per_aggregate)):
                    mermaid += f"  B{agg} --> A{tor}\n"

        # Generate Spine Switches
        for spine in range(topology['num_spine_switches']):
            # Define each Spine switch
            mermaid += f"  C{spine}([Spine Switch {spine + 1}])\n"
            for agg in range(topology['num_aggregate_switches']):
                # Connect Spine switch to Aggregate switch based on configuration
                if agg % self.aggregates_per_spine == spine % self.aggregates_per_spine:
                    mermaid += f"  C{spine} --> B{agg}\n"

        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)

        # Write the mermaid graph to the specified file
        file_path = os.path.join(directory, filename)
        with open(file_path, 'w') as f:
            f.write(mermaid)

        # Notify the user of the file generation
        print(f"Generated mermaid topology to {file_path}")