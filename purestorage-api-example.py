#!/usr/bin/env python
'''
Doc
http://pythonhosted.org/purestorage/api.html#module-purestorage
Blog:
http://www.purestorage.com/blog/pure-storage-rest-client-and-python-library/

Testing:
script <Purestorage IP> <username> <password>
'''

import sys, purestorage, traceback

# Disable unverified HTTPS request warning(s)
import urllib3
urllib3.disable_warnings()

purestorage_conf = {
  'ip':       sys.argv[1],
  'username':  sys.argv[2],
  'password': sys.argv[3],
}

try:
    array = purestorage.FlashArray(purestorage_conf['ip'], purestorage_conf['username'], purestorage_conf['password'])
except Exception as e:
    for line in traceback.format_exception(*sys.exc_info()):
         print line.strip()
    sys.exit(1)

# list hosts
try:
    for host in array.list_hosts():
        print host
except Exception as e:
    for line in traceback.format_exception(*sys.exc_info()):
         print line.strip()
    sys.exit(1)

# list volumes
try:
    for volume in array.list_volumes():
        print volume
except Exception as e:
    for line in traceback.format_exception(*sys.exc_info()):
         print line.strip()
    sys.exit(1)
    
# logout
array.invalidate_cookie()