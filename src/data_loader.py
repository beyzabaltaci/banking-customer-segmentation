import pandas as pd

def load_customer_data():
    data = pd.DataFrame({
        "customer_id": [1, 2, 3, 4, 5],
        "age": [23, 45, 35, 52, 29],
        "monthly_income": [3000, 9000, 5000, 12000, 4500],
        "credit_card_spend": [1200, 3000, 1800, 5000, 1600],
        "late_payment_count": [3, 0, 1, 0, 2]
    })

    return data
