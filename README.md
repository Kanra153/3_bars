# Closest bars
The script allows you to find the biggest, the smallest and the closest bar from https://data.mos.ru/opendata/7710881420-bary. To find the closest bar you need also to input your coordinates. 

# How to use

You need Python 3.5 or higher to launch script

Launch on Linux:

```bash

$ python bars.py path/to/file # possibly requires call of python3 executive instead of just python
Please, input longtitude:30
Please, input latitude:50
The biggest bar is:
 {
   "global_id": 169375059,
   "Name": "Спорт бар «Красная машина»",
   "IsNetObject": "нет",
   "OperatingCompany": null,
   "AdmArea": "Южный административный округ",
   "District": "Даниловский район",
   "Address": "Автозаводская улица, дом 23, строение 1",
   "PublicPhone": [
      {
         "PublicPhone": "(905) 795-15-84"
      }
   ],
   "SeatsCount": 450,
   "SocialPrivileges": "нет"
}

```


# Project goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
