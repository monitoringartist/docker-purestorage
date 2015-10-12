Docker image for Purestorage API
================================

Python Pure Storage API. [Docker Image](https://hub.docker.com/r/monitoringartist/docker-purestorage/)
[![](https://badge.imagelayers.io/monitoringartist/docker-purestorage:latest.svg)](https://imagelayers.io/?images=monitoringartist/docker-purestorage:latest 'Get your own badge on imagelayers.io')

Typical usage:

```
# ls 
purestorage-api-example.py
# docker run --rm -v  $(pwd):/pure -ti pure python /pure/purestorage-api-example.py \
<pure_storage_ip> <pure_storage_username> '<pure_storage_password>'
```

References
==========

- http://pythonhosted.org//purestorage/quick_start.html
- http://pythonhosted.org/purestorage/api.html
- http://www.purestorage.com/blog/pure-storage-rest-client-and-python-library/

Author
======

[Devops Monitoring zExpert](http://www.jangaraj.com), who loves monitoring 
systems, which start with letter Z. Those are Zabbix and Zenoss.

Professional monitoring services:

[![Monitoring Artist]
(http://monitoringartist.com/img/github-monitoring-artist-logo.jpg)]
(http://www.monitoringartist.com)
