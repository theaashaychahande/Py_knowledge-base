"""
1. Definition:  
Non-blocking concurrent execution 
2. Why Use:  
Handle I/O operations efficiently 
"""

import asyncio

async def fetch_data(user):
    print(f"Fetching {user}'s data...")
    await asyncio.sleep(1)
    return f"{user}_results"

async def main():
    results = await asyncio.gather(
        fetch_data("Disha"),
        fetch_data("Apurv")
    )
    print(results)

asyncio.run(main())

"""
Output:
Fetching Disha's data...
Fetching Apurv's data...
['Disha_results', 'Apurv_results']
"""
