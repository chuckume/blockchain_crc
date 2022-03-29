from brownie import *

print(len(accounts))


p = project.load(r'D:\code\blockchain_crc\project1', name="IntegerTest")
p.load_config()


p1 = project.load(r'D:\code\blockchain_crc\project1', name="SignedIntegerTest")
p1.load_config()

from brownie.project.IntegerTest import *
from brownie.project.SignedIntegerTest import *

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

try:
    integer.setVal(-1)
    print("PRINTING", integer.getVal())
except OverflowError:
    print('OVERFLOW ERROR')



integer = accounts[0].deploy(SignedIntegerTest)
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


integer.setVal(-1)
assert integer.getVal() == -1


import time
time.sleep(1) 
