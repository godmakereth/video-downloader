from .base_downloader import BaseDownloader
import time
import os
import yt_dlp

class FacebookDownloader(BaseDownloader):
    def __init__(self, output_path="downloads"):
        super().__init__(output_path)
        
    def _get_common_options(self):
        """獲取 Facebook 特定的下載選項"""
        options = super()._get_common_options()
        # Facebook 特定的選項
        options.update({
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # 優先下載最高畫質
            'merge_output_format': 'mp4',  # 強制合併為 MP4
            'outtmpl': os.path.join(self.output_path, 'facebook_%(uploader)s_%(id)s_%(timestamp)s.%(ext)s'),
            'cookiesfrombrowser': ('chrome',),
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            }
        })
        return options

    def download(self, url):
        """覆寫下載方法，加入時間戳記和用戶名稱"""
        try:
            # 生成時間戳記
            timestamp = int(time.time())
            
            ydl_opts = self._get_common_options()
            ydl_opts['outtmpl'] = ydl_opts['outtmpl'].replace('%(timestamp)s', str(timestamp))
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print("正在獲取影片信息...")
                info = ydl.extract_info(url, download=True)
                
                if not info:
                    return False, "無法獲取影片信息，請確保您已登入 Facebook 並有權限訪問該影片"
                
                title = info.get('title', '未知標題')
                uploader = info.get('uploader', 'unknown_user')
                format = info.get('format', '未知格式')
                
                # 檢查是否成功下載
                output_file = ydl.prepare_filename(info)
                if not os.path.exists(output_file):
                    return False, "下載失敗，請檢查您的 Facebook 登入狀態和影片權限"
                
                return True, f"成功下載：{title} (來自 {uploader}, 格式: {format})"
                
        except Exception as e:
            error_msg = str(e)
            if "login" in error_msg.lower():
                return False, "下載失敗：請確保您已登入 Facebook"
            elif "private" in error_msg.lower():
                return False, "下載失敗：此影片為私人影片或需要登入"
            elif "not found" in error_msg.lower():
                return False, "下載失敗：找不到影片，請確認 URL 是否正確"
            else:
                return False, f"下載失敗：{error_msg}" 