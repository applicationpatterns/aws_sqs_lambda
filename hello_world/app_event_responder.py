def lambda_handler(event, context):
    """Sample pure Lambda function"""
    print(f'{event=}')
    for record in event['Records']:
        print("processing next message")
        payload = record["body"]
        print(f'{record["body"]=}, {record["messageAttributes"]["line"]["stringValue"]}')
        if record["messageAttributes"]["line"]["stringValue"] == '5':
            print(f'lets pretend something wrong with message 5')
            raise Exception('got error with message 5')
