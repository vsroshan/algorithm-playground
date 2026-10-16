Algorithm Playground

An interactive Python command-line application for exploring searching and sorting algorithms, visualizing their behavior, and measuring their performance.

Built as a hands-on learning project inspired by CS50 Week 3: Algorithms.

Overview

Understanding an algorithm is more than memorizing its time complexity.

Algorithm Playground lets users experiment with different algorithms, observe their behavior, measure their performance, and compare their trade-offs.

The project demonstrates how algorithm selection can affect performance as input sizes increase.

Features

* Implementations of five classic algorithms.
* Step-by-step searching demonstrations.
* Visual representations of sorting operations.
* Configurable datasets containing 10, 100, 1,000, or 10,000 numbers.
* Execution-time measurements using Python’s high-resolution performance timer.
* Element-comparison counts.
* Searching and sorting benchmarks.
* Automated unit tests.
* No third-party Python dependencies.

Algorithms Implemented

Algorithm	Category	Time Complexity	Notes
Linear Search	Searching	O(n)	Checks elements sequentially.
Binary Search	Searching	O(log n)	Requires sorted input.
Bubble Sort	Sorting	O(n²) worst case	Compares and swaps adjacent elements.
Selection Sort	Sorting	O(n²)	Repeatedly selects the minimum element.
Merge Sort	Sorting	O(n log n)	Uses divide and conquer.

Complexities shown above describe time growth. They do not represent measured execution times.

Requirements

* Python 3.9 or later.
* A terminal.
* Git, if you want to clone the repository or upload your work to GitHub.

No third-party packages are required.

Installation

1. Clone the repository

git clone https://github.com/vsroshan/algorithm-playground.git

2. Open the project directory

cd algorithm-playground

3. Create a virtual environment

python3 -m venv .venv

4. Activate the virtual environment

On macOS or Linux:

source .venv/bin/activate

On Windows:

.venv\Scripts\Activate.ps1

5. Install dependencies

There are no third-party dependencies.

You can optionally run:

python -m pip install -r requirements.txt

6. Start the application

On macOS or Linux:

python3 main.py

If your virtual environment is active, the following also works:

python main.py

How to Use

When the application starts, you will see a menu similar to this:

============================================================
                  ALGORITHM PLAYGROUND
============================================================
Learn. Visualize. Experiment.
Current dataset size: 10
1. Linear Search
2. Binary Search
3. Bubble Sort
4. Selection Sort
5. Merge Sort
6. Compare Searching Algorithms
7. Compare Sorting Algorithms
8. Generate New Dataset
9. Exit
Choose an option:

Generate a Dataset

Choose option 8 and select a dataset size.

Available sizes:

* 10 numbers
* 100 numbers
* 1,000 numbers
* 10,000 numbers

The application generates random integers for the selected dataset.

Explore Searching Algorithms

Choose Linear Search or Binary Search.

Enter a number to find and observe how the algorithm examines the data.

Linear Search checks elements one at a time.

Binary Search repeatedly halves the search range, but it requires sorted input.

Explore Sorting Algorithms

Choose Bubble Sort, Selection Sort, or Merge Sort.

Observe the algorithm’s progress and compare the final sorted output.

Step-by-step output is most useful for small datasets. Large datasets can produce a substantial amount of terminal output.

Compare Searching Algorithms

Choose option 6.

The application reports:

* Dataset size.
* Search target.
* Number of element comparisons.
* Measured execution time.

Binary Search uses a sorted copy of the dataset. The time needed to prepare that sorted copy is excluded from the search measurement.

Compare Sorting Algorithms

Choose option 7.

The application runs each sorting algorithm against the same original dataset.

It reports comparison counts and measured execution times.

Bubble Sort and Selection Sort can become slow on large datasets because their worst-case time complexity is quadratic.

Running the Tests

From the project directory, execute:

python -m unittest discover -s tests -v

The tests check searching behavior, sorting correctness, duplicate values, empty lists, and randomly generated inputs.

Understanding Big-O Notation

Big-O notation describes how an algorithm’s resource requirements grow as the input size increases.

Linear Search — O(n)

Linear Search checks elements one at a time.

In the worst case, doubling the number of elements approximately doubles the number of comparisons.

Binary Search — O(log n)

Binary Search eliminates approximately half of the remaining search range after each comparison.

This makes it substantially more scalable than Linear Search for sufficiently large sorted datasets.

Bubble Sort — O(n²)

Bubble Sort repeatedly compares neighboring elements.

Its worst-case number of comparisons grows quadratically with input size.

Selection Sort — O(n²)

Selection Sort repeatedly finds the smallest element in the unsorted portion of the list.

Its standard implementation performs quadratic work regardless of whether the input is already sorted.

Merge Sort — O(n log n)

Merge Sort divides the list into smaller sections, sorts those sections, and merges them.

It generally scales much better than the two quadratic sorting algorithms for large datasets.

Measuring Performance

The application uses Python’s time.perf_counter() to measure elapsed time.

Measured execution times depend on hardware, Python version, system activity, input distribution, and implementation details.

For reliable comparisons:

* Run benchmarks more than once.
* Compare algorithms using identical input data.
* Distinguish element-comparison counts from total execution time.
* Remember that a single timing measurement can be noisy.
* Account for preprocessing when comparing complete workflows.

Binary Search is benchmarked on a dataset that has already been sorted. If the application must sort the data specifically for a single search, the sorting cost should also be considered.

Project Structure

algorithm-playground/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── tests/
    └── test_algorithms.py

Learning Outcomes

Through this project, I explored:

* Searching and sorting algorithms.
* Arrays and lists.
* Iteration and recursion.
* Functions and return values.
* Divide-and-conquer strategies.
* Time complexity and Big-O notation.
* Performance measurement.
* Automated testing.
* Python command-line application design.

Future Improvements

Potential extensions include:

* Interactive terminal animations.
* A graphical algorithm visualizer.
* Average-case and worst-case benchmark experiments.
* Repeated benchmark trials and median timings.
* Space-complexity comparisons.
* Custom datasets and target selection.
* Additional algorithms such as insertion sort, quicksort, and hash-based search.
* Exporting benchmark results to CSV.

Learning Project

This project was created for educational purposes to explore algorithm design, implementation, correctness, and performance.

The implementations are written explicitly to make the underlying logic easier to study.

⸻

Built with Python |  Algorithms, Visualization, and Performance
