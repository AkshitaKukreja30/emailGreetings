import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

from template import html

# msg = email.message.Message()
# msg = MIMEMultipart('alternative')
msg = MIMEMultipart("related")
msg['Subject'] = 'Test'
msg['From'] = 'akshita.kukreja@cygrp.com'
msg['To'] = 'kukrejaakshita@gmail.com'
# msg.add_header('Content-Type','text/html')

html = html.replace("[NAME]","XYZ")
html = html.replace("[GREETING]","Happy Birthday")
html = html.replace("[CUSTOMISED_TEXT]","kuch bhi daal dete hai")

print(type(html))
print(html)
# Record the MIME types of both parts - text/plain and text/html.
# part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
fp = open('happyBirthday.jpeg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
msg.attach(part2)
msgImage.add_header('Content-ID', '<image1>')
msgImage.add_header("Content-Disposition", "inline", filename="myimage") 
msg.attach(msgImage)


# msg.set_payload('<html><head><style>table{font-family:arial,sans-serif;border-collapse:collapse;width:100%;}td,th{border:1pxsolid#dddddd;text-align:left;padding:8px;}tr:nth-child(even){background-color:#dddddd;}</style></head><body><h2>HTMLTable</h2><table><tr><th>Company</th><th>Contact</th><th>Country</th></tr><tr><td>AlfredsFutterkiste</td><td>MariaAnders</td><td>Germany</td></tr><tr><td>CentrocomercialMoctezuma</td><td>FranciscoChang</td><td>Mexico</td></tr><tr><td>ErnstHandel</td><td>RolandMendel</td><td>Austria</td></tr><tr><td>IslandTrading</td><td>HelenBennett</td><td>UK</td></tr><tr><td>LaughingBacchusWinecellars</td><td>YoshiTannamuri</td><td>Canada</td></tr><tr><td>MagazziniAlimentariRiuniti</td><td>GiovanniRovelli</td><td>Italy</td></tr></table></body></html>')

# Send the message via local SMTP server.
# s = smtplib.SMTP('')
finalBody = msg.as_string()
# print(finalBody)

s = smtplib.SMTP('smtp.office365.com', 587)
s.starttls()
s.login('akshita.kukreja@cygrp.com','Twist@2020')
s.sendmail(msg['From'], [msg['To']], finalBody)
s.quit()