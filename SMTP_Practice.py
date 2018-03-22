from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email.utils import parseaddr, formataddr
from email import encoders
import smtplib
#输入Email地址和口令
from_addr = input('From:')

password = input('Password:')

#输入收件人地址
to_addr = input('To:')

#输入SMTP服务器地址
smtp_server = input('SMTP server:')

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(),addr))

#指定发件人和邮件主题
#MIMEText第一个参数就是邮件正文，第二个参数是MIME的subtype，plain表示纯文本，最后用utf-8保证多语言兼容性
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>','html', 'utf-8')

#邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addr('Python <%s>' % from_addr)
msg['Subject'] = Header('text', 'utf-8').encode()
msg['To'] = _format_addr('磨剑 <%s>' % to_addr)

#邮件正文
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

#添加附件
with open('/Users/lizhengdao/Downloads/test.png', 'rb') as f:
    #设置附件的MIME和文件名，这里是png类型
    mime = MIMEBase('image', 'png', filename = 'test.png')
    #加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    #把附件内容读进来
    mime.set_payload(f.read())
    #用Base64编码
    encoders.encode_base64(mime)
    #添加到MIMEMultipart
    msg.attach(mime)
try:
#通过SMTP发送
    sever = smtplib.SMTP(smtp_server, 25)# SMTP协议默认端口是25
#打印出和SMTP服务器交互的所有信息
    sever.set_debuglevel(1)
#登陆服务器
    sever.login(from_addr, password)
#发邮件
    sever.sendmail(from_addr, [to_addr], msg.as_string())
    sever.quit()
    print('Success!')
except smtplib.SMTPException as e:
    print('Fail,%s' % e)
#weibibia@163.com
#zzz5112530
#740405000@qq.com
#smtp.163.com
