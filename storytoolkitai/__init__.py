import os
from os.path import dirname, realpath
import sys
C_DIR = dirname(realpath(__file__))
P_DIR = dirname(C_DIR)
sys.path.insert(0, P_DIR)

# define a global target dir so we remember where we chose to save stuff last time when asked
# but start with the user's home directory

# user_home_dir = os.path.expanduser("~") 
user_home_dir = P_DIR
initial_target_dir = user_home_dir

# this is where StoryToolkitAI stores the config files
# including project.json files and others
# on Mac, this is usually /Users/[username]/StoryToolkitAI
# on Windows, it's normally C:\Users\[username]\StoryToolkitAI
# on Linux, it's probably /home/[username]/StoryToolkitAI
USER_DATA_PATH = os.path.join(user_home_dir, 'StoryToolkitAI')

# create user data path if it doesn't exist
if not os.path.exists(USER_DATA_PATH):
    os.makedirs(USER_DATA_PATH)

# this is where we store the app configuration
APP_CONFIG_FILE_PATH = os.path.join(USER_DATA_PATH, 'config.json')

# the location of the log file
APP_LOG_FILE = os.path.join(USER_DATA_PATH, 'app.log')


