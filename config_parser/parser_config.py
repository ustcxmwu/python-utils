import configparser
import os


def get_config(section, key):
    config = configparser.ConfigParser()
    path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'config.ini')
    config.read(path, encoding='utf-8')
    return config.get(section, key)

#其中 os.path.split(os.path.realpath(__file__))[0] 得到的是当前文件模块的目录


if __name__ == '__main__':
    dir = os.path.split(os.path.realpath(__file__))[0]
    print(dir)
    host = get_config("database", "dbhost")
    print(host)
