import os
import yt_dlp

class BaseDownloader:
    def __init__(self, output_path="downloads"):
        self.output_path = output_path
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            
    def _get_common_options(self):
        """獲取通用的下載選項"""
        return {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(self.output_path, '%(title)s.%(ext)s'),
            'quiet': False,
            'no_warnings': False,
            'cookiesfrombrowser': ('chrome',),
            'restrict_filenames': True,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-us,en;q=0.5',
                'Sec-Fetch-Mode': 'navigate',
            }
        }
    
    def download(self, url):
        """基礎下載方法，子類別可以覆寫此方法"""
        try:
            ydl_opts = self._get_common_options()
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get('title', '未知標題')
                return True, f"成功下載：{title}"
        except Exception as e:
            return False, f"下載失敗：{str(e)}" 