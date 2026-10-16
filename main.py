import random
import time
from typing import Callable, Optional

============================================================

ALGORITHM PLAYGROUND

A beginner-friendly algorithm visualization and benchmarking

application 

============================================================

————————————————————

CONFIGURATION

————————————————————

DATASET_SIZES = [10, 100, 1000, 10000]

ALGORITHMS = {
“1”: “Linear Search”,
“2”: “Binary Search”,
“3”: “Bubble Sort”,
“4”: “Selection Sort”,
“5”: “Merge Sort”,
}

TIME_COMPLEXITIES = {
“Linear Search”: “O(n)”,
“Binary Search”: “O(log n)”,
“Bubble Sort”: “O(n^2)”,
“Selection Sort”: “O(n^2)”,
“Merge Sort”: “O(n log n)”,
}

————————————————————

DISPLAY HELPERS

————————————————————

def print_header(title: str) -> None:
“”“Display a formatted section heading.”””

print("\n" + "=" * 60)
print(title.center(60))
print("=" * 60)

def display_array(
values: list[int],
active_indices: Optional[set[int]] = None,
found_index: Optional[int] = None,
max_display: int = 30,
) -> None:
“””
Display an array and mark the positions being inspected.

For large arrays, display a small window around the first
active index instead of printing thousands of numbers.
"""
active_indices = active_indices or set()
if not values:
    print("(empty array)")
    return
if len(values) <= max_display:
    start = 0
    end = len(values)
else:
    reference = min(active_indices) if active_indices else 0
    start = max(0, reference - 5)
    end = min(len(values), start + max_display)
    if end == len(values):
        start = max(0, end - max_display)
    print(
        f"Showing positions {start} to {end - 1} "
        f"of {len(values)} elements."
    )
visible_values = values[start:end]
print("\nIndex : ", end="")
for index in range(start, end):
    print(f"{index:>5}", end=" ")
print("\nValue : ", end="")
for value in visible_values:
    print(f"{value:>5}", end=" ")
print("\n       ", end="")
for index in range(start, end):
    if index == found_index:
        marker = "FOUND"
    elif index in active_indices:
        marker = "  ^  "
    else:
        marker = "     "
    print(f"{marker:>5}", end=" ")
print("\n")

def pause() -> None:
“”“Wait for the user before continuing.”””

input("\nPress Enter to continue...")

————————————————————

DATASET GENERATION

————————————————————

def generate_dataset(size: int) -> list[int]:
“””
Generate a list of random integers.

Values range from 0 to 99999. Duplicate values are possible.
"""
return [random.randint(0, 99999) for _ in range(size)]

————————————————————

LINEAR SEARCH

————————————————————

def linear_search(
values: list[int],
target: int,
visualize: bool = False,
) -> tuple[Optional[int], int]:
“””
Search for a target by inspecting elements from left to right.

Returns:
    A tuple containing the target index (or None) and
    the number of comparisons performed.
"""
comparisons = 0
print_header("LINEAR SEARCH") if visualize else None
if visualize:
    print(f"Searching for: {target}")
    display_array(values)
for index, value in enumerate(values):
    comparisons += 1
    if visualize:
        print(f"Checking index {index}: {value}")
        display_array(values, active_indices={index})
    if value == target:
        if visualize:
            print(f"FOUND {target} at index {index}!")
        return index, comparisons
if visualize:
    print(f"{target} was not found.")
return None, comparisons

————————————————————

BINARY SEARCH

————————————————————

def binary_search(
values: list[int],
target: int,
visualize: bool = False,
) -> tuple[Optional[int], int]:
“””
Search a sorted list by repeatedly halving the search range.

The input list must already be sorted.
Returns:
    A tuple containing the target index (or None) and
    the number of comparisons performed.
"""
comparisons = 0
left = 0
right = len(values) - 1
print_header("BINARY SEARCH") if visualize else None
if visualize:
    print(f"Searching for: {target}")
    print("Binary search requires sorted data.")
    display_array(values)
while left <= right:
    middle = (left + right) // 2
    comparisons += 1
    if visualize:
        print(
            f"Checking index {middle}: {values[middle]}\n"
            f"Current search range: {left} to {right}"
        )
        display_array(values, active_indices={middle})
    if values[middle] == target:
        if visualize:
            print(f"FOUND {target} at index {middle}!")
        return middle, comparisons
    if values[middle] < target:
        left = middle + 1
    else:
        right = middle - 1
if visualize:
    print(f"{target} was not found.")
return None, comparisons

————————————————————

BUBBLE SORT

————————————————————

def bubble_sort(
values: list[int],
visualize: bool = False,
) -> tuple[list[int], int]:
“””
Sort values by repeatedly comparing adjacent elements.

Returns:
    The sorted list and the number of comparisons performed.
"""
result = values.copy()
comparisons = 0
length = len(result)
print_header("BUBBLE SORT") if visualize else None
if visualize:
    print("Comparing neighboring elements and swapping as needed.")
    display_array(result)
for end in range(length - 1, 0, -1):
    swapped = False
    for index in range(end):
        comparisons += 1
        if visualize:
            print(
                f"Comparing {result[index]} and "
                f"{result[index + 1]}"
            )
        if result[index] > result[index + 1]:
            result[index], result[index + 1] = (
                result[index + 1],
                result[index],
            )
            swapped = True
            if visualize:
                print("Swapped!")
                display_array(
                    result,
                    active_indices={index, index + 1},
                )
    if not swapped:
        break
if visualize:
    print("Sorting complete!")
    display_array(result)
return result, comparisons

————————————————————

SELECTION SORT

————————————————————

def selection_sort(
values: list[int],
visualize: bool = False,
) -> tuple[list[int], int]:
“””
Repeatedly find the smallest remaining element and move it
into its correct position.

Returns:
    The sorted list and the number of comparisons performed.
"""
result = values.copy()
comparisons = 0
length = len(result)
print_header("SELECTION SORT") if visualize else None
if visualize:
    print("Finding the minimum element in each remaining section.")
    display_array(result)
for start in range(length):
    minimum_index = start
    for index in range(start + 1, length):
        comparisons += 1
        if visualize:
            print(
                f"Current minimum: {result[minimum_index]}; "
                f"checking: {result[index]}"
            )
        if result[index] < result[minimum_index]:
            minimum_index = index
    if minimum_index != start:
        result[start], result[minimum_index] = (
            result[minimum_index],
            result[start],
        )
    if visualize:
        print(f"Position {start} is now sorted.")
        display_array(result)
if visualize:
    print("Sorting complete!")
    display_array(result)
return result, comparisons

————————————————————

MERGE SORT

————————————————————

def merge_sort(
values: list[int],
visualize: bool = False,
) -> tuple[list[int], int]:
“””
Sort values using the divide-and-conquer strategy.

Repeatedly splits the list into smaller sections and merges
them back together in sorted order.
Returns:
    The sorted list and the number of element comparisons.
"""
comparisons = 0
print_header("MERGE SORT") if visualize else None
if visualize:
    print("Divide the list, sort each half, then merge.")
    display_array(values)
def sort_section(section: list[int]) -> list[int]:
    nonlocal comparisons
    if len(section) <= 1:
        return section.copy()
    middle = len(section) // 2
    left_half = sort_section(section[:middle])
    right_half = sort_section(section[middle:])
    merged = []
    left_index = 0
    right_index = 0
    while (
        left_index < len(left_half)
        and right_index < len(right_half)
    ):
        comparisons += 1
        if left_half[left_index] <= right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1
    merged.extend(left_half[left_index:])
    merged.extend(right_half[right_index:])
    if visualize and len(values) <= 30:
        print(f"Merging {left_half} and {right_half}")
        print(f"Result: {merged}")
    return merged
result = sort_section(values)
if visualize:
    print("Sorting complete!")
    display_array(result)
return result, comparisons

————————————————————

ALGORITHM SELECTION

————————————————————

def get_integer(prompt: str) -> int:
“”“Keep asking until the user enters a valid integer.”””

while True:
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a valid whole number.")

def choose_dataset(current_dataset: list[int]) -> list[int]:
“”“Let the user select a dataset size.”””

print_header("GENERATE DATASET")
print("1. 10 numbers")
print("2. 100 numbers")
print("3. 1,000 numbers")
print("4. 10,000 numbers")
choice = input("\nChoose a dataset size: ").strip()
sizes = {
    "1": 10,
    "2": 100,
    "3": 1000,
    "4": 10000,
}
if choice not in sizes:
    print("Invalid selection. Keeping the current dataset.")
    return current_dataset
dataset = generate_dataset(sizes[choice])
print(f"\nGenerated {len(dataset)} numbers successfully.")
print(f"First 10 values: {dataset[:10]}")
return dataset

def choose_search_algorithm() -> str:
“”“Ask the user to select a searching algorithm.”””

print("\n1. Linear Search")
print("2. Binary Search")
while True:
    choice = input("Choose a searching algorithm: ").strip()
    if choice in ("1", "2"):
        return choice
    print("Please choose 1 or 2.")

def choose_sort_algorithm() -> str:
“”“Ask the user to select a sorting algorithm.”””

print("\n1. Bubble Sort")
print("2. Selection Sort")
print("3. Merge Sort")
while True:
    choice = input("Choose a sorting algorithm: ").strip()
    if choice in ("1", "2", "3"):
        return choice
    print("Please choose 1, 2, or 3.")

————————————————————

SEARCHING DEMONSTRATION

————————————————————

def run_search_demo(dataset: list[int]) -> None:
“”“Run and visualize the selected searching algorithm.”””

choice = choose_search_algorithm()
target = get_integer("Enter the number to search for: ")
if choice == "1":
    algorithm = linear_search
    values = dataset.copy()
    name = "Linear Search"
else:
    algorithm = binary_search
    values = sorted(dataset)
    name = "Binary Search"
print(f"\nAlgorithm: {name}")
print(f"Time complexity: {TIME_COMPLEXITIES[name]}")
start_time = time.perf_counter()
result, comparisons = algorithm(
    values,
    target,
    visualize=True,
)
elapsed = time.perf_counter() - start_time
print_header("SEARCH RESULTS")
if result is not None:
    print(f"Target found at index: {result}")
else:
    print("Target not found.")
print(f"Comparisons: {comparisons}")
print(f"Elapsed time: {elapsed:.6f} seconds")

————————————————————

SORTING DEMONSTRATION

————————————————————

def run_sort_demo(dataset: list[int]) -> None:
“”“Run and visualize the selected sorting algorithm.”””

choice = choose_sort_algorithm()
algorithms: dict[
    str,
    Callable[[list[int], bool], tuple[list[int], int]]
] = {
    "1": bubble_sort,
    "2": selection_sort,
    "3": merge_sort,
}
algorithm = algorithms[choice]
name = {
    "1": "Bubble Sort",
    "2": "Selection Sort",
    "3": "Merge Sort",
}[choice]
print(f"\nAlgorithm: {name}")
print(f"Time complexity: {TIME_COMPLEXITIES[name]}")
if len(dataset) > 100:
    print(
        "\nThis visualization may take a while for large datasets, "
        "especially with quadratic-time algorithms."
    )
    confirmation = input(
        "Continue with step-by-step visualization? (y/n): "
    ).strip().lower()
    if confirmation != "y":
        return
start_time = time.perf_counter()
sorted_values, comparisons = algorithm(
    dataset,
    visualize=True,
)
elapsed = time.perf_counter() - start_time
print_header("SORT RESULTS")
print(f"Algorithm: {name}")
print(f"Time complexity: {TIME_COMPLEXITIES[name]}")
print(f"Comparisons: {comparisons}")
print(f"Elapsed time: {elapsed:.6f} seconds")
print(f"Sorted correctly: {sorted_values == sorted(dataset)}")

————————————————————

SEARCHING ALGORITHM BENCHMARK

————————————————————

def benchmark_searching(dataset: list[int]) -> None:
“””
Compare linear and binary search.

Sorting required for binary search is performed outside the
timed search operation and explained in the output.
"""
print_header("SEARCHING ALGORITHM COMPARISON")
sorted_dataset = sorted(dataset)
# Use a known existing value so both algorithms find the target.
target = dataset[len(dataset) // 2]
algorithms = [
    ("Linear Search", linear_search, dataset),
    ("Binary Search", binary_search, sorted_dataset),
]
print(f"Dataset size: {len(dataset)}")
print(f"Target: {target}")
print("\nBinary Search uses a pre-sorted dataset.")
print("Sorting time is not included in its search measurement.\n")
print(
    f"{'Algorithm':<20}"
    f"{'Complexity':<15}"
    f"{'Comparisons':<15}"
    f"{'Time (seconds)':<18}"
)
print("-" * 68)
for name, algorithm, values in algorithms:
    start_time = time.perf_counter()
    result, comparisons = algorithm(
        values,
        target,
        visualize=False,
    )
    elapsed = time.perf_counter() - start_time
    print(
        f"{name:<20}"
        f"{TIME_COMPLEXITIES[name]:<15}"
        f"{comparisons:<15}"
        f"{elapsed:<18.8f}"
    )
    assert result is not None, (
        f"{name} should find the selected target."
    )

————————————————————

SORTING ALGORITHM BENCHMARK

————————————————————

def benchmark_sorting(dataset: list[int]) -> None:
“””
Compare the sorting algorithms using identical input data.

Each algorithm receives a fresh copy of the same dataset.
"""
print_header("SORTING ALGORITHM COMPARISON")
algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    ("Merge Sort", merge_sort),
]
print(f"Dataset size: {len(dataset)}")
print("Each algorithm receives the same original data.\n")
print(
    f"{'Algorithm':<20}"
    f"{'Complexity':<15}"
    f"{'Comparisons':<15}"
    f"{'Time (seconds)':<18}"
)
print("-" * 68)
for name, algorithm in algorithms:
    values = dataset.copy()
    start_time = time.perf_counter()
    sorted_values, comparisons = algorithm(
        values,
        visualize=False,
    )
    elapsed = time.perf_counter() - start_time
    print(
        f"{name:<20}"
        f"{TIME_COMPLEXITIES[name]:<15}"
        f"{comparisons:<15}"
        f"{elapsed:<18.8f}"
    )
    assert sorted_values == sorted(dataset), (
        f"{name} did not sort the dataset correctly."
    )
print(
    "\nNote: Python's built-in sorting is used only to verify "
    "correctness, not to perform the benchmarked sort."
)

————————————————————

MAIN MENU

————————————————————

def display_menu(dataset: list[int]) -> None:
“”“Display the application menu.”””

print_header("ALGORITHM PLAYGROUND")
print("Learn. Visualize. Experiment.\n")
print(f"Current dataset size: {len(dataset)}")
print("\n1. Linear Search")
print("2. Binary Search")
print("3. Bubble Sort")
print("4. Selection Sort")
print("5. Merge Sort")
print("6. Compare Searching Algorithms")
print("7. Compare Sorting Algorithms")
print("8. Generate New Dataset")
print("9. Exit")

def main() -> None:
“”“Start the application.”””

dataset = generate_dataset(10)
while True:
    display_menu(dataset)
    choice = input("\nChoose an option: ").strip()
    if choice == "1":
        run_search_demo(dataset)
    elif choice == "2":
        run_search_demo(dataset)
    elif choice in ("3", "4", "5"):
        run_sort_demo(dataset)
    elif choice == "6":
        benchmark_searching(dataset)
    elif choice == "7":
        benchmark_sorting(dataset)
    elif choice == "8":
        dataset = choose_dataset(dataset)
    elif choice == "9":
        print("\nThanks for exploring algorithms!")
        print("Keep experimenting. Keep learning.")
        break
    else:
        print("\nInvalid choice. Please select 1-9.")
    pause()

if name == “main”:
main()
