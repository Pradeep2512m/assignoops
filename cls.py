class bike:
    def __init__(self, model, customer, amount):
        self.model = model
        self.customer = customer
        self.amount = amount

    def printdata(self):
        print(self.model)
        print(self.customer)
        print(self.amount)

pulsar = bike("tidg","pradeep","60000")
apache = bike("ghdr","aravind","45000")

pulsar.printdata()
apache.printdata()