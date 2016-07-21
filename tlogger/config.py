# import argparse

# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('-vt', '--verbose_tags', metavar='N', type=str, nargs='+',)
# parser.add_argument('-v', '--verbose', action='store_true', default=False)

# parse_args = parser.parse_args()
# logger_config_tags = parse_args.verbose_tags
# verbose = parse_args.verbose
import sys

logger_config_tags = None
verbose = False

collecting_tags = False

for arg in sys.argv:
    if arg == "-t" or arg == "--verbose-tags":
        collecting_tags = True
        continue
    elif arg == "-v" or arg == "--verbose":
        collecting_tags = False
        verbose = True
    elif arg[0] == "-":
        collecting_tags = False
    elif collecting_tags:
        logger_config_tags = logger_config_tags or []
        logger_config_tags.append(arg)
        continue

def get_is_verbose():
    return verbose

def get_tags():
    return logger_config_tags
