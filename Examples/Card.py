async def main():
    async with starrailcard.MiHoMoCard() as card:
        print(card)        
        
asyncio.run(main())
