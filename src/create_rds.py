import yaml
from utils import create_or_update_stack

STACK_NAME = 'migration-rds-stack'

if __name__ == "__main__":    
    with open('aws/cloudformations/rds_database.yml') as f:        
        template_body = f.read()
        create_or_update_stack(STACK_NAME, template_body)
        