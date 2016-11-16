#!/usr/bin/env python2.7
import smtplib, string, subprocess, argparse

parser = argparse.ArgumentParser()
parser.add_argument("username", help=" [string] echo the string you use here")
parser.add_argument("password", help=" [string] echo the string you use here")
parser.add_argument("toAddress", help=" [string] echo the string you use here")
parser.add_argument("fromAddress", help=" [string] echo the string you use here")
parser.add_argument("server", help=" [string] echo the string you use here")
parser.add_argument("--port", help=" [int] echo the string you use here", default="587")
args = parser.parse_args()

#raspberrypi@reish.net raspberrypi raspberrypi@reish.net raspberrypi@reish.net host2.cubicle43.com 587

# Settings
fromaddr = args.fromAddress
toaddr = args.toAddress

# Googlemail login details
username = args.username
password = args.password

output_if = subprocess.Popen(['ifconfig'], stdout=subprocess.PIPE).communicate()[0]
output_cpu = open('/proc/cpuinfo', 'r').read()

BODY = string.join((
"From: %s" % fromaddr,
"To: %s" % toaddr,
"Subject: Your RasPi just booted",
"",
output_if,
output_cpu,
), "\r\n")

# send the email
server = smtplib.SMTP(args.server + ":" + args.port)
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, BODY)
server.quit()