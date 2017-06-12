from pprint import pprint


def update(data, service, count):
    pass


def main():
    example_data = {
        'ginger': {
            'django': 2,
            'flask': 3,
        },
        'cucumber': {
            'flask': 1,
        },
    }

    print("Configuration before:")
    pprint(example_data)

    update(example_data, 'pylons', 7)

    print("Configuration after:")
    pprint(example_data)

if __name__ == '__main__':
    main()
