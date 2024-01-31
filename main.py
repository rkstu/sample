"""
2.Write a Javascript, Python, or OCaml program that:
-accepts a list of integers
-emits an error message if the list is not a multiple of 10 in length
-returns or prints a list of integers based on the input list, but with items at positions which are a multiple of 2 or 3 removed
Host your program at a public git-based repository and include robust testing for your program.
"""

def process_list(input_list):
    # Check if the length of the list is a multiple of 10
    if len(input_list) % 10 != 0:
        raise ValueError("Input list length must be a multiple of 10")

    # Remove items at positions which are a multiple of 2 or 3
    result_list = [x for i, x in enumerate(input_list) if (i + 1) % 2 != 0 and (i + 1) % 3 != 0]

    return result_list

if __name__ == "__main__":
    # Example usage
    try:
        input_list = list(range(1, 21))
        result = process_list(input_list)
        print("Input List:", input_list)
        print("Result List:", result)
    except ValueError as e:
        print("Error:", e)
