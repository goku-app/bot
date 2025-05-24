
<p align="center">
  <img src="https://cdn.pfps.gg/pfps/5277-goku-ultra-instinct.gif" width="150" height="150">
  <h1 align="center">GOKU - Discord Raid Bot</h1>
</p>

<p align="center">
  <a href="https://github.com/goku-app/bot/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/goku-app/bot?style=social"></a>
  <a href="https://github.com/goku-app/bot/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/goku-app/bot?style=social"></a>
  <a href="https://github.com/goku-app/bot/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/goku-app/bot"></a>
  <a href="https://github.com/goku-app/bot/commits/main"><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/goku-app/bot"></a>
</p>

<p align="center">
GOKU is a <b>Discord raid bot</b> designed for <b>educational and development purposes only</b>. It allows users to send automated messages and flood a server with custom spam messages without admin permissions.  
</p>

---

## 📑 Table of Contents
- [How It Works](#-how-it-works)
- [Commands](#-commands)
- [Demonstration](#-demonstration)
- [Example Usage](#-example-usage)
- [Installation](#-installation)
- [Star History](#%EF%B8%8F-star-history)

---

## 📌 How It Works  
1. **Add the bot to your Discord Account**  
2. **Use slash commands** to execute actions  
3. **Watch it spam messages** in public channels  

---

## 📜 Commands  

### `/kill`  
🔹 Starts spamming a preset raid message.  

### `/kill-custom <message>`  
🔹 Spams the server with a **custom message**.  

### `/send <message> [anonymous]`  
🔹 Sends a **single message**, either publicly or anonymously.  

### `/help`  
🔹 Displays bot information and the support server link.  

## ⚙ Demonstration  

This bot is also self-hosted by me. You can invite it on our Discord server: **[dsc.gg/beignet](https://discord.gg/sc5tfyEUqD)**. You are free to host this yourself.  

## 🚀 Example Usage

> [!IMPORTANT]  
> For the commands to work, it is necessary to have the **'Use External Apps'** permission enabled in the current channel. Otherwise, the messages will be private and will only be seen by the user itself. You can use Vencord's Plugin called [PermissionsViewer](https://vencord.dev/plugins/PermissionsViewer) to see the permissions in the channel.

```sh
/kill
# The bot floods the channel with pre-made raid messages
```

```sh
/kill-custom text:Hello
# The bot floods the channel with custom raid messages
```

```sh
/send text:Hello anonymous=True
# The bot sends a simple message anonymously.

/send text:Hello anonymous=False
# The bot sends a simple message, but the username of the person is visible.
```

> [!NOTE]
> Even if your username is hidden from the messages, that doesn’t mean you’re completely hidden from them! Setting the value "anonymous" to true makes it harder for others to find, but people can still see your username and ban you. You can check out [NTTS's video](https://youtu.be/6vjG34uyPz0?si=Zc1ulknyH6eQRRdL&t=329) where this is explained in detail.

## 🔧 Installation  

1. [**Download the latest release**](https://github.com/goku-app/bot/releases/latest).
   
3. **Unarchive the ZIP file you downloaded from the release.**

4. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
5. **Add your bot token:**
   
   Open src/TOKEN.txt and paste your Discord bot token inside.

6. **Run the bot:**
   ```sh
   python bot.py
   ```
## ⭐️ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=goku-app/bot&type=Date)](https://www.star-history.com/#goku-app/bot&Date)
