import csv

class Customer():
    def __init__(self, cust_id, fName, lName, company, address, city, state, zip):
        self.cust_id = cust_id
        self.first_name = fName
        self.last_name = lName
        self.company_name = company
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        str = ""
        if (self.company_name == ""):
            str + self.first_name + " " + self.last_name + "\n" + self.address + "\n" + self.city + ", " + self.state + " " + self.zip
        else:
            str + self.first_name + " " + self.last_name + "\n" + self.company_name + "\n" + self.address + "\n" + self.city + ", " + self.state + " " + self.zip
        return str

customerList = []
with open('customers.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        customerList.append(Customer(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

def main():
    customerList.pop(0)
    print("Custommer Viewer\n")
    while True:
        id = input("Enter customer ID: ")
        flag = 0
        for Customer in customerList:
            if(Customer.cust_id == id):
                print()
                print(Customer)
                print()
                flag - 1
                break
        if (flag == 0):
            print("No custommer with that ID\n")
        choice = input("Continue? (y/n): ").lower()
        if choice == "n":
            break

if(__name__ == "__main__"):
    main()