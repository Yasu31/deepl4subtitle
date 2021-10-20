# deepl4subtitle
Deeplを使って字幕ファイル(.sbv)を翻訳します。タイムスタンプも含めて出力しますが、翻訳時はタイムスタンプは文の一部とは切り離されるので、.sbvファイルをそのまま翻訳機に突っ込むよりも高精度な翻訳ができるはずです。

## つかいかた
入力する.sbvファイルの前処理として、**文の終わりにピリオド(.)を打っていく**。これで、Deeplが文の区切りを正しく認識してくれる。
```bash
# install deepl 
# https://pypi.org/project/deepl/
pip3 install deepl
python3 deepl4subtitle.py -i sample.sbv -o output.sbv -k YOUR_DEEPL_API_KEY
```

## サンプル
sample video: https://www.youtube.com/watch?v=CL7HuMLIPO0

* sample.xbv: Youtubeが自動で生成した字幕を若干手直ししたもの
* sample_deepl4subtitle.sbv: deepl4subtitleを使って翻訳したもの
* sample_raw_deepl.sbv: sample.xbvの中身をそのままDeeplにコピペして翻訳したもの

sample_raw_deeplだと、タイムスタンプが文章の一部であることが原因であちこちで怪しい翻訳が発生していたのが、sample_deepl4subtitleでは概ね解消されている。


## 中でやってること
### original
(文末のピリオドは手作業で加える必要がある)
```sbv
0:00:01.340,0:00:04.780
クラウドコンピューティングという言葉を
知っているだろうか.

0:00:04.780,0:00:08.110
クラウドコンピューティングとは
インターネットの先にあるデータセンター

0:00:08.110,0:00:12.420
のサーバーに処理してもらうシステム形態
を指す言葉である.
```

### ↓ move timestamp within XML tag, remove newlines
```xml
<timestamp ts="0:00:01.340,0:00:04.780"/>クラウドコンピューティングという言葉を知っているだろうか.<timestamp ts="0:00:04.780,0:00:08.110"/>クラウドコンピューティングとはインターネットの先にあるデータセンター<timestamp ts="0:00:08.110,0:00:12.420"/>のサーバーに処理してもらうシステム形態を指す言葉である.
```

### ↓ translate with Deepl through API, ignoring XML tags
```xml
<timestamp ts="0:00:01.340,0:00:04.780"/>Do you know the term "cloud computing"? <timestamp ts="0:00:04.780,0:00:08.110"/> Cloud computing is a term that refers to a form of system that is processed by servers in a data center <timestamp ts="0:00:08.110,0:00:12.420"/>located beyond the Internet. 
```

### ↓ put back timestamp and newlines
```sbv
0:00:01.340,0:00:04.780
Do you know the term "cloud computing"? 

0:00:04.780,0:00:08.110
 Cloud computing is a term that refers to a form of system that is processed by servers in a data center 

0:00:08.110,0:00:12.420
located beyond the Internet. 
```