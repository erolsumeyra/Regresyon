# Scipy kütüphanesinde stats modülünü çağırıyoruz
from scipy import stats

# Numpy nümerik hesap kütüphanesi
import numpy as np

# Toplam nokta sayısı
N = 50

# 5'er 5'er artsın
noise=5

# Hep aynı değerleri oluşturması için seed değerini sabitleme
np.random.seed(42)

# x noktaları 1'den 50'ye kadar artsın
x = np.linspace(0,50,N)

# y noktaları lineer bir doğrunun üzerine rastgele gürültü eklenmesi ile 
y = (a*x + b) + np.random.rand(len(x))*noise

plt.figure()

plt.scatter(x, y,color='red')
plt.xlabel("x değerleri")
plt.ylabel("y değerleri")

# x=0 ve y=0 eksenleri
plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.plot(x, slope*x + intercept, 'g', label='Fitted line',color='blue');

plt.title("Lineer regresyon");

print("a: %.2f b: %.2f " % (slope,intercept))
