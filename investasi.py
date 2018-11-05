nama = raw_input("Nama Anda : ")
inv = ["uang", "emas","properti"]
lanjut="y"
data=[]
while lanjut == "y":
	print "pilih bidang investasi"
	print "=============="
	for i in inv:
		print i
	print "=============="
	invf = raw_input("Masukan Investasi : ")
	if invf == inv[0]:
		print "anda Menginvestasikan",invf
		modal = eval(raw_input("Masukan Modal Awal Anda : Rp"))
		print "Modal Anda Rp.",modal
		pb = eval(raw_input("masukan Pendapatan Perbulan : Rp"))
		untung = pb*12-modal
		persen = str(untung/modal*100)+"%"
		balikm = round(modal/pb)
		print "++++++++++++++++++++++++++++++++++++++++++++++++++++"
		print " Persentase Keuntungan Pertahun = ",persen
		print " Keuntungan Pertahun = Rp.",untung
		print " Balik Modal bulan Ke-",balikm
		print "++++++++++++++++++++++++++++++++++++++++++++++++++++"
	elif invf == inv[1]:
		print "anda Menginvestasikan",invf
		modal = eval(raw_input("Masukan Modal Awal Anda Dalam Satuan Gram : "))
		print "Modal Anda ",modal,"gram"
		hargag = eval(raw_input("Harga Emas Pergram sekarang: Rp "))
		pb = eval(raw_input("Harga perkiraan Kenaikan Pergram Emas Perbulan : Rp"))
		hmas = modal*hargag
		naikpb = modal+pb
		untung = hmas*12+naikpb
		persen = str(untung/hmas*100)+"%"
		balikm = round(modal/naikpb)
		print "++++++++++++++++++++++++++++++++++++++++++++++++++++"
		print " Persentase Keuntungan Pertahun = ",persen
		print " Keuntungan Pertahun = Rp.",untung
		print " Balik Modal bulan Ke-",balikm
		print "++++++++++++++++++++++++++++++++++++++++++++++++++++"
	elif invf == inv[2]:
		print "anda Menginvestasikan",invf
		print "anda Menginvestasikan",invf
		modal = eval(raw_input("Masukan Modal Awal Anda : Rp"))
		print "Modal Anda Rp.",modal
		pb = eval(raw_input("masukan Pendapatan Perbulan : Rp"))
		untung = pb*12-modal
		persen = str(untung/modal*100)+"%"
		balikm = round(modal/pb)
		print "++++++++++++++++++++++++++++++++++++++++++++++++++++"
		print " Persentase Keuntungan Pertahun = ",persen
		print " Keuntungan Pertahun = Rp.",untung
		print " Balik Modal bulan Ke-",balikm
		print "++++++++++++++++++++++++++++++++++++++++++++++++++++"
	else:
		print "inputan tidak falid"
	data.append([invf, untung, persen, balikm])
	lanjut = raw_input("apakah ingin menghiung yang lain?(y/t)")


for i in range(len(data)):
	print "data anda ke-"+ str(i+1) +": investasi "+ data[i][0] +", persen "+ data[i][2] +", untung Rp"+ str(data[i][1])+", balik modal bulan ke-"+str(data[i][3])

#import csv
#with open('data.csv', 'w', newline='') as f:
	#write = csv.writer(f)
	#write.writerow(['Nama', 'Investasi', 'Modal', 'Untung', 'Balik Modal', 'Persentase Keuntungan'])
	#for i in range(data):
		#write.writerow([data[i][5]], [data[i][0]], [data[i][4]], [data[i][1]], [data[i][3]], [data[i][2]])
