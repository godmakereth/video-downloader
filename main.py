from downloaders.youtube_downloader import YouTubeDownloader
from downloaders.instagram_downloader import InstagramDownloader
from downloaders.facebook_downloader import FacebookDownloader
from downloaders.tiktok_downloader import TikTokDownloader
import asyncio
import re

class VideoDownloader:
    def __init__(self, output_path="downloads"):
        self.youtube_downloader = YouTubeDownloader(output_path)
        self.instagram_downloader = InstagramDownloader(output_path)
        self.facebook_downloader = FacebookDownloader(output_path)
        self.tiktok_downloader = TikTokDownloader(output_path)
        
    def _get_downloader(self, url):
        """根據 URL 選擇適當的下載器"""
        if 'youtube.com' in url or 'youtu.be' in url:
            return self.youtube_downloader
        elif 'instagram.com' in url:
            return self.instagram_downloader
        elif 'facebook.com' in url:
            return self.facebook_downloader
        elif 'tiktok.com' in url:
            return self.tiktok_downloader
        else:
            raise ValueError("不支援的影片平台")

    async def download_video(self, url):
        try:
            downloader = self._get_downloader(url)
            print(f"正在嘗試下載 {url}...")
            return downloader.download(url)
        except ValueError as e:
            return False, str(e)
        except Exception as e:
            return False, f"下載失敗：{str(e)}"

async def main():
    downloader = VideoDownloader()
    
    while True:
        print("\n=== 多平台影音下載器 ===")
        print("支援的平台：YouTube、Instagram、Facebook、TikTok")
        print("輸入 'q' 退出程式")
        
        url = input("\n請輸入影片網址：")
        if url.lower() == 'q':
            break
            
        success, message = await downloader.download_video(url)
        print(message)

if __name__ == "__main__":
    asyncio.run(main()) 