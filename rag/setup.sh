mkdir dataset
wget https://clarin-pl.eu/dspace/bitstream/handle/11321/324/czywieszki.zip -O dataset/czywieszze.zip
unzip dataset/czywieszze.zip -d dataset/czywieszze
mkdir dataset/czywieszze/czywieszki2.0/wiki
tar -xf dataset/czywieszze/czywieszki2.0/Czywiesz.tar --directory dataset/czywieszze/czywieszki2.0/wiki