@echo off
:: Copyright (c) Mac Clayton. All rights reserved.
:: Licensed under the MIT license. See LICENSE file in the project root for details.
:: v - verbose
:: f - failfast
:: c - catch CTRL-C
python.exe -m unittest discover -vfc
