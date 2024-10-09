class NetworkTopologyGenerator:
    def __init__(self, servers_per_tor=30, tors_per_aggregate=4, aggregates_per_spine=2):
        self.servers_per_tor = servers_per_tor
        self.tors_per_aggregate = tors_per_aggregate
        self.aggregates_per_spine = aggregates_per_spine

    def generate_topology(self, total_servers):
        # Calculate the number of Top-of-Rack (ToR) switches required
        num_tor_switches = -(-total_servers // self.servers_per_tor)  # Ceiling division

        # Calculate the number of Aggregate switches required
        num_aggregate_switches = -(-num_tor_switches // self.tors_per_aggregate)  # Ceiling division

        # Calculate the number of Spine switches required
        num_spine_switches = -(-num_aggregate_switches // self.aggregates_per_spine)  # Ceiling division

        return {
            "total_servers": total_servers,
            "num_tor_switches": num_tor_switches,
            "num_aggregate_switches": num_aggregate_switches,
            "num_spine_switches": num_spine_switches
        }

    def display_topology(self, topology):
        print(f"Total Servers: {topology['total_servers']}")
        print(f"Top-of-Rack Switches: {topology['num_tor_switches']}")
        print(f"Aggregate Switches: {topology['num_aggregate_switches']}")
        print(f"Spine Switches: {topology['num_spine_switches']}")

    def generate_mermaid_topology(self, topology, file):
        mermaid = "graph TD\n"

        # Generate Top-of-Rack Switches and Servers
        for tor in range(topology['num_tor_switches']):
            mermaid += f"  A{tor}([ToR Switch {tor + 1}])\n"
            for server in range(self.servers_per_tor):
                server_id = tor * self.servers_per_tor + server + 1
                if server_id > topology['total_servers']:
                    break
                mermaid += f"  A{tor} --> S{server_id}([Server {server_id}])\n"

        # Generate Aggregate Switches
        for agg in range(topology['num_aggregate_switches']):
            mermaid += f"  B{agg}([Aggregate Switch {agg + 1}])\n"
            for tor in range(topology['num_tor_switches']):
                if tor // self.tors_per_aggregate == agg % max(1, (topology['num_aggregate_switches'] // self.tors_per_aggregate)):
                    mermaid += f"  B{agg} --> A{tor}\n"

        # Generate Spine Switches
        for spine in range(topology['num_spine_switches']):
            mermaid += f"  C{spine}([Spine Switch {spine + 1}])\n"
            for agg in range(topology['num_aggregate_switches']):
                if agg % self.aggregates_per_spine == spine % self.aggregates_per_spine:
                    mermaid += f"  C{spine} --> B{agg}\n"

        with open(file, 'w') as f:
            f.write(mermaid)

        print(f"Generated mermaid topology to {file}")