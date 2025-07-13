import os

project_dir = "/mnt/data/optimasi-produksi"

# Struktur direktori
dirs = [
    project_dir,
    os.path.join(project_dir, "data")
]

# Buat direktori
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Isi file main.py (Streamlit app)
main_py = '''\
import streamlit as st
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value
import matplotlib.pyplot as plt
import numpy as np

st.title("Aplikasi Optimasi Produksi (Linear Programming)")

st.markdown("### Input Data Produksi")
num_products = st.number_input("Jumlah Produk", min_value=2, max_value=5, value=2)

profits = []
for i in range(num_products):
    profits.append(st.number_input(f"Keuntungan per unit produk x{i+1}", value=10.0))

num_constraints = st.number_input("Jumlah Batasan", min_value=1, max_value=3, value=2)
constraints = []
rhs = []

st.markdown("### Input Batasan")
for j in range(num_constraints):
    st.markdown(f"Batasan {j+1}")
    coefs = []
    for i in range(num_products):
        coefs.append(st.number_input(f"Koefisien x{i+1} (Batasan {j+1})", key=f"{i}_{j}", value=1.0))
    constraints.append(coefs)
    rhs.append(st.number_input(f"Nilai maksimum batasan {j+1}", value=100.0, key=f"rhs_{j}"))

if st.button("Hitung Solusi Optimal"):
    model = LpProblem("Optimasi_Produksi", LpMaximize)
    x = [LpVariable(f"x{i+1}", lowBound=0) for i in range(num_products)]
    model += lpSum([profits[i] * x[i] for i in range(num_products)]), "Total_Keuntungan"
    for j in range(num_constraints):
        model += lpSum([constraints[j][i] * x[i] for i in range(num_products)]) <= rhs[j]

    model.solve()

    st.success("Solusi ditemukan:")
    for var in model.variables():
        st.write(f"{var.name} = {var.value()}")
    st.write(f"Total Keuntungan = {value(model.objective)}")

    if num_products == 2:
        # Visualisasi area feasible untuk 2 variabel
        x_vals = np.linspace(0, max(rhs) + 10, 400)
        plt.figure(figsize=(8, 6))
        for j in range(num_constraints):
            y_vals = [(rhs[j] - constraints[j][0]*x)/constraints[j][1] if constraints[j][1] != 0 else np.nan for x in x_vals]
            plt.plot(x_vals, y_vals, label=f"Batasan {j+1}")
        plt.xlabel("x1")
        plt.ylabel("x2")
        plt.xlim(left=0)
        plt.ylim(bottom=0)
        plt.title("Area Feasible")
        plt.legend()
        st.pyplot(plt.gcf())
'''

# Isi file requirements.txt
requirements_txt = '''\
streamlit
pulp
matplotlib
numpy
'''

# Isi file README.md
# Aplikasi Optimasi Produksi (Linear Programming)

## Fitur
- Input jumlah produk dan batasan sumber daya
- Visualisasi area feasible (untuk 2 variabel)
- Output solusi optimal dan total keuntungan

## Cara Menjalankan

```bash
pip install -r requirements.txt
streamlit run main.py
