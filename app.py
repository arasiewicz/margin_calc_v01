from flask import Flask, request, render_template

app = Flask(__name__)


def calculate_margin(cost_price, selling_price, margin_percent, profit):
    if cost_price and selling_price:
        margin_percent = ((selling_price - cost_price) / cost_price) * 100
        profit = selling_price - cost_price
    elif cost_price and margin_percent:
        selling_price = cost_price + (cost_price * (margin_percent / 100))
        profit = selling_price - cost_price
    elif cost_price and profit:
        selling_price = cost_price + profit
        margin_percent = ((selling_price - cost_price) / cost_price) * 100

    return margin_percent, selling_price, profit


@app.route('/', methods=['GET', 'POST'])
def index():
    margin_percent = selling_price = profit = None

    if request.method == 'POST':
        cost_price = float(request.form.get('cost_price', 0))
        selling_price = request.form.get('selling_price')
        if selling_price:
            selling_price = float(selling_price)
        else:
            selling_price = 0

        # Obsługa pola 'margin_percent'
        margin_percent = request.form.get('margin_percent')
        if margin_percent:
            margin_percent = float(margin_percent)
        else:
            margin_percent = 0

        # Obsługa pola 'profit'
        profit = request.form.get('profit')
        if profit:
            profit = float(profit)
        else:
            profit = 0

        margin_percent, selling_price, profit = calculate_margin(cost_price, selling_price, margin_percent, profit)

    return render_template('index.html', margin_percent=margin_percent, selling_price=selling_price, profit=profit)


if __name__ == '__main__':
    app.run(debug=True)
