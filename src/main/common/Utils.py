def display_results(result, input_file):
    for option in result:
        print(option, end=" ")
    print(f"{input_file.split('/')[-1]}")
