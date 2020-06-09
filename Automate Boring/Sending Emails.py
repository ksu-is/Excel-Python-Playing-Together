#Sending Emails
#this does not work properly
import smtplib

conn=smtplib.SMTP('smtp.comcast.net', '993')
type(conn)
conn
conn.ehlo()
conn.starttls()
conn.login('doug.03@comcast.net', 'Kat49ers')
conn.sendmail('doug.03@comcast.net', 'doug.03@comcast.net', 'Subject: so long... \n\nDear Doug,\nSo long and thanks for all the fiash\n\n- Doug')
conn.quit
