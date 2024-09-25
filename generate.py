from faker import Faker
import csv
faker = Faker("ar_SA")
data =[]
keys = ['name', 'job', 'phone','email', 'country', 'salary']


def create_file(file, rows):
    with open(file, 'w') as f:
        w = csv.DictWriter(f, fieldnames= keys)
        w.writeheader()
        for row in range(int(rows)):
            for row in range(int(rows)):
                list_data = {}
                list_data['name']= faker.name()
                list_data['job']= faker.job()
                list_data['phone']= faker.phone_number()
                list_data['email']= faker.free_email()
                list_data['country']= faker.country()
                list_data['salary']= faker.random_int(min=300000, max=15000000)
                
                data.append(list_data)
            
        w.writerows(data)
            
            
    

name = input("Enter the name of the file: ")
row = input("Enter the number of rows: ")
create_file(name, row)
        