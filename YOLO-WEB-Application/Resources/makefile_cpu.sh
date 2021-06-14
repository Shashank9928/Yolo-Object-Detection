cd ../darknet
sed -i 's/OPENCV=0/OPENCV=1/' Makefile
sed -i 's/GPU=1/GPU=0/' Makefile
sed -i 's/CUDNN=1/CUDNN=0/' Makefile
make