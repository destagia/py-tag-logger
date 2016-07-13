import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-v', '--verbose_tags', metavar='N', type=str, nargs='+', default=None,
                   help='log target')

logger_config_tags = parser.parse_args().verbose_tags

def get_tags():
    return logger_config_tags
