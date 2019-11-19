# Example of usage
# python interviewio.py -files 500 -size 1024 -dir TestDirectory -P Hello -parallel 2

import argparse
import multiprocessing
import os
import sys
from datetime import datetime


def main():
    args = get_namespace()
    number_of_files = args.files
    path = args.dir
    number_of_parallel = args.parallel

    check_path_to_file(path)
    file_names = []
    for i in range(number_of_files):
        file_names.append(str(i) + '.txt')

    before_creation = datetime.now()
    with multiprocessing.Pool(processes=number_of_parallel) as pool:
        file_creation_time_array = pool.map(create_file, file_names)

    after_creation = datetime.now()
    delta = after_creation - before_creation

    average = 0
    for i in file_creation_time_array:
        average += i
    print("Create", number_of_files, "files in", path, "in", number_of_parallel, "threads")
    print("Min:", min(file_creation_time_array), "ms", end=" ")
    print("Max:", max(file_creation_time_array), "ms", end=" ")
    print("Avr:", round(average / len(file_creation_time_array)), "ms", end=" ")
    print("Total:", delta.seconds * 1000000 + delta.microseconds, "ms")


def create_file(file_name):
    args = get_namespace()

    file_size = args.size
    file_pattern = args.P
    path = args.dir
    file_path = os.path.join(path, file_name)

    amount = file_size // len(file_pattern)
    difference_in_file_size = file_size - len(file_pattern) * amount

    before = datetime.now()

    with open(file_path, "w") as somefile:
        somefile.write(file_pattern * amount)
        somefile.write(file_pattern[:difference_in_file_size])
        somefile.close()

    after = datetime.now()
    delta = after - before
    
    return int(delta.seconds * 1000000 + delta.microseconds)


def check_path_to_file(file_path):
    if os.path.exists(file_path):
        return 0
    else:
        os.mkdir(file_path)


def get_namespace():
    parser = create_parser()
    return parser.parse_args(sys.argv[1:])


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-files', default=1, required=True, type=int)
    parser.add_argument('-size', default="1", required=True, type=int)
    parser.add_argument('-dir', default="/", required=True, type=str)
    parser.add_argument('-P', default=" ", required=True, type=str)
    parser.add_argument('-parallel', default=1, type=int)
    return parser


if __name__ == '__main__':
    main()
