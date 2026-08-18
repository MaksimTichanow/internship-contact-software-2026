numbers = [3, 9, 10, 15, 31, 64, 127, 255, 512, 1023]

def odd_or_even():
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is an even Number")
            continue


odd_or_even()