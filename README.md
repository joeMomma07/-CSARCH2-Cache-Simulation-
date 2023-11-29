
## Simulation Project CSARCH2 : 4-Way BSA-LRU Cache Simulation

### Overview

This Python-based simulation project, developed for CSARCH S11 Group 5, models a 4-way set-associative cache using the Least Recently Used (LRU) replacement policy. It's designed to help understand cache behaviors in computer architecture.

### Team Members
- Johanna Christine C. Aperin
- Jilliane Margaux C. Elloso

### Features

- **Simulation of 4-Way Set-Associative Cache:** Models a cache with configurable parameters.
- **Different Test Cases:** Supports sequential, random, and mid-repeat block access patterns.
- **LRU Replacement Policy:** Implements the LRU strategy for cache block replacement.
- **Logging and Statistics:** Outputs cache operations and performance metrics to a log file.
- **Interactive GUI:** Built with Tkinter for easy operation and visualization.

### Configuration Parameters

- `SETS`: Number of sets in the cache (default 8).
- `BLOCKS_PER_SET`: Number of blocks in each set (default 4).
- `WORDS_PER_BLOCK`: Number of words in each block (default 16).
- `CACHE_ACCESS_TIME`: Simulated time to access the cache (default 1).
- `MEM_ACCESS_TIME`: Simulated time to access the main memory (default 10).

### Core Data Structures

- `cache_memory`: 2D list representing the cache.
- `LRUstack`: List of lists tracking the LRU order for each set.
- `memory`: List representing the main memory blocks being accessed.

### Simulation Functions

- `select_choice()`: Configures the memory access pattern based on user selection.
- `run_simulation()`: Runs the cache simulation, logging activities and computing performance metrics.

### GUI Components

- Dropdown menus for test case selection and block configuration.
- Text display for memory and cache states.
- Buttons for initiating different stages of the simulation.
- Labels to display results and statistics.

### Usage

1. **Set Up Parameters:** Choose a test case and specify the number of blocks.
2. **Run Simulation:** Click the "Run Simulator" button to start the simulation.
3. **View Results:** Observe the cache behavior and performance metrics in the GUI and the log file.

### Log File

- `caching_log.txt`: Contains detailed logs of memory accesses, cache hits/misses, and final cache state.

### Test Case Analysis

**Test Case 1 Analysis:**

For the first test case, the 2n means that the sequence only has a maximum of 64. The sequence will repeat 4 times. The amount of memory size will depend on the user input as well as the number of misses and hits. At the end of the code, the hits will be 0 and the misses will be the same as the memory size because of the replacement of the lowest numbers with the highest number. Since the algorithm is LRU, the high numbers will be the youngest and will be the last one to be replaced.
Under a 4-way BSA + LRU algorithm, this pattern heavily stresses the cache as the sequence quickly exceeds the cache capacity, leading to frequent replacements. As the sequence repeats, the cache's eviction policy, LRU (Least Recently Used), ensures that the oldest elements are replaced first.


**Test Case 2 Analysis:**

For the second test case, we interpreted it with 4n meaning the maximum. Based on the specifications, the number of cache blocks is 32 which will make the maximum 128. The program will now generate random numbers from 0 to 128. After this, it will now proceed to the caching process where it will commute the hit and miss rate as well as the memory access time. Random sequences challenge the caching system by lacking a predictable pattern. This test evaluates how the cache algorithm handles unpredictable access patterns. In a 4-way BSA + LRU system, randomness may result in varied hit rates, affected by the chance of cache hits or misses based on the random block selection.

**Test Case 3 Analysis:**

For the third test case, stems from the fact that when n is 16 or less, the memory access sequence perfectly aligns with the 32 available cache blocks. What distinguishes this test case is its distinctive repetition in the middle section. This repetition contributes to a generally elevated hit rate compared to a straightforward 2n sequence. Consequently, the breaking point, where the sequence invariably results in misses, is pushed higher, given that the first half of the sequence logically contends for a limited number of spots within the cache block. The repetition within this sequence impacts the cache performance. This test explores how the caching algorithm adapts to repetitive patterns within a sequence, affecting the hit rates. The test case aims to observe the influence of repetitive sections on cache behavior and its handling of contention for cache space.






 
