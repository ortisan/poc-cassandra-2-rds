import boto3
import yaml

if __name__ == "__main__":
    client = boto3.client('cloudformation')    
    with open('aws/cloudformations/buckets.yml') as f:        
        contents = f.read()
        response = client.create_stack(StackName='migration-buckets', TemplateBody=contents, TimeoutInMinutes=10, OnFailure='DELETE')
        print(response)
        print(dir(response))