Sentimental Times
============

Our visualization tracks the sentiment of some newspapers towards the Presidential 
candidates from the time-period starting just after the first debate and
just before the election night. 

Team
====

Morgan - Hacker and developer - Python scripting to scrape newspaper sites 
and interact with NYTimes and NPR  APIs to get relevant article URLs 
formatted in JSON for Sentiment Analysis API calls.
Manually made JSON data for all SF Gate articles since there is no API available
Tried unsuccessfully to use Google Custom Search API to scrape various newspapers

Bharathkumar Gunasekaran - Hacker & Developer - Researched various sentiment 
analysis tools; implemented sentiment analysis for all articles with "Alchemy API".
Formatted data to be CSV for use in D3 visualization

Chan Kim - Hacker & Designer - Created javascript visualization that graphs 
Presidential candidate sentiment in various newspapers in the weeks before 
the election with special reference to the debates.
Also created the HTML/CSS front-end of the site.

Technologies
============
	Python
	HTML/CSS
	Javascript
	D3
    Alchemy API
	NT TImes API
	NPR API
    Google Search API

Deploying
=========

Live URL - http://people.ischool.berkeley.edu/~chan/iolab/sentiment_times/
GIT Repo : https://github.com/morganwallace1/IOLab-Project-3

Testing
=======================
We tested on Chrome and Firefox

Quirks and known issues
=======================

1. When there are multiple articles on a particular day, we tried to average the
scores and have a single score for the day. But due to time constraints, we 
were ont able to implement this



