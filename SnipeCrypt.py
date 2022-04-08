# Libs Data
from web3 import Web3
from threading import Timer
from datetime import date, datetime
from configparser import ConfigParser
import json
import time
import logging
import webbrowser
import subprocess
import ctypes
import sys
import os
import requests
import keyboard
import asyncio
from urllib import request
from os import system

sys.setrecursionlimit(10000)
#hwid_get = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
os.system("") #allows different colour text to be used


#GenerateLicense ----------------------------------------------------------------------------------
#AppVer = '2.31'
#VerCheck = '2.31'

# Read License ------------------------------------------------------------------------------------


#AbiCode LoadHere
l = open('./Router/Liquidity.json')
p = open('./Router/PancakeSwap.json')
u = open('./Router/UniswapV2.json')
s = open('./Router/CheckerV5.json')

config= ConfigParser()
config.read("SnipeCrypt.ini")

bsc = config['Version']['Network']
web3 = Web3(Web3.HTTPProvider(bsc))


if config['Version']['Type'] == '1':
 factoryTestnet = web3.toChecksumAddress('0xb7926c0430afb07aa7defde6da862ae0bde767bc')    
 routerTestnet = web3.toChecksumAddress('0x9Ac64Cc6e4415144C455BD8E4837Fea55603e5c3')
elif config['Version']['Type'] == '0':
 factoryTestnet = web3.toChecksumAddress('0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73')    
 routerTestnet = web3.toChecksumAddress('0x10ED43C718714eb63d5aA57B78B54704E256024E')


bnb = web3.toChecksumAddress(config['TokenSetup']['BNB']) 
busd = web3.toChecksumAddress(config['TokenSetup']['BUSD']) 
WalletOwner = web3.toChecksumAddress(config['TokenSetup']['MyAddress'])
TargetContractBuy = web3.toChecksumAddress(config['TokenSetup']['MyTargetContract'])
TargetContractSell = web3.toChecksumAddress(config['TokenSetup']['MyTargetContract'])  
GasFeeBuy = config['FeeSetting']['GasBuyFee']

tokenB = busd 
spend = bnb  

uniswap_factory = factoryTestnet  
panRouterContractAddress = routerTestnet
uniswap_factory_abi = json.load(u)
panabi = json.load(p)
lpabi = json.load(l)
sellAbi = json.load(s)
contractbuy = web3.eth.contract(address=panRouterContractAddress, abi=panabi)
contract = web3.eth.contract(address=uniswap_factory, abi=uniswap_factory_abi)
tokenToBuy = TargetContractBuy


# -----------------------------------------------------------------------------------------------------------------------

# Start From Here.
# New Detection Anti Rug Pull Scanner

#delaySell = config['Premium']['SellDelay']
#multiply = config['Premium']['MultiGas']

#delayOnSellMs = 1e3 * delaySell,
#currentNonce = 0
#antiBotMultiTx = 1

#if config['Premium']['AntiBot'] == '1':
#   antiBotMultiTx != 0


#transactionToDetect = (
#  config['Premium']['FrontRunTransaction']
#).toFixed(0),
#skipBlock = config['Premium']['SkipBlocks']
#countDown = date.__format__(config['Premium']['SetCountDown']);

addLiquidityETH = "0xf305d719",
addLiquidity = "0xe8e33700",
addLiquidityDxsale = "0x267dd102",
removeLiquidity = "0xbaa2abde",
removeLiquidityETH = "0x02751cec",
removeLiquidityETHSupportingFeeOnTransferTokens = "0xaf2979eb",
removeLiquidityETHWithPermit = "0xded9382a",
removeLiquidityETHWithPermitSupportingFeeOnTransferTokens = "0x5b0d5984",
removeLiquidityWithPermit = "0x2195995c",


#def getNonce(e) :
#  return web3.eth.getTransaction(e)



  

# -----------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------
class style(): # Class of different text colours - default is white
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

start_time = time.time()
now = datetime.now()
date_time = now.strftime("%m/%d/%Y,%H:%M:%S")  
print(style.MAGENTA+'[' + date_time + ']' + " [Info] Loading Assets Library"+style.RESET)

print(style.MAGENTA) #change following text to magenta

ascii = """
Response From Server : Api Approved...OK
"""
print(style.WHITE)
ctypes.windll.kernel32.SetConsoleTitleW("SCNTokenPro | is Loading...")


# -----------------------------------------------------------------------------------------------------------------------

# Call Function ---------------------------------------------------------------------------------------------
sellTokenContract = web3.eth.contract(TargetContractSell, abi=sellAbi)
if config['Version']['BuyType'] == '0':
 buyTokenContract = web3.eth.contract(spend, abi=sellAbi)
elif config['Version']['BuyType'] == '1':
 buyTokenContract = web3.eth.contract(busd, abi=sellAbi)
balance = web3.eth.get_balance(WalletOwner)
humanReadable = web3.fromWei(balance,'ether')
balance = sellTokenContract.functions.balanceOf(WalletOwner).call()
symbol = sellTokenContract.functions.symbol().call()
name = sellTokenContract.functions.name().call()
mysymbl = buyTokenContract.functions.symbol().call()
myname = buyTokenContract.functions.name().call()
readable = web3.fromWei(balance,'ether')
balanceWallet = str(readable) + " " + symbol
tokenValue = balance
tokenValue2 = web3.fromWei(tokenValue, 'ether')
# Call Function ---------------------------------------------------------------------------------------------

os.system('cls')



def Program():
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S")    
    print( '[' + date_time + ']' +" [Welc] SCNTokenPro 2020 (C) | Build 4.11 | Tutorial Read ManualBook.txt")
    if web3.isConnected():
        print( '[' + date_time + ']' + " [Info] Private Node is "+style.GREEN +"Connect"+style.RESET)
    if config['Version']['Type'] == '0':
        print('[' + date_time + ']' + " [Info] Network is "+ style.RED + "Mainnet"+style.RESET)
        logging.basicConfig(filename="./SystemLog/Function.Log",  level=logging.INFO)
        logging.info('[' + date_time + ']' + ' PROGRAM RUNNING , NETWORK IS MAINNET')
    elif config['Version']['Type']  == '1':
        print('[' + date_time + ']' + " [Info] Network is "+ style.RED + "Testnet"+style.RESET)
        logging.basicConfig(filename="./SystemLog/Function.Log",  level=logging.INFO)
        logging.info('[' + date_time + ']' + ' PROGRAM RUNNING , NETWORK IS TESTNET')
    if config['Version']['BuyType'] == '0':
     print('[' + date_time + ']' + " [Info] Swap Amount: ",config['ProfitSetting']['Purchase'], mysymbl)   
     #print('[' + date_time + ']' + " [Info] BALANCE: ",humanReadable,"TOKEN:", mysymbl)
    elif config['Version']['BuyType'] == '1':
     print('[' + date_time + ']' + " [Info] Swap Amount: ",config['ProfitSetting']['Purchase'], mysymbl)   
     #print('[' + date_time + ']' + f" [Info] BALANCE SNIPER: {float(tokenValue2)} NAME: {name} SYMBOL: {symbol}.")  
# Call Function Wallet --------------------------------------------------------------------------------------------------
     
    if (str(tokenValue2) == '0'):
         print('[' + date_time + ']' + f" [Info] Convert {mysymbl} 0 {symbol}")  
    elif (str(tokenValue2) > '1'):  
        if config['Version']['BuyType'] == '0':
         test = contractbuy.functions.getAmountsOut(balance,[TargetContractSell, spend]).call()
         data = (test[1] * 10 **-0x12)
         convertWBNB = round(data, -(int("{:e}".format(data).split('e')[1]) - 4))
         print('[' + date_time + ']' + f" [Info] Convert {mysymbl} : {style.GREEN}{str(convertWBNB)}{style.RESET} {symbol}.")
        elif config['Version']['BuyType'] == '1':
         test = contractbuy.functions.getAmountsOut(balance,[TargetContractSell, tokenB]).call()
         data = (test[1] * 10 **-0x12)
         print('[' + date_time + ']' + f" [Info] Convert {mysymbl} : {style.GREEN}{str(data)}{style.RESET} {symbol}.")
    walletBalance = round(humanReadable, -(int("{:e}".format(humanReadable).split('e')[1]) - 4))
    ctypes.windll.kernel32.SetConsoleTitleW("SCNTokenPro | Tokens Detected: " + str(symbol) + " | Tokens Name: " + str(name)  + " | Wallet Balance: " + str(walletBalance) + " BNB")
        
# Main Menu ------------------------------------------------------------------------------------------------------------- 

# SMART FUNCTION BNB ---------------------------------------------------------------------------------------------------------
def LPBNB():
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S")
    print('[' + date_time + ']' +  " [Scan] Start Scan Liquidity | Version BNB...")
    lp = pair
    lpcontract = web3.eth.contract(address=lp, abi=lpabi)
    balance = lpcontract.functions.getReserves().call()
    b = balance[0]
    #print(b)
    if b > 0:
        print('[' + date_time + ']' +  " [Scan] Liquidity Found | Version BNB...")
        buy_bnb()
    else:
        print('[' + date_time + ']' +  " [Scan] Liquidity Not Found | Version BNB...")
        BUYBNB()

def SNIPEBNB():
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S") 
    
    global pair
    pair = contract.functions.getPair(TargetContractBuy, spend).call()
    if pair != web3.toChecksumAddress('0x0000000000000000000000000000000000000000'):
         print('[' + date_time + ']' + " [Info] Token Status : ",pair," | Version BNB | [TRUE]" )
         LPBNB()
    else:
        print('[' + date_time + ']' + " [Info] Token Status : ",pair," | Version BNB | [TRUE]" )

    
# SMART FUNCTION BNB ---------------------------------------------------------------------------------------------------------      


def monitor():
 start_time = time.time()
 now = datetime.now()
 date_time = now.strftime("%m/%d/%Y,%H:%M:%S")
 print(style.RED + '[' + date_time + ']' +  " [Info] Monitor Price Target Start..."+style.RESET)
 while True:
    # Check Profit Now Function ----------------------------------------------------------------------------------------------  
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S")   
    sellTokenContract = web3.eth.contract(TargetContractSell, abi=sellAbi)
    balance = sellTokenContract.functions.balanceOf(WalletOwner).call()
    buyTokenContract = web3.eth.contract(busd, abi=sellAbi)
    if config['Version']['BuyType'] == '0':
     test = contractbuy.functions.getAmountsOut(balance,[TargetContractSell, spend]).call()
     data = (test[1] * 10 **-0x12)
     data3 = (test[1] * 10 **-0x12) * 5
     datafinal = data3 * int(config['ProfitSetting']['GetProfit'])
     ConvertProfit = round(data, -(int("{:e}".format(data).split('e')[1]) - 4))
     ConvertProfit2 = round(datafinal, -(int("{:e}".format(datafinal).split('e')[1]) - 4))
     print('[' + date_time + ']','[Info] HOLD/PROFIT (NOW/TP) BNB:',str(ConvertProfit),str(ConvertProfit2))
    elif config['Version']['BuyType'] == '1':
     test = contractbuy.functions.getAmountsOut(balance,[TargetContractSell, busd]).call()
     data = (test[1] * 10 **-0x12)
     data3 = (test[1] * 10 **-0x12) * 5
     datafinal = data3 * int(config['ProfitSetting']['GetProfit'])
     print('[' + date_time + ']','[Info] HOLD/PROFIT (NOW/TP) BUSD:',str(data),str(datafinal))
# Check Profit Now Function ---------------------------------------------------------------------------------------------- 
    if keyboard.is_pressed("s"):
        if config['Version']['BuyType'] == '0':
            sell_bnb()
        elif config['Version']['BuyType'] == '1':
            sell_busd()

def verifcontract():
    sellTokenContract = web3.eth.contract(busd, abi=sellAbi)
    approve = sellTokenContract.functions.approve(routerTestnet, 115792089237316195423570985008687907853269984665640564039457584007913129639935
    ).buildTransaction({
        'from': WalletOwner,
        'gasPrice': web3.toWei(config['FeeSetting']['GasApproveFee'], 'gwei'),
        'nonce': web3.eth.get_transaction_count(WalletOwner),
    })
    signed_txn = web3.eth.account.sign_transaction(
    approve, private_key=config['TokenSetup']['PrivateKey'])
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print('[' + date_time + ']' +  " [Verf] Starting Verif Token | Version BUSD...")
    logging.basicConfig(filename="./SystemLog/Function.Log",  level=logging.INFO)
    logging.info('[' + date_time + ']' + ' APPROVE [BUSD] IS EXECUTE | YOUR TX HASH INFO :: ' + web3.toHex(tx_token))
    if config['Version']['Type'] == '1':
         webbrowser.open_new_tab('https://testnet.bscscan.com/tx/'+web3.toHex(tx_token))
    elif config['Version']['Type'] == '0':
        webbrowser.open_new_tab('https://bscscan.com/tx/'+web3.toHex(tx_token))
    print('[' + date_time + ']' +  " [Verf] Snipe Success [Verif] | Version BUSD...") 
    os.system('py SCNTokenPro.pyc')
    exit()

# Buy ------------------------------------------------------------------------------------------------------------- 
def buy_bnb():
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S")     
    configApi= ConfigParser()
    configApi.read("SnipeCrypt.ini")
    spamapi = 'https://aywt3wreda.execute-api.eu-west-1.amazonaws.com/default/IsHoneypot?chain=bsc2&token='+configApi['API']['RugAddress']
    SetBuyTax = configApi['Premium']['SetBuyTax']
    response = request.urlopen(spamapi)
    honeycheck = json.loads(response.read()) 
    
    if honeycheck['BuyTax'] >= int(configApi['Premium']['SetBuyTax']) or honeycheck['IsHoneypot'] == True:
     print('[' + date_time + ']' + " [Info] Token Status : ",pair," | HoneyPotToken : ",honeycheck['IsHoneypot']," | Limit Tax : ",SetBuyTax," | Tax Fee : ",honeycheck['BuyTax']," | Version BNB | [BLOCK]")
     buy_bnb()
    else:
     print('[' + date_time + ']' + " [Info] Token Status : ",pair," | HoneyPotToken : ",honeycheck['IsHoneypot']," | Limit Tax : ",SetBuyTax," | Tax Fee : ",honeycheck['BuyTax']," | Version BNB | [ALLOW]")
    print('[' + date_time + ']' +  " [Buys] Starting Buy Token | Version BNB...")
    currentNonce = web3.eth.get_transaction_count(WalletOwner)
    pancakeswap2_txn = contractbuy.functions.swapExactETHForTokens( 
    0, #FALSE, #--- this function write like? address or?
    [spend,tokenToBuy],
    WalletOwner,
    (int(time.time()) + 10000)
    ).buildTransaction({
    'from': WalletOwner,
    'value': web3.toWei(config['ProfitSetting']['Purchase'],'ether'),
    'gas':int(config['FeeSetting']['GasBuyFeeUsed']),
    'gasPrice': web3.toWei(config['FeeSetting']['GasBuyFee'],'gwei'),
    'nonce': web3.eth.get_transaction_count(WalletOwner),
    })
    signed_txn = web3.eth.account.sign_transaction(pancakeswap2_txn, private_key=config['TokenSetup']['PrivateKey'])
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)    
    print('[' + date_time + ']' +  " [Buys] Write SystemLog [BUY] | Version BNB...")
    logging.basicConfig(filename="./SystemLog/Function.Log",  level=logging.INFO)
    logging.info('[' + date_time + ']' + ' BUYING PROGRAM IS EXECUTE | YOUR TX HASH INFO :: ' + web3.toHex(tx_token))   
    print('[' + date_time + ']' +  " [Buys] Generating TXHash [BUY] | Version BNB...")
    time.sleep(6) 
    if config['Version']['Type'] == '1':
     webbrowser.open_new_tab('https://testnet.bscscan.com/tx/'+web3.toHex(tx_token))
    elif config['Version']['Type'] == '0':
        webbrowser.open_new_tab('https://bscscan.com/tx/'+web3.toHex(tx_token))  
    print('[' + date_time + ']' +  " [Buys] Snipe Success [BUY] | Version BNB...")
    monitor()
# Buy BUSD -------------------------------------------------------------------------------------------------------------   
def buy_busd():
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S")   
    sellTokenContract = web3.eth.contract(busd, abi=sellAbi)
    print('[' + date_time + ']' +  " [Buys] Starting Buy Token | Version BUSD...")
    amountOutMin  = 0
    pancakeswap2_txn = contractbuy.functions.swapExactTokensForTokens( 
    int(config['ProfitSetting']['Purchase']+'000000000000000000'), 0,
    [tokenB,tokenToBuy],
    WalletOwner,
    (int(time.time()) + 10000)
    ).buildTransaction({
    'from': WalletOwner,
    'gas':int(config['FeeSetting']['GasBuyFeeUsed']),
    'gasPrice': web3.toWei(config['FeeSetting']['GasBuyFee'],'gwei'),
    'nonce': web3.eth.get_transaction_count(WalletOwner),
    })
    signed_txn = web3.eth.account.sign_transaction(pancakeswap2_txn, private_key=config['TokenSetup']['PrivateKey'])
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print('[' + date_time + ']' +  " [Buys] Write SystemLog [BUY] | Version BUSD...")
    logging.basicConfig(filename="./SystemLog/Function.Log",  level=logging.INFO)
    logging.info('[' + date_time + ']' + ' BUYING PROGRAM IS EXECUTE | YOUR TX HASH INFO :: ' + web3.toHex(tx_token))   
    print('[' + date_time + ']' +  " [Buys] Generating TXHash [BUY] | Version BUSD...")
    time.sleep(6) 
    if config['Version']['Type'] == '1':
     webbrowser.open_new_tab('https://testnet.bscscan.com/tx/'+web3.toHex(tx_token))
    elif config['Version']['Type'] == '0':
     webbrowser.open_new_tab('https://bscscan.com/tx/'+web3.toHex(tx_token))
    print('[' + date_time + ']' +  " [Buys] Snipe Success [BUY] | Version BUSD...")   
    monitor()
# Buy BUSD -------------------------------------------------------------------------------------------------------------  
# Sell  Function BNB ---------------------------------------------------------------------------------------------------------
def sell_bnb():  
    sellTokenContract = web3.eth.contract(TargetContractSell, abi=sellAbi)
    balance = sellTokenContract.functions.balanceOf(WalletOwner).call()
    symbol = sellTokenContract.functions.symbol().call()
    name = sellTokenContract.functions.name().call()
    tokenValue = balance
    tokenValue2 = web3.fromWei(tokenValue, 'ether')
    configApi= ConfigParser()
    configApi.read("SnipeCrypt.ini")
    spamapi = 'https://aywt3wreda.execute-api.eu-west-1.amazonaws.com/default/IsHoneypot?chain=bsc2&token='+configApi['API']['RugAddress']
    response = request.urlopen(spamapi)
    honeycheck = json.loads(response.read())
    SetBuyTax = configApi['Premium']['SetBuyTax']
    if (honeycheck['BuyTax'] >= int(configApi['Premium']['SetBuyTax']) or honeycheck['IsHoneypot'] == True):
     print('[' + date_time + ']' + " [Info] HoneyPotToken : ",honeycheck['IsHoneypot']," | Limit Tax : ",SetBuyTax," | Max Fee : ",honeycheck['BuyTax']," | Version BNB | [SELL]")
     sell_bnb()
    else:
     print('[' + date_time + ']' + " [Info] HoneyPotToken : ",honeycheck['IsHoneypot']," | Limit Tax : ",SetBuyTax," | Max Fee : ",honeycheck['BuyTax']," | Version BNB | [SELL]") 
    if(tokenValue2 == 0):
        print('[' + date_time + ']' + f" [Warn] SWAPPING: {tokenValue2} NO TOKEN. EXIT PROGRAM") 
        os.system('pause')
        exit()
    else:
        print('[' + date_time + ']' + f" [Warn] SWAPPING: {tokenValue2} NAME: {name} SYMBOL: {symbol}.") 
    approve = sellTokenContract.functions.approve(panRouterContractAddress, balance
    ).buildTransaction({
        'from': WalletOwner,
        'gasPrice': web3.toWei(config['FeeSetting']['GasApproveFee'], 'gwei'),
        'nonce': web3.eth.get_transaction_count(WalletOwner),
    })

    signed_txn = web3.eth.account.sign_transaction(
    approve, private_key=config['TokenSetup']['PrivateKey'])
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print('[' + date_time + ']' + " [Warn] ----- GENERATING HASH TX -----")
    logging.basicConfig(filename="./SystemLog/Function.Log",  level=logging.INFO)
    logging.info('[' + date_time + ']' + ' APPROVE SELL IS EXECUTE | YOUR TX HASH INFO :: ' + web3.toHex(tx_token))
    #print('[' + date_time + ']' + " APPROVED PROGRAM IS EXECUTE | YOUR TX HASH INFO :: " + web3.toHex(tx_token))
    print('[' + date_time + ']' + " [Warn] ----- SYSTEM OK, GOING TO SELL -----")
    time.sleep(6) # Waiting Approve TimeStamp
    pancakeswap2_txn = contractbuy.functions.swapExactTokensForETH(
        balance, 0,
        [TargetContractSell, spend],
        WalletOwner,
        (int(time.time()) + 1000000)
    ).buildTransaction({
        'from': WalletOwner,
        'gasPrice': web3.toWei(config['FeeSetting']['GasSellFee'], 'gwei'),
        'nonce': web3.eth.get_transaction_count(WalletOwner),
    })
    signed_txn = web3.eth.account.sign_transaction(
    pancakeswap2_txn, private_key=config['TokenSetup']['PrivateKey'])
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print('[' + date_time + ']' + " [Warn] ----- GENERATING HASH TX -----")
    logging.info('[' + date_time + ']' + ' SELL IS EXECUTE | YOUR TX HASH INFO :: ' + web3.toHex(tx_token))
    print('[' + date_time + ']' + " [Warn] ----- SELL TOKEN SUCCESS -----")
    time.sleep(6)   
    if config['Version']['Type']  == '0':
       webbrowser.open_new_tab('https://bscscan.com/tx/'+web3.toHex(tx_token))
    elif config['Version']['Type']  == '1' :   
       webbrowser.open_new_tab('https://testnet.bscscan.com/tx/'+web3.toHex(tx_token))
    print('[' + date_time + ']' + " [Syst] Application is Restarting For (5) Seconds.")
    time.sleep(5)
    os.system('py SCNTokenPro.pyc')
    exit()
# Sell  Function ---------------------------------------------------------------------------------------------------------  

# Sell  Function BUSD ---------------------------------------------------------------------------------------------------------
def sell_busd():  
    sellTokenContract = web3.eth.contract(TargetContractSell, abi=sellAbi)
    balance = sellTokenContract.functions.balanceOf(WalletOwner).call()
    symbol = sellTokenContract.functions.symbol().call()
    name = sellTokenContract.functions.name().call()
    tokenValue = balance
    tokenValue2 = web3.fromWei(tokenValue, 'ether')
    configApi= ConfigParser()
    configApi.read("SnipeCrypt.ini")
    spamapi = 'https://aywt3wreda.execute-api.eu-west-1.amazonaws.com/default/IsHoneypot?chain=bsc2&token='+configApi['API']['RugAddress']
    response = request.urlopen(spamapi)
    honeycheck = json.loads(response.read())
    SetBuyTax = configApi['Premium']['SetBuyTax']
    if (honeycheck['BuyTax'] >= int(configApi['Premium']['SetBuyTax']) or honeycheck['IsHoneypot'] == True):
     print('[' + date_time + ']' + " [Info] HoneyPotToken : ",honeycheck['IsHoneypot']," | Limit Tax : ",SetBuyTax," | Max Fee : ",honeycheck['BuyTax']," | Version BNB | [SELL]")
     sell_busd()
    else:
     print('[' + date_time + ']' + " [Info] HoneyPotToken : ",honeycheck['IsHoneypot']," | Limit Tax : ",SetBuyTax," | Max Fee : ",honeycheck['BuyTax']," | Version BNB | [SELL]") 
    if(tokenValue2 == 0):
        print('[' + date_time + ']' + f" [Warn] SWAPPING: {tokenValue2} NO TOKEN. EXIT PROGRAM") 
        os.system('pause')
        exit()
    else:
        print('[' + date_time + ']' + f" [Warn] SWAPPING: {tokenValue2} NAME: {name} SYMBOL: {symbol}.") 
    approve = sellTokenContract.functions.approve(panRouterContractAddress, balance
    ).buildTransaction({
        'from': WalletOwner,
        'gasPrice': web3.toWei(config['FeeSetting']['GasApproveFee'], 'gwei'),
        'nonce': web3.eth.get_transaction_count(WalletOwner),
    })

    signed_txn = web3.eth.account.sign_transaction(
    approve, private_key=config['TokenSetup']['PrivateKey'])
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print('[' + date_time + ']' + " [Warn] ----- GENERATING HASH TX -----")
    logging.basicConfig(filename="./SystemLog/Function.Log",  level=logging.INFO)
    logging.info('[' + date_time + ']' + ' APPROVE SELL IS EXECUTE | YOUR TX HASH INFO :: ' + web3.toHex(tx_token))
    print('[' + date_time + ']' + " [Warn] ----- SYSTEM OK, GOING TO SELL -----")
    time.sleep(6) # Waiting Approve TimeStamp
    pancakeswap2_txn = contractbuy.functions.swapExactTokensForTokens(
        balance, 0,
        [TargetContractSell, tokenB],
        WalletOwner,
        (int(time.time()) + 1000000)
    ).buildTransaction({
        'from': WalletOwner,
        'gasPrice': web3.toWei(config['FeeSetting']['GasSellFee'], 'gwei'),
        'nonce': web3.eth.get_transaction_count(WalletOwner),
    })
    signed_txn = web3.eth.account.sign_transaction(
    pancakeswap2_txn, private_key=config['TokenSetup']['PrivateKey'])
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print('[' + date_time + ']' + " [Warn] ----- GENERATING HASH TX -----")
    logging.info('[' + date_time + ']' + ' SELL IS EXECUTE | YOUR TX HASH INFO :: ' + web3.toHex(tx_token))
    print('[' + date_time + ']' + " [Warn] ----- SELL TOKEN SUCCESS -----")
    time.sleep(6)   
    if config['Version']['Type']  == '0':
       webbrowser.open_new_tab('https://bscscan.com/tx/'+web3.toHex(tx_token))
    elif config['Version']['Type']  == '1' :   
       webbrowser.open_new_tab('https://testnet.bscscan.com/tx/'+web3.toHex(tx_token))
    os.system('pause')
    exit() 
# Sell  Function ---------------------------------------------------------------------------------------------------------  

# -----------------------------------------------------------------------------------------------------------

#def monitorrugpulltest():
#     print(style.YELLOW + '[' + date_time + ']' +  "[Token] Starting Monitor RugPull...")
#     nonce = web3.eth.get_transaction_count(WalletOwner)
#     if (nonce != nonce and nonce.data.includes(TargetContractBuy) and nonce.data.includes("0xbaa2abde") and nonce.data.includes("0x02751cec") and nonce.data.includes("0xaf2979eb") and nonce.data.includes("0xded9382a") and nonce.data.includes("0x5b0d5984") and nonce.data.includes("0x2195995c")):
#         print(style.YELLOW + '[' + date_time + ']' +  "[Token] Rugpull Detected...")
#         print(style.YELLOW + '[' + date_time + ']' +  "[Token] Start Selling Token...")
#         if config['Version']['BuyType'] == '0':
#            sell_bnb()
#         elif config['Version']['BuyType'] == '1':
#            sell_busd()
# SMART FUNCTION BUSD ---------------------------------------------------------------------------------------------------------
def LPBUSD():
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S")
    print('[' + date_time + ']' +' [Scan] ----- SCAN LIQUIDITY [BUSD] -----')
    lp = pair
    lpcontract = web3.eth.contract(address=lp, abi=lpabi)
    balance = lpcontract.functions.getReserves().call()
    b = balance[0]
    #print(b)
    if b > 0:
        print('[' + date_time + ']' +' [Scan] ----- LIQUIDITY FOUND [BUSD] -----')
        buy_busd()
    else:
        print('[' + date_time + ']' +' [Scan] ----- LIQUIDITY NOT FOUND [BUSD] -----')
        BUYBUSD()

def SNIPEBUSD():
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S") 
    print('[' + date_time + ']' +' [Scan] ----- SCAN PAIR [BUSD] -----')
    
    global pair
    pair = contract.functions.getPair(TargetContractBuy, busd).call()
    #print('[' + date_time + ']' + pair)
    if pair != web3.toChecksumAddress('0x0000000000000000000000000000000000000000'):
        print('[' + date_time + ']' +' [Scan] ----- PAIR FOUND [BUSD] -----')
        LPBUSD()
# SMART FUNCTION BUSD --------------------------------------------------------------------------------------------------------- 

# CHECKER ---------------------------------------------------------------------------------------------------------------------
def honeypotbuytax():
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S") 
    configApi= ConfigParser()
    configApi.read("SnipeCrypt.ini")
    spamapi = 'https://aywt3wreda.execute-api.eu-west-1.amazonaws.com/default/IsHoneypot?chain=bsc2&token='+configApi['API']['RugAddress']
    response = request.urlopen(spamapi)
    honeycheck = json.loads(response.read())
    if (honeycheck['BuyTax'] >= int(configApi['Premium']['SetBuyTax'])):
        print('[' + date_time + ']' +' [Scan] ----- CHECKER SCAN [ANTIBOT] -----')
        print('[' + date_time + ']' + " [Info] HIGH TAX BUY : ",honeycheck['BuyTax'])
        honeypotbuytax()
    else:
        print('[' + date_time + ']' +' [Scan] ----- CHECKER SCAN [ANTIBOT] -----')
        print('[' + date_time + ']' + " [Info] TAX NORMAL, BUY NOW",honeycheck['BuyTax'])   
        if config['Version']['BuyType'] == '0':
               SNIPEBNB()
        elif config['Version']['BuyType'] == '1':
            buy_busd()
def honeypotselltax():
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S") 
    configApi= ConfigParser()
    configApi.read("SnipeCrypt.ini")
    spamapi = 'https://aywt3wreda.execute-api.eu-west-1.amazonaws.com/default/IsHoneypot?chain=bsc2&token='+configApi['API']['RugAddress']
    response = request.urlopen(spamapi)
    honeycheck = json.loads(response.read())
    if(honeycheck['SellTax'] >= int(configApi['Premium']['SetSellTax'])) :
        print('[' + date_time + ']' + " [Info] HIGH SELL TAX : ",honeycheck['SellTax'] ,"FLOOD SELL HIGH TAX") 
        HONEYPOTSELL()
    else:
        print('[' + date_time + ']' +' [Scan] ----- CHECKER SCAN [ANTIBOT] -----')
        print('[' + date_time + ']' + " [Info] TAX NORMAL, BUY NOW",honeycheck['SellTax'])   
        if config['Version']['BuyType'] == '0':
               sell_bnb()
        elif config['Version']['BuyType'] == '1':
            sell_busd()

run = True
def BUYBNB():
	global run
	SNIPEBNB()
	if run:
		Timer(0, BUYBNB).start()

run = True
def BUYBUSD():
	global run
	SNIPEBUSD()
	if run:
		Timer(0, BUYBUSD).start()

run = True
def HONEYPOTBUY():
	global run
	honeypotbuytax()
	if run:
		Timer(0, HONEYPOTBUY).start()

run = True
def HONEYPOTSELL():
	global run
	honeypotselltax()
	if run:
		Timer(0, HONEYPOTSELL).start()


while True:
    Program()
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S") 
    pil=input( '[' + date_time + ']' +' [Info] Choose : ')
    if pil == '1':
        if config['Version']['BuyType'] == '0':
         BUYBNB()
         break
        elif config['Version']['BuyType'] == '1':
         BUYBUSD()
         break
    if pil == '2':
        if config['Version']['BuyType'] == '0':
         sell_bnb()
         break
        elif config['Version']['BuyType'] == '1':
         sell_busd()
         break
    if pil == '3':
        verifcontract()
        break
    if pil == '6':
        monitor()
        break
    if pil == '0':
        print('[' + date_time + ']' + " [Syst] Application is Restarting...")
        os.system('py SCNTokenPro.pyc')
        break