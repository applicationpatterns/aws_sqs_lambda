def lambda_handler(event, context):
    """Sample pure Lambda function"""
    print(f'{event=}')
    for record in event['Records']:
        print("test")
        payload = record["body"]
        print(str(payload))
