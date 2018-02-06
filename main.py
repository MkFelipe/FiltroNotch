import matplotlib.pyplot as plt
from scipy import misc
import cv2
import numpy as np
from pylab import *
import time

#lendo imagem em tons de cinza
img = cv2.imread('lady.jpg',0)

#dimensões da imagem
x,y = img.shape   # valor x,y

#Fourier
ini = time.time()
f1 = np.fft.fft2(img)
f2 = np.fft.fftshift(f1)
timef = time.time()

print "Tempo calculo Fourier: ", timef-ini, 'segundos' 

#calculando spectro da imagem
spectre = 20*np.log(np.abs(f2))

#plotando resultados
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Imagem original')
plt.subplot(122),plt.imshow(spectre, cmap = 'gray')
plt.title('Spectrum')
plt.show()

#matrizes de pontos (cada coluna representa uma coordenada x,y)
matrix1 = [
    [73, 72, 36, 32],
    [52, 19, 71, 52],
]

matrix2 = [
    [110, 136, 136, 176],
    [33, 27, 60, 60],
]

#convertendo matrizes para matrix numpy
matrix1 = np.matrix(matrix1)
matrix2 = np.matrix(matrix2)

#matriz controle
normal = [
    [198 ,198, 198, 198],
    [162, 162, 162, 162],
]


#usando simetria para encontrar pontos do 3ª e 4ª quadrante
matrixr1 =  normal - matrix1 
matrixr2 = normal - matrix2 

w = 3.5
j = 0

#filtrando cada ponto com janela 8x8 definida em W
ini = time.time()
for j in range(4):
    f2[matrix1[1,j]-w:matrix1[1,j]+w, matrix1[0,j]-w:matrix1[0,j]+w] = 1         #aplicando janela de corte 7x7
    f2[matrix2[0,j]-w:matrix1[0,j]+w, matrix1[1,j]-w:matrix1[1,j]+w] = 1
    f2[matrixr1[1,j]-w:matrixr1[1,j]+w, matrixr1[0,j]-w:matrixr1[0,j]+w] = 1
    f2[matrixr2[1,j]-w:matrixr2[1,j]+w, matrixr2[0,j]-w:matrixr2[0,j]+w] = 1

f2[32-w:32+w, 110-w:110+w] = 1        
f2[62-w:62+w, 135-w:135+w] = 1
f2[60-w:60+w, 176-w:176+w] = 1
f2[27-w:27+w, 134-w:134+w] = 1 

f_inverse = np.fft.ifftshift(f2)       
returns = np.fft.ifft2(f_inverse)           #retornando imagem para o domínio espacial
returns = np.abs(returns)                  
timef = time.time() 
print "Tempo aplicação filtro Notch: ", timef-ini, 'segundos'

spectre_filter = 20*np.log(np.abs(f2))

#plotando resultado final
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image')
plt.subplot(132),plt.imshow(returns, cmap = 'gray')
plt.title('Image after Notch')
plt.subplot(133),plt.imshow(spectre_filter, cmap = 'gray')
plt.title('Spectrum after filter')
plt.show()