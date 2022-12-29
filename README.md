# K-tai-Hu-Pad

〇 ケースキットの組立方法は[コチラ](/BuildGuide_CaseKit.md)

# CircuitPythonのインストール

1. 以下のURLから、Seeed Studio XIAO nRF52840向けのファームウェアをダウンロードします。<br>
    https://circuitpython.org/board/Seeed_XIAO_nRF52840_Sense/

    <img src="img/img01_1.png" width="500px" /> <br>
	※動作確認はCircuitPython 7.3.3で実施しました。<br>
 <br>

2. Seeed Studio XIAO nRF52840をPCに接続します。<br>
接続するとPCにXIAO-SENSEドライブが認識されるので、先ほどダウンロードしたCircuitPythonのファームウェア<br>
（adafruit-circuitpython-Seeed_XIAO_nRF52840_Sense-ja-7.3.3.uf2）をXIAO-SENSEドライブにコピーします。<br>
    <img src="img/img02.png" width="500px" /> <br>
<br>

3. Seeed Studio XIAO nRF52840をリセットし、PCにCIRCUITPYドライブが認識されることを確認します。<br>
 <br>

# KMK Firmwareのインストール

1. 以下のURLから、KMK Firmwareをダウンロードします。<br>
https://github.com/KMKfw/kmk_firmware/archive/refs/heads/master.zip

2. 以下のURLから、adafruit_bleをダウンロードします。<br>
https://github.com/adafruit/Adafruit_CircuitPython_BLE

3. 以下のURLから、K-tai-Hu-Padのソースコードをダウンロードします。<br>
https://github.com/agepan-ft-miku/K-tai-Hu-Pad/tree/main/board


4. 以下のファイルをCIRCUITPYドライブのルートにコピーします。<br>
・master.zip内のkmkフォルダ<br>
・K-tai-Hu-Pad/boardのkb.py<br>
・K-tai-Hu-Pad/boardのmain.py<br>

5. CIRCUITPYドライブのルートにlibフォルダを作成し、その中にadafruit_bleフォルダをコピーします。<br>

6. CIRCUITPYドライブ/kmk/modulesフォルダに、K-tai-Hu-Pad/boardのpimoroni_trackball.pyで置き換えます。 <br>

以上でファームウェアのインストールは完了です。<br>
<br>

