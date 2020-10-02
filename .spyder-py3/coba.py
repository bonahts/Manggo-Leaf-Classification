#bar plot
import matplotlib.pyplot as plt
import pandas as pd
kategori = ['Golek', 'Gadung', 'Arumanis', 'Lalijowo']
jumlah = [50, 30, 100, 80]

fig,ax = plt.subplots()
_ = ax.bar(kategori, jumlah)
_ = ax.set_xlabel('Kategori')
_ = ax.set_ylabel('Jumlah')
_ = ax.set_title ('Jenis Tanaman Mangga')