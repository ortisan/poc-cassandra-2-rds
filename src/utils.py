
import boto3
from botocore.exceptions import ClientError
client = boto3.client('cloudformation')

def stack_exists(name):
    try:
        data = client.describe_stacks(StackName = name)
    except ClientError:
        return False
    return data['Stacks'][0]['StackStatus'] != "DELETED"

def create_or_update_stack(name, template_body):
    if stack_exists(name):
        response = client.update_stack(StackName=name, TemplateBody=template_body)
        try:
            waiter = client.get_waiter('stack_update_complete')
            waiter.wait(
                StackName=name,
                NextToken='pagination',
                WaiterConfig={
                    'Delay': 10,
                    'MaxAttempts': 120
                }
            )
        except ClientError as exc:
            print(exc)
    else:        
        response = client.create_stack(StackName=name, TemplateBody=template_body, TimeoutInMinutes=10, OnFailure='DELETE')
        try:
            waiter = client.get_waiter('stack_create_complete')
            waiter.wait(
                StackName=name,
                NextToken='pagination',
                WaiterConfig={
                    'Delay': 10,
                    'MaxAttempts': 120
                }
            )
        except ClientError as exc:
            print(exc)