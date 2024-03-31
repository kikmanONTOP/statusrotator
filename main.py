@tasks.loop(seconds=60)
async def change_status():
    statuses = ['https://github.com/kikmanONTOP', 'd3vshub on top', '/contact', 'https://dsc.gg/d3vshub']
    current_status = getattr(change_status, "current_status", None)
    if current_status is None or len(current_status) >= len(statuses):
        change_status.current_status = statuses[:1]
    else:
        change_status.current_status.append(statuses[len(current_status)])
    status = nextcord.Game(name=change_status.current_status[-1])
    await bot.change_presence(activity=status, status=nextcord.Status.do_not_disturb)
@bot.event
async def on_ready():
    print(f'Přihlášen jako {bot.user}')
    await change_status()
    change_status.start()