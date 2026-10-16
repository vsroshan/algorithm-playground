"""A beginner-friendly algorithm visualization and benchmarking app."""

import random
import time
from typing import Callable, Optional


TIME_COMPLEXITIES = {
    "Linear Search": "O(n)",
    "Binary Search": "O(log n)",
    "Bubble Sort": "O(n^2)",
    "Selection Sort": "O(n^2)",
    "Merge Sort": "O(n log n)",
}


def print_header(title: str) -> None:
    """Display a formatted section heading."""
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def display_array(
    values: list[int],
    active_indices: Optional[set[int]] = None,
    found_index: Optional[int] = None,
    max_display: int = 30,
) -> None:
    """Display an array, highlighting any active or found positions."""
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
    """Wait for the user before continuing."""
    input("\nPress Enter to continue...")


def generate_dataset(size: int) -> list[int]:
    """Generate a list of random integers between 0 and 99999."""
    return [random.randint(0, 99999) for _ in range(size)]


def linear_search(
    values: list[int],
    target: int,
    visualize: bool = False,
) -> tuple[Optional[int], int]:
    """Search left to right, returning the target index and comparisons."""
    comparisons = 0
    if visualize:
        print_header("LINEAR SEARCH")
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


def binary_search(
    values: list[int],
    target: int,
    visualize: bool = False,
) -> tuple[Optional[int], int]:
    """Search a sorted list by repeatedly halving the search range."""
    comparisons = 0
    left = 0
    right = len(values) - 1
    if visualize:
        print_header("BINARY SEARCH")
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


def bubble_sort(
    values: list[int],
    visualize: bool = False,
) -> tuple[list[int], int]:
    """Sort values with bubble sort and return the comparison count."""
    result = values.copy()
    comparisons = 0
    length = len(result)
    if visualize:
        print_header("BUBBLE SORT")
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


def selection_sort(
    values: list[int],
    visualize: bool = False,
) -> tuple[list[int], int]:
    """Sort values with selection sort and return the comparison count."""
    result = values.copy()
    comparisons = 0
    length = len(result)
    if visualize:
        print_header("SELECTION SORT")
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


def merge_sort(
    values: list[int],
    visualize: bool = False,
) -> tuple[list[int], int]:
    """Sort values with merge sort and return the comparison count."""
    comparisons = 0
    if visualize:
        print_header("MERGE SORT")
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


def get_integer(prompt: str) -> int:
    """Keep asking until the user enters a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")


def choose_dataset(current_dataset: list[int]) -> list[int]:
    """Let the user select a dataset size."""
    print_header("GENERATE DATASET")
    print("1. 10 numbers")
    print("2. 100 numbers")
    print("3. 1,000 numbers")
    print("4. 10,000 numbers")
    choice = input("\nChoose a dataset size: ").strip()
    sizes = {"1": 10, "2": 100, "3": 1000, "4": 10000}
    if choice not in sizes:
        print("Invalid selection. Keeping the current dataset.")
        return current_dataset

    dataset = generate_dataset(sizes[choice])
    print(f"\nGenerated {len(dataset)} numbers successfully.")
    print(f"First 10 values: {dataset[:10]}")
    return dataset


def run_search_demo(dataset: list[int], choice: str) -> None:
    """Run and visualize the selected searching algorithm."""
    if choice == "1":
        algorithm = linear_search
        values = dataset.copy()
        name = "Linear Search"
    else:
        algorithm = binary_search
        values = sorted(dataset)
        name = "Binary Search"

    target = get_integer("Enter the number to search for: ")
    print(f"\nAlgorithm: {name}")
    print(f"Time complexity: {TIME_COMPLEXITIES[name]}")
    start_time = time.perf_counter()
    result, comparisons = algorithm(values, target, visualize=True)
    elapsed = time.perf_counter() - start_time
    print_header("SEARCH RESULTS")
    if result is not None:
        print(f"Target found at index: {result}")
    else:
        print("Target not found.")
    print(f"Comparisons: {comparisons}")
    print(f"Elapsed time: {elapsed:.6f} seconds")


def run_sort_demo(dataset: list[int], choice: str) -> None:
    """Run and visualize the selected sorting algorithm."""
    algorithms: dict[
        str,
        tuple[str, Callable[[list[int], bool], tuple[list[int], int]]],
    ] = {
        "3": ("Bubble Sort", bubble_sort),
        "4": ("Selection Sort", selection_sort),
        "5": ("Merge Sort", merge_sort),
    }
    name, algorithm = algorithms[choice]
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
    sorted_values, comparisons = algorithm(dataset, visualize=True)
    elapsed = time.perf_counter() - start_time
    print_header("SORT RESULTS")
    print(f"Algorithm: {name}")
    print(f"Time complexity: {TIME_COMPLEXITIES[name]}")
    print(f"Comparisons: {comparisons}")
    print(f"Elapsed time: {elapsed:.6f} seconds")
    print(f"Sorted correctly: {sorted_values == sorted(dataset)}")


def benchmark_searching(dataset: list[int]) -> None:
    """Compare linear and binary search on the same target."""
    print_header("SEARCHING ALGORITHM COMPARISON")
    sorted_dataset = sorted(dataset)
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
        result, comparisons = algorithm(values, target, visualize=False)
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


def benchmark_sorting(dataset: list[int]) -> None:
    """Compare the sorting algorithms using identical input data."""
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
        sorted_values, comparisons = algorithm(values, visualize=False)
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


def display_menu(dataset: list[int]) -> None:
    """Display the application menu."""
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
    """Start the application."""
    dataset = generate_dataset(10)
    while True:
        display_menu(dataset)
        choice = input("\nChoose an option: ").strip()
        if choice in ("1", "2"):
            run_search_demo(dataset, choice)
        elif choice in ("3", "4", "5"):
            run_sort_demo(dataset, choice)
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


if __name__ == "__main__":
    main()
