import feedparser
from datetime import datetime
d = feedparser.parse('http://feeds.feedburner.com/wondermark')
wondermarktitle = d.entries[0].title
wondermarktitle = wondermarktitle.encode("utf-8")
wondermarktitle = wondermarktitle[0]

if wondermarktitle == '#':
	s = d.entries[0].published
	s = s[0:24]
	updateforWMtime = datetime.strptime(s, '%a, %d %b %Y %H:%M:%S')
	updateforWM = updateforWMtime.strftime('%m/%d/%Y')
else:
		s = d.entries[1].published
		s = s[0:24]
		updateforWMtime = datetime.strptime(s, '%a, %d %b %Y %H:%M:%S')
		updateforWM = updateforWMtime.strftime('%m/%d/%Y')
