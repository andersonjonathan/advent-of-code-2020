from helper import get_input


def decode_position(x):
    for z in ['f', 'F', 'l', 'L']:
        x = x.replace(''.join(z), '0')
    for o in ['b', 'B', 'r', 'R']:
        x = x.replace(''.join(o), '1')
    return int(x, 2)


def main():
    data = [decode_position(x) for x in get_input(5).split('\n') if x]
    print(max(data))


if __name__ == '__main__':
    main()
