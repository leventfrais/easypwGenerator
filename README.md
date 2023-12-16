# easypwGenerator

## 简介

使用python进行开发的基于社会工程学的字典生成器。主要由已泄露的个人信息进行推断生成弱口令词典。支持名、号、连接符、addition进行排列组合枚举

## 使用

```cmd
optional arguments:
  -h, --help            show this help message and exit

  -n NAME, --name NAME  The full TRUE name of the victim (LiMing)(Charles)(Sunny)
  -idn IDNAME, --idName IDNAME
                        The id name of the victim (s1mple)(3liza)(s0ow)
  -bir BIRTH, --birth BIRTH
                        The full birthdate of the victim (19991231)
  -jbn JOBNUM [JOBNUM ...], --jobNum JOBNUM [JOBNUM ...]
                        The job number of the victim (just numbers)
  -pn PHONENUM [PHONENUM ...], --phoneNum PHONENUM [PHONENUM ...]
                        The phone number(17777777777)

  -cc CONCHAR, --conChar CONCHAR
                        The connecting char between ((,._[]<>) BEWARE: the more you give the slower it will be)
  -len LENGTH, --length LENGTH
                        The minimal length of the pw (6)
  -add ADDITION [ADDITION ...], --addition ADDITION [ADDITION ...]
                        The additional words you want to add(520)(china)(1314)
```

```cmd
样例输入
python main.py -n YuanJie -idn Pilatus -bir 20210102 -cc ._ -len 8 -add woaini 1314 520 1314520 shabi djb dajiba shuaige
---
Namespace(name='YuanJie', idName='Pilatus', birth='20210102', jobNum=None, phoneNum=None, conChar='._', length=8, addition=['woaini', '1314', '520', '1314520', 'shabi', 'djb', 'dajiba', 'shuaige'])
```

![preview](.\preview.png)
