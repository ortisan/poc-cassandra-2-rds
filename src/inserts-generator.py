import uuid

QTD_REGISTERS = int(1e6) # 10 bi

if __name__ == "__main__":
    with open('data/person-in.csv', 'w') as csvfile:
        for i in range(1, QTD_REGISTERS):             
            id = str(uuid.uuid4())
            csvfile.write(id + ",VOS,Marianne\n")
            
    

    