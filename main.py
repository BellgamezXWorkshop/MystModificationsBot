# MystModificationsStore made by MystModifications

import discord
from discord.ext import commands

# Initialize the bot with a prefix
bot = commands.Bot(command_prefix="!")

# Store inventory as a dictionary (product_name: quantity)
inventory = {
    "product1": 10,
    "product2": 15,
    "product3": 5,
}

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def display_inventory(ctx):
    """Display the store's inventory."""
    inventory_message = "\n".join([f"{product}: {quantity}" for product, quantity in inventory.items()])
    await ctx.send(f"**Store Inventory:**\n{inventory_message}")

@bot.command()
async def order(ctx, product_name, quantity=1):
    """Place an order for a product."""
    product_name = product_name.lower()
    
    if product_name in inventory and inventory[product_name] >= quantity:
        # Update inventory
        inventory[product_name] -= quantity
        await ctx.send(f"Order placed: {quantity}x {product_name}")
    else:
        await ctx.send("Sorry, the product is out of stock or the quantity requested is not available.")

@bot.command()
async def add_product(ctx, product_name, quantity):
    """Add a product to the store's inventory."""
    product_name = product_name.lower()
    
    if product_name in inventory:
        inventory[product_name] += int(quantity)
    else:
        inventory[product_name] = int(quantity)
    
    await ctx.send(f"{quantity}x {product_name} added to inventory.")

# Replace 'YOUR_TOKEN' with your actual bot token
bot.run("MTE1MTM2MDIwMTIwNzg0NDg4NQ.GA82C-.S8EMiTdI-Y1yrZ22zvHNBlxJp656sMEuD8sVJo")
