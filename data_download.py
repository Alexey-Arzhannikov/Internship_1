import yfinance as yf


def fetch_stock_data(ticker, period):
    """ Получает исторические данные об акциях для указанного тикера и временного периода.
    Возвращает DataFrame с данными."""
    stock = yf.Ticker(ticker)
    if len(period) > 3:
        list_with_space = period.split(',')
        start, end = [elem.strip() for elem in list_with_space]
        data = stock.history(start=start, end=end)
        return data
    else:
        data = stock.history(period=period)
        return data


def calculate_and_display_average_price(data):
    """Вычисляет и выводит среднюю цену закрытия акций за заданный период."""
    average_price = data['Close'].mean(axis=0)
    print(f'\nСредняя цена закрытия акций за заданный период: {average_price}\n')
    return data


def notify_if_strong_fluctuations(data, threshold=15):
    """Функция уведомляет пользователя, если цена акций колебалась более чем на заданный процент за период."""
    percent = (data['Close'].max() - data['Close'].min()) / data['Close'].mean() * 100

    if percent >= threshold:
        print(f'цена акций колебалась на {percent}%')
