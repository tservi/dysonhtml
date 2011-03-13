#!/usr/bin/env python
# coding=UTF-8

# python 3
# this is a real python 3 project, take care!

import urllib.request, urllib.parse, urllib.error
from email.mime.text import MIMEText
import smtplib
import sys, socket
import datetime




now              = datetime.datetime.today()
#print( now )
day     =   "{0}".format( now.strftime( "%d" ) )
month   =   "{0}".format( now.strftime( "%m" ) ) 
#print( day + ' - ' + month )
url     = 'http://www.myswitzerland.com/fr/event_calendar/event_results.cfm?e_day=' + day + '&&zeitraum=30&e_month=' + month
url     = 'http://www.myswitzerland.com/fr/event_calendar/event_results.cfm?e_day=' + day + '&region=013&zeitraum=1&e_month=' + month
page    = urllib.request.urlopen( url )
content = str( page.read( ) , 'utf-8')

# first step : extracting the max number of pages
pns     = content.split( "&pn=" )
nums    = 11
for p in pns[ 1:-1 ]:
    if int( p.split( '">' ) [ 0 ] ) > nums :
        nums = int( p.split( '">' ) [ 0 ] )
print( "Number of events for this month : " + str( nums )  )

#second step : for every pages extracting the events id
pages   = range( 1, nums + 1 , 10 )
#print( str( pages ) )
eventids = []
url += "&pn="
for p in pages:
    print( "Extracting events id on the page " + str( p ) + ": " )
    page    = urllib.request.urlopen( url + str( p ) )
    content = str( page.read() , 'utf-8' )
    parts   = content.split( 'event_display_int.cfm?event_id=' )
    for p in parts[ 1 : -1 ]:
        eventid = p.split( '"')[ 0 ]
        if eventid not in eventids:
            eventids.append( eventid ) 
            print( "   -> Event id : " + eventid )
        
# third step : for every event id searching the page
def reset_myEvent() :
    return { 'event_id' : '' ,
            'title_fr' : '' ,
            'title_de' : '' ,
            'title_it' : '' ,
            'title_en' : '' ,
            'description_fr' : '' ,
            'description_de' : '' ,
            'description_it' : '' ,
            'description_en' : '' ,
            'date_from' : '' ,
            'date_to' : '' ,
            'time_from' : '' ,
            'time_to' : '' ,
            'additionnal_info_fr' : '' ,
            'additionnal_info_de' : '' ,
            'additionnal_info_it' : '' ,
            'additionnal_info_en' : '' ,
            'locality' : '',
            'street' : '' ,
            'address_info' : '' ,
            'price_from' : '' ,
            'price_to' : '' ,
            'phone' : '',
            'fax' : '' ,
            'url' : '' ,
            'email' : '' ,
            'yearly' : '' ,
            'picture_url' : '' ,
            'fk_category' : '' ,
            }
myEvents = []
url = 'http://www.myswitzerland.com/fr/event_calendar/event_display_int.cfm?event_id='
for e in eventids:
    print( "Extracting event id : " + e )
    page    = urllib.request.urlopen( url + e )
    content = str( page.read(), 'utf-8' )
    myE     = reset_myEvent()
    myE[ 'event_id' ] = e
    myE[ 'title_fr' ] = content.split( '<h1>' )[ 1 ] . split(' </h1' )[ 0 ] 
    #myE[ 'locality' ] = content.split( '<h2>' )[ 1 ] . split(' </h2' )[ 0 ]
    myEvents.append( myE )

print( myEvents )
dyson = """
**********************************************************************

        dd   y         y   ssssssss     ooooooo       n        n 
        dd    y       y    s           o       o      nn       n
        dd     y    y      s          o         o     n  n     n 
     ddddd      yyy        ssssssss   o         o     n    n   n
     dd dd       y                s   o         o     n      n n
     dd dd       y                s    o       o      n        n
     ddddd       y         ssssssss     ooooooo       n        n   
 
*********************************************************************
 """
print ( dyson )
chars = str( input( "Appuyez sur enter pour quitter le programme!") )
print( "" )
