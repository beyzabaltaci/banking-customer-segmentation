def credit_decision(score):
    return "Approved" if score >= 600 else "Rejected"

def apply_credit_decision(data):
    data["credit_decision"] = data["risk_score"].apply(credit_decision)
    return data
