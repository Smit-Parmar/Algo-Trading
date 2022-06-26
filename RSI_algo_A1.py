study("RSI Algo", overlay=true)
myPeriod = input(defval=14, type=integer, title="Period")
myThresholdUp = input(defval=60, type=float, title="Upper Threshold")
myThresholdDn = input(defval=40, type=float, title="Lower Threshold")
myAlgoFlipToggle = input(defval=false, type=bool, title="Imverse Algorthim")
myLineToggle = input(defval=true, type=bool, title="Show Lines")
myLabelToggle = input(defval=true, type=bool, title="Show Labels")
myRSI=rsi(close, myPeriod)
buy = myAlgoFlipToggle ? falling(myRSI,1) and cross(myRSI, myThresholdDn) : rising(myRSI, 1) and cross(myRSI,myThresholdUp)
sell = myAlgoFlipToggle ? rising(myRSI, 1) and cross(myRSI,myThresholdUp) : falling(myRSI,1) and cross(myRSI, myThresholdDn)
myPosition = buy==1 ? 0 : sell==1 or myPosition[1]==1 ? 1 : 0
trendColor = buy ? red : sell ? green : na

buy_entry=myLabelToggle ? buy and myPosition[1]==1 ? low - 0.005 : na : na
sell_entry=myLabelToggle ? sell and myPosition[1]==0 ? high + 0.005 : na : na

plotshape(myLabelToggle ? buy and myPosition[1]==1 ? low - 0.005 : na : na, style=shape.triangleup, text="BUY",textcolor = green)
plotshape(myLabelToggle ? sell and myPosition[1]==0 ? high + 0.005 : na : na,style=shape.triangledown, text="SELL",textcolor = red)

alertcondition(myLabelToggle ? buy and myPosition[1]==1 ? low - 0.005 : na : na, title='buy new', message='BUY')
alertcondition(myLabelToggle ? sell and myPosition[1]==0 ? high + 0.005 : na : na, title='sell new', message='SELL')


###################################################################
study("RSI Algo", overlay=true)
myPeriod = input(defval=14, type=integer, title="Period")
myThresholdUp = input(defval=70, type=float, title="Upper Threshold")
myThresholdDn = input(defval=30, type=float, title="Lower Threshold")
myAlgoFlipToggle = input(defval=false, type=bool, title="Imverse Algorthim")
myLineToggle = input(defval=true, type=bool, title="Show Lines")
myLabelToggle = input(defval=true, type=bool, title="Show Labels")
myRSI=rsi(close, myPeriod)
buy = myAlgoFlipToggle ? falling(myRSI,1) and cross(myRSI, myThresholdDn) : rising(myRSI, 1) and cross(myRSI,myThresholdUp)
sell = myAlgoFlipToggle ? rising(myRSI, 1) and cross(myRSI,myThresholdUp) : falling(myRSI,1) and cross(myRSI, myThresholdDn)
myPosition = buy==1 ? 0 : sell==1 or myPosition[1]==1 ? 1 : 0
trendColor = buy ? red : sell ? green : na
plot(myLineToggle ? buy and myPosition[1]==1 ? low - 0.004: sell and myPosition[1]==0 ? high + 0.004 : na : na, color=trendColor, style=line, linewidth=4, editable=false)
plotshape(myLabelToggle ? buy and myPosition[1]==1 ? low - 0.005 : na : na, style=shape.labelup, location=location.absolute, text="Buy", transp=0, textcolor = white, color=black, editable=false)
plotshape(myLabelToggle ? sell and myPosition[1]==0 ? high + 0.005 : na : na, style=shape.labeldown, location=location.absolute, text="Sell", transp=0, textcolor = white, color=black, editable=false)
alertcondition(myLabelToggle ? buy and myPosition[1]==1 ? low - 0.005 : na : na, title='buy new', message='BUY')
alertcondition(myLabelToggle ? sell and myPosition[1]==0 ? high + 0.005 : na : na, title='sell new', message='SELL')

##############################################################################
study("RSI Algo", overlay=true)
myPeriod = input(defval=14, type=integer, title="Period")
myThresholdUp = input(defval=70, type=float, title="Upper Threshold")
myThresholdDn = input(defval=30, type=float, title="Lower Threshold")
myAlgoFlipToggle = input(defval=false, type=bool, title="Imverse Algorthim")
myLineToggle = input(defval=true, type=bool, title="Show Lines")
myLabelToggle = input(defval=true, type=bool, title="Show Labels")
myRSI=rsi(close, myPeriod)
buy = myAlgoFlipToggle ? falling(myRSI,1) and cross(myRSI, myThresholdDn) : rising(myRSI, 1) and cross(myRSI,myThresholdUp)
sell = myAlgoFlipToggle ? rising(myRSI, 1) and cross(myRSI,myThresholdUp) : falling(myRSI,1) and cross(myRSI, myThresholdDn)
myPosition = buy==1 ? 0 : sell==1 or myPosition[1]==1 ? 1 : 0
trendColor = buy ? red : sell ? green : na
plot(myLineToggle ? buy and myPosition[1]==1 ? low - 0.004: sell and myPosition[1]==0 ? high + 0.004 : na : na, color=trendColor, style=line, linewidth=4, editable=false)
plotshape(myLabelToggle ? buy and myPosition[1]==1 ? low - 0.005 : na : na, style=shape.labelup, location=location.absolute, text="Buy", transp=0, textcolor = white, color=black, editable=false)
plotshape(myLabelToggle ? sell and myPosition[1]==0 ? high + 0.005 : na : na, style=shape.labeldown, location=location.absolute, text="Sell", transp=0, textcolor = white, color=black, editable=false)
