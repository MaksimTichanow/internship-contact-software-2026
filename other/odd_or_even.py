numbers = [3, 9, 10, 15, 31, 64, 127, 255, 512, 1023]


def first_even(your_list):
    for num in your_list:
        if num % 2 == 0:
            print(f"{num} is an even Number")
            break

def all_even(your_list):
    for num in your_list:
        if num % 2 == 0:
            print(f"{num} is an even Number")
            continue
