import boto3

def sendTemplateEmail(source_email, email_to, cc, bcc, template_name):
    ses = boto3.client('ses')
    response = ses.send_templated_email(
    Source=source_email,
    Destination={
        'ToAddresses': email_to,
        'CcAddresses': cc
    },
    ReplyToAddresses=[],
    Template=template_name,
    TemplateData='{}'
    )

    print(response)
    return response

def main():
    source_email="email@nimasratna.click"
    email_to=['nimas.sari@metranet.co.id']
    cc=[]
    bcc=[]
    template_name='Test_template_3'
    sendTemplateEmail(source_email, email_to, cc, bcc, template_name)


main()