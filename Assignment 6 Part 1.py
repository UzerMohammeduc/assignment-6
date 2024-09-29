import random
import time

# Deterministic Selection Algorithm (Median of Medians)
def deterministic_select(arr, k):
    """
    Select the k-th smallest element in arr using the deterministic
    Median of Medians algorithm.

    :param arr: List of elements to select from.
    :param k: The order statistic to find (1-based index).
    :return: The k-th smallest element in arr.
    """
    # Base case: If the list is small, sort and return the k-th element.
    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    # Divide arr into sublists of at most 5 elements each.
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    # Find the median of each sublist.
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

    # Recursively find the median of medians.
    pivot = deterministic_select(medians, len(medians) // 2 + 1)

    # Partition the array into elements less than, equal to, and greater than the pivot.
    low = [el for el in arr if el < pivot]
    high = [el for el in arr if el > pivot]
    count = arr.count(pivot)

    # Determine the position of the pivot element.
    if k <= len(low):
        # The k-th smallest is in the low partition.
        return deterministic_select(low, k)
    elif k > len(low) + count:
        # The k-th smallest is in the high partition.
        return deterministic_select(high, k - len(low) - count)
    else:
        # The pivot is the k-th smallest element.
        return pivot


# Randomized Selection Algorithm (Quickselect)
def randomized_select(arr, k):
    """
    Select the k-th smallest element in arr using the randomized Quickselect algorithm.

    :param arr: List of elements to select from.
    :param k: The order statistic to find (1-based index).
    :return: The k-th smallest element in arr.
    """
    # If the list contains only one element, return it.
    if len(arr) == 1:
        return arr[0]

    # Randomly select a pivot element from arr.
    pivot = random.choice(arr)

    # Partition the array into elements less than, equal to, and greater than the pivot.
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    # Determine the position of the pivot elements.
    if k <= len(lows):
        # The k-th smallest is in the lows partition.
        return randomized_select(lows, k)
    elif k > len(lows) + len(pivots):
        # The k-th smallest is in the highs partition.
        return randomized_select(highs, k - len(lows) - len(pivots))
    else:
        # The pivot is the k-th smallest element.
        return pivots[0]


# Benchmarking Function
def benchmark_selection_algorithms():
    # Generate different types of input arrays
    random_array = [random.randint(1, 1000) for _ in range(1000)]
    sorted_array = sorted(random_array)
    reverse_sorted_array = sorted_array[::-1]

    # Test k-th element
    k = 500  # Arbitrary k value (1-based index)

    # Function to measure time taken by an algorithm
    def measure_time(func, array, k):
        start_time = time.time()
        result = func(array.copy(), k)
        end_time = time.time()
        return end_time - start_time, result

    # Measure time for randomized algorithm
    print("Randomized Quickselect:")
    time_taken, result = measure_time(randomized_select, random_array, k)
    print(f"Random array: {time_taken} seconds, Result: {result}")
    
    time_taken, result = measure_time(randomized_select, sorted_array, k)
    print(f"Sorted array: {time_taken} seconds, Result: {result}")
    
    time_taken, result = measure_time(randomized_select, reverse_sorted_array, k)
    print(f"Reverse sorted array: {time_taken} seconds, Result: {result}")

    # Measure time for deterministic algorithm
    print("\nDeterministic Median of Medians:")
    time_taken, result = measure_time(deterministic_select, random_array, k)
    print(f"Random array: {time_taken} seconds, Result: {result}")
    
    time_taken, result = measure_time(deterministic_select, sorted_array, k)
    print(f"Sorted array: {time_taken} seconds, Result: {result}")
    
    time_taken, result = measure_time(deterministic_select, reverse_sorted_array, k)
    print(f"Reverse sorted array: {time_taken} seconds, Result: {result}")


if __name__ == "__main__":
    benchmark_selection_algorithms()
