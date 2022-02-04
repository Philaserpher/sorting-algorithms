from SortingBar import SortingBar
import random

BLUE = (50, 72, 168)
RED = (168, 50, 52)

NUMBER_OF_BARS = 10


def generate_random_bars(length, start=None, increment=None):

    if not start:
        start = 20
    if not increment:
        increment = 20

    bar_list = []
    for i in range(length):
        bar_list.append(SortingBar(i*increment+start, 20, i))

    return bar_list


def insertion_sort(bar_list):
    length = len(bar_list)
    for i in range(length):
        pointer = i-1
        current = bar_list[i]
        while (pointer >= 0 and
               current.get_height() < bar_list[pointer].get_height()):

            bar_list[pointer+1] = bar_list[pointer]
            pointer -= 1
        pointer += 1
        bar_list[pointer] = current

    return bar_list


def selection_sort(bar_list):
    result = []
    while bar_list:
        lowest, lowest_key = bar_list[0], 0

        for i in range(len(bar_list)):
            if bar_list[i].get_height() < lowest.get_height():
                lowest, lowest_key = bar_list[i], i

        result.append(lowest)
        bar_list.pop(lowest_key)

    return result


def bubble_sort(bar_list):
    pass


if __name__ == '__main__':
    bar_list = generate_random_bars(NUMBER_OF_BARS)
    random.shuffle(bar_list)
    bar_list = selection_sort(bar_list)
    for i in bar_list:
        print(i.get_height())
