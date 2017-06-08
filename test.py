#!/usr/bin/env python3
# coding:utf-8

import easyquotation
import time

sina_stock = easyquotation.use('sina')

js_load = sina_stock.real('000159')


def getStockInfo(stockid):
    return sina_stock.real(stockid)

def printStockInfo(stockinfo,stockid):
    print("{stock_name} 开盘价：{stock_open} 现价：{stock_now} 买1：{stock_bid1} 卖1:{stock_ask1}".format(stock_name=stockinfo[stockid]['name'],
                                                                                          stock_open=stockinfo[stockid]['open'],
                                                                                          stock_now=stockinfo[stockid]['now'],
                                                                                          stock_bid1=stockinfo[stockid]['bid1'],
                                                                                          stock_ask1=stockinfo[stockid]['ask1']))
# 计算KDJ数据
def getKDJ(dataarr,period):
    KDJ = {}
    PDK = 50
    PDD = 50
    PDJ = 50
    for i in range(0,len(dataarr)-1):
        if i < period:
            continue



while True:
    time.sleep(1)
    stockid = '000159'
    stock_info = getStockInfo(stockid)
    printStockInfo(stock_info,stockid)
