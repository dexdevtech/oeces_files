database = [('Dexter', 'Dexter1'),
            ('Lea', 'Lea1'),
            ('Brian', 'Brian1'),
            ('Trisha', 'Trisha1'),
            ('Aira', 'Aira1'),]

def get_account(username, password):
    account = (username, password)
    if account in database:
        return True
    return False












