import argparse
import os


def main():
    args = get_args_from_cmd_line()
    check_input_file_exists(args.input)
    exit()

# This takes in command line arguments and passes them out as an object, args can be accessed by name i.e. args.input
def get_args_from_cmd_line():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', action='store', type=str,
                        help='The input file to get URL\'s from')
    parser.add_argument('-o', '--output', action='store', type=str,
                        help='The output folder where videos will be stored.')

    return parser.parse_args()


# This function checks for the existence of the input file, and terminates the program if it cannot be found
def check_input_file_exists(input_filepath):
    if not os.path.exists(input_filepath):
        print("The input file provided could not be found, terminating.")
        exit()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()