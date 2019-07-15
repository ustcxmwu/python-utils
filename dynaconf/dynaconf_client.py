# from dynaconf import settings
from dynaconf import LazySettings
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("all", help="section name of all setting file", type=str)
    parser.add_argument("part", help="section name of part setting file", type=str)
    args = parser.parse_args()
    print(args.all)
    print(args.part)

    all_settings = LazySettings(
        ENV_FOR_DYNACONF=args.all,
        SETTINGS_FILE_FOR_DYNACONF=['all.toml'],
    )

    part_settings = LazySettings(
        ENV_FOR_DYNACONF=args.part,
        SETTINGS_FILE_FOR_DYNACONF=['part.toml'],
    )

    print(all_settings.HOST)
    print(all_settings.PORT)
    print(all_settings.AUTH.user)
    print(all_settings.FUXI)

    print(part_settings.HOST)
    print(part_settings.PORT)
    print(part_settings.AUTH.user)
    print(part_settings.FUXI)
