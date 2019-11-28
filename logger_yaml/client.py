import yaml
import logging
import logging.config
from jinja2 import Template


if __name__ == '__main__':
    with open("logger.yaml", 'r') as f:
        template = Template(f.read())
        c = template.render(app='test')
        LOG = yaml.load(c)
    print(LOG)
    logging.config.dictConfig(LOG)

    logger = logging.getLogger('test')
    logger.debug("Debug 伏羲伏羲")
    logger.info("Info 伏羲伏羲")
    logger.warning("warn, 伏羲伏羲")
    logger.error("error 伏羲伏羲")
    logger.critical("critical 伏羲伏羲")

    rlease_logger = logging.getLogger('rlease')
    rlease_logger.debug("Debug 伏羲伏羲, rlease")
    rlease_logger.info("Info 伏羲伏羲, rlease")
    rlease_logger.warning("warn, 伏羲伏羲, rlease")
    rlease_logger.error("error 伏羲伏羲, rlease")
    rlease_logger.critical("critical 伏羲伏羲, rlease")
