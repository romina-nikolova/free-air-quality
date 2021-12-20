import os
import logging


if __name__ == "__main__":
    logging.basicConfig(filename='main.log',
                        level=logging.INFO,
                        format='%(asctime)s:Line no-%(lineno)d:%(message)s')

    logger = logging.getLogger(__name__)

    logger.info(""" Generating template environment variables... """)
    os.system("python generate_template_variables.py")
    logger.info(""" Template environment variables generated. """)

    logger.info(""" Creating bit.io tables... """)
    os.system("python 1_bitdotio/create_bitdotio_tables.py")
    logger.info(""" bit.io tables created. """)
