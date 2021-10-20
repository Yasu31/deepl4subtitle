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
