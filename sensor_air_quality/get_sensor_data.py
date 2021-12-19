from sps30 import SPS30
from time import sleep
from retry import retry


@retry(OSError, tries=3, delay=2)
def get_sps30_data(logger):
    sps = SPS30(1)

    sleep(2)

    if sps.read_article_code() == sps.ARTICLE_CODE_ERROR:
        logger.exception("ARTICLE CODE CRC ERROR!")
        raise Exception("ARTICLE CODE CRC ERROR!")
    else:
        logger.info("ARTICLE CODE: " + str(sps.read_article_code()))

    if sps.read_device_serial() == sps.SERIAL_NUMBER_ERROR:
        logger.exception("SERIAL NUMBER CRC ERROR!")
        raise Exception("SERIAL NUMBER CRC ERROR!")
    else:
        logger.info("DEVICE SERIAL: " + str(sps.read_device_serial()))

    sps.start_measurement()

    while not sps.read_data_ready_flag():
        logger.warning("New Measurement is not available!")
        if sps.read_data_ready_flag() == sps.DATA_READY_FLAG_ERROR:
            logger.exception("DATA-READY FLAG CRC ERROR!")
            raise Exception("DATA-READY FLAG CRC ERROR!")

    if sps.read_measured_values() == sps.MEASURED_VALUES_ERROR:
        logger.exception("MEASURED VALUES CRC ERROR!")
        raise Exception("MEASURED VALUES CRC ERROR!")
    else:
        logger.info("PM1.0 Value in µg/m3: " +
                    str(sps.dict_values['pm1p0']))
        logger.info("PM2.5 Value in µg/m3: " +
                    str(sps.dict_values['pm2p5']))
        logger.info("PM4.0 Value in µg/m3: " +
                    str(sps.dict_values['pm4p0']))
        logger.info("PM10.0 Value in µg/m3: " +
                    str(sps.dict_values['pm10p0']))
        #      print ("NC0.5 Value in 1/cm3: " +
        #      str(sps.dict_values['nc0p5']))
        #      print ("NC1.0 Value in 1/cm3: " +
        #      str(sps.dict_values['nc1p0']))
        #      print ("NC2.5 Value in 1/cm3: " +
        #      str(sps.dict_values['nc2p5']))
        #      print ("NC4.0 Value in 1/cm3: " +
        #      str(sps.dict_values['nc4p0']))
        #      print ("NC10.0 Value in 1/cm3: " +
        #      str(sps.dict_values['nc10p0']))
        logger.info("Typical Particle Size in µm: " +
                    str(sps.dict_values['typical']))

    sleep(5)

    sps.stop_measurement()

    # enables fan-cleaning manually for 10 seconds (referred by datasheet)
    sps.start_fan_cleaning()

    return [round(sps.dict_values['pm1p0'], 3),
            round(sps.dict_values['pm2p5'], 3),
            round(sps.dict_values['pm4p0'], 3),
            round(sps.dict_values['pm10p0'], 3),
            round(sps.dict_values['typical'], 3)]
