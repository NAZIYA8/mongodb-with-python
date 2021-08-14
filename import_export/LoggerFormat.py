import logging

logger = logging
   
logger.basicConfig(filename='importexport.log', level=logging.INFO,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')
logger.basicConfig(filename='importexport.log', level=logging.ERROR,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineno)d')