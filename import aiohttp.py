# import aiohttp
# import asyncio
# import json
# import os

# async def posts():
#     url = 'https://jsonplaceholder.typicode.com/posts'
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             posts = await response.json()
#             os.makedirs('data', exist_ok=True)
#         for item in posts:
#             file_path = f"data_folder/file_{item['id']}.json"

#             with open('hi.json', 'w', encoding="utf_8") as f:
#                 json.dump(posts, f, ensure_ascii=False, indent=3 )
#                 print("всеэ сохранено")

# if __name__ == "__main__":
#     asyncio.run(posts())

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