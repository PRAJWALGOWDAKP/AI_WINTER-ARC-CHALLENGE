import asyncio
import httpx


async def fetch_user(client,user_id):
    url=f"https://jsonplaceholder.typicode.com/users/{user_id}"

    response=await client.get(url)
    response.raise_for_status()

    user=response.json()

    print(f"User ID: {user['id']}")
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")

    return user

async def main():
    async with httpx.AsyncClient(timeout=10.0) as client:
        results=await asyncio.gather(
           fetch_user(client,1),
           fetch_user(client,2),    
           fetch_user(client,3),
        )

        print(f"Total users fetched: {len(results)}")

if __name__=="__main__":
    asyncio.run(main())