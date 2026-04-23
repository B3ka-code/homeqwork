
import aiohttp
import asyncio
import json
import os

async def posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            all_posts = await response.json() # Получили список
            
            os.makedirs('my_data', exist_ok=True)
            
            for item in all_posts:
                file_path = f"my_data/file_{item['id']}.json"

                with open(file_path, 'w', encoding="utf_8") as f:
                    json.dump(item, f, ensure_ascii=False, indent=3)
            
            print("Всё сохранено в папку my_data!")

if __name__ == "__main__":
    asyncio.run(posts())
