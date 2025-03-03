##Computer Networking Project: Tail-Latency Reduction Using Mininet

## Overview

This project explores the field of computer networking, specifically focusing on understanding and reducing tail-latency. We use **Mininet**, a network simulator, to simulate various network topologies and test different algorithms aimed at improving the performance and reducing the tail-latency in a network. Tail-latency refers to the higher-than-average latency that occurs at the tail-end of the distribution, which can significantly impact performance, especially in real-time and large-scale systems.

## Objective

The primary goal of this project is to:
- Investigate the impact of different networking algorithms on tail-latency.
- Experiment with network configurations and determine effective strategies for minimizing latency in diverse scenarios.

## Tools & Technologies

- **Mininet**: A network emulator for testing virtual networks. Mininet allows the simulation of complex network topologies and is an essential tool for this project.
- **Python**: The project uses Python to develop scripts for simulating network configurations, running tests, and collecting results.
- **Algorithms**: Various networking algorithms and traffic management techniques were tested to reduce tail-latency.

## Approach

1. **Network Simulation**: The project sets up several virtual networks using Mininet. These simulations are designed to mimic real-world networking scenarios, including different link speeds, traffic patterns, and topologies.
   
2. **Algorithm Testing**: Multiple algorithms were tested for their ability to reduce tail-latency, including:
   - Congestion control mechanisms
   - Load balancing techniques
   - Queue management strategies
   - Traffic scheduling algorithms

3. **Metrics Collection**: During the tests, various metrics are measured, focusing specifically on tail-latency and overall network throughput.

4. **Analysis & Results**: After running multiple test cases, the results are analyzed to determine which algorithms and configurations provide the best reduction in tail-latency.

## Results

The results section would include the key findings from the experiments, highlighting the effectiveness of different algorithms in reducing tail-latency under varying network conditions.

## Setup & Usage

### Requirements

- **Mininet**: Installation guide can be found [here](https://mininet.org/download/).
- **Python 3**: Required for running the simulation scripts.
- Additional Python libraries may be required depending on the test scripts used. These can be installed via `pip`:
  ```bash
  pip install -r requirements.txt
  ```

## Conclusion

This project demonstrates the use of Mininet in exploring and understanding the dynamics of tail-latency in computer networks. By experimenting with various algorithms and network configurations, the project aims to identify effective methods for minimizing tail-latency, which is crucial for improving the performance of modern applications, especially those requiring real-time communication.

## Future Work

Future work could involve testing additional algorithms, exploring larger and more complex network topologies, and integrating real-world hardware to validate the simulation results.

