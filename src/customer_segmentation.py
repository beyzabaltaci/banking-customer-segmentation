from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
def segment_customers(data):
    X = data[["age", "monthly_income", "credit_card_spend"]]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=3, random_state=42)
    data["segment"] = kmeans.fit_predict(X_scaled)

    data["segment"].value_counts().sort_index().plot(kind="bar")
    plt.title("Müşteri Segment Dağılımı")
    plt.xlabel("Segment")
    plt.ylabel("Müşteri Sayısı")
    plt.savefig("../visuals/segment_distribution.png", bbox_inches="tight")
    plt.close()

    return data


