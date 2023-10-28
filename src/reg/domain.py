from .reg.reg.extra.url_regex_custom import regex

EMAIL_HEAD=['E-mail.','E-MAIL','Email.','MAIL.','Mail.','mailto:','-mail']

EMAIL_REMOVE_END=['css$','png$','jpg$','gif$','example.*$','sample.*$','xxx.*$','aaa.*$','XXX.*$','abc.*$','sentry.*$','CSS$','wixpress.*$','calendar.*$','ico$']
EMAIL_REMOVE_START=['//','abc','mailto:']

'''RFC 5322 Official Standard_https://emailregex.com/'''
EMAIL_REGEX=r'''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''

URL_REGEX_COMPILED=regex

COMMON_DOMAIN=['yahoo.co.jp','gmail.com','softbank.jp','docomo.ne.jp','jcom.home.ne.jp','dion.ne.jp','hotmail.com','nifty.com','outlook.jp','ocn.ne.jp']

HOMEPAGE_HEAD=['https://','http://']

HTTP_TYPO='^[Hh]{1}[TPtp]{3,5}[sS]{0,1}[\.:/]{1,4}|^[Hh]{1}[TPtp]{3,5}[sS]{0,1}'
