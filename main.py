# 4-oy 10 dars
# homeworks
import multiprocessing

# 1
def file_reader_function(filepath):
    with open(filepath, 'r') as file:
        return file.read()

class FileReader:
    def __init__(self, filepath):
        self.filepath = filepath

    def __enter__(self):
        self.file = open(self.filepath, 'r')
        return self.file.read()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
#----------------------------------------------
# 2
def sum_of_numbers(numbers):
    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    return total
#----------------------------------------------
# 3
def rotate_list(lst):
    return lst[1:] + lst[:1]
#----------------------------------------------
# 4
def find_min_max(numbers):
    return min(numbers), max(numbers)
#----------------------------------------------
# 5
def find_element(lst, element):
    return element in lst
#----------------------------------------------
# 6
def remove_duplicates(lst):
    return list(set(lst))
#----------------------------------------------
# 7
def reverse_words(words):
    return [word[::-1] for word in words]
#----------------------------------------------
# 8
def find_longest_word(words):
    return max(words, key=len)
#----------------------------------------------
# 9
def find_duplicates_in_dict(d):
    values = list(d.values())
    return [value for value in set(values) if values.count(value) > 1]
#----------------------------------------------
# 10
def find_and_sort_numbers_in_dict(d):
    numbers = [value for value in d.values() if isinstance(value, (int, float))]
    return sorted(numbers)
#----------------------------------------------
# 11.
def double_numbers_in_dict(d):
    return {k: (v * 2 if isinstance(v, (int, float)) else v) for k, v in d.items()}
#----------------------------------------------
# 12.
def find_max_value_key(d):
    return max(d, key=d.get)
#----------------------------------------------
# 13.
def find_average_of_values(d):
    values = [v for v in d.values() if isinstance(v, (int, float))]
    return sum(values) / len(values) if values else None
#----------------------------------------------
# 14.
def merge_dicts(d1, d2):
    merged = d1.copy()
    for k, v in d2.items():
        if k in merged:
            merged[k] += v
        else:
            merged[k] = v
    return merged
#----------------------------------------------
# 15.
def find_longest_and_shortest_keys(d):
    keys = d.keys()
    return max(keys, key=len), min(keys, key=len)
#----------------------------------------------
# 16.
def convert_numeric_strings_to_numbers(d):
    return {k: (int(v) if isinstance(v, str) and v.isdigit() else v) for k, v in d.items()}
#----------------------------------------------
# Multiprocessing function to execute all tasks
def execute_task(task, *args):
    return task(*args)

def main():
    # Input examples
    numbers = [1, 2, 3, 4, 5]
    lst = [1, 2, 3, 4]
    words = ["hello", "world", "python"]
    d = {"a": 1, "b": 2, "c": "3", "d": 2}

    tasks = [
        (sum_of_numbers, numbers),
        (rotate_list, lst),
        (find_min_max, numbers),
        (find_element, lst, 3),
        (remove_duplicates, [1, 2, 2, 3, 4, 4]),
        (reverse_words, words),
        (find_longest_word, words),
        (find_duplicates_in_dict, d),
        (find_and_sort_numbers_in_dict, d),
        (double_numbers_in_dict, d),
        (find_max_value_key, d),
        (find_average_of_values, d),
        (merge_dicts, {"a": 1}, {"a": 2, "b": 3}),
        (find_longest_and_shortest_keys, d),
        (convert_numeric_strings_to_numbers, d),
    ]

    with multiprocessing.Pool() as pool:
        results = [pool.apply(execute_task, task) for task in tasks]


    for i, result in enumerate(results, 1):
        print(f"Task {i}: {result}")