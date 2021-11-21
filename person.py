#stores all user information
class Person:
    def __init__(self, name, ticket_id, num_masks, account_balance):
        self.name = name
        self.ticket_id = ticket_id
        self.num_masks = num_masks
        self.account_balance = account_balance

    def login(self, name, ticket_id):
        if self.name == name and self.ticket_id == ticket_id:
            return True
        return False

    def get_mask(self, mask_type):
        if mask_type == 'regular':
            if self.num_masks > 0:
                self.num_masks -= 1
                return True
            else:
                print('You have no masks remaining this week.')
                return False
        if mask_type == 'faceshield':
            if self.account_balance >= 1:
                self.account_balance -= 1
                return True
            else:
                print('Insufficient funds.')
        return False

    def add_funds(self, amount):
        self.account_balance += amount

    def simulate_new_week(self):
        self.num_masks = 7
