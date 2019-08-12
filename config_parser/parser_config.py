import configparser
import os
import json


def get_config(section, key):
    config = configparser.ConfigParser()
    path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'config.ini')
    config.read(path, encoding='utf-8')
    return config.get(section, key)


if __name__ == '__main__':
    dir = os.path.split(os.path.realpath(__file__))[0]
    print(dir)
    host = get_config("database", "dbhost")
    print(host)

    print(2*(2, 3))
    a = [(2, 3), (4, 5), (2, 3)]
    d = json.dumps(a)
    print(d)
