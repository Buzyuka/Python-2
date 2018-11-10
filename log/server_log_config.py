import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('app.main')

formatter = logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s")

fh = logging.FileHandler("server.log", encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)

logger.addHandler(console)

rotating = TimedRotatingFileHandler("server.log", "D", 1)
rotating.setLevel(logging.DEBUG)
rotating.setFormatter(formatter)

logger.addHandler(rotating)
