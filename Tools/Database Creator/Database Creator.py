import argparse
import os


def main():
    args = get_args_from_cmd_line()
    check_input_file_exists(args.input)
    check_output_folder_exists(args.output)

    title_index_map = {}

    update_title_index_map_with_existing_files(args.output, title_index_map)
    generate_output_from_input_file(title_index_map, args.input, args.output, create_txt_output)

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


# This will check the title_index map to see if a movie title currently exists,
# and will either add it if it doesn't or increment it if it does
def increment_title_in_index_map(title_index_map, movie_title):
    if movie_title in title_index_map:
        title_index_map[movie_title] = title_index_map[movie_title] + 1
    else:
        title_index_map.update({movie_title: 0})
    return


# This function iterates through the given output folder and updates the title_index_map with the found occurrences of
# each movie title which currently exists at runtime
# WARNING: assumes that all files in the output folder follow the naming scheme laid out in the planning document
def update_title_index_map_with_existing_files(output_folder_filepath, title_index_map):
    # Iterate through all files in output folder
    for filename in os.listdir(output_folder_filepath):
        # For each file found, lookup the title in the title-index map,
        # initialize at 0 if not found and increment the index if found
        curr_index = 0
        tak_bool = False
        for char in filename:
            if char == '-' and tak_bool:
                break
            elif char == '-' and not tak_bool:
                tak_bool = True
            curr_index += 1
        movie_title = filename[:curr_index]
        increment_title_in_index_map(title_index_map, movie_title)
    return


# This is a dummy function which creates txt files, used in the testing of generate_output_from_input_file
def create_txt_output(filename, output_folder_filepath, url):
    filename_with_ext = filename + ".txt"
    final_path = output_folder_filepath + '\\' + filename_with_ext
    temp_file_handle = open(final_path, "w")
    temp_file_handle.close()
    return


# This function processes the incoming movie title to generate
# the final format for the label an incoming file will receive
# (as laid out in the planning doc)
def generate_output_filename(title_index_map, movie_title, actor):
    movie_title = movie_title.replace(' ', '_')
    actor = actor.replace(' ', '_')
    increment_title_in_index_map(title_index_map, movie_title)
    return actor + "-" + movie_title + "-" + str(title_index_map[movie_title] + 1)


# This function takes in a function, create_output, and uses that to generate output files by parsing the input file
# WARNING: Assumes input file is of the correct format, as laid out in the planning doc
def generate_output_from_input_file(title_index_map, input_filepath, output_folder_filepath, create_output):
    with open(input_filepath) as input_file:
        curr_movie_title = ""
        curr_actor = ""
        while input_file:
            curr_line = input_file.readline()
            if curr_line == "":
                break

            if curr_line[0] == 'A':
                curr_actor = curr_line[7:-1]
            elif curr_line[0] == 'T':
                curr_movie_title = curr_line[7:-1]
                continue
            elif curr_line[0] == 'U':
                url = curr_line[5:-1]
                output_filename = generate_output_filename(title_index_map, curr_movie_title, curr_actor)
                create_output(output_filename, output_folder_filepath, url)
                continue
            elif curr_line[0] == '\n':
                continue
    return


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()