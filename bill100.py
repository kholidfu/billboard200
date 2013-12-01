import re
import urllib2
from collections import Counter

def tryint(s):
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


if __name__ == '__main__':
    b = Billboard100Parser()
    print b.get_ids()
