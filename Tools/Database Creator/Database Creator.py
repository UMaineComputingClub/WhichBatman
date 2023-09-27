import argparse


def main():
    args = get_args_from_cmd_line()
    exit()


def get_args_from_cmd_line():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', action='store', type=str,
                        help='The input file to get URL\'s from')
    parser.add_argument('-o', '--output', action='store', type=str,
                        help='The output folder where videos will be stored.')

    return parser.parse_args()
