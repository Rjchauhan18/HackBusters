from django.shortcuts import render

# Create your views here.

import os
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Stock
from .utils import get_data,get_model
from django.db.models import Q
import json

stocks = Stock.objects.all() # Get all stocks from the database



def home(request):
    
    # Home Page hero section starting
    Nifty_chart_div = get_data.create_graph('^NSEI',timeframe='1m')
    Nifty_chart = Nifty_chart_div.to_html(full_html=True, default_height=500, default_width=530)

    BankNifty_chart = get_data.create_graph('^NSEBANK',timeframe='1m')
    BankNifty_chart = BankNifty_chart.to_html(full_html=True, default_height=700, default_width=1800)

    Sensex_chart = get_data.create_graph('^BSESN',timeframe='1m')
    Sensex_chart = Sensex_chart.to_html(full_html=True, default_height=700, default_width=1800)



    if 'q' in request.GET:
        search = request.GET['q']

        # searched_stock_sym = Stock.objects.filter(full_name__icontains=search).values_list('symbol', flat=True)[0]
        search = Stock.objects.filter(full_name__icontains=search).values_list('full_name', flat=True)[0]
        # print(searched_stock_sym)
        charts='/chart/?q='+search
        return HttpResponseRedirect(charts)


    data = {
        'stocks': stocks,
        'Nifty_chart':Nifty_chart, 
        'BankNifty_chart':BankNifty_chart, 
        'Sensex_chart':Sensex_chart, 
    }

    return render(request, 'T3_app/index.html', data)

    

def chart(request):
    chart_div = None
    info = None

    if 'q' in request.GET:
        searched_stock = request.GET['q']
        stock_symbol = Stock.objects.filter(full_name__icontains=searched_stock).values_list('symbol', flat=True)[0]

        #Searched stocks graph
        fig = get_data.create_graph(stock_symbol,timeframe='5m') 
        chart_div = fig.to_html(full_html=True, default_height=700, default_width=1800)

        #Searched stocks info
        info = get_data.get_info(stock_symbol)

    data={
        'stocks': stocks,
        'searched_stock': stock_symbol,
        'chart_div': chart_div,
        'info': info
    }

    return render(request, 'T3_app/charts.html', data)

def ta(request):
    decision_tree_chart = None
    decision1_tree_chart = None
    randomeforest_tree_chart = None
    xgboost_tree_chart = None



    if 'q' in request.GET:
        search = request.GET['q']

        # searched_stock_sym = Stock.objects.filter(full_name__icontains=search).values_list('symbol', flat=True)[0]
        search = Stock.objects.filter(full_name__icontains=search).values_list('full_name', flat=True)[0]
        # print(searched_stock_sym)
        charts='/chart/?q='+search
        return HttpResponseRedirect(charts)


    # stocks_list = Stock.objects.all() # Get all stocks from the database
    
    # searched_stock = None
    # searched_stock_sym = None
    # decision_tree_chart = None
    # if 'selected_stock' in request.POST:
    #     searched_stock_sym = request.POST.get('selected_stock')
    #     print(searched_stock_sym)
    #     print(type(searched_stock_sym))
    #     searched_stock= Stock.objects.filter(symbol__icontains=searched_stock_sym).values_list('full_name', flat=True)[0]
    #     fig1= get_model.fetch_data_and_predict('ITC.NS')

    #     decision_tree_chart = fig1.to_html(full_html=True, default_height=700, default_width=1800)
    fig= get_model.DecisionTree_model_predict('^NSEI')
    fig1= get_model.DecisionTree_predict('^NSEI')
    fig2= get_model.RandomForest_predict('^NSEI')
    fig3= get_model.XgBoost_predict('^NSEI')
    
    decision_tree_chart = fig.to_html(full_html=True, default_height=700, default_width=1800)
    decision1_tree_chart = fig1.to_html(full_html=True, default_height=700, default_width=1800)
    randomeforest_tree_chart = fig2.to_html(full_html=True, default_height=700, default_width=1800)
    xgboost_tree_chart = fig3.to_html(full_html=True, default_height=700, default_width=1800)
    
    data={
        'stocks':stocks,
        'decision_tree_chart':decision_tree_chart,
        'decision1_tree_chart':decision1_tree_chart,
        'randomeforest_tree_chart':randomeforest_tree_chart,
        'xgboost_tree_chart':xgboost_tree_chart
    }
    return render(request, 'T3_app/technical.html',data)


def fundamental(request):



    if 'q' in request.GET:
        search = request.GET['q']

        # searched_stock_sym = Stock.objects.filter(full_name__icontains=search).values_list('symbol', flat=True)[0]
        search = Stock.objects.filter(full_name__icontains=search).values_list('full_name', flat=True)[0]
        # print(searched_stock_sym)
        charts='/chart/?q='+search
        return HttpResponseRedirect(charts)

    data={
        'stocks':stocks
    }
    return render(request, 'T3_app/fundamental.html',data)


def about(request):

    if 'q' in request.GET:
        search = request.GET['q']

        # searched_stock_sym = Stock.objects.filter(full_name__icontains=search).values_list('symbol', flat=True)[0]
        search = Stock.objects.filter(full_name__icontains=search).values_list('full_name', flat=True)[0]
        # print(searched_stock_sym)
        charts='/chart/?q='+search
        return HttpResponseRedirect(charts)


    data={
        'stocks':stocks
    }
    return render(request, 'T3_app/about.html',data)