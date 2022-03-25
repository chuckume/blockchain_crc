from brownie import accounts, Greeter

# Source: https://mirabdulhaseeb.medium.com/truffle-vs-hardhat-vs-brownie-lets-compare-ea08b927d084
def main():
    deployer_account = accounts[0]
    greeter = Greeter.deploy("Hello, World!", {'from': deployer_account})
    print("Deployed at: ", greeter.address)