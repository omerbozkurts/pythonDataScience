print("hello world")

print("merhaba dunya")

# sanal ortamlari listelemek icin
# conda env list

# sanal ortam olusturmak icin
# conda create -n ortamadi

# olusturulan sanal ortamin icine girmek icin
# conda activate ortamadi

# sanal ortamdan cikmak icin
# conda deactivate

# sanal ortamdaki paketleri goruntulemek icin
# conda list

# paket yuklemek icin
# conda install package_name

# ayni anda birden fazla paket yuklemek icin
# conda install package1_name package2_name package3_name

# paket silme
# conda remove paket_ismi

# paketin belirli versiyonunu yukleme
# conda install numpy=1.20.1

# paketin versiyonunu yukseltmek icin
# conda upgrade package_name

# tum paketleri guncellemek icin
# conda upgrade -all

# pip : pypi : python package index - paket yonetim araci
# pip install package_name

# pip ile istenilen surumle paket yukleme
# pip install pandas==1.2.1

# kullanilan kutuphanelerin versiyonlarini baska birine aktarmak icin yaml dosyasi kullanilir
# conda ile yaml dosyasi olusturmak icin
# conda env export > environment.yaml

# bir yaml dosyasi kullanarak environment olusturmak icin
# conda env create -f environment.yaml

# bir ortami silmek icin
# conda env remove -n environment_adi