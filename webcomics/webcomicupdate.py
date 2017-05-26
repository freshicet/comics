import feedparser
from datetime import datetime
from django.utils.dateparse import parse_datetime

d = feedparser.parse('http://flakypastry.runningwithpencils.com/flakypastryrss.xml')
updateforFPtime = datetime.strptime(d.modified, '%a, %d %b %Y %H:%M:%S %Z')
updateforFP = updateforFPtime.strftime('%m/%d/%Y')

d = feedparser.parse('http://theawkwardyeti.com/comic/feed/')
updateforTAYtime = datetime.strptime(d.modified, '%a, %d %b %Y %H:%M:%S %Z')
updateforTAY = updateforTAYtime.strftime('%m/%d/%Y')

d = feedparser.parse('http://www.girlgeniusonline.com/ggmain.rss')
s = d.entries[0].published
s = s[0:24]
updateforGGtime = datetime.strptime(s, '%a, %d %b %Y %H:%M:%S')
updateforGG = updateforGGtime.strftime('%m/%d/%Y')


d = feedparser.parse('http://www.lackadaisycats.com/rss/')
updateforLADtime = datetime.strptime(d.entries[0].published,'%dth %B, %Y')
updateforLAD = updateforLADtime.strftime('%m/%d/%Y')


d = feedparser.parse('http://megatokyo.com/rss/')
updateforMTtime = datetime.strptime(d.modified, '%a, %d %b %Y %H:%M:%S %Z')
updateforMT = updateforMTtime.strftime('%m/%d/%Y')



d = feedparser.parse('http://www.quantumvibe.com/qvrss')
s = d.entries[0].published
s = s[0:24]
updateforQVtime = datetime.strptime(s, '%a, %d %b %Y %H:%M:%S')
updateforQV = updateforQVtime.strftime('%m/%d/%Y')

d = feedparser.parse('http://feeds.feedburner.com/sandraandwoo')
s = d.entries[0].published
s = s[0:24]
updateforSAWtime = datetime.strptime(s, '%a, %d %b %Y %H:%M:%S')
updateforSAW = updateforSAWtime.strftime('%m/%d/%Y')

d = feedparser.parse('https://xkcd.com/rss.xml')
s = d.entries[0].published
s = s[0:24]
updateforxkcdtime = datetime.strptime(s, '%a, %d %b %Y %H:%M:%S')
updateforxkcd = updateforxkcdtime.strftime('%m/%d/%Y')


d = feedparser.parse('http://www.qwantz.com/rssfeed.php')
s = d.entries[0].published
s = s[0:24]
updateforD_Ctime = datetime.strptime(s, '%a, %d %b %Y %H:%M:%S')
updateforD_C = updateforD_Ctime.strftime('%m/%d/%Y')


d = feedparser.parse('http://feeds.feedburner.com/buttersafe')
s = d.entries[0].published
s = s[0:24]
updateforBStime = datetime.strptime(s, '%a, %d %b %Y %H:%M:%S')
updateforBS = updateforBStime.strftime('%m/%d/%Y')


d = feedparser.parse('http://pbfcomics.com/feed/')
s = d.entries[0].published
s = s[0:24]
updateforpbftime = datetime.strptime(s, '%a, %d %b %Y %H:%M:%S')
updateforpbf = updateforD_Ctime.strftime('%m/%d/%Y')


d = feedparser.parse('http://cardboard-crack.com/rss')
s = d.entries[0].published
s = s[0:24]
updateforCCtime = datetime.strptime(s, '%a, %d %b %Y %H:%M:%S')
updateforCC = updateforCCtime.strftime('%m/%d/%Y')

d = feedparser.parse('http://abominable.cc/rss')
s = d.entries[0].published
s = s[0:24]
updateforTAtime = datetime.strptime(s, '%a, %d %b %Y %H:%M:%S')
updateforTA = updateforTAtime.strftime('%m/%d/%Y')

d = feedparser.parse('http://www.smbc-comics.com/rss.php')
s = d.entries[0].published
s = s[0:24]
updateforSMBCtime = datetime.strptime(s, '%a, %d %b %Y %H:%M:%S')
updateforSMBC = updateforSMBCtime.strftime('%m/%d/%Y')

d = feedparser.parse('http://axecop.com/feed/')
s = d.entries[0].published
s = s[0:24]
updateforACtime = datetime.strptime(s, '%a, %d %b %Y %H:%M:%S')
updateforAC = updateforACtime.strftime('%m/%d/%Y')