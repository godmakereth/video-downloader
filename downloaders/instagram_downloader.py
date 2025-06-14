from .base_downloader import BaseDownloader
import time
import hashlib
import os
import yt_dlp

class InstagramDownloader(BaseDownloader):
    def __init__(self, output_path="downloads"):
        super().__init__(output_path)
        
    def _get_common_options(self):
        """獲取 Instagram 特定的下載選項"""
        options = super()._get_common_options()
        # Instagram 特定的選項
        options.update({
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # 優先下載最高畫質
            'extract_flat': True,  # 不遞迴下載
            'outtmpl': os.path.join(self.output_path, 'instagram_%(uploader)s_%(id)s_%(timestamp)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # 確保輸出為 MP4 格式
            }],
        })
        return options

    def download(self, url):
        """覆寫下載方法，加入時間戳記和用戶名稱"""
        try:
            # 生成時間戳記
            timestamp = int(time.time())
            
            ydl_opts = self._get_common_options()
            # 替換模板中的變數
            ydl_opts['outtmpl'] = ydl_opts['outtmpl'].replace('%(timestamp)s', str(timestamp))
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get('title', '未知標題')
                uploader = info.get('uploader', 'unknown_user')
                format = info.get('format', '未知格式')
                return True, f"成功下載：{title} (來自 {uploader}, 格式: {format})"
        except Exception as e:
            return False, f"下載失敗：{str(e)}" 