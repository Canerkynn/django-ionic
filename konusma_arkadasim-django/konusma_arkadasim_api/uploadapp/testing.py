# -*- coding: utf-8 -*-x


import os
import pickle
import sys
from python_speech_features import mfcc
import scipy.io.wavfile as wav

def loadModels():
    global model_A,model_B,model_C,model_CC,model_D,model_E,model_F,model_G,model_GG,model_H;
    global model_I,model_i,model_J,model_K,model_L,model_M,model_N,model_O,model_P,model_R,model_S;
    global model_SS,model_T,model_U,model_UU,model_V,model_Y,model_Z;



    hmmPath = os.path.join('../audio_hmm/hmm', 'a')
    file = open(hmmPath,"rb")
    model_A = pickle.load(file)
    file.close()
    
    
    hmmPath = os.path.join('../audio_hmm/hmm', 'e')
    file = open(hmmPath,"rb")
    model_E = pickle.load(file)
    file.close()
    
    hmmPath = os.path.join('../audio_hmm/hmm', 'ı')
    file = open(hmmPath,"rb")
    model_I = pickle.load(file)
    file.close()
    
    hmmPath = os.path.join('../audio_hmm/hmm', 'i')
    file = open(hmmPath,"rb")
    model_i = pickle.load(file)
    file.close()
    
    hmmPath = os.path.join('../audio_hmm/hmm', 'o')
    file = open(hmmPath,"rb")
    model_O = pickle.load(file)
    file.close()
    
    hmmPath = os.path.join('../audio_hmm/hmm', 'u')
    file = open(hmmPath,"rb")
    model_U = pickle.load(file)
    file.close()
    
    hmmPath = os.path.join('../audio_hmm/hmm', 'ü')
    file = open(hmmPath,"rb")
    model_UU = pickle.load(file)
    file.close()
    

    
def testWav(file):
    (rate,sig) = wav.read(file)
    mfcc_feat_test = mfcc(sig,rate,nfft=4096)
    
    modelSkorA = model_A.score(mfcc_feat_test)
    modelSkorE = model_E.score(mfcc_feat_test)
    modelSkorI = model_I.score(mfcc_feat_test)
    modelSkori = model_i.score(mfcc_feat_test)
    modelSkorO = model_O.score(mfcc_feat_test)
    modelSkorU = model_U.score(mfcc_feat_test)
    modelSkorUU = model_UU.score(mfcc_feat_test)

    
    
    t = max(modelSkorA,modelSkorE,modelSkorI,modelSkori,modelSkorO,modelSkorU,modelSkorUU)
    
    if (t == modelSkorA): return 'a'
    if (t == modelSkorE): return 'e'
    if (t == modelSkorI): return 'ı'
    if (t == modelSkori): return 'i'
    if (t == modelSkorO): return 'o'
    if (t == modelSkorU): return 'u'
    if (t == modelSkorUU): return 'ü'



    
    
if __name__ == '__main__':
    loadModels()
    fileName = 'C:/Users/Lenovo/Desktop/TEZ/tezz/tez_siniflandirici/ses'
    alfabe = "e"
    dogru=0
    yanlis=0
    yanlis_dizi=[]
    for  element in alfabe:
        testFile = fileName+'/'+element+'.wav'
        sonuc = testWav(testFile)
        
        #Sınıflandırmadan çıkan harflere göre pratik yapması için kelime önerisi yapılacaktır.
        if sonuc == 'a':
            print("A harfi için önerilen kelimler")
            onerilenKelimeler = ['haber','asker','kafa'] #Harfin basta,ortada ve sonda olacak şekilde seçilmiştir
            
            for kelime in onerilenKelimeler:
                print(kelime)
               #karşılaştırma işlemi burada yapılmalı
                
        elif sonuc == 'e':
            print("E harfi için önerilen kelimler")
            onerilenKelimeler = ['sevmek','yemek','ilçe']
            
            for kelime in onerilenKelimeler:
                print(kelime)
               #karşılaştırma işlemi burada yapılmalı        
                
        elif sonuc == 'ı':
            print("I harfi için önerilen kelimler")
            onerilenKelimeler = ['yarış','hızlı','ırmak']
            
            for kelime in onerilenKelimeler:
                print(kelime)
               #karşılaştırma işlemi burada yapılmalı  
                
        elif sonuc == 'i':
            print("İ harfi için önerilen kelimler")
            onerilenKelimeler = ['çizgi','isim','pilot']
            
            for kelime in onerilenKelimeler:
                print(kelime)
               #karşılaştırma işlemi burada yapılmalı  
                
        elif sonuc == 'o':
            print("O harfi için önerilen kelimler")
            onerilenKelimeler = ['olta','koşmak','çocuk']
            
            for kelime in onerilenKelimeler:
                print(kelime)
               #karşılaştırma işlemi burada yapılmalı
                
        elif sonuc == 'ö':
            print("Ö harfi için önerilen kelimler")
            onerilenKelimeler = ['ördek','göl','kötü']
            
            for kelime in onerilenKelimeler:
                print(kelime)
               #karşılaştırma işlemi burada yapılmalı
                
        elif sonuc == 'u':
            print("U harfi için önerilen kelimler")
            onerilenKelimeler = ['uzun','kuru','uludağ']
            
            for kelime in onerilenKelimeler:
                print(kelime)
               #karşılaştırma işlemi burada yapılmalı
                   
        elif sonuc == 'ü':
            print("Ü harfi için önerilen kelimler")
            onerilenKelimeler = ['rüya','ücret','ütü']
            
            for kelime in onerilenKelimeler:
                print(kelime)
               #karşılaştırma işlemi burada yapılmalı
        if (str(element)  == sonuc):
           print("dogru tahmin edildi harf : "+sonuc)
           dogru+=1
        else:
           print("yanliş tahmin edildi !! \t doğrusu : "+str(element)+"\t tahmin edilen : "+sonuc)
           yanlis+=1
           yanlis_dizi.append(str(element))
           
        print("dogru tahmin sayisi: "+str(dogru)+"\nyanlis tahmin sayisi: "+str(yanlis))
        print(yanlis_dizi)
    

                
       #print(testWav(testFile))
    