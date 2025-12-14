def risk_label(late_payment):
    if late_payment == 0:
        return "Low"
    elif late_payment <= 2:
        return "Medium"
    else:
        return "High"
def risk_to_score(risk):
    if risk == "Low":
        return 800
    elif risk == "Medium":
        return 600
    else:
        return 400

def apply_risk_scoring(data):
    data["risk_level"] = data["late_payment_count"].apply(risk_label)
    data["risk_score"] = data["risk_level"].apply(risk_to_score)
    return data
