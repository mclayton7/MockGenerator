@echo off
:: v - verbose
:: f - failfast
:: c - catch CTRL-C
python.exe -m unittest discover -vfc
