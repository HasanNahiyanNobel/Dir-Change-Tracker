import os
import glob
from datetime import datetime


def list_files(path, tree_file):
    """
    Lists files in the given path. Concept from: https://stackoverflow.com/a/9728478
    Additionally, prints a count of audio and video files in the console.

    :param path: The root. Tree starts to populate from here.
    :param tree_file: The file where the tree is to be written.
    :return: None
    """
    count_audio = 0
    count_video = 0
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
    print('Number of audios: ' + count_audio.__str__())
    print('Number of videos: ' + count_video.__str__())


def format_files():
    """
    Format every .py file using yapf Google style
    :return: None
    """
    py_files = glob.glob('*.py')
    for py_file in py_files:
        os.system('yapf ' + py_file + ' -i --style google --no-local-style')
