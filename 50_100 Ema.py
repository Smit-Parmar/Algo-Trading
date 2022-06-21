//@version=2
study(title="EMA", overlay=true)

ema1 = ema(close,50)
ema2 = ema(close,100)

buy=ema1>ema2
sell=ema1<ema2

myPosition = buy==1 ? 0 : sell==1 or myPosition[1]==1 ? 1 : 0
buy_signals=buy and myPosition[1]==1 ? low - 0.005 : na
sell_signals=sell and myPosition[1]==0 ? high + 0.005 : na

plotshape(buy_signals, style=shape.triangleup,style=shape.triangleup, text="BUY",textcolor = green)
plotshape(sell_signals, style=shape.triangledown, style=shape.triangledown, text="SELL",textcolor = red)

alertcondition(buy_signals, title='ema < 30', message='ema is below 30')
alertcondition(sell_signals, title='ema > 70', message='ema is above 70')// © smit_p33