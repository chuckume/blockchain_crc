from brownie import *
print(len(accounts))

p = project.load(r'D:\code\blockchain_crc\project1', name="HelloWorld")

p.load_config()

from brownie.project.HelloWorld import *
network.connect('development')

print(len(accounts))

greeter = accounts[0].deploy(HelloWorld)


print(greeter.greet)
greeter.wait(1)

