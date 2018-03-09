#!/bin/bash
export datadir="/media/xu/Jiachuan_HFSplus/data"

# op_list files have been generated, decompose images
python Decompose_Image.py BOSS1441_POINT1_M/J/op_list
python Decompose_Image.py BOSS1441_POINT1_M/H/op_list
python Decompose_Image.py BOSS1441_POINT1_M/K/op_list
python Decompose_Image.py BOSS1441_POINT2_M/J/op_list
python Decompose_Image.py BOSS1441_POINT2_M/H/op_list
python Decompose_Image.py BOSS1441_POINT2_M/K/op_list

# make list for decomposed images, exclude bad quality images
cd $datadir/BOSS1441_POINT1_DECOMP/J
python ListforMosaic.py context_1J
cd $datadir/BOSS1441_POINT1_DECOMP/H
python ListforMosaic.py context_1H
cd $datadir/BOSS1441_POINT1_DECOMP/K
python ListforMosaic.py context_1K
cd $datadir/BOSS1441_POINT2_DECOMP/J
python ListforMosaic.py context_2J
cd $datadir/BOSS1441_POINT2_DECOMP/H
python ListforMosaic.py context_2H
cd $datadir/BOSS1441_POINT2_DECOMP/K
python ListforMosaic.py context_2K

# mosaic
cd $datadir
bash BOSS1441_POINT1_DECOMP/J/mosaic_script.sh
bash BOSS1441_POINT1_DECOMP/H/mosaic_script.sh
bash BOSS1441_POINT1_DECOMP/K/mosaic_script.sh
bash BOSS1441_POINT2_DECOMP/J/mosaic_script.sh
bash BOSS1441_POINT2_DECOMP/H/mosaic_script.sh
bash BOSS1441_POINT2_DECOMP/K/mosaic_script.sh
