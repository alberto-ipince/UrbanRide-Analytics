import pandas as pd
import random
import numpy as np
import os

random.seed(42)
np.random.seed(42)

NUM_PAYMENTS = 120000

payment_methods = [
    "Cash",
    "Credit Card",
    "Debit Card",
    "Digital Wallet"
]

transaction_statuses = [
    "Completed",
    "Refunded",
    "Pending"
]

payments = []

for payment_id in range(1, NUM_PAYMENTS + 1):

    payment_method = random.choices(
        payment_methods,
        weights=[0.35, 0.30, 0.20, 0.15]
    )[0]

    discount_applied = round(
        max(0, np.random.normal(2, 3)),
        2
    )

    tip_amount = round(
        max(0, np.random.normal(4, 5)),
        2
    )

    transaction_status = random.choices(
        transaction_statuses,
        weights=[0.94, 0.03, 0.03]
    )[0]

    payment = {
        "payment_id": payment_id,
        "payment_method": payment_method,
        "discount_applied": discount_applied,
        "tip_amount": tip_amount,
        "transaction_status": transaction_status
    }

    payments.append(payment)

payments_df = pd.DataFrame(payments)

current_dir = os.path.dirname(__file__)

output_path = os.path.join(
    current_dir,
    "../../data/raw/payments.csv"
)

payments_df.to_csv(output_path, index=False)

print("payments.csv generated successfully")