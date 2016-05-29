"""
Notes: =========================================================================
Notes: logging module:
Notes:
Notes:      logging.debug
Notes:      logging.info
Notes:      logging.warning
Notes:      logging.error
Notes:      logging.critical
Notes:
Notes:
"""

import logging

# Get to know about module logging content
print "========================================================================"
print "logging Module : start"
print dir(logging)
print "logging Module : end"
print "========================================================================"

logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
