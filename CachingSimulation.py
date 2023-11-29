import random
import os
import tkinter as tk
from tkinter import ttk

# Simulation Project CSARCH2

# CSARCH S11 Group 5 
# APERIN, Johanna Christine C.
# ELLOSO, Jilliane Margaux C.

SETS = 8
BLOCKS_PER_SET = 4
WORDS_PER_BLOCK = 16
EMPTY = ''
CACHE_ACCESS_TIME = 1
MEM_ACCESS_TIME = 10
LOG_FILENAME = "caching_log.txt"

cache_memory = [[EMPTY for j in range(BLOCKS_PER_SET)] for i in range(SETS)] 
LRUstack = [[] for i in range(SETS)]
memory = []
cachesize = BLOCKS_PER_SET * SETS

def select_choice():
    global cache_memory, LRUstack, memory, cachesize
    choice = test_case_var.get()
    cachesize = int(block_entry.get())
    if choice == 'Sequential blocks':
        memorysize = 2*cachesize
        sequence = list(range(0, memorysize))
        for i in range(4):
            memory.extend(sequence)
    elif choice == 'Random blocks':
        randrange = 64
        memorysize = 4*cachesize
        memory = [random.randint(1, randrange) for i in range(memorysize)]
    elif choice == 'Mid-repeat blocks':  
        memorysize = cachesize
        sequence = list(range(0, memorysize-1))
        sequence.extend(list(range(1, memorysize*2)))
        for i in range(4):
            memory.extend(sequence)

    result_label.config(text=f"Resulting memory size: {len(memory)}")
    memory_display.delete("1.0", tk.END) 
    memory_display.insert(tk.END, str(memory))


def run_simulation():
    global cache_memory, LRUstack, memory, cachesize
    f = open(LOG_FILENAME, "w")
    f.write(f"Starting Memory : {memory}\n")

    cache_hits = cache_miss = cache_set = block_num = fchoice = 0

    for index, val in enumerate(memory):
        # Check if the value exists in any cache set
        if any(val in cset for cset in cache_memory):
            cache_hits += 1  # Increment hit count
            cache_set = next(i for i, cset in enumerate(cache_memory) if val in cset)  # Find the cache set where the value exists
            f.write(f"-- [{val}] | CACHE SET: {cache_set} | BLK: {cache_memory[cache_set].index(val)}--\n")
            
            # Update LRU stack: move the accessed block to the top (as it's the most recently used)
            LRUstack[cache_set].remove(val)
            LRUstack[cache_set].append(val)
            
        else: 
            cache_miss += 1 # Increment miss count
            cache_set = index % SETS  # Determine the cache set based on the index
            f.write(f"-- NO VALUE [{val}] --\n")
            f.write(f"-- INDEX: [{index}] | VAL: [{val}] | TO CACHE SET: [{cache_set}] --\n")
            # Check if there's an empty block in the cache set
            if any(block == EMPTY for block in cache_memory[cache_set]):
                f.write("-- SET NOT FULL --\n")
                block_num = cache_memory[cache_set].index(EMPTY) # Find the index of the first empty block
            else:
                f.write("-- SET FULL --\n")
                
                # Evict the Least Recently Used block (LRU)
                LRUval = LRUstack[cache_set][0]
                LRUstack[cache_set].remove(LRUval)
                block_num = cache_memory[cache_set].index(LRUval)
             # Place the value in the cache block and update the LRU stack
            cache_memory[cache_set][block_num] = val 
            f.write(f"-- VAL:[{val}] | PLACED IN CACHE SET: [{cache_set}] BLK: [{block_num}] --\n")

            LRUstack[cache_set].append(val)

        f.write("\n") 


    mem_access = len(memory)

    miss_penaly = 1 + MEM_ACCESS_TIME
    average_access_time = ((cache_hits/mem_access) * CACHE_ACCESS_TIME + (cache_miss/mem_access) * miss_penaly)
    total_access_time = (average_access_time*cachesize)

    for cset in cache_memory:
        f.write(f"{cset}\n")
    f.write(f"Memory access count = {mem_access}\n")
    f.write(f"{cache_hits} hits, {cache_miss} misses\n")
    f.write(f"Hitrate = {cache_hits}/{mem_access}\nMissrate = {cache_miss}/{mem_access}\n")
    f.write(f"Average Memory Access Time = {average_access_time: .2f} ns\n")
    f.write(f"Total Memory access time = {total_access_time} ns")

    f.close()
    
    final_cache_label.config(text="Final Cache Memory", justify="center")
    for i, cset in enumerate(cache_memory):
        formatted_set = ', '.join(str(item) for item in cset)
        cache_state_labels[i].config(text=f"[{formatted_set}]", justify="center",fg="#526534")

    final_stats_label.config(text="Final Statistics", justify="center",fg="#526534")
    stats_labels["access_count"].config(text=f"Memory Access Count: {mem_access}", justify="center", fg="#526534")
    stats_labels["hits_misses"].config(text=f"Hits: {cache_hits} Misses: {cache_miss}", justify="center", fg="#526534")
    stats_labels["hit_miss_rate"].config(text=f"Hit Rate: {cache_hits}/{mem_access} Miss Rate: {cache_miss}/{mem_access}", justify="center", fg="#526534")
    stats_labels["avg_total_time"].config(text=f"Avg Access Time: {average_access_time:.2f} ns Total Time: {total_access_time} ns", justify="center", fg="#526534")


     
# Main window
root = tk.Tk()
root.title("4-Way Cache Memory Simulation (BSA-LRU)")
root.geometry("600x650")
root.configure(bg="#8d9e6f") 
custom_style = ttk.Style()
custom_style.configure("Custom.TCombobox", foreground="#526534")

# Dropdown menu for test cases
test_case_var = tk.StringVar()
test_case_label = tk.Label(root, text="Select test case",font=("bold", 16),fg='white',bg='#8d9e6f')
test_case_label.pack(pady=10)
test_case_dropdown = ttk.Combobox(root, textvariable=test_case_var,style="Custom.TCombobox")
test_case_dropdown['values'] = ('Sequential blocks', 'Random blocks', 'Mid-repeat blocks')
test_case_dropdown.pack(pady=5)

# Entry for blocks
block_number_var = tk.StringVar()
block_number_label = tk.Label(root, text="Blocks",font=("bold", 16),fg='white',bg='#8d9e6f')
block_number_label.pack(pady=5)

block_entry = tk.Entry(root,fg="#526534")
block_entry.pack(pady=5)

# Button to submit choice
submit_button = tk.Button(root, text="Submit", command=select_choice,highlightbackground='#8d9e6f',fg="#526534")
submit_button.pack(pady=5)


memory_display = tk.Text(root, height=10, width=50,fg="#526534")
memory_display.pack(pady=5)

# Label to display results
result_label = tk.Label(root, text="",bg='#8d9e6f', fg='white')
result_label.pack()

# Button to submit choice
run_button = tk.Button(root, text="Run Simulator", command=run_simulation,highlightbackground='#8d9e6f',fg="#526534")
run_button.pack()

container_master=tk.Frame(root, width=350, height=300, bd=2,bg="#8d9e6f")
container_master.pack()

# Final Cache Memory Label
final_cache_label = tk.Label(container_master,text="", anchor="w", font=("bold", 16),bg='#8d9e6f', fg='white')
final_cache_label.pack(fill="both", expand=True,padx=10)

# Create a frame to contain the labels
label_container = tk.Frame(container_master, width=150, height=200, bd=1)
label_container.pack_propagate(False)  
label_container.pack(side="left",padx=10) 

# Cache State Labels
cache_state_labels = [tk.Label(label_container, text="", anchor="w", justify="center") for _ in range(len(cache_memory))]
for lbl in cache_state_labels:
    lbl.pack(fill="both",side="top",anchor="w")  # Align labels to the left (west)

# Statistics Frame
statistics_container = tk.Frame(container_master, width=350, height=150,bd=1,
                           highlightbackground="#ebefe3", bg="#ebefe3")
statistics_container.pack_propagate(False)  
statistics_container.pack(side="right",padx=10) 


final_stats_label = tk.Label(statistics_container,text="",anchor="w", font=("bold", 16))
final_stats_label.pack(fill="both", expand=True,side="top",padx=10)

# Labels for Statistics
stats_labels = {
    "access_count": tk.Label(statistics_container, text="", anchor="w",justify="center",fg="#526534"),
    "hits_misses": tk.Label(statistics_container, text="", anchor="w",justify="center",fg="#526534"),
    "hit_miss_rate": tk.Label(statistics_container, text="", anchor="w",justify="center",fg="#526534"),
    "avg_total_time": tk.Label(statistics_container, text="", anchor="w",justify="center",fg="#526534"),
}
for lbl in stats_labels.values():
    lbl.pack(fill="both", expand=True,anchor="w",padx=10)

# Run the GUI application
root.mainloop()
       
