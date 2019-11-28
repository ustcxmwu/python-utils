import logging

# 生成日志实例，日志器
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('test')
# 基本单元的配置(LEVER)
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 生成管道分支，处理器
handler_1 = logging.FileHandler(filename='log.txt', encoding='utf-8')
handler_2 = logging.StreamHandler()

# 自定义格式，格式器
fmt1 = logging.Formatter(fmt='%(asctime)s.%(msecs)03d-%(name)s-%(levelname)s-%(message)s',
                         datefmt="%Y-%m-%d %X")
fmt2 = logging.Formatter(fmt='%(asctime)s.%(msecs)03d-%(name)s-%(levelname)s-%(message)s', datefmt="%X")
handler_1.setFormatter(fmt1)
handler_2.setFormatter(fmt2)

# 对接分支管道与源头，处理器
logger.addHandler(handler_1)
logger.addHandler(handler_2)

# 层级结构，logger的名称是一个以'.'分割的层级结构，每个'.'后面的logger都是'.'前面的logger的children，通常配合过滤器一起使用
# 过滤器

rotate_file_handler = RotatingFileHandler('rotate.log', mode='a', maxBytes=5 * 1024 * 1024, backupCount=2,
                                          encoding=None, delay=0)
rotate_file_handler.setFormatter(fmt2)
rotate_file_handler.setLevel(logging.INFO)

app_log = logging.getLogger('root')
app_log.setLevel(logging.INFO)

app_log.addHandler(rotate_file_handler)

# 开始记录
if __name__ == '__main__':
    logger.debug("芹泽多摩雄")
    logger.info("真")
    logger.warning("男")
    logger.error("人")
    logger.critical("！")
    while True:
        app_log.info('rotate')
