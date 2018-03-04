import logging


log = logging.getLogger('3rd-party')


def do_3rd_party_thing():
    log.debug(1)
    log.info(2)
    log.warning(3)
    log.error(4)
