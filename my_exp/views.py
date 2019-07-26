from django.shortcuts import render

# Create your views here.

pengalaman1_judul = 'Code Uploader Intern'
pengalaman1_tahun = 2015
pengalaman1_tempat = 'PT.SGP, Bogor'
pengalaman1_deskripsi = 'Magang seagai uploader code kedalam chip IC barang-barang elektronik'

pengalaman2_judul = 'Jasa tugas akhir'
pengalaman2_tahun = 2018
pengalaman2_tempat = 'Kampusku'
pengalaman2_deskripsi = 'Membantu kaka tingkat jurusan mesin dalam membuat alat tugas akhir. ngoding bahasa pada arduino'

pengalaman3_judul = 'Kelas Online Beling'
pengalaman3_tahun = 2019
pengalaman3_tempat = 'Rumahku'
pengalaman3_deskripsi = 'Belajar pemograman web menggunakan framework django yang menggunakan bahasa python'

def index(request):
	response = {
		'pengalaman1_judul': pengalaman1_judul,
		'pengalaman1_tahun': pengalaman1_tahun,
		'pengalaman1_tempat': pengalaman1_tempat,
		'pengalaman1_deskripsi': pengalaman1_deskripsi,	

		'pengalaman2_judul': pengalaman2_judul,
		'pengalaman2_tahun': pengalaman2_tahun,
		'pengalaman2_tempat': pengalaman2_tempat,
		'pengalaman2_deskripsi': pengalaman2_deskripsi,

		'pengalaman3_judul': pengalaman3_judul,
		'pengalaman3_tahun': pengalaman3_tahun,
		'pengalaman3_tempat': pengalaman3_tempat,
		'pengalaman3_deskripsi': pengalaman3_deskripsi,
	}
	return render(request, 'my_exp.html', response)