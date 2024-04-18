from django.shortcuts import render

from django.http import HttpResponseRedirect
from .models import Stock
from .utils import get_data

# Create your views here.

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

    return render(request, 'dsei_app/index.html', data)

    

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

    return render(request, 'dsei_app/charts.html', data)
