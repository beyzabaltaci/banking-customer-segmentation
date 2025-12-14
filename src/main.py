from data_loader import load_customer_data
from customer_profile import profile_customers
from risk_scoring import apply_risk_scoring
from credit_decision import apply_credit_decision
from customer_segmentation import segment_customers

data = load_customer_data()
data = profile_customers(data)
data = apply_risk_scoring(data)
data = apply_credit_decision(data)
data = segment_customers(data)
print(data)
