""""
This file contains code for Blockchain Banking activities.
Last modified : 28/4/2021
Author: Luciana C., castorinaluciana@gmail.com

Customer Department, Licesing ....

"""


import json

################################# Activity 1 ##########################################3333
class User():
    """ User class to represent each customer."""

    def __init__(self, name):
        """ Create a User class object.
        Parameters:
            clientName : str
                name of the banking customer
        """
        self.name = name
        self.amount_of_money = 0
    
    def display_information(self):
        """ Show User class data to standard out (screen). """
        print(self.name, self.amount_of_money)

    def deposit_money(self, amount):
        """Deposit money into this customer 's account.
        Parameters:
           amount: int 
                the amount of money to deposit
        """
        self.amount_of_money +=  amount

    def withdraw_money(self, amount):
        """ Withdraw money from this customer's account.
        Parameters: 
            amount : int
                the amount of money to withdraw
        """
        self.amount_of_money -= amount
    
    def transfer_money(self, amount):
        """ Transfer money from this cutomer's account to another account.
        Note, will need to call receive_transfer_money of receiver's User object.
        Parameters: 
            amount : int
                the amount of money to transfer
        """
        self.amount_of_money -= amount
    
    def receive_transfer_money(self, amount):
        """ Receive the transfer money sent by another customer
            Parameters:
                amount : int
                    the amount of money received
        """
        
        self.amount_of_money += amount

def read_transactions():
    """ Open the transactions file and process the transactions inside."""

    file1 = open('c:/Users/hitoc/Documents/GitHub/Term 6/Transactions2.txt', 'r')
    Lines = file1.readlines()
    collectionOfCustomers = {} # {name_of_customers: User class object}

    for line in Lines:# Go through all lines in the Transactions.txt file
        line.split()
        transactionSplitted = line.split()
        if len(transactionSplitted) > 7: # if this is the first line (line of names)
            for customer in transactionSplitted: # Go through only the first line
                collectionOfCustomers[customer] = User(customer)
        elif transactionSplitted[1] == "deposit": #call appropiate function for each transaction types
            collectionOfCustomers.get(transactionSplitted[0]).deposit_money(int(transactionSplitted[2]))
        elif transactionSplitted[1] == "withdraw":
            collectionOfCustomers.get(transactionSplitted[0]).withdraw_money(int(transactionSplitted[2]))
        elif transactionSplitted[1] == "transfer":
            collectionOfCustomers.get(transactionSplitted[0]).transfer_money(int(transactionSplitted[2]))
            collectionOfCustomers.get(transactionSplitted[3]).receive_transfer_money(int(transactionSplitted[2]))
        #print(collectionOfCustomers)
        #input('')
    
    for customer in collectionOfCustomers.values(): # show the information to screen for debugging
        customer.display_information()
#read_transactions() #Uncomment this line to run the code


############################### Activity 2 ############################# 

class Block():
    """ A block class to represent each block in Blockchain """

    def __init__(self, previousBlockHash):
        """ Create a Block class object
        Parameters:
            previous_hash : str
                link to the hash of the previous block 
        """ 
        self.previousBlockHash = previousBlockHash
        self.transactions = []
        self.myHash = None

    def hash_myself(self):
        """Generate a hash of this current block"""
        self.myHash = str(hash(str(self.previousBlockHash) + str(self.transactions)))

    def add_transaction(self, transaction):
        """Add a new transaction to the current block """
        self.transactions.append(transaction)

    def show_block_details(self):
        """Display the information of this block to screen"""
        print(self.previousBlockHash, self.transactions, self.myHash)

    def save_to_file(self):
        """Generate a json format of this block.
        Returns:
            json representation of block class
        """
        return json.dumps(self.__dict__, sort_keys=True, indent=4)

#{

#    key1: value1,
#    key2: value2,
#    key3: value3,

#}

#GenesisBlock <----- Block1 <----- Block 2

def read_transactions2():
    """Open and read the transactions file, process the transactions storing it in blockchain"""

    file1 = open('c:/Users/hitoc/Documents/GitHub/Term 6/Transactions2.txt', 'r')
    Lines = file1.readlines()
    counter = 0 #counting which line are we reading
    currentBlock = Block(None) #point to the current block (latest block) in our block chain
    for line in Lines: #we are 1 line at a time 
        #print(line)
        if counter == 0: #this is the first line
            genesisBlock = Block(None)  #point to the current block (latest block) in our block chain 
            genesisBlock.add_transaction(line)
            genesisBlock.hash_myself()
            currentBlock.previousBlockHash = genesisBlock.myHash #current block points to the genesis block
            with open("BCoutput.json", "a") as f: # saving genesis block to file
                f.write(genesisBlock.save_to_file())

        elif counter > 0 and counter % 10 == 0: # >0 means this is not a genesis block, counter 10 % ==0 means it is divisible by 10 
            currentBlock.hash_myself()
            currentBlock.show_block_details()
            with open("BCoutput.json", "a") as f:
                f.write(currentBlock.save_to_file())
            newBlock = Block(currentBlock.myHash) #newBlock is pointing to old block
            currentBlock = newBlock
            currentBlock.add_transaction(line)
        else:
            currentBlock.add_transaction(line)
        counter += 1
        
    #Handle adding the last block into file, ending block in our blockchain
    currentBlock.hash_myself()
    with open("BCoutput.json", "a") as f:
        f.write(currentBlock.save_to_file())


read_transactions2()