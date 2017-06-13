from pprint import pprint


def update_service_count(data, host_name, service, count):
    if not data[host_name].get(service):
        data[host_name].update({service: count})
    else:
        data[host_name][service] += count


def update(data, service, count):
    while count > 0:
        list_summary_count = []
        for host_name, service_count in data.items():
            list_summary_count.append((sum(service_count.values()), host_name))
        max_count = max(list_summary_count)
        min_count = min(list_summary_count)
        if max_count[0] > min_count[0]:
            diff_count = max_count[0] - min_count[0]
            if count > diff_count:
                update_service_count(data, min_count[1], service, diff_count)
                count -= diff_count
            else:
                update_service_count(data, min_count[1], service, count)
                count = 0
        else:
            if count % 2 != 0:
                count_first_half = count // 2
                count_second_half = count - count_first_half
                update_service_count(data, max_count[1], service, count_first_half)
                update_service_count(data, min_count[1], service, count_second_half)
                count = 0
            else:
                update_service_count(data, max_count[1], service, int(count/2))
                update_service_count(data, min_count[1], service, int(count/2))
                count = 0


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
