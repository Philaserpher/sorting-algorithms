from SortingBar import SortingBar
import random

BLUE = (50, 72, 168)
RED = (168, 50, 52)

NUMBER_OF_BARS = 20


def generate_random_bars(length, start=None, increment=None):

    if not start:
        start = 20
    if not increment:
        increment = 20

    bar_list = []
    for i in range(length):
        bar_list.append(SortingBar(i*increment+start, 20, i))

    return bar_list


def merge_sort(bar_list):
    if len(bar_list) <= 1:
        return bar_list

    midpoint = len(bar_list)//2

    half1 = merge_sort(bar_list[:midpoint])
    half2 = merge_sort(bar_list[midpoint:])
    final_list = []
    while half1 and half2:
        if half1[0].get_height() < half2[0].get_height():
            final_list.append(half1.pop(0))
        else:
            final_list.append(half2.pop(0))
    while half1:
        final_list.append(half1.pop(0))
    while half2:
        final_list.append(half2.pop(0))

    return final_list


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
    bar_list = merge_sort(bar_list)
    for i in bar_list:
        print(i.get_height())
