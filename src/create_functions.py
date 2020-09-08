import boto3
import yaml

if __name__ == "__main__":
    client = boto3.client('cloudformation')
    with open('aws/cloudformations/lambda_rds_tables.yml') as f:        
        contents = f.read()
        response = client.create_stack(StackName='lambdas-stack', TemplateBody=contents, TimeoutInMinutes=10, OnFailure='DELETE')
