from brownie import *

print(len(accounts))


p = project.load(r'D:\code\blockchain_crc\project1', name="BooleanTest")
p.load_config()



from brownie.project.BooleanTest import *

network.connect('development')

print(len(accounts))

contract = accounts[0].deploy(BooleanTest)
contract.setVal(True)
assert contract.getVal() == True


contract.setVal(False)
assert contract.getVal() == False
print("PRINTING", contract.getVal())

try:
    contract.setVal('STRING DATA')
except ValueError as e:
    print(e.args[0])


try:
    contract.setVal(222)
except ValueError as e:
    print(e.args[0])

import time
time.sleep(1) 
