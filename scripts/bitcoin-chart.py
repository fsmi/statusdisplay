#!/usr/bin/env python3

import kraken
import time
import sys
import os

def print_chart(values, rows=20, columns=70):
    interval = int(values[1][0]) - int(values[0][0])
    row_scale = 5
    left_distance = 7

    text = list('EUR/BTC▲\n')
    maximum = float(max(m[2] for m in values[-columns:]))
    minimum = float(min(m[3] for m in values[-columns:]))
    for row in range(rows):
        point = maximum - row * ((maximum - minimum)/rows)
        caption = str(round(point))
        if row % row_scale == 0:
            text.append(caption + '€' + (left_distance - len(caption) - 1) * ' ' + '┤')
        else:
            text.append((left_distance) * ' ' + '│')
        for element in values[-columns:]:
            open_value = float(element[1])
            high_value = float(element[2])
            low_value = float(element[3])
            close_value = float(element[4])
            low_range = maximum - (row + 1) * ((maximum - minimum)/rows)
            high_range = point
            middle_range = (low_range + high_range) / 2.0
            end_color = '\033[0m'
            if open_value < close_value:
                higher_value = close_value
                lower_value = open_value
                color = '\033[32m'
            else:
                higher_value = open_value
                lower_value = close_value
                color = '\033[31m'

            if (lower_value < low_range or lower_value < middle_range) and higher_value >= low_range:
                if (higher_value < middle_range):
                    if (high_value > middle_range):
                        text.append(color + '╽' + end_color)
                    else: 
                        text.append(color + '╻' + end_color)
                else:
                    text.append(color + '┃' + end_color)
            elif (lower_value >= middle_range) and (lower_value < high_range):
                if (low_value  < middle_range):
                    text.append(color + '╿' + end_color)
                else:
                    text.append(color + '╹' + end_color)
            elif (high_value >= low_range) and (low_value < middle_range):
                if (high_value < middle_range):
                    text.append(color + '╷' + end_color)
                else:
                    text.append(color + '│' + end_color)
            elif (low_value < high_range) and (high_value >= middle_range):
                if (low_value > middle_range):
                    text.append(color + '╵' + end_color)
                else:
                    text.append(color + '│' + end_color)
            else:
                text.append(' ')

        text.append('\n')
    text.append((left_distance * ' ') + '┼' + columns * '─' + '►\n')
    text.append((left_distance + columns - 15) * ' ' + ' ' + 'step:' + ' ' + str(int(interval / 60)) + ' ' + 'min')
    return ''.join(text)


def main():
    api = kraken.public()
    sz = os.get_terminal_size()
    os.system('setterm -cursor off')
    while True:
        try:
            data = api.getOHLC(interval=1)
            printable_chart = print_chart(data, columns=sz.columns-9, rows=sz.lines-5)
            os.system('clear')
            print(printable_chart)
            print(time.asctime(time.localtime(time.time())))
        except:
            pass
        time.sleep(30)

if __name__ == '__main__':
    main()
