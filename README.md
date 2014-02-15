PyMPOS
======

PyMPOS - A Python command-line utility to pull information from any [php-MPOS](https://github.com/MPOS/php-mpos) site.
Currently only implements the getuserbalance end point.

How to install:
1) Clone this repository
2) python setup.py install
3) Create ~/.pympos and use/modify this template:
```bash
[pympos]
apikey=<api key>
server=<domain>
```

Example:

```bash
[pympos]
apikey=abcdefghijklmnopqrstuvwxyz1234567890
server=pool.dogechain.info
```

Coming soon - availability in PyPi!