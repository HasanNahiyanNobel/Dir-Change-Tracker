from datetime import datetime
from utilities import list_files, format_files

# Root of directory
ROOT = 'H:\My Drive\উত্তম সঙ্গীত'

# Variables
now = datetime.now().strftime('%Y_%m_%d_%H%M%S')
tree_name = 'tree_' + now
tree_path = 'out\\' + tree_name + '.txt'

# Format all the files using Google style guide
format_files()

# Generate output file
list_files(ROOT, tree_path)
