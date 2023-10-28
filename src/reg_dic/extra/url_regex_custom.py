from .url_regex import ipv4_re,ipv6_re,host_re
import re

regex = re.compile( 
    r'(?:http|ftp)s?://' # http(s):// or ftp(s)://
    r'(?:\S+(?::\S*)?@)?'  # user:pass authentication 
    r'(?:' + ipv4_re + '|' + ipv6_re + '|' + host_re + ')' # localhost or ip
    r'(?::\d{2,5})?'  # optional port
    r'(?:[/?#][^\s]*)?'  # resource path
    r'\Z', re.IGNORECASE)
