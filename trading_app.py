from flask import Flask, render_template, request
import random
import numpy
import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime

def get_tp_sl(stop,target,buy_or_sell,symbol,lot,point,price):
	if buy_or_sell=="BUY":
		order_type=mt5.ORDER_TYPE_BUY
		sl=float("{0:.4f}".format(price - stop * point *10))
		tp=float("{0:.4f}".format(price + target * point *10))
		return {"symbol":symbol,"lot":lot,"point":point,"price":price,
				"sl":sl,"tp":tp,"buy_or_sell":buy_or_sell,"order_type":order_type}
	else:
		order_type=mt5.ORDER_TYPE_SELL
		sl=float("{0:.4f}".format(price + stop * point *10))
		tp=float("{0:.4f}".format(price - target * point *10))
		return {"symbol":symbol,"lot":lot,"point":point,"price":price,
				"sl":sl,"tp":tp,"buy_or_sell":buy_or_sell,"order_type":order_type}


def symbol_trade(buy_or_sell,symbol,point,price,timeframe): #Get target and stop loss according to currency pairs
	if symbol=="GBPUSDm": #GBPUSD pairs
		if timeframe=="15M":
				lot=0.03
				stop=100
				target=50
				data=get_tp_sl(stop,target,buy_or_sell,symbol,lot,point,price)
				print("GBPUSD 15 min",data)
				return data

	elif symbol=="AUDUSDm": #AUDUSD pair
		if timeframe=="15M":
				lot=0.03
				stop=80
				target=40
				data=get_tp_sl(stop,target,buy_or_sell,symbol,lot,point,price)
				print("AUDUSD 15 min",data)
				return data

	elif symbol=="NZDCADm": #AUDUSD pair
		if timeframe=="15M":
				lot=0.03
				stop=80
				target=40
				data=get_tp_sl(stop,target,buy_or_sell,symbol,lot,point,price)
				print("NZDCAD 15 min",data)
				return data


def get_order(buy_or_sell,symbol,timeframe): #for five munite timeframe
	positions = mt5.positions_get(symbol=symbol)
	print(positions)
	if len(positions)>0:
		for i in positions:
			if str(i[9])==str(lot_size):
				ticket=i[0]
				mt5.Close(symbol,ticket=ticket) #delete previous order

	point = mt5.symbol_info(symbol).point
	price = float("{0:.4f}".format(mt5.symbol_info_tick(symbol).ask))
	data=symbol_trade(buy_or_sell,symbol,point,price,timeframe)
	return data


app = Flask(__name__)
@app.route("/",methods=['GET', 'POST'])
def index():
	if not mt5.initialize(server="Exness-MT5Trial6",login=111111,password="password"):
	    print("initialize() failed")
	    mt5.shutdown()
	else:
		print("initialize")
		if request.method == 'POST':
			order_type=mt5.ORDER_TYPE_SELL
			print(request.data)
			temp=str(request.data).replace("b","")
			temp2=temp.replace("'","")
			print(temp2)
			list1=list(temp2.split(" "))
			print(list1)
			buy_or_sell=list1[0]
			symbol=list1[1]+"m"
			timeframe=list1[2] 
			data={}

			data=get_order(buy_or_sell,symbol,timeframe)

			deviation = 10
			print(data)
			try:
				trade = {
				    "action": mt5.TRADE_ACTION_DEAL,
				    "symbol": data["symbol"],
				    "volume": data["lot"],
				    "type": data["order_type"],
				    "price": data["price"],
				    "sl":data["sl"],
				    "tp":data["tp"],
				    "deviation": deviation,
				    "magic": int(datetime.now().timestamp()),
				    "comment": "python script open",
				    "type_time": mt5.ORDER_TIME_GTC,
				    "type_filling": mt5.ORDER_FILLING_IOC,
				}
				result = mt5.order_send(trade)
				print(result)
				
				return "Trade Placed"
			except Exception as e:
				print(e)
				return "ERROR"


if __name__=="__main__":
    app.run(port=5000)
