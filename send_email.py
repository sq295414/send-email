import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
from conf import *

'''
from_addr = '18838939163@163.com' # 发件人邮箱
password = 'sbm201111' # 这里是授权码，并非邮箱密码
smtp_server = 'smtp.163.com' # smtp 服务器地址
to_addr = '1351718272@qq.com' # 收件人邮箱
'''
def send_email(title, content):
	msg = MIMEText(content, 'plain', 'utf-8')
	msg['From'] = '{}'.format(email_dict['from_addr'])
	msg['To'] = email_dict['to_addr']
	msg['Subject'] = title

	server = smtplib.SMTP_SSL(email_dict['smtp_server'], 465) # SSL端口465
	server.set_debuglevel(1)
	server.login(email_dict['from_addr'], email_dict['password'])
	server.sendmail(email_dict['from_addr'], [email_dict['to_addr']], msg.as_string())
	server.quit()

if __name__ == '__main__':
	domain = 'test.fr'
	send_email(domain + ' | ' + time.strftime("%Y-%m-%d %H:%M:%S"),domain + ' registered.')	