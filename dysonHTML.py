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
page    = urllib.request.urlopen( url )
content = str( page.read( ) , 'utf-8')

# first step : extracting the max number of pages
pns     = content.split( "&pn=" )
nums    = 11
for p in pns[ 2:-1 ]:
    if int( p.split( '">' ) [ 0 ] ) > nums :
        nums = int( p.split( '">' ) [ 0 ] )
print( nums )

pages   = range( 1, nums + 1 , 10 )
print( pages ) 
#second step : for every pages extracting the events id



# third step : for every event id searching the page

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
