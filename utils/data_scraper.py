import lxml.html
from lxml.cssselect import CSSSelector

import requests

def scrape(url):
    r = requests.get(url)

    # build the DOM Tree
    tree = lxml.html.fromstring(r.text)

    # print the parsed DOM Tree
    #print lxml.html.tostring(tree)
    
    # construct a CSS Selector
    sel = CSSSelector('p')

    # Apply the selector to the DOM tree.
    results = sel(tree)

    '''
    Kelly's Hard Work <3
    #print match.text
    for num in range (0, len(results)):
        match = results[num]
        
        #if there are links in the result, it won't scrape properly.
        if "href=" in lxml.html.tostring(match):
            index1 = lxml.html.tostring(match).index('<a href=')
            index2 = lxml.html.tostring(match).index('</a>')
            a = lxml.html.tostring(match)[index1+1:index2+1].index('>')
            b = lxml.html.tostring(match)[index1+1:index2+1].index('<')
            #stuff before the link + stuff inside the link + stuff after the link
            result = lxml.html.tostring(match)[0:index1] + lxml.html.tostring(match)[index1+2:index2][a:b] + lxml.html.tostring(match)[index2:-1]
            results[num] = lxml.html.fromstring(result)
    '''
            
    # get the text out of all the results
    data = []
    for result in results:
        data.append(result.text_content())
    #returns a list of text
    return data

def convert(txt):
    try:
        return lxml.html.fromstring(txt).text
    except:
        return ""

#print convert("&#8220;Life Inside Out&#8221; chronicles a mother-son musical partnership that grows from a family&#8217;s financial hardships.")
#print scrape('https://www.nytimes.com/2017/11/21/movies/coco-review-pixar-disney.html?rref=collection%2Fcollection%2Fmovie-guide&action=click&contentCollection=undefined&region=stream&module=stream_unit&version=latest-stories&contentPlacement=8&pgtype=collection&_r=0')
