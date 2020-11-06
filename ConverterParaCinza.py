import os, cv2

diretorio = 'caminho das imagens coloridas'
arquivos = os.listdir(diretorio)
Count = 0
for a in arquivos:
	
 	imgColorida = cv2.imread(diretorio+'/'+a)
 	print(a)
 	imgTonsDeCinza = cv2.cvtColor(imgColorida, cv2.COLOR_BGR2GRAY)
 	Count = Count + 1
 	cv2.imwrite(diretorio+'img'+str(Count)+'.jpg', imgTonsDeCinza)