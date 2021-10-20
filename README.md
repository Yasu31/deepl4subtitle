# deepl4subtitle
Deeplを使って字幕ファイル(.sbv)を翻訳します。タイムスタンプも含めて出力しますが、翻訳時はタイムスタンプは文の一部とは切り離されるので、.sbvファイルをそのまま翻訳機に突っ込むよりも高精度な翻訳ができるはずです。

```bash
# install deepl 
# https://pypi.org/project/deepl/
pip3 install deepl
python3 deepl4subtitle.py -i sample.sbv -o output.sbv -k YOUR_DEEPL_API_KEY
```

sample video: https://www.youtube.com/watch?v=CL7HuMLIPO0