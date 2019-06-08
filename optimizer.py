import HHO as hho
import GA as ga
import functions
import csv
import numpy
import time

# Fonksiyon Değerleri
def selector(algo,func_details,popSize,Iterasyon):
    function_name=func_details[0]
    lb=func_details[1]
    ub=func_details[2]
    dim=func_details[3]
    x=hho.HHO(getattr(functions, function_name), lb, ub, dim, popSize, Iterasyon)

    # Algoritma listesi
    if(algo==0):
        x=hho.HHO(getattr(functions, function_name),lb,ub,dim,popSize,Iterasyon)
    if(algo==1):
        x=ga.GA(getattr(functions, function_name),lb,ub,dim,popSize,Iterasyon)
    return x

# Çalışmasını istediğiniz algoritmaları "True" ile belirtiniz.
HHO=True
GA=False

# Çalışmasını istediğiniz fonksiyonları "True" ile belirtiniz.
F1=True
F2=True
F3=True
F4=True
F5=True
F6=True
F7=True
F8=True
F9=True
F10=True
F11=True
F12=True
F13=True
F14=True
F15=True
F16=True
F17=True
F18=True
F19=True
F20=True
F21=True
F22=True
F23=True

algorithm=[HHO,GA]
func=[F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15,F16,F17,F18,F19,F20,F21,F22,F23]
        
# Fonksiyonun tekrar sayısını belirtiniz
FuncAgain=1

# Genel Parametreler
PopulationSize = 500
Iterations= 50

# Excel formatında çıktı almak isterseniz "True" ile belirtiniz.
Export=True

# ExportToFile= Dosya adı ve formatı
ExportToFile="kontrol-"+time.strftime("%Y-%m-%d-%H-%M-%S")+".csv"

# En az bir kere çalışıp çalışmadığını kontrol eden değişken
Flag=True

# İterasyon isimlerinin gönderileceği değişken dizisi
CnvgHeader=[]
for l in range(0,Iterations):
	CnvgHeader.append("Iterasyon - "+str(l+1))

for i in range (0, len(algorithm)): # Algoritma dizisindeki değerleri kontrol eder
    for j in range (0, len(func)): # Fonksiyon dizisindeki değerleri kontrol eder
        if((algorithm[i]==True) and (func[j]==True)): # Değerlerin "True" olup olmadığını kontrol eder
            for k in range (0,FuncAgain): # Fonksiyonların kaç kez çalışacağını kontrol eder

                func_details=functions.getFunctionDetails(j)
                x=selector(i,func_details,PopulationSize,Iterations)
                if(Export==True): # CSV formatında çıktı alınıp alınmayacağını kontrol eder
                    with open(ExportToFile, 'a',newline='\n') as out:
                        writer = csv.writer(out,delimiter=',')
                        if (Flag==False): # just one time to write the header of the CSV file
                            # header= numpy.concatenate([["Algoritma","Fonksiyon","Baslama Zamani","Bitis Zamani","Calisma Suresi"],CnvgHeader])
                            header= numpy.concatenate([["Algoritma","Fonksiyon","Calisma Suresi"],CnvgHeader])
                            writer.writerow(header)
                        # a=numpy.concatenate([[x.optimizer,x.objfname,x.startTime,x.endTime,x.executionTime],x.convergence])
                        a=numpy.concatenate([[x.optimizer,x.objfname,x.executionTime],x.convergence])
                        writer.writerow(a)
                    out.close()
                Flag=True # at least one experiment

if (Flag==False): # Faild to run at least one experiment
    print("No Optomizer or Cost function is selected. Check lists of available optimizers and cost functions")
