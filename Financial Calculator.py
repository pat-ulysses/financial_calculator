# -*- coding: utf-8 -*-
"""Kalkulator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bB-U2Ou-weh4ufw0QTZveSnboySiChIZ
"""

#Import library yang digunakan untuk plot pie chart
import matplotlib.pyplot as plt
import numpy as np

#Fungsi Kalkulator Retirement Fund
def f1():
    "==========================Input User=============================="
    print('\n---Welcome to Retirement Fund Calulator---')
    cost=(input("Current living cost (per month) : "))
    currentage=input('Current Age : ')
    dead=(input('Expected Age : '))
    retire=(input('Expected Retirement Age : '))
    inflation=(input("Inflation assumption (per year in percentage) : "))
    i=(input('Invesment Return Rate (per year in percentage) : '))

    "==========================Check Input=============================="
    while cost.isnumeric()==False:
        cost=input("Current living cost (per month) : ")
    else :
        cost=float(cost)
        while cost<0:
            cost=float(input("Please input valid education cost (per year) : "))

    while inflation.isnumeric()==False:
        inflation=input("Inflation assumption (per year in percentage) : ")
    else :
        inflation=float(inflation)/100
        while inflation <0 or inflation >1 :
            inflation=float(input("Please input valid Inflation (per year in percentage) : "))/100

    while i.isnumeric()==False:
        i=input('Invesment Return Rate (per year in percentage) : ')
    else :
        i=float(i)/100
        while i<0 or i>1:
            i=float(input('Please input valid Return Rate (per year in percentage) : '))/100

    while currentage.isnumeric()==False:
        currentage=input('Current Age : ')
    else:
        currentage=float(currentage)
        while currentage%1!=0 or currentage<0:
            currentage=float(input('Please input valid current Age (age cannot have decimals) : '))

    while retire.isnumeric()==False:
        retire=(input('Expected Retirement Age : '))
    else:
        retire=float(retire)
        while retire<0 or retire%1!=0:
            retire=float(input('Expected Retirement Age : '))

    while dead.isnumeric()==False:
        dead=(input('Expected Age : '))
    else:
        dead=float(dead)
        while dead%1!=0:
            dead=float(input('Expected Age (expected age cannot have decimals) : '))

    while currentage >= retire or currentage >= dead:
        currentage=float(input('Current age cannot be larger than retirement age or expected age : '))

    while retire >=dead:
        retire=float(input('Expected retirement age cannot be larger than expected age : '))
    "=================================================================="
    invesmentperiod=retire-currentage  #Mencari periode investasi dengan mengurangi umur pensiun dengan umur sekarang
    pensionperiod=dead-retire #Mencari periode pensiun dengan mengurangi expected age dengan umur pensiun
    currentyearly=cost*12 #Mencari total uang yang dibutuhkan untuk bertahan hidup per tahun
    futureyearly=currentyearly*((1+inflation)**invesmentperiod) #Mencari Future Value yearly living cost
    sumannliving=((1+inflation)**(pensionperiod)-1)/inflation #Mencari nilai annuitas yearly living cost selama periode pensiun


    i12=(1+i)**(1/12)-1 #Mencari interest rate yang dicompound 12 kali 1 tahun
    sumanninv=((1+i12)**(12*invesmentperiod)-1)/i12 #Mencari nilai future value dari annuity selama masa investasi
    ann=(1-(1+i12)**(-12*invesmentperiod))/i12 #Mencari nilai annuity selama masa investasi

    "=================================================================="
    targetfuture=futureyearly*sumannliving #Mencari total uang yang harus dikumpulkan pada waktu masa akhir pensiun
    monthlyinstallment=targetfuture/sumanninv #Mencari uang yang harus dikumpulkan setiap bulan agar bisa mencapai target
    lumpsum=monthlyinstallment*ann #Mencari total uang yang perlu untuk ditabung sekali pada masa awal investasi agar dapat memenuhi target

    "=================================================================="
    print('\nYour target adjusted after inflation is',targetfuture)
    print('Monthly Installment to be invested every month to achieve target',monthlyinstallment)
    print('Lumpsum amount to be invesed once at the beginning of the invesment period',lumpsum)
#Fungsi Kalkulator Investasi
def f2():
    #Fungsi menghasilkan output jika user memilih pilihan 1 atau 3 pada pertanyaan 'How your money is contributed'
    def output13():
        totalcontributions=additional*time #Menghitung tambahan dana selama masa investasi
        totalinterest=total-(starting_amount+totalcontributions) #Menghitung total bunga yang didapatkan selama masa investasi
        print('\nYour end balance is',total)
        print('Your starting amount is',starting_amount)
        print('Your total contributions is', totalcontributions)
        print('Your total interest is', totalinterest)
        pie=np.array([totalinterest,totalcontributions,starting_amount]) #Membentuk array untuk ditunjukan pada pie chart
        pielabels=['Total Interest','Total Contributions','Starting Amount'] #Label untuk pie chart
        plt.pie(pie,labels=pielabels,startangle=90,autopct='%1.0f%%') #Plot pie chart dengan label dan persentase
        plt.show #Menunjukan plot

    #Fungsi menghasilkan output jika user memilih pilihan 2 atau 4 pada pertanyaan 'How your money is contributed'
    def output24():
        totalcontributions=12*additional*time #Menghitung tambahan dana selama masa investasi
        totalinterest=total-(starting_amount+totalcontributions) #Menghitung total bunga yang didapatkan selama masa investasi
        print('\nYour end balance is',total)
        print('Your starting amount is',starting_amount)
        print('Your total contributions is', totalcontributions)
        print('Your total interest is', totalinterest)
        pie=np.array([totalinterest,totalcontributions,starting_amount]) #Membentuk array untuk ditunjukan pada pie chart
        pielabels=['Total Interest','Total Contributions','Starting Amount'] #Label untuk pie chart
        plt.pie(pie,labels=pielabels,startangle=90,autopct='%1.0f%%') #Plot pie chart dengan label dan persentase
        plt.show #Menunjukan plot


    #InputUser1
    print('\n---Welcome to Invesment Calulator---')
    time=input('Please input the amount of time your money is invested (in years): ')
    returnrate=input('Please input your invesment return rate (in %): ')
    starting_amount=input('Please input starting amount : ')
    additional=input('Please input your additional contribution :')

    #InputUser2
    print('How is your interest rate compounded?')
    print('1. Annualy')
    print('2. Semi-Annualy')
    print('3. Quarterly')
    print('4. Monthly')
    compound=input('Please input how your interest rate is compounded :')

    #InputUser3
    print('How is your money contributed ?')
    print('1. At the end of each year ')
    print('2. At the end of each month')
    print('3. At the beginning of each year')
    print('4. At the beginning of each month')
    choice=input('Please choose how your money is contributed : ')

    #Check Input (untuk memeriksa jika input user sesuai dengan yang program inginkan)
    choices=['1','2','3','4']
    compounds=['1','2','3','4']

    while starting_amount.isnumeric()==False:
        starting_amount=input('Please input starting amount : ')
    else:
        starting_amount=float(starting_amount)
        while starting_amount<0: #Memeriksa starting amount agar tidak lebih kecil dari 0
            starting_amount=float(input('Please input valid starting amount : '))

    while additional.isnumeric()==False:
        additional=input('Please input your additional contribution :')
    else:
        additional=float(additional)
        while additional<0: #Memeriksa additional agar tidak lebih kecil dari 0
            additional=float(input('Please a valid additional contribution :'))

    while time.isnumeric()==False:
        time=input("Amount of time to achieve your target (years): ")
    else:
        time=float(time)
        while time%1!=0 or time<0:
            time=float(input("Please input valid amount of time to achieve your target (time cannot have decimal places): "))

    while returnrate.isnumeric()==False:
         returnrate=input('Invesment Return Rate (in %) : ')
    else :
         returnrate=float(returnrate)/100
         while returnrate<0 or returnrate>1:
             returnrate=float(input('Please input valid Return Rate (in %) : '))/100

    while compound not in compounds:
        print('How is your interest rate compounded?')
        print('1. Annualy')
        print('2. Semi-Annualy')
        print('3. Quarterly')
        print('4. Monthly')
        compound=input('Please choose the number of how your interest rate is compounded :')
    while choice not in choices:
        print('How is your money contributed ?')
        print('1. At the end of each year ')
        print('2. At the end of each month')
        print('3. At the beginning of each year')
        print('4. At the beginning of each month')
        choice=input('Please choose the number of how your money is contributed?: ')

    #Proses Kalkulasi
    if compound=='1': #Jika user memilih interest rate yang diinput compounded per tahun (i)
        i=returnrate #Menyatakan return rate sebagai variabel i(return rate compounded per tahun)
        d=i/(1+i) #Mencari nilai diskonto dengan nilai interest
        i12=((1+i)**(1/12)-1) #Mencari interest rate yang dicompound 12 kali setahun
        d12=1-((1+i12)**(-12/12)) #Mencari diskonto yang dicompound 12 kali setahun
        if choice=='1':#Jika user memilih uang ditambahkan pada akhir setiap tahun selama n tahun
            sumann=((1+i)**(time)-1)/i
            lumpsum=starting_amount*((1+i)**(time)) #Mencari Future Value sejumlah uang yang diinvest pada masa awal investasi
            additioninv=additional*sumann #Mencari nilai total semua uang yang ditambahakan selama n tahun
            total=lumpsum+additioninv #Mencari total uang yang didapat di masa akhir investasi
            output13()
        elif choice=='2': #Jika user memilih uang ditambahkan pada akhir setiap bulan selama n tahun
            sumann=((1+i12)**(12*time)-1)/i12
            lumpsum=starting_amount*((1+i)**(time)) #Mencari Future Value sejumlah uang yang diinvest pada masa awal investasi
            additioninv=additional*sumann #Mencari nilai total semua uang yang ditambahakan selama n tahun
            total=lumpsum+additioninv #Mencari total uang yang didapat di masa akhir investasi
            output24()
        elif choice=='3': #Jika user memilih uang ditambahkan pada awal setiap tahun selama n tahun
            sumangn=((1+i)**(time)-1)/d
            lumpsum=starting_amount*((1+i)**(time)) #Mencari Future Value sejumlah uang yang diinvest pada masa awal investasi
            additioninv=additional*sumangn #Mencari nilai total semua uang yang ditambahakan selama n tahun
            total=lumpsum+additioninv #Mencari total uang yang didapat di masa akhir investasi
            output13()
        elif choice=='4': #Jika user memilih uang ditambahkan pada awal setiap bulan selama n tahun
            sumangn=((1+i12)**(12*time)-1)/d12
            lumpsum=starting_amount*((1+i)**(time)) #Mencari Future Value sejumlah uang yang diinvest pada masa awal investasi
            additioninv=additional*sumangn #Mencari nilai total semua uang yang ditambahakan selama n tahun
            total=lumpsum+additioninv  #Mencari total uang yang didapat di masa akhir investasi
            output24()

    elif compound=='2':
        i2=returnrate/2 #Menyatakan i2(return rate compounded 2 kali setahun) sebagai variabel i2
        i12=((1+i2)**(2/12)-1) #Mencari nilai interest rate yang dicompound 12 kali setahun
        d12=1-((1+i12)**(-12/12)) #Mencari nilai diskonto yang dicompound 12 kali setahun
        i=((1+i2)**2)-1 #Mencari nilai interest rate yang dicompound 1 kali 1 tahun
        d=i/(1+i) #Mencari nilai diskonto yang dicompouind 1 kali 1 tahun
        if choice=='1': #Jika user memilih uang ditambahkan pada akhir setiap tahun sealama n tahun
            sumann=((1+i)**(time)-1)/i
            lumpsum=starting_amount*((1+(i2))**(2*time)) #Mencari Future Value sejumlah uang yang diinvest pada masa awal investasi
            additioninv=additional*sumann #Mencari nilai total semua uang yang ditambahakan selama n tahun
            total=lumpsum+additioninv #Mencari total uang yang didapat di masa akhir investasi
            output13()
        elif choice=='2': #Jika user memilih uang ditambahkan pada akhir setiap bulan selama n tahun
            sumann=((1+i12)**(12*time)-1)/i12
            lumpsum=starting_amount*((1+i2)**(2*time)) #Mencari Future Value sejumlah uang yang diinvest pada masa awal investasi
            additioninv=additional*sumann #Mencari nilai total semua uang yang ditambahakan selama n tahun
            total=lumpsum+additioninv #Mencari total uang yang didapat di masa akhir investasi
            output24()
        elif choice=='3': #Jika user memilih uang ditambahkan pada awal setiap tahun selama n tahun
            sumangn=((1+i)**(time)-1)/d
            lumpsum=starting_amount*((1+i2)**(2*time)) #Mencari Future Value sejumlah uang yang diinvest pada masa awal investasi
            additioninv=additional*sumangn #Mencari nilai total semua uang yang ditambahakan selama n tahun
            total=lumpsum+additioninv #Mencari total uang yang didapat di masa akhir investasi
            output13()
        elif choice=='4': #Jika user memilih uang ditambahkan pada awal setiap bulan selama n tahun
            sumangn=((1+i12)**(12*time)-1)/d12
            lumpsum=starting_amount*((1+i2)**(2*time)) #Mencari Future Value sejumlah uang yang diinvest pada masa awal investasi
            additioninv=additional*sumangn #Mencari nilai total semua uang yang ditambahakan selama n tahun
            total=lumpsum+additioninv #Mencari total uang yang didapat di masa akhir investasi
            output24()

    elif compound=='3':
        i4=returnrate/4 #Menyatakan i4(return rate compounded 4 kali setahun) sebagai variabel i4
        i12=((1+i4)**(4/12)-1) #Mencari nilai interest rate yang dicompound 12 kali setahun
        d12=1-((1+i12)**(-12/12)) #Mencari nilai diskonto yang dicompound 12 kali setahun
        i=((1+i4)**4)-1 #Mencari nilai interest rate yang dicompound 1 kali 1 tahun
        d=i/(1+i) #Mencari nilai diskonto yang dicompouind 1 kali 1 tahun
        if choice=='1': #Jika user memilih uang ditambahkan pada akhir setiap tahun
            sumann=((1+i)**(time)-1)/i
            lumpsum=starting_amount*((1+i4)**(4*time)) #Mencari Future Value sejumlah uang yang diinvest pada masa awal investasi
            additioninv=additional*sumann #Mencari nilai total semua uang yang ditambahakan selama n tahun
            total=lumpsum+additioninv #Mencari total uang yang didapat di masa akhir investasi
            output13()
        elif choice=='2': #Jika user memilih uang ditambahkan pada akhir setiap bulan selama n tahun
            sumann=((1+i12)**(12*time)-1)/i12
            lumpsum=starting_amount*((1+i4)**(4*time)) #Mencari Future Value sejumlah uang yang diinvest pada masa awal investasi
            additioninv=additional*sumann #Mencari nilai total semua uang yang ditambahakan selama n tahun
            total=lumpsum+additioninv #Mencari total uang yang didapat di masa akhir investasi
            output24()
        elif choice=='3': #Jika user memilih uang ditambahkan pada awal setiap tahun selama n tahun
            sumangn=((1+i)**(time)-1)/d
            lumpsum=starting_amount*((1+i4)**(4*time)) #Mencari Future Value sejumlah uang yang diinvest pada masa awal investasi
            additioninv=additional*sumangn #Mencari nilai total semua uang yang ditambahakan selama n tahun
            total=lumpsum+additioninv #Mencari total uang yang didapat di masa akhir investasi
            output13()
        elif choice=='4': #Jika user memilih uang ditambahkan pada awal setiap bulan selama n tahun
            sumangn=((1+i12)**(12*time)-1)/d12
            lumpsum=starting_amount*((1+i4)**(4*time))
            additioninv=additional*sumangn #Mencari nilai total semua uang yang ditambahakan selama n tahun
            total=lumpsum+additioninv #Mencari total uang yang didapat di masa akhir investasi
            output24()

    elif compound=='4':
        i12=returnrate/12 #Menyatakan i12(return rate compounded 12 kali setahun) sebagai variabel i12
        d12=1-((1+i12)**(-12/12)) #Mencari nilai diskonto yang dicompound 12 kali setahun
        i=((1+i12)**12)-1 #Mencari nilai interest rate yang dicompound 1 kali 1 tahun
        d=i/(1+i) #Mencari nilai diskonto yang dicompouind 1 kali 1 tahun
        if choice=='1':#Jika user memilih uang ditambahkan pada akhir setiap tahun
            sumann=((1+i)**(time)-1)/i
            lumpsum=starting_amount*((1+i12)**(12*time)) #Mencari Future Value sejumlah uang yang diinvest pada masa awal investasi
            additioninv=additional*sumann #Mencari nilai total semua uang yang ditambahakan selama n tahun
            total=lumpsum+additioninv #Mencari total uang yang didapat di masa akhir investasi
            output13()
        elif choice=='2': #Jika user memilih uang ditambahkan pada akhir setiap bulan selama n tahun
            sumann=((1+i12)**(12*time)-1)/i12
            lumpsum=starting_amount*((1+i12)**(12*time)) #Mencari Future Value sejumlah uang yang diinvest pada masa awal investasi
            additioninv=additional*sumann #Mencari nilai total semua uang yang ditambahakan selama n tahun
            total=lumpsum+additioninv #Mencari total uang yang didapat di masa akhir investasi
            output24()
        elif choice=='3': #Jika user memilih uang ditambahkan pada awal setiap tahun selama n tahun
            sumangn=((1+i)**(time)-1)/d
            lumpsum=starting_amount*((1+i12)**(12*time)) #Mencari Future Value sejumlah uang yang diinvest pada masa awal investasi
            additioninv=additional*sumangn #Mencari nilai total semua uang yang ditambahakan selama n tahun
            total=lumpsum+additioninv #Mencari total uang yang didapat di masa akhir investasi
            output13()
        elif choice=='4': #Jika user memilih uang ditambahkan pada awal setiap bulan selama n tahun
            sumangn=((1+i12)**(12*time)-1)/d12
            lumpsum=starting_amount*((1+i12)**(12*time)) #Mencari Future Value sejumlah uang yang diinvest pada masa awal investasi
            additioninv=additional*sumangn #Mencari nilai total semua uang yang ditambahakan selama n tahun
            total=lumpsum+additioninv #Mencari total uang yang didapat di masa akhir investasi
            output24()

'=============================Calculator================================'
print('================================================================')
print('============ Welcome to multipurpose calculator ================')
print('1. Retirement Fund Calculator')
print('2. Invesment Calculator')
choose=input("Enter the number of function which you want to use :")

#Check Input
choosen=['1','2','3']
while choose not in choosen:
    choose=input("Please input the number of which function you want to use :")

#Proses Kalkulasi
if choose=='1':
    f1()
elif choose=='2':
    f2()
