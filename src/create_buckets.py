import yaml
from utils import create_or_update_stack

STACK_NAME = 'migration-buckets-stack'

if __name__ == "__main__":    
    
    botocore.errorfactory.AlreadyExistsException
    
    with open('aws/cloudformations/buckets.yml') as f:        
        template_body = f.read()
        create_or_update_stack(STACK_NAME, template_body)