import boto3
from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/template/create', methods =['POST'])
def create_template():
    ses = boto3.client('ses')
    json_data = request.get_json(force=True)
    response = ses.create_template(
    Template = {
        'TemplateName' : json_data['TemplateName'],
        'SubjectPart'  : json_data['SubjectPart'],
        'TextPart'     : json_data['TextPart'],
        'HtmlPart'     : json_data['HtmlPart']
        }
    )

    print(response)
    return jsonify(response)

@app.route('/send/email', methods=['POST'])
def sendEmail():
    ses = boto3.client('ses')
    json_data = request.get_json(force=True)
    print(json_data)
    response = ses.send_email(
    Source = json_data['sourceEmail'],
     Destination={
        'ToAddresses': json_data['emailTo'],
        'CcAddresses': json_data['cc'],
        'BccAddresses': json_data['bcc']
     },
     ReplyToAddresses=[ ],
     Message={
         'Subject': {
            'Data': json_data['subjectData'],
            'Charset': 'UTF-8'
        },
        'Body': {
            'Text': {
                'Data': json_data['body'],
                'Charset': 'UTF-8'
            },
            'Html': {
                'Data': json_data['htmlData'],
                'Charset': 'UTF-8'
            }
        }
     }
    )

    print(response)
    return jsonify(response)


@app.route('/send/rawemail', methods=['POST'])
def sendRawEmail():
    ses = boto3.client('ses')
    json_data = request.get_json(force=True)
    response = ses.send_raw_email(
     Destinations= json_data['emailTo'],
     RawMessage={
        'Data': json_data['rawData'],
    }
    )
    print(response)
    return jsonify(response)

def sendTemplateEmail(source_email, email_to, cc, bcc, template_name, TemplateData):
    ses = boto3.client('ses')
    response = ses.send_templated_email(
    Source=source_email,
    Destination={
        'ToAddresses': email_to
    },
    ReplyToAddresses=[],
    ReturnPath='',
    SourceArn='',
    ReturnPathArn='',
    Tags=[
        {
            'Name': '',
            'Value': ''
        },
    ],
    ConfigurationSetName='',
    Template=template_name,
    TemplateArn='',
    TemplateData=TemplateData
    )

    print(response)
    return response




    # source_email="email@nimasratna.click"
    # email_to=['nimas.sari@metranet.co.id']
    # cc=[]
    # template_name='TEST_TEMPLATE'
    # sendEmail(source_email, email_to, cc, template_name)
    #create_template()

if __name__ == '__main__':
    app.run(debug=True)
    
