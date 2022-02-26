import os
import glob
from datetime import datetime


def list_files(path, tree_file):
    """
    Lists files in the given path.
    Concept from: https://stackoverflow.com/a/9728478

    :param path: The root. Tree starts to populate from here.
    :param tree_file: The file where the tree is to be written.
    :return: None
    """
    with open(tree_file, 'w', encoding='utf-8') as tf:
        for root, dirs, files in os.walk(path):
            level = root.replace(path, '').count(os.sep)
            indent = ' ' * 4 * level
            tf.writelines('{}{}/'.format(indent, os.path.basename(root)) + '\n')
            sub_indent = ' ' * 4 * (level + 1)
            for f in files:
                if not f == 'desktop.ini':  # Ignore `desktop.ini` files
                    file_path = os.path.join(root, f)
                    last_modified_timestamp = os.path.getmtime(file_path)
                    last_modified = datetime.fromtimestamp(
                        last_modified_timestamp).__str__()
                    tf.writelines('{}{}'.format(sub_indent, f) + ' ' +
                                  last_modified + '\n')


def format_files():
    """
    Format every .py file using yapf Google style
    :return: None
    """
    py_files = glob.glob('*.py')
    for py_file in py_files:
        os.system('yapf ' + py_file + ' -i --style google --no-local-style')
