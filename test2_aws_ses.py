import boto3


def create_template():
    ses = boto3.client('ses')
    response = ses.create_template(
    Template = {
        'TemplateName' : 'TEST_TEMPLATE',
        'SubjectPart'  : 'TEST Email AWS SES',
        'TextPart'     : 'this in your OTP Code: 7393',
        'HtmlPart'     : ''
    }
    )

    print(response)



def sendEmail(source_email, email_to, cc, template_name):
    ses = boto3.client('ses')
    response = ses.send_templated_email(
    Source = source_email,
     Destination={
        'ToAddresses': email_to,
        'CcAddresses': cc
     },
     ReplyToAddresses=[ ],
    Template= template_name,
    TemplateData='{}'
    )

    print(response)



def main():
    source_email="email@nimasratna.click"
    email_to=['nimas.sari@metranet.co.id']
    cc=[]
    template_name='Test_template_3'
    sendEmail(source_email, email_to, cc, template_name)


main()
