import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    a = np.array(lst).reshape(3, 3)

    result = {}

    for stat in ['mean', 'var', 'std', 'max', 'min', 'sum']:
        func = getattr(np, stat)
        result_name = stat if stat != 'std' else 'standard deviation'
        result[result_name] = [
            func(a, axis=0).tolist(),    # Columns
            func(a, axis=1).tolist(),    # Rows
            func(a).item()               # Flattened
        ]

    return result

# 💡 ENTER YOUR 9 NUMBERS HERE
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Run and print the result
print(calculate(numbers))

