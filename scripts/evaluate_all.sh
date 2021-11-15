#!/usr/bin/env bash

MIX=0.95

echo ""
echo ""
echo "standard"
echo "---------------------------"
echo "f(a,a)":
python evaluate.py -predictions_premises sim_preds/s2match-090-100.txt \
		   -mixing_value $MIX
echo "f(c,c)":
python evaluate.py -predictions_conclusions sim_preds/s2match-090-100-c-cbar.txt \
		   -mixing_value $MIX
echo "f(aa',cc')":
python evaluate.py -predictions_premises sim_preds/s2match-090-100.txt \
		   -predictions_conclusions sim_preds/s2match-090-100-c-cbar.txt \
		   -mixing_value $MIX


echo ""
echo ""
echo "concept focus"
echo "---------------------------"
echo "f(a,a)":
python evaluate.py -predictions_premises sim_preds/s2match-090-100-conceptfocus3.txt \
		   -mixing_value $MIX
echo "f(c,c)":
python evaluate.py -predictions_conclusions sim_preds/s2match-090-100-c-cbar-conceptfocus3.txt \
		   -mixing_value $MIX
echo "f(aa',cc')":
python evaluate.py -predictions_premises sim_preds/s2match-090-100-conceptfocus3.txt \
		   -predictions_conclusions sim_preds/s2match-090-100-c-cbar-conceptfocus3.txt \
		   -mixing_value $MIX

echo ""
echo ""
echo "structure focus"
echo "---------------------------"
echo "f(a,a)":
python evaluate.py -predictions_premises sim_preds/s2match-090-100-structfocus3.txt \
		   -mixing_value $MIX
echo "f(c,c)":
python evaluate.py -predictions_conclusions sim_preds/s2match-090-100-c-cbar-structfocus3.txt \
		   -mixing_value $MIX
echo "f(aa',cc')":
python evaluate.py -predictions_premises sim_preds/s2match-090-100-structfocus3.txt \
		   -predictions_conclusions sim_preds/s2match-090-100-c-cbar-structfocus3.txt \
		   -mixing_value $MIX
