import os.path
import sys
from host_list import list
from exclude import ex_list


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText# Email variables
import smtplib
fromaddr = "d.ansong@ucl.ac.uk"
toaddr = ["d.ansong@ucl.ac.uk"]
server = smtplib.SMTP('smtp-server.ucl.ac.uk', 587)
m_hosts =[] 


def check_Hosts():

    #remove exludeded hosts from original host list
    for element in ex_list:
        #print(element)
        if element in list:
            list.remove(element)
    
     
    # open Nornir hostfile
    with open ('hosts.yaml') as host_file:
        hf = host_file.read()
        # check if hostfile entries exit in nornir hosts
        for x in list:
            if x not in hf:
                #print(x)
                m_hosts.append(x)
        No_list = len(list)
        No_m_hosts = len(m_hosts)
        print(m_hosts)
        print('There are {} devices that are in the ucl host file'.format(No_list))
        print('There are {} devices that are not in Nornir Host list'.format(No_m_hosts))
        return m_hosts
        
def send_mail(m_hosts):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = ",".join(toaddr)
    msg['Subject'] = 'Missing Host From '
    body = str(m_hosts)
    print(m_hosts)
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

def main():
    m_hosts = check_Hosts()
    send_mail(m_hosts)
    


if __name__ == '__main__':
    main()


