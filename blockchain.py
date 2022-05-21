import functools

# Initializing our blockchain list
MINING_REWARD = 10

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
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + tx_amt[0] if len(tx_amt) > 0 else 0, tx_sender, 0)

    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = functools.reduce(lambda tx_sum, tx_amt: tx_sum + tx_amt[0] if len(tx_amt) > 0 else 0, tx_recipient, 0)
    
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

    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True

    return False

def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)

    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }

    copied_transaction = open_transactions[:]
    copied_transaction.append(reward_transaction)

    block = {
        'previous_hash': hashed_block, 
        'index': len(blockchain), 
        'transactions': copied_transaction
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

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']

def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])

waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('5: Check transaction validity')
    print('h: Manipulate the chain')
    print('q: Exit')

    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print('Added transaction!')
        else:
            print('Transaction failed!')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_element()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print('All transactions are valid')
        else:
            print('There are invalid transactions!')
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
    print('Balance of {}: {:6.2f}'.format('Gavin', get_balance('Gavin')))
else:
    print('User left!')    

print('Done!')