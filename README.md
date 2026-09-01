# ServerGuard Pro 🛡️

A powerful, feature-rich Discord bot for server management, moderation, and automation. Free tier + premium features.

## Features

### Free Tier
- ✅ Basic moderation (kick, ban, mute, warn)
- ✅ Welcome messages & member management
- ✅ Simple logging & audit trails
- ✅ Basic role management
- ✅ Community commands (ping, uptime, help)

### Premium Tier ($4.99/month)
- 🎯 Advanced auto-moderation (spam, toxicity detection)
- 🎯 Detailed analytics & statistics dashboard
- 🎯 Custom commands & automations
- 🎯 Premium support & priority updates
- 🎯 Role reaction messages
- 🎯 Advanced logging with filters
- 🎯 Member verification system

## Quick Start

### Prerequisites
- Python 3.9+
- Discord bot token (create at [Discord Developer Portal](https://discord.com/developers/applications))

### Installation

```bash
git clone https://github.com/Izo-200812/ServerGuard-Pro.git
cd ServerGuard-Pro
pip install -r requirements.txt
```

### Configuration

1. Create a `.env` file:
```
DISCORD_TOKEN=your_bot_token_here
DATABASE_URL=sqlite:///serverguard.db
STRIPE_KEY=your_stripe_key_here
```

2. Run the bot:
```bash
python main.py
```

## Monetization Strategy

- **Stripe Integration** for premium subscriptions ($4.99/month)
- **Premium server tier** - unlock all features
- **Custom bot hosting** - premium support option
- **Dashboard access** - analytics & configuration panel

## Project Structure

```
ServerGuard-Pro/
├── main.py              # Bot entry point
├── cogs/
│   ├── moderation.py    # Moderation commands
│   ├── logging.py       # Logging & audit
│   └── premium.py       # Premium features
├── utils/
│   ├── database.py      # Database operations
│   └── stripe_api.py    # Payment processing
├── config.py            # Configuration
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## Contributing

Contributions welcome! Open an issue or PR to improve the bot.

## License

MIT License - see LICENSE file

## Support

- 📧 Email: support@serverguard.dev
- 🔗 Discord: [Join our server](https://discord.gg/serverguard)
- 📊 Dashboard: https://serverguard.dev

---

**Made with ❤️ by the ServerGuard Team**
