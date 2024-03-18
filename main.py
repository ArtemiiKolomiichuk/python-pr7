from app.io.input import *
from app.io.output import *


def main():
    data = input_from_console()
    write_in_console(data)
    write_in_file("data/output/output_0.txt", data)

    data = input_from_file("data/data.json")
    write_in_console(data)
    write_in_file("data/output/output_1.txt", data)

    data = input_from_file_pandas("data/data_2.json")
    write_in_console(data)
    write_in_file("data/output/output_2.txt", data.to_string())

if __name__ == "__main__":
    main()