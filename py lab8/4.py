def count_file_lines(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for _ in file)
    return line_count