import yt_dlp
import os
from .base_downloader import BaseDownloader

class YouTubeDownloader(BaseDownloader):
    def __init__(self, output_path="downloads"):
        super().__init__(output_path)
        if not os.path.exists(output_path):
            os.makedirs(output_path)

    def _get_common_options(self):
        """獲取 YouTube 特定的下載選項"""
        options = super()._get_common_options()
        # 可以在這裡添加 YouTube 特定的選項
        return options

    def download(self, url):
        try:
            # 設定 yt-dlp 選項
            ydl_opts = self._get_common_options()
            ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'  # 優先下載 MP4 格式
            ydl_opts['merge_output_format'] = 'mp4'  # 強制合併為 MP4
            ydl_opts['outtmpl'] = os.path.join(self.output_path, '%(title)s.%(ext)s')  # 簡化輸出檔名
            ydl_opts['quiet'] = False
            ydl_opts['no_warnings'] = False
            ydl_opts['cookiesfrombrowser'] = ('chrome',)
            ydl_opts['restrict_filenames'] = True
            ydl_opts['http_headers'] = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-us,en;q=0.5',
                'Sec-Fetch-Mode': 'navigate',
            }

            # 下載影片
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get('title', '未知標題')
                return True, f"成功下載：{title}"

        except Exception as e:
            return False, f"下載失敗：{str(e)}" 