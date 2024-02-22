def display_results(result, input_file):
    if isinstance(result, tuple):
        print(f"{result[0]} {result[1]} {result[2]} {input_file.split('/')[-1]}")
    else:
        print(f"{result} {input_file}")