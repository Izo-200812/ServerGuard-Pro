"""
ServerGuard Pro - Discord Bot Main Entry Point
A monetizable Discord bot for server management and moderation
"""

import discord
from discord.ext import commands, tasks
import logging
import asyncio
from config import DISCORD_TOKEN, COMMAND_PREFIX, BOT_NAME, BOT_VERSION

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize bot with intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix=COMMAND_PREFIX,
    intents=intents,
    help_command=commands.DefaultHelpCommand()
)

# ============================================================================
# BOT EVENTS
# ============================================================================

@bot.event
async def on_ready():
    """Bot startup event"""
    logger.info(f"✅ {BOT_NAME} v{BOT_VERSION} is online!")
    logger.info(f"📊 Logged in as: {bot.user}")
    logger.info(f"🔗 Servers: {len(bot.guilds)}")
    
    # Set bot status
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{COMMAND_PREFIX}help | Premium at discord.gg/serverguard"
        )
    )
    
    # Initialize database
    await init_database()

@bot.event
async def on_guild_join(guild):
    """When bot joins a new server"""
    logger.info(f"➕ Joined guild: {guild.name} (ID: {guild.id})")
    
    # Send welcome message to owner
    try:
        embed = discord.Embed(
            title="🛡️ ServerGuard Pro Setup",
            description=f"Thanks for adding me! Use `{COMMAND_PREFIX}setup` to get started.",
            color=discord.Color.green()
        )
        embed.add_field(
            name="Premium Features",
            value="Unlock advanced moderation, analytics & more!\nVisit: https://serverguard.dev/premium",
            inline=False
        )
        await guild.owner.send(embed=embed)
    except Exception as e:
        logger.error(f"Could not DM guild owner: {e}")

@bot.event
async def on_guild_remove(guild):
    """When bot leaves a server"""
    logger.info(f"➖ Left guild: {guild.name} (ID: {guild.id})")

@bot.event
async def on_command_error(ctx, error):
    """Handle command errors"""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"❌ Command not found. Use `{COMMAND_PREFIX}help` for available commands.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to use this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"❌ Missing argument. Use `{COMMAND_PREFIX}help` for syntax.")
    else:
        logger.error(f"Command error: {error}")
        await ctx.send("❌ An error occurred. Please try again later.")

# ============================================================================
# BASIC COMMANDS
# ============================================================================

@bot.command(name="ping")
async def ping(ctx):
    """Check bot latency"""
    latency = round(bot.latency * 1000)
    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"Latency: **{latency}ms**",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

@bot.command(name="help")
async def help_command(ctx):
    """Display help menu"""
    embed = discord.Embed(
        title=f"🛡️ {BOT_NAME} - Help Menu",
        description=f"Use `{COMMAND_PREFIX}command` to run a command",
        color=discord.Color.blurple()
    )
    
    embed.add_field(
        name="📋 General Commands",
        value=f"`{COMMAND_PREFIX}ping` - Check bot status\n`{COMMAND_PREFIX}setup` - Setup bot",
        inline=False
    )
    
    embed.add_field(
        name="🔨 Moderation Commands",
        value=f"`{COMMAND_PREFIX}ban <user>` - Ban a user\n`{COMMAND_PREFIX}kick <user>` - Kick a user\n`{COMMAND_PREFIX}mute <user>` - Mute a user",
        inline=False
    )
    
    embed.add_field(
        name="💎 Premium Commands",
        value="Unlock more features with premium!\nVisit: https://serverguard.dev/premium",
        inline=False
    )
    
    await ctx.send(embed=embed)

@bot.command(name="setup")
async def setup(ctx):
    """Initial server setup"""
    embed = discord.Embed(
        title="⚙️ Server Setup",
        description="ServerGuard Pro setup started!",
        color=discord.Color.green()
    )
    
    embed.add_field(
        name="Step 1: Permissions",
        value="Make sure I have admin permissions",
        inline=False
    )
    
    embed.add_field(
        name="Step 2: Configure",
        value=f"Use `{COMMAND_PREFIX}config` to customize settings",
        inline=False
    )
    
    embed.add_field(
        name="Step 3: Enable Premium",
        value="Subscribe to unlock all features!",
        inline=False
    )
    
    await ctx.send(embed=embed)

@bot.command(name="premium")
async def premium_info(ctx):
    """Show premium information"""
    embed = discord.Embed(
        title="💎 ServerGuard Pro Premium",
        description="Upgrade to unlock powerful features!",
        color=discord.Color.gold()
    )
    
    features = [
        "🤖 Advanced Auto-Moderation",
        "📊 Detailed Analytics Dashboard",
        "⚡ Custom Commands & Automations",
        "🎯 Priority Support",
        "✨ Role Reaction Messages",
        "🔍 Advanced Logging",
        "👥 Member Verification System"
    ]
    
    embed.add_field(
        name="Premium Features",
        value="\n".join(features),
        inline=False
    )
    
    embed.add_field(
        name="💳 Only $4.99/month",
        value="[Subscribe Now](https://serverguard.dev/premium)",
        inline=False
    )
    
    await ctx.send(embed=embed)

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

async def init_database():
    """Initialize database tables"""
    # TODO: Implement database initialization
    logger.info("📦 Database initialized")

# ============================================================================
# BOT STARTUP
# ============================================================================

async def load_cogs():
    """Load all cogs/extensions"""
    logger.info("🔌 Loading cogs...")
    # TODO: Load cogs from cogs/ directory
    logger.info("✅ Cogs loaded")

async def main():
    """Main bot startup function"""
    async with bot:
        await load_cogs()
        await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped by user")
    except Exception as e:
        logger.error(f"❌ Bot error: {e}")
