# oysterx.gpx.converter

## Introduction
- 因為 oysterX 本身沒有可以匯出的功能。因此我想寫個工具可以把 oysterX 備份在 dropbox 的紀錄轉成 gpx 檔案，用以儲存自己的日常 gps 軌跡。結論是這個程式可成功運作。
- 本來想直接看備份在 dropbox 的 sqlite3 檔案裡面的座標，我想直接倒出來轉成 GPX 檔案。不過後來發現好像大部分都被存在不是備份的地方。
- `OXDB_user` 檔案裡面有個 `OXStory` table, 裡面有很多座標。裡面的座標數量雖然不少，但以我使用的時間來看，我預期他應該會備份的資料量遠遠不止於此。所以我猜測應該是只有標誌性的座標資料而已，當作各個城市的標誌紀錄？大部分的座標資料猜測是存在別的地方。

## Capability
- 讀 `OXDB_user` 檔，並且產生 gpx 檔案
- 轉出來的檔案會把所有資料都放在同一個 track 裏面，如果連續兩點距離太遠就會切成不同的 segment, 不會使最後的 segment 連起來的線是爛掉的。

## Usage
1. 先安裝好 [poetry](https://python-poetry.org/) , 這是一個 python 的虛擬環境，讓一個專案需要的 module 不會污染到 global 環境的好東西。
2. 把 dropbox 的同步備份檔案 `OXDB_user` 複製到 `main.py` 所在的資料夾中。
3. ```bash
	poetry install
	./main.py
	```
4. 獲得轉檔完成的 gpx 檔案。