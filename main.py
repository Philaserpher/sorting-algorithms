from SortingBar import SortingBar
import random


NUMBER_OF_BARS = 10


def generate_random_bars(len, start=None, increment=None):

    if not start:
        start = 20
    if not increment:
        increment = 20

    bar_list = []
    for i in range(0, len):
        bar_list.append(SortingBar(i*increment+start, 20, i))

    return bar_list


if __name__ == '__main__':
    bar_list = generate_random_bars(NUMBER_OF_BARS)
    random.shuffle(bar_list)
    for i in bar_list:
        print(i.get_height())
