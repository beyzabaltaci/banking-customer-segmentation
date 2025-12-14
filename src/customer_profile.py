import pandas as pd
pd.set_option('display.max_columns', None)
import matplotlib.pyplot as plt

def profile_customers(data):
    data["income_group"] = pd.cut(
        data["monthly_income"],
        bins=[0, 4000, 8000, 15000],
        labels=["Düşük Gelir", "Orta Gelir", "Yüksek Gelir"]
    )

    data["income_group"].value_counts().sort_index().plot(kind="bar")
    plt.title("Müşteri Gelir Segmenti Dağılımı")
    plt.xlabel("Gelir Segmenti")
    plt.ylabel("Müşteri Sayısı")
    plt.savefig("../visuals/income_segment_distribution.png", bbox_inches="tight")
    plt.close()
    return data