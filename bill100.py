#!/usr/bin/python
import json
import re
import urllib2
from collections import Counter

def tryint(s):
    """Human sorting by nedbat.
    http://nedbatchelder.com/blog/200712/human_sorting.html"""
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    return [tryint(i) for i in re.findall(r"[0-9][0-9]?[0-9]?$", s)]

class Billboard100Parser(object):

    def __init__(self):
        self.url = 'http://www.youtube.com/playlist?list=PL55713C70BA91BD6E'

    def get_html(self):
        html = urllib2.urlopen(self.url).read()
        return html

    def get_titles(self):
        data = self.get_html()
        pattern = re.compile(r"ltr\">(.*?)</span>")
        found = re.findall(pattern, data)
        return found

    def get_videos(self):
        pattern = r"watch.*index=\d[1-9]?[0-9]?[0-9]?"
        found = re.findall(re.compile(pattern), self.get_html())[1:]
        results = Counter(found)
        # sort the results using natural sorts
        results = sorted(results, key=alphanum_key)
        return results

    def get_ids(self):
        #pattern = r"v=(.*?)&"
        found = [re.search(r"v=(.*?)&", i).group(1) for i in self.get_videos()]
        return found

    def to_json(self):
        data = {'results': []}
        for i in zip(self.get_titles(), self.get_ids()):
            data['results'].append({'title': i[0], 'id': i[1]})
        return data


if __name__ == '__main__':
    b = Billboard100Parser()
    for i in b.to_json()['results']:
        print i['title']
        print i['id']
        print "========================"
