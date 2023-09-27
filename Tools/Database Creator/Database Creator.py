import argparse
import os


def main():
    args = get_args_from_cmd_line()
    check_input_file_exists(args.input)
    check_output_folder_exists(args.output)

    title_index_map = {}

    update_title_index_map_with_existing_files(args.output, title_index_map)

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
    input_file_extension = input_filepath[-4:]
    if input_file_extension != ".txt":
        print("The input file is not a .txt file, terminating.")
        exit()
    if not os.path.exists(input_filepath):
        print("The input file provided could not be found, terminating.")
        exit()
    return


# This function checks for the existence of the provided output folder, and with user permission creates it in the event
# that it cannot be found
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
    return

# This function iterates through the given output folder and updates the title_index_map with the found occurrences of
# each movie title which currently exists at runtime
def update_title_index_map_with_existing_files(output_folder_filepath, title_index_map):
    # Iterate through all files in output folder
    for filename in os.listdir(output_folder_filepath):
        # For each file found, lookup the title in the title-index map,
        # initialize at 0 if not found and increment the index if found
        curr_index = 0
        for char in filename:
            if char == '-':
                break
            curr_index += 1
        movie_title = filename[:curr_index]
        if movie_title in title_index_map:
            title_index_map[movie_title] = title_index_map[movie_title] + 1
        else:
            title_index_map.update({movie_title: 0})
    return


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()