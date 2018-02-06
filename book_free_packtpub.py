#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import time
from bs4 import BeautifulSoup

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

hour_start= time.time()
print 'Start script: ',time.ctime(hour_start), '\n'


site_url = urllib2.urlopen("https://www.packtpub.com/packt/offers/free-learning")

source_code = BeautifulSoup(site_url)

name_book = source_code.find('div', class_="dotd-title").text

#Send Email
fromaddr = "send email"
recipients = "destination email" #[email1, email2]
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = ", ".join(recipients)
msg['Subject'] = "Free Book Packtpub"
 
body = "The book free today is: " + name_book + '\n' + "Download: https://www.packtpub.com/packt/offers/free-learning"

msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "your password")
text = msg.as_string()
server.sendmail(fromaddr, recipients, text)
server.quit()
