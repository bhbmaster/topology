# Network Topology Generator

This project provides a Python script to generate a network topology based on a specified number of servers. The topology is represented as a mermaid diagram and saved to a specified directory.

## Usage

To run the script, use the following command:

```bash
python main.py [total_servers] [output_directory]
```

### Arguments

- `total_servers` (Optional): The total number of servers in the network. If not provided, the user will be prompted to enter it.
- `output_directory` (Optional): The directory where the mermaid topology file will be saved. If not provided, the user will be prompted to enter it.

## Description

The script calculates the number of switches required at each level of the network (Top-of-Rack, Aggregate, Spine) and generates a mermaid diagram representing the topology. The diagram is saved to the specified output directory.

## Files

- `topo.py`: Contains the `NetworkTopologyGenerator` class, which handles the generation of the network topology and the mermaid diagram.
- `main.py`: The main script that handles user input and coordinates the generation and saving of the topology.

## Requirements

- Python 3.x

## Example

To generate a topology for 100 servers and save the output to a directory named `output`, run:

```bash
python main.py 100 output
```