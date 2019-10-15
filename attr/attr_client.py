from enum import Enum
import yaml

from collections import OrderedDict


class EnumA(Enum):
    ONE = 1
    TWO = 2
    THREE = 3


class BaseDefaultConfig(object):
    f = 1
    e = 2
    c = 3
    b = EnumA.THREE
    a = {
        0: {
            0: 200,
            1: 800
        },
    }

    @classmethod
    def to_dict(cls):
        attr_dict = OrderedDict()
        for name in cls.__dict__:
            if name.startswith('__') or callable(getattr(cls, name)):
                pass
            elif isinstance(getattr(cls, name), Enum):
                attr_dict[name] = str(getattr(cls, name))
            elif isinstance(getattr(cls, name), dict):
                attr_dict[name] = str(getattr(cls, name))
            else:
                attr_dict[name] = getattr(cls, name)
        return attr_dict

    @classmethod
    def dumps(cls):
        yaml.add_representer(OrderedDict, represent_ordered_dict)
        return yaml.dump(cls.to_dict())


    @classmethod
    def dump(cls, filename: str):
        with open(filename, 'w') as f:
            f.write(cls.dumps())

def represent_ordered_dict(self, data: dict):
    ret_value = []
    for key, value in data.items():
        node_key = self.represent_data(key)
        node_value = self.represent_data(value)
        ret_value.append((node_key, node_value))

    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', ret_value)


if __name__ == '__main__':
    # a = BaseDefaultConfig.to_dict()
    # yaml.add_representer(OrderedDict, represent_ordered_dict)
    print(BaseDefaultConfig.dumps())
    BaseDefaultConfig.dump('a.yaml')

    b = OrderedDict()
    b['c'] = 1
    b['a'] = 2
    print(yaml.dump(b))


    c = [1, 2, 3, 4]
    print(yaml.dump(str(c)))

