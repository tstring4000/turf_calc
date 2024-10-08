# Filename: turf_calc.py
# Author: Tyler Stringer
# Date: 2024-10-08
# Details: Calculator to determine how many doors per turf/list for political door-to-door canvassing list sizes.

# Minimum and maximum doors per list
min_doors = 85
max_doors = 95

# Start an infinite loop to keep the program running until the user provides non-numeric input
while True:
    # Get the total number of doors as an integer from the user
    user_input = input('Enter the number of total doors in turf (or any non-numeric value to exit): ').strip()

    # Check if the input is a number; if not, exit the program
    if not user_input.isdigit():
        print('Non-numeric input detected. Exiting the program. Goodbye!')
        break

    doors = int(user_input)

    # Initialize the counters for lists and leftover doors
    list_counts = {}  # To keep track of how many lists of each size are created
    leftover_doors = doors  # Start with all doors available

    # Create lists of the minimum size first (85 doors)
    while leftover_doors >= min_doors:
        list_counts[min_doors] = list_counts.get(min_doors, 0) + 1
        leftover_doors -= min_doors

    # Then fill with lists of the maximum size (95 doors) if possible
    while leftover_doors >= max_doors:
        list_counts[max_doors] = list_counts.get(max_doors, 0) + 1
        leftover_doors -= max_doors

    # Display the results
    print(f'With a total of {doors} doors, the optimal distribution is as follows:')
    for list_size, count in sorted(list_counts.items(), reverse=True):
        print(f'- {count} list(s) of size {list_size} doors')
    print(f'- Leftover doors that do not fit into a list: {leftover_doors}')

    # Additional information for evenly splitting into smaller chunks
    print(f'- Divided evenly by 2, there are ~{doors / 2:.0f} doors/list')
    print(f'- Divided evenly by 3, there are ~{doors / 3:.0f} doors/list')
    print(f'- Divided evenly by 4, there are ~{doors / 4:.0f} doors/list')
    print(f'- Divided evenly by 5, there are ~{doors / 5:.0f} doors/list')
    print('\n')
