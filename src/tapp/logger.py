from logging import INFO, basicConfig, getLogger

basicConfig(level=INFO, format="%(asctime)s %(name)s %(levelname)s: %(message)s")
logger = getLogger("likeapp")
