# Initializing our blockchain list
genesis_block = {
    'previous_hash': '', 
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Gavin'
participants = {'Gavin'}

def hash_block(last_block):
    return '-'.join([str(last_block[key]) for key in last_block])

def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent

def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    
    return blockchain[-1]

def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain
    
    Arguments:
        sender: The sender of the coins.
        recipient: The recipient of the coints.
        amount: The amount of coinst sent with the transaction (default = 1.0)
    """

    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)

def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)

    block = {
        'previous_hash': hashed_block, 
        'index': len(blockchain), 
        'transactions': open_transactions
    }
    blockchain.append(block)
    return True

def get_transaction_value():
    """ Returns the input of the user as float """
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: ')) 

    return tx_recipient, tx_amount

def get_user_choice():
    return input('Your choice: ') 

def print_blockchain_element():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)

def verify_chain():
    """ Verify the current blockchain and return True if it's valid, False otherwise """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue # skip genesis block
        if block['previous_hash'] != hash_block(blockchain[index-1]):
            return False
    return True

waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('h: Manipulate the chain')
    print('q: Exit')

    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_element()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '', 
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Gav', 'amount': 100}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input invalid. Please a value from the list')
    if not verify_chain():
        print_blockchain_element()
        print('Invalid blockchain!')
        break
    print(get_balance('Gavin'))
else:
    print('User left!')    

print('Done!')