from brownie import *

print(len(accounts))


p = project.load(r'D:\code\blockchain_crc\project1', name="IntegerTest")
p.load_config()

from brownie.project.IntegerTest import *
network.connect('development')

print(len(accounts))

integer = accounts[0].deploy(IntegerTest)
integer.setVal(1)
assert integer.getVal() == 1
print("PRINTING", integer.getVal())

integer.setVal("22")
assert integer.getVal() == 22
print("PRINTING", integer.getVal())


try:
    integer.setVal("AA")
    print("PRINTING", integer.getVal())
except TypeError:
    print('RAISED TYPE ERROR')


import time
time.sleep(1) 
