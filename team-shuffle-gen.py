#!/usr/bin/env python3

import sys
import random
import argparse

def generate_random_groups(names, group_size, num_lines):
    previous_group = set()
    all_names = set(names)

    for _ in range(num_lines):
        available_names = list(all_names - previous_group)

        if len(available_names) < group_size:
            available_names = list(all_names)

        group = random.sample(available_names, group_size)
        print(" , ".join(group))

        previous_group = set(group)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate random groups from a list of names.")
    parser.add_argument("-g", "--group_size", type=int, required=True, help="Number of people in each group")
    parser.add_argument("-n", "--num_lines", type=int, required=True, help="Number of groups to generate")
    return parser.parse_args()

def read_names_from_stdin():
    names = []
    for line in sys.stdin:
        name = line.strip()
        if name:  # 空行を無視する
            names.append(name)
    return names

def main():
    args = parse_arguments()

    names = read_names_from_stdin()

    if not names:
        print("Error: No input provided. Please provide a list of names via standard input.")
        sys.exit(1)

    if len(names) < args.group_size:
        print(f"Error: Not enough names. Need at least {args.group_size} names, but only got {len(names)}.")
        sys.exit(1)

    generate_random_groups(names, args.group_size, args.num_lines)

if __name__ == "__main__":
    main()
