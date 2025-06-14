# 多平台影音下載器 (Multi-Platform Video Downloader)

一個功能強大的多平台影音下載工具，支援 YouTube、Instagram、Facebook 和 TikTok，自動下載最高畫質影片。

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

## 🌟 功能特點

- 📥 支援多個主流影音平台
  - YouTube：支援最高畫質下載，自動合併影片和音訊
  - Instagram：支援最高畫質下載，包含上傳者資訊
  - Facebook：支援最高畫質下載，需要登入
  - TikTok：支援最高畫質下載，包含上傳者資訊
- 🎥 自動選擇最佳畫質（優先下載最高畫質 MP4）
- 🔄 自動合併影片和音訊
- 🔐 支援 Chrome 瀏覽器 cookies
- 💻 簡潔的命令列介面
- ⚡ 非同步下載處理
- 📝 檔案命名包含上傳者資訊和時間戳記
- 📊 詳細的下載狀態和錯誤訊息

## 📋 系統需求

- Python 3.9 或更高版本
- pip（Python 套件管理器）
- FFmpeg（用於影片處理）
- Chrome 瀏覽器（用於 cookies）

## 🚀 快速開始

### 1. 安裝 FFmpeg

#### Windows
```bash
# 使用 Chocolatey
choco install ffmpeg

# 或使用 Scoop
scoop install ffmpeg
```

#### macOS
```bash
# 使用 Homebrew
brew install ffmpeg
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install ffmpeg

# CentOS/RHEL
sudo yum install ffmpeg
```

### 2. 安裝程式

1. 克隆專案：
```bash
git clone https://github.com/yourusername/video-downloader.git
cd video-downloader
```

2. 建立虛擬環境：
```bash
python3 -m venv venv
```

3. 啟動虛擬環境：
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

4. 安裝依賴套件：
```bash
pip install -r requirements.txt
```

## 💡 使用方法

1. 確保虛擬環境已啟動
2. 執行程式：
```bash
python main.py
```
3. 在提示時輸入影片網址
4. 等待下載完成
5. 下載的檔案會存放在 `downloads` 資料夾中

## 📁 檔案命名規則

- YouTube：`[標題].mp4`
- Instagram：`instagram_[上傳者]_[ID]_[時間戳記].mp4`
- Facebook：`facebook_[上傳者]_[ID]_[時間戳記].mp4`
- TikTok：`tiktok_[上傳者]_[ID]_[時間戳記].mp4`

## ⚠️ 注意事項

- 請確保您有權限下載相關影片
- 部分平台（如 Facebook）可能需要登入才能下載
- 下載的影片僅供個人使用
- 請遵守相關平台的使用條款
- 確保已安裝 FFmpeg 以支援影片處理
- 使用前請確保已登入 Chrome 瀏覽器

## 📂 專案結構

```
video_downloader/
├── downloaders/
│   ├── __init__.py
│   ├── base_downloader.py      # 基礎下載器類別
│   ├── youtube_downloader.py   # YouTube 下載器
│   ├── instagram_downloader.py # Instagram 下載器
│   ├── facebook_downloader.py  # Facebook 下載器
│   └── tiktok_downloader.py    # TikTok 下載器
├── downloads/                  # 下載檔案存放目錄
├── main.py                    # 主程式
├── requirements.txt           # 依賴套件列表
└── README.md                  # 說明文件
```

## 📦 依賴套件

- yt-dlp：用於下載影片的核心套件
- FFmpeg：用於影片處理和合併

## 🤝 貢獻指南

1. Fork 本專案
2. 建立您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟一個 Pull Request

## 📝 授權

本專案採用 MIT 授權條款。詳見 [LICENSE](LICENSE) 文件。

## ⚖️ 免責聲明

本工具僅供學習和研究使用。使用者應遵守相關法律法規和平台使用條款。開發者不對使用者的行為負責。

## 📞 聯絡方式

如有問題或建議，請開啟 Issue 或 Pull Request。

## 🙏 致謝

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - 強大的影片下載工具
- [FFmpeg](https://ffmpeg.org/) - 影片處理工具 