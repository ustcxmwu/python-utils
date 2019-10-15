import os
from enum import Enum

import yaml


class Hero:
    def __init__(self, name, hp, sp):
        self.name = name
        self.hp = hp
        self.sp = sp


class AlgoType(Enum):
    Online = 1
    Offline = 2


class Config():
    def __init__(self, path=None):
        if not path:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.yaml')
        with open(path, 'r', encoding='utf-8') as f:
            self.config = yaml.full_load(f.read())

        if self.config.get('custom', None) is not None:
            for key, value in self.config.get('custom').items():
                self.config['default'][key] = value

    def __getattr__(self, attr):
        return self.config['default'][attr]


if __name__ == '__main__':
    # a = yaml.full_load("""
    # !!python/object:__main__.Hero
    # name: Welthyr Syxgon
    # hp: 1200
    # sp: 0
    # """)
    # print(a)
    print(yaml.__version__)
    a = Config()
    print(a.Smtp_Server)
