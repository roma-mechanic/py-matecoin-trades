import json
from decimal import Decimal


def calculate_profit(name_file: str):
    with open(name_file, "r") as trade_info, open("app.main.profit.json'", "w") as f:
        transactions_data = json.load(trade_info)
        matecoin_account = 0
        profit = 0
        for trades in transactions_data:
            if trades["bought"] is None:
                trades["bought"] = 0
            if trades["sold"] is None:
                trades["sold"] = 0

            profit += (Decimal(trades["sold"]) - Decimal(trades["bought"])) * Decimal(trades["matecoin_price"])
            matecoin_account += Decimal(trades["bought"]) - Decimal(trades["sold"])
        result = {"earned_money": str(profit), "matecoin_account": str(matecoin_account)}
        json.dump(result, f, indent=2)
