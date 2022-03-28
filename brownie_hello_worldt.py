from brownie import *
# from brownie.network import accounts
print(len(accounts))


p = project.load('D:\project2', name="Greeter")
p.load_config()

from brownie.project.Greeter import *
network.connect('development')

print(len(accounts))

greeter = accounts[0].deploy(Greeter, "Hello, World!")

print(greeter.greet())

greeter.setGreeting("Hola, mundo!")
print(greeter.greet())

print(dir(greeter))

#