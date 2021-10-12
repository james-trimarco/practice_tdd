from typing import List

# Re-factor the function compute_stats into the following functions:
# read_ints: Reads in the data from random_nums.txt and convert them into a list of integers
# count: Returns the total number of elements in random_nums.txt
# summation: Returns the sum of all of the elements in random_nums.txt
# average: Returns the average of all of the elements in random_nums.txt
# minimum: Returns the smallest integer in random_nums.txt
# maximum: Returns the largest integer in random_nums.txt


def read_ints(file_name: str) -> List[int]:
    with open(file_name, "r") as file:
        ints = []
        for line in file:
            if line.strip().isnumeric():
                ints.append(int(line))
            else:
                continue
    return ints


def count(data: List[int]) -> int:
    return len(data)


def summation(data: List[int]) -> int:
    return None  # sum(data)


def compute_stats(file):
    total = 0
    sum = 0
    average = 0
    with open(file, "r") as f:
        first_line = int(f.readline())
        f.seek(0)
        min = first_line
        max = first_line
        for num in f:
            num = int(num)
            total += 1
            sum += num
            if min > num:
                min = num
            if max < num:
                max = num

        print(f"total = {total}")
        print(f"summation = {sum}")
        print(f"average = {round(sum / total)}")
        print(f"Minimum = {min}")
        print(f"Maximum = {max}")


if __name__ == "__main__":
    read_ints("random_nums.txt")
