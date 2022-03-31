from brownie import *

print(len(accounts))


p = project.load(r'D:\code\blockchain_crc\project1', name="AddressTest")
p.load_config()



from brownie.project.AddressTest import *

network.connect('development')

print(len(accounts))


contract = accounts[0].deploy(AddressTest)

print(dir(accounts[0]))
address0 = accounts[0].address
balance0 = accounts[0].balance()
deployment_address0 = accounts[0].get_deployment_address()
print(address0, balance0, deployment_address0)

address1 = accounts[0].address
balance1 = accounts[0].balance()
deployment_address1 = accounts[0].get_deployment_address()
print(address1, balance1, deployment_address1)

accounts[0].transfer(to=address1, amount=1000)

balance1 = accounts[0].balance()
print(address0, balance0, deployment_address0)
print(address1, balance1, deployment_address1)


accounts[0].transfer(accounts[1], "10 ether")
print('ACCOUNT 0 BALANCE', accounts[0].balance())
print('ACCOUNT 1 BALANCE', accounts[1].balance())


# val = "0xB7e390864a90b7b923C9f9310C6F98aafE43F707"
# contract.setVal(val)
# assert contract.getVal() == val

# try:
#     contract.setVal("True")
# except ValueError as e:
#     print(e.args[0])

# try:
#     contract.setVal(True)
# except ValueError as e:
#     print(e.args[0])

# try:
#     contract.setVal(1)
# except ValueError as e:
#     print(e.args[0])

import time
time.sleep(1) 
