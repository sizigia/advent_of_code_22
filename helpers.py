def retrieve_input(day_number):
    filename = f"inputs/input_d{day_number}.txt"
    with open(filename) as file:
        lines = file.readlines()
        file.close()
    return lines