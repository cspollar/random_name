import argparse
import random


def get_names(file_object):
    """Return List of Names."""
    return [x.strip() for x in file_object.readlines() if x.strip()]


def get_random_name(file):
    with open(file, "r") as f:
        names = get_names(f)
    return random.choice(names)


def add_name(file, name):
    with open(file, "a") as f:
        f.write(name + "\n")
    return name


def remove_name(file, name):
    with open(file, "r") as f:
        names = get_names(f)
        names.remove(name)
    with open(file, "w") as f:
        # Overwrite file with new names
        for name in names:
            f.write(name + "\n")
    return name


def main():
    parser = argparse.ArgumentParser(description="Random name from a list")
    parser.add_argument("file", type=str, help="A file with names of each line")
    parser.add_argument("--add", help="name to add to file")
    parser.add_argument("--remove", help="name to remove from file")

    args = parser.parse_args()

    if not args.add or args.remove:
        try:
            message = f"Random Selection: {get_random_name(args.file)}"
        except:
            message = f"Unable to open {args.file}"

    if args.add:
        try:
            message = f"Added: {add_name(args.file, args.add)}"
        except:
            message = f"Unable to add {args.add} to {args.file}"

    if args.remove:
        try:
            message = f"Removed: {remove_name(args.file, args.remove)}"
        except:
            message = f"Unable to remove {args.remove} from {args.file}"

    print(message)


if __name__ == "__main__":
    main()
