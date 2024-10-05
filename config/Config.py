import configparser
import os

class Config:
    def __init__(self, env='dev'):
        self.config = configparser.ConfigParser(inline_comment_prefixes=('#', ';')) 
        self.env = env
        self.config_file = os.path.join('config', f'{env}.ini')
        self.config.read(self.config_file,'UTF-8')

    def get(self, section, option):
        return self.config.get(section, option)

    # ... other methods