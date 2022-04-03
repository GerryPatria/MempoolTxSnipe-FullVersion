# Libs Data
from unittest import result
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
from urllib import request
from os import system
sys.setrecursionlimit(10000)
hwid_get = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()


#GenerateLicense ----------------------------------------------------------------------------------
keyserial = 'fdc8afe2bedab325aea3ebffde4d557d8c9af0e9.json' #string license
HotWalletPrivKey = '88662ea0e244d71b23a4eb51b65f9cfb18d1ff025996826a1c5a32d1bde0bf2f' # 0x5D22189b684C4De8BD3C38314c68f7d842278FC4
AppVer = '2.31'

# Read License ------------------------------------------------------------------------------------
LicUrls = 'https://upd.eventoffair.com/app_tracker.json'
response = request.urlopen(LicUrls)
data = json.loads(response.read())
# Get Connector PC
load = data["gerry"]
# Get Connector PC
UserHWID = load[0]["UserConnector"]
AppType = load[0]["AppType"]
VerCheck = load[0]["AppVer"]
ClientStatus = load[0]["Client"]
Status = load[0]["Status"]


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
sender_address = web3.toChecksumAddress(config['TokenSetup']['MyAddress'])
tokenA = web3.toChecksumAddress(config['TokenSetup']['MyTargetContract'])
tokenToSell = web3.toChecksumAddress(config['TokenSetup']['MyTargetContract'])  
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
tokenToBuy = tokenA


# -----------------------------------------------------------------------------------------------------------------------
ascii = """
[1] BUY (FALSE ANTIBOT BYPASS)
[2] SELL (FALSE ANTIBOT BYPASS)
[3] BUY (TRUE ANTIBOT BYPASS)
[4] SELL (TRUE ANTIBOT BYPASS)
[5] VERIF (IF YOU USE BUSD)
[6] MONITOR & TAKE PROFIT (FALSE ANTIBOT BYPASS)
[0] EXIT
Note : 
  • Before Running App You Need Setup Config "Snipecrypt.ini" to Avoid Loss Assets.
  • Read Every Information on Console Before Running Menu.
  • Need Internet Connection Stable. (Internet Not Stable App Will Crash)
  • Function Monitor, If you not have Coin and run this menu, you Will Crash.
"""

# -----------------------------------------------------------------------------------------------------------------------

# Call Function ---------------------------------------------------------------------------------------------
sellTokenContract = web3.eth.contract(tokenToSell, abi=sellAbi)
if config['Version']['BuyType'] == '0':
 buyTokenContract = web3.eth.contract(spend, abi=sellAbi)
elif config['Version']['BuyType'] == '1':
 buyTokenContract = web3.eth.contract(busd, abi=sellAbi)
balance = web3.eth.get_balance(sender_address)
humanReadable = web3.fromWei(balance,'ether')
balance = sellTokenContract.functions.balanceOf(sender_address).call()
symbol = sellTokenContract.functions.symbol().call()
name = sellTokenContract.functions.name().call()
mysymbl = buyTokenContract.functions.symbol().call()
myname = buyTokenContract.functions.name().call()
readable = web3.fromWei(balance,'ether')
balanceWallet = str(readable) + " " + symbol
tokenValue = balance
tokenValue2 = web3.fromWei(tokenValue, 'ether')
# Call Function ---------------------------------------------------------------------------------------------

# SMART FUNCTION BNB ---------------------------------------------------------------------------------------------------------
def LPBNB():
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S")
    print('[' + date_time + ']' +' [Scan] ----- SCAN LIQUIDITY [BNB] -----')
    lp = pair
    lpcontract = web3.eth.contract(address=lp, abi=lpabi)
    balance = lpcontract.functions.getReserves().call()
    b = balance[0]
    #print(b)
    if b > 0:
        print('[' + date_time + ']' +' [Scan] ----- LIQUIDITY FOUND [BNB] -----')
        buy_bnb()
    else:
        print('[' + date_time + ']' +' [Scan] ----- LIQUIDITY NOT FOUND [BNB] -----')
        BUYBNB()

def SNIPEBNB():
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S") 
    print('[' + date_time + ']' +' [Scan] ----- SCAN PAIR [BNB] -----')
    
    global pair
    pair = contract.functions.getPair(tokenA, spend).call()
    #print('[' + date_time + ']' + pair)
    if pair != web3.toChecksumAddress('0x0000000000000000000000000000000000000000'):
        print('[' + date_time + ']' +' [Scan] ----- PAIR FOUND [BNB] -----')
        LPBNB()
# SMART FUNCTION BNB ---------------------------------------------------------------------------------------------------------      

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
    pair = contract.functions.getPair(tokenA, busd).call()
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
               buy_bnb()
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



def Program():
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S")    
    if(hwid_get != UserHWID):
          ctypes.windll.kernel32.SetConsoleTitleW('SnipeCryptBot | V.'+AppVer+' | Failed') 
          print('YOUR CONNECTOR HAS NOT CONNECTED | FAILED GET DATA. CONTACT DEV')
          logging.basicConfig(filename="./SystemLog/Error.Log",  level=logging.INFO)
          logging.info('[' + date_time + ']' + ' YOUR CONNECTOR IS FAILED...')
          os.system('pause')
          exit()
    elif (hwid_get == UserHWID):
     ctypes.windll.kernel32.SetConsoleTitleW('SnipeCryptBot | V.'+AppVer+' | Running | **SharedProfit') 
     print(ascii)
    if(AppVer != VerCheck):
     print('[' + date_time + ']' + ' [Err] YOUR APP IS NOT VERIFIED, UPDATE APP Now BUILD UPDATE :: ',VerCheck)
     logging.basicConfig(filename="./SystemLog/Error.Log",  level=logging.INFO)
     logging.info('[' + date_time + ']' + ' YOUR APP IS NOT VERIFIED..')
     os.system('pause')
     exit()
    elif (hwid_get == UserHWID):
     print('[' + date_time + ']' + ' [Info] WEB3 API CONNECT :: ',web3.isConnected())
    if config['Version']['Type'] == '0':
        print('[' + date_time + ']' + " [Info] VERSION NETWORK: MAINNET")
        logging.basicConfig(filename="./SystemLog/Function.Log",  level=logging.INFO)
        logging.info('[' + date_time + ']' + ' PROGRAM RUNNING , NETWORK IS MAINNET')
    elif config['Version']['Type']  == '1':
        print('[' + date_time + ']' + " [Info] VERSION NETWORK: TESTNET")
        logging.basicConfig(filename="./SystemLog/Function.Log",  level=logging.INFO)
        logging.info('[' + date_time + ']' + ' PROGRAM RUNNING , NETWORK IS TESTNET')
    if config['Version']['BuyType'] == '0':
     print('[' + date_time + ']' + " [Info] TOTAL SWAP: ",config['ProfitSetting']['Purchase'], mysymbl)   
     print('[' + date_time + ']' + " [Info] BALANCE: ",humanReadable,"TOKEN:", mysymbl)
    elif config['Version']['BuyType'] == '1':
     print('[' + date_time + ']' + " [Info] TOTAL SWAP: ",config['ProfitSetting']['Purchase'], mysymbl)   
     print('[' + date_time + ']' + f" [Info] BALANCE SNIPER: {float(tokenValue2)} NAME: {name} SYMBOL: {symbol}.")  
# Call Function Wallet --------------------------------------------------------------------------------------------------
     
    if (str(tokenValue2) == '0'):
         print('[' + date_time + ']' + f" [Info] BALANCE TOKEN: 0 {symbol} {mysymbl}.")  
    elif (str(tokenValue2) > '1'):  
        if config['Version']['BuyType'] == '0':
         test = contractbuy.functions.getAmountsOut(balance,[tokenToSell, spend]).call()
         data = (test[1] * 10 **-0x12)
         print('[' + date_time + ']' + f" [Info] PROFIT BUY: {str(data)} {symbol} -> {mysymbl}.")
        elif config['Version']['BuyType'] == '1':
         test = contractbuy.functions.getAmountsOut(balance,[tokenToSell, tokenB]).call()
         data = (test[1] * 10 **-0x12)
         print('[' + date_time + ']' + f" [Info] PROFIT BUY: {str(data)} {symbol} -> {mysymbl}.")  
        
# Main Menu ------------------------------------------------------------------------------------------------------------- 
def monitor():
 while True:
    # Check Profit Now Function ----------------------------------------------------------------------------------------------  
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S")    

    sellTokenContract = web3.eth.contract(tokenToSell, abi=sellAbi)
    balance = sellTokenContract.functions.balanceOf(sender_address).call()
    buyTokenContract = web3.eth.contract(busd, abi=sellAbi)
    if config['Version']['BuyType'] == '0':
     test = contractbuy.functions.getAmountsOut(balance,[tokenToSell, spend]).call()
    elif config['Version']['BuyType'] == '1':
     test = contractbuy.functions.getAmountsOut(balance,[tokenToSell, busd]).call()
    data = (test[1] * 10 **-0x12)
    data3 = (test[1] * 10 **-0x12) * 5
    datafinal = data3 * int(config['ProfitSetting']['GetProfit'])
    print('[' + date_time + ']','[Info] HOLD/PROFIT (NOW/TP):',"{:.0%}".format(data/100),str(data),"{:.0%}".format(datafinal/100*int(config['ProfitSetting']['GetProfit'])),str(datafinal))
    
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
        'from': sender_address,
        'gasPrice': web3.toWei(config['FeeSetting']['GasApproveFee'], 'gwei'),
        'nonce': web3.eth.get_transaction_count(sender_address),
    })
    signed_txn = web3.eth.account.sign_transaction(
    approve, private_key=config['TokenSetup']['PrivateKey'])
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print('[' + date_time + ']' + " [Warn] ----- GENERATING HASH TX [BUSD] -----")
    logging.basicConfig(filename="./SystemLog/Function.Log",  level=logging.INFO)
    logging.info('[' + date_time + ']' + ' APPROVE [BUSD] IS EXECUTE | YOUR TX HASH INFO :: ' + web3.toHex(tx_token))
    if config['Version']['Type'] == '1':
         webbrowser.open_new_tab('https://testnet.bscscan.com/tx/'+web3.toHex(tx_token))
    elif config['Version']['Type'] == '0':
        webbrowser.open_new_tab('https://bscscan.com/tx/'+web3.toHex(tx_token))
    print('[' + date_time + ']' +' [Warn] ----- SNIPE SUCCESS -----')    
    os.system('pause')
    exit()

# Buy ------------------------------------------------------------------------------------------------------------- 
def buy_bnb():
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S")      
    print('[' + date_time + ']' +' [Buys] ----- START SNIPE [BNB] -----') 
    pancakeswap2_txn = contractbuy.functions.swapExactETHForTokens( 
    0, #FALSE, #--- this function write like? address or?
    [spend,tokenToBuy],
    sender_address,
    (int(time.time()) + 10000)
    ).buildTransaction({
    'from': sender_address,
    'value': web3.toWei(config['ProfitSetting']['Purchase'],'ether'),
    'gas':int(config['FeeSetting']['GasBuyFeeUsed']),
    'gasPrice': web3.toWei(config['FeeSetting']['GasBuyFee'],'gwei'),
    'nonce': web3.eth.get_transaction_count(sender_address),
    })
    signed_txn = web3.eth.account.sign_transaction(pancakeswap2_txn, private_key=config['TokenSetup']['PrivateKey'])
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)    
    print('[' + date_time + ']' + " [Warn] ----- CHECK SYSTEM LOG [BNB] -----")
    logging.basicConfig(filename="./SystemLog/Function.Log",  level=logging.INFO)
    logging.info('[' + date_time + ']' + ' BUYING PROGRAM IS EXECUTE | YOUR TX HASH INFO :: ' + web3.toHex(tx_token))   
    print('[' + date_time + ']' + " [Warn] ----- GENERATING HASH TX [BNB] -----")
    time.sleep(6) 
    if config['Version']['Type'] == '1':
     webbrowser.open_new_tab('https://testnet.bscscan.com/tx/'+web3.toHex(tx_token))
    elif config['Version']['Type'] == '0':
        webbrowser.open_new_tab('https://bscscan.com/tx/'+web3.toHex(tx_token))
    print('[' + date_time + ']' +' [Warn] ----- SNIPE SUCCESS [BNB] -----')    
    os.system('pause')
    exit()
# Buy BUSD -------------------------------------------------------------------------------------------------------------   
def buy_busd():
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S")   
    sellTokenContract = web3.eth.contract(busd, abi=sellAbi)
    print('[' + date_time + ']' +' [Buys] ----- START SNIPE [BUSD] -----')
    amountOutMin  = 0
    pancakeswap2_txn = contractbuy.functions.swapExactTokensForTokens( 
    int(config['ProfitSetting']['Purchase']+'000000000000000000'), 0,
    [tokenB,tokenToBuy],
    sender_address,
    (int(time.time()) + 10000)
    ).buildTransaction({
    'from': sender_address,
    'gas':int(config['FeeSetting']['GasBuyFeeUsed']),
    'gasPrice': web3.toWei(config['FeeSetting']['GasBuyFee'],'gwei'),
    'nonce': web3.eth.get_transaction_count(sender_address),
    })
    signed_txn = web3.eth.account.sign_transaction(pancakeswap2_txn, private_key=config['TokenSetup']['PrivateKey'])
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print('[' + date_time + ']' + " [Warn] ----- CHECK SYSTEM LOG [BUSD] -----")
    logging.basicConfig(filename="./SystemLog/Function.Log",  level=logging.INFO)
    logging.info('[' + date_time + ']' + ' BUYING PROGRAM IS EXECUTE | YOUR TX HASH INFO :: ' + web3.toHex(tx_token))   
    print('[' + date_time + ']' + " [Warn] ----- GENERATING HASH TX [BUSD] -----")
    time.sleep(6) 
    if config['Version']['Type'] == '1':
     webbrowser.open_new_tab('https://testnet.bscscan.com/tx/'+web3.toHex(tx_token))
    elif config['Version']['Type'] == '0':
     webbrowser.open_new_tab('https://bscscan.com/tx/'+web3.toHex(tx_token))
    print('[' + date_time + ']' +' [Warn] ----- SNIPE SUCCESS [BUSD] -----')    
    os.system('pause')
    exit()
# Buy BUSD -------------------------------------------------------------------------------------------------------------  
# Sell  Function BNB ---------------------------------------------------------------------------------------------------------
def sell_bnb():  
    sellTokenContract = web3.eth.contract(tokenToSell, abi=sellAbi)
    balance = sellTokenContract.functions.balanceOf(sender_address).call()
    symbol = sellTokenContract.functions.symbol().call()
    name = sellTokenContract.functions.name().call()
    tokenValue = balance
    tokenValue2 = web3.fromWei(tokenValue, 'ether')
    if(tokenValue2 == 0):
        print('[' + date_time + ']' + f" [Warn] SWAPPING: {tokenValue2} NO TOKEN. EXIT PROGRAM") 
        os.system('pause')
        exit()
    else:
        print('[' + date_time + ']' + f" [Warn] SWAPPING: {tokenValue2} NAME: {name} SYMBOL: {symbol}.") 
    approve = sellTokenContract.functions.approve(panRouterContractAddress, balance
    ).buildTransaction({
        'from': sender_address,
        'gasPrice': web3.toWei(config['FeeSetting']['GasApproveFee'], 'gwei'),
        'nonce': web3.eth.get_transaction_count(sender_address),
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
        [tokenToSell, spend],
        sender_address,
        (int(time.time()) + 1000000)
    ).buildTransaction({
        'from': sender_address,
        'gasPrice': web3.toWei(config['FeeSetting']['GasSellFee'], 'gwei'),
        'nonce': web3.eth.get_transaction_count(sender_address),
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

# Sell  Function BUSD ---------------------------------------------------------------------------------------------------------
def sell_busd():  
    sellTokenContract = web3.eth.contract(tokenToSell, abi=sellAbi)
    balance = sellTokenContract.functions.balanceOf(sender_address).call()
    symbol = sellTokenContract.functions.symbol().call()
    name = sellTokenContract.functions.name().call()
    tokenValue = balance
    tokenValue2 = web3.fromWei(tokenValue, 'ether')
    if(tokenValue2 == 0):
        print('[' + date_time + ']' + f" [Warn] SWAPPING: {tokenValue2} NO TOKEN. EXIT PROGRAM") 
        os.system('pause')
        exit()
    else:
     print('[' + date_time + ']' + f" [Warn] SWAPPING: {tokenValue2} NAME: {name} SYMBOL: {symbol}.") 
     approve = sellTokenContract.functions.approve(panRouterContractAddress, balance
    ).buildTransaction({
        'from': sender_address,
        'gasPrice': web3.toWei(config['FeeSetting']['GasApproveFee'], 'gwei'),
        'nonce': web3.eth.get_transaction_count(sender_address),
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
        [tokenToSell, tokenB],
        sender_address,
        (int(time.time()) + 1000000)
    ).buildTransaction({
        'from': sender_address,
        'gasPrice': web3.toWei(config['FeeSetting']['GasSellFee'], 'gwei'),
        'nonce': web3.eth.get_transaction_count(sender_address),
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


Program()
while True:
    start_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y,%H:%M:%S") 
    pil=input( '[' + date_time + ']' +' [Info] MENU : ')
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
        HONEYPOTBUY()
        break
    if pil == '4':
        HONEYPOTSELL()
        break
    if pil == '5':
        verifcontract()
        break
    if pil == '6':
        monitor()
        break
    if pil == '0':
        exit()
        break