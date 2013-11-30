# -*- coding: utf-8 -*-
import alfred
import urllib2
import json


def main(stats=False):
    status = json.load(urllib2.urlopen('http://kaffe.abakus.no/api/status'))['coffee']
    item = alfred.Item(
        uid='abakaffe',
        arg="",
        title=u'Kaffetrakteren er %s' % (u'på' if status['status'] else u'av'),
        subtitle=u'Sist skrudd på %s' % status['last_start'],
        valid=False,
        icon='icon.png'
    )
    return alfred.render([item])

if __name__ == "__main__":
    print main()
