import argparse
import os


def main():
    args = get_args_from_cmd_line()
    check_input_file_exists(args.input)
    check_output_folder_exists(args.output)
    title_index_map = {}

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
# WARNING THIS ASSUMES CORRECT INPUT FILE FORMAT AND DOES NO CHECKING
def check_input_file_exists(input_filepath):
    if not os.path.exists(input_filepath):
        print("The input file provided could not be found, terminating.")
        exit()


def check_output_folder_exists(output_filepath):
    if not os.path.exists(output_filepath):
        print("The output folder provided could not be found.")
        while True:
            user_permission = input("Would you like to create a new folder to house output? (y/n): ")
            if user_permission == 'y' or user_permission == "Y" or user_permission == "yes" or user_permission == "Yes":
                print("Creating new folder at ", output_filepath)
                os.mkdir(output_filepath)
                break
            elif user_permission == 'n' or user_permission == 'N' or user_permission == "no" or user_permission == "No":
                print("With no output folder, program cannot continue, terminating")
                exit()
            else:
                print("Invalid input, please provide response as yes or no")
                continue


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()