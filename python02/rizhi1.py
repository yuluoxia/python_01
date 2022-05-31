#loguru模块
#可以格式化日志
from loguru import logger
logger.info("hello world")

#输出不同的日志级别： 分别是 debug,info,warning,success,error
logger.debug("这是一条debug(调试)日志")
logger.info("这是一条debug(普通)日志")
logger.warning("这是一条debug(警告)日志")
logger.success("这是一条debug(成功)日志")
logger.error("这是一条debug(错误)日志")
#输出到文件： add()
logger.add("b.log",format="{time} | {level} | {module} | {line} | {message}",level="INFO")
logger.debug("这是一条debug(调试)日志")
logger.info("这是一条debug(普通)日志")
logger.warning("这是一条debug(警告)日志")
logger.success("这是一条debug(成功)日志")
logger.error("这是一条debug(错误)日志")
#进行传入参数的格式化：
logger.error("我的名字叫{}","张三")