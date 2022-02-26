import os
import glob
from datetime import datetime


# Functions
def prepend_line(filepath, line_to_prepend):
    """
    Prepend lines at the beginning of a file. Concept from https://stackoverflow.com/a/5917395.

    :param filepath: Path of the file.
    :param line_to_prepend: The line to prepend.
    :return: Nothing.
    """
    with open(filepath, 'r+', encoding='utf-8') as a_file:
        content = a_file.read()
        a_file.seek(0, 0)
        a_file.write(line_to_prepend.rstrip('\r\n') + '\n' + content)


def list_files(path, tree_file):
    """
    Lists files in the given path. Concept from: https://stackoverflow.com/a/9728478

    :param path: The root. Tree starts to populate from here.
    :param tree_file: The file where the tree is to be written.
    :return: None
    """
    # Define variables
    count_audio = 0
    count_video = 0

    # Write tree
    with open(tree_file, 'w', encoding='utf-8') as tf:
        for root, dirs, files in os.walk(path):
            level = root.replace(path, '').count(os.sep)
            indent = ' ' * 4 * level
            tf.writelines('{}{}/'.format(indent, os.path.basename(root)) + '\n')
            sub_indent = ' ' * 4 * (level + 1)
            for f in files:
                file_path = os.path.join(root, f)
                if not f == 'desktop.ini':  # Ignore `desktop.ini` files
                    last_modified_timestamp = os.path.getmtime(file_path)
                    last_modified = datetime.fromtimestamp(
                        last_modified_timestamp).__str__()
                    tf.writelines('{}{}'.format(sub_indent, f) + ' ' +
                                  last_modified + '\n')
                if file_path.endswith('.mp3') \
                        or file_path.endswith('.wma') \
                        or file_path.endswith('.flac') \
                        or file_path.endswith('.wav'):
                    count_audio += 1
                elif file_path.endswith('.mp4') \
                        or file_path.endswith('.mkv') \
                        or file_path.endswith('.flv') \
                        or file_path.endswith('.wmv') \
                        or file_path.endswith('.mov') \
                        or file_path.endswith('.avi'):
                    count_video += 1

    # Prepend datetime and count of audio and video files to the file
    date_time = datetime.now().strftime('%B %d, %Y, %I:%M %p')
    line = 'Last generation: ' + date_time + '\n'
    line += 'Number of audios: ' + count_audio.__str__() + '\n'
    line += 'Number of videos: ' + count_video.__str__() + '\n\n'
    prepend_line(tree_file, line)


def format_files():
    """
    Format every .py file using yapf Google style
    :return: None
    """
    py_files = glob.glob('*.py')
    for py_file in py_files:
        os.system('yapf ' + py_file + ' -i --style google --no-local-style')
