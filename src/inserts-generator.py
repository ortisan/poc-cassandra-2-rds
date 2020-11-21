import uuid
import random

ROWS = int(100)

if __name__ == "__main__":
    with open('data/cassandra/person-in.csv', 'w') as csvfile:
        for i in range(0, ROWS):
            id = str(uuid.uuid4())
            id2 = str(uuid.uuid4())
            random_number = random.randint(0, 10)
            if random_number < 3:
                csvfile.write(id + ",VOS,Marianne,\"[{id: "+ id + ", phone_number: 123456}, {id: "+ id2 + ", phone_number: 123456, description: 'Smartphone', creation_date: '2018-04-26 05:59:38'}]\"\n")
            else:
                csvfile.write(id + ",VOS,Marianne,\"[{id: "+ id + ", phone_number: 123456}, {id: "+ id2 + ", phone_number: 123456, creation_date: '2018-04-26 05:59:38'}]\"\n")
