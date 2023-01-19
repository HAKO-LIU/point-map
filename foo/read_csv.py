# coding=utf-8
# date: 2023/1/11 9:37

import csv


def read_csv(path: str):
    # print(path)
    pin_code = ''
    try:
        with open(path, 'r') as csv_file:
            for line in csv_file:
                pin_code += line.replace(',', '').replace('\n', '')
    except FileNotFoundError:
        return -1

    # print(pin_code)
    return pin_code


if __name__ == "__main__":
    # read_csv('../pin/走.csv')
    read_csv('../pin/口.csv')
