"""
Configuration settings for ServerGuard Pro
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Discord Bot Configuration
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
COMMAND_PREFIX = os.getenv("PREFIX", "!")
BOT_INTENTS = [
    "message_content",
    "members",
    "guilds",
    "guild_messages",
    "direct_messages",
    "moderation",
]

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///serverguard.db")

# Stripe Configuration (Payment Processing)
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY")
PREMIUM_PRICE_ID = os.getenv("PREMIUM_PRICE_ID", "price_1234567890")

# Bot Settings
BOT_NAME = "ServerGuard Pro"
BOT_VERSION = "1.0.0"
SUPPORT_SERVER = "https://discord.gg/serverguard"

# Premium Features
PREMIUM_PRICE = 4.99
PREMIUM_FEATURES = [
    "advanced_moderation",
    "analytics_dashboard",
    "custom_commands",
    "priority_support",
    "role_reactions",
    "advanced_logging",
    "member_verification",
]

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = "serverguard.log"
