class CRMTool:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer_id, name, email, phone):
        if customer_id in self.customers:
            print("Customer ID already exists.")
        else:
            self.customers[customer_id] = {
                'Name': name,
                'Email': email,
                'Phone': phone
            }
            print(f"Customer {name} added successfully.")

    def view_customer(self, customer_id):
        customer = self.customers.get(customer_id)
        if customer:
            print(f"Customer ID: {customer_id}")
            for key, value in customer.items():
                print(f"{key}: {value}")
        else:
            print("Customer not found.")

    def update_customer(self, customer_id, name=None, email=None, phone=None):
        customer = self.customers.get(customer_id)
        if customer:
            if name:
                customer['Name'] = name
            if email:
                customer['Email'] = email
            if phone:
                customer['Phone'] = phone
            print(f"Customer {customer_id} updated successfully.")
        else:
            print("Customer not found.")

    def delete_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            print(f"Customer {customer_id} deleted successfully.")
        else:
            print("Customer not found.")

    def list_customers(self):
        if self.customers:
            for customer_id, customer_data in self.customers.items():
                print(f"\nCustomer ID: {customer_id}")
                for key, value in customer_data.items():
                    print(f"{key}: {value}")
        else:
            print("No customers found.")


# Testing the CRM Tool with live output
crm = CRMTool()

# Add customers
crm.add_customer(1, "Alice Smith", "alice@example.com", "555-1234")
crm.add_customer(2, "Bob Jones", "bob@example.com", "555-5678")

# List all customers
print("\nListing all customers:")
crm.list_customers()

# View a specific customer
print("\nViewing customer with ID 1:")
crm.view_customer(1)

# Update a customer
print("\nUpdating customer with ID 2:")
crm.update_customer(2, phone="555-8765")

# View updated customer
print("\nViewing updated customer with ID 2:")
crm.view_customer(2)

# Delete a customer
print("\nDeleting customer with ID 1:")
crm.delete_customer(1)

# List all customers again
print("\nListing all customers after deletion:")
crm.list_customers()
