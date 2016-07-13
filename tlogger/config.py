import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-vt', '--verbose_tags', metavar='N', type=str, nargs='+',)
parser.add_argument('-v', '--verbose', action='store_true', default=False)

parse_args = parser.parse_args()
logger_config_tags = parse_args.verbose_tags
verbose = parse_args.verbose

def get_is_verbose():
    return verbose

def get_tags():
    return logger_config_tags
