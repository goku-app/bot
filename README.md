<p align="center">
  <img src="https://cdn.pfps.gg/pfps/5277-goku-ultra-instinct.gif" width="150" height="150">
  <h1 align="center">GOKU - Discord Raid Bot</h1>
</p>
<p align="center">
GOKU is a <b>Discord raid bot</b> designed for <b>educational and development purposes only</b>. It allows users to send automated messages and flood a server with custom spam messages.  
</p>

---

## 📑 Table of Contents
- [How It Works](#-how-it-works)
- [Commands](#-commands)
- [Demonstration](#-demonstration)
- [Example Usage](#-example-usage)
- [Installation](#-installation)

---

## 📌 How It Works  
1. **Add the bot to your server**  
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

This bot is also self-hosted by me. You can invite it on our Discord server: **[dsc.gg/beignet](https://discord.gg/sc5tfyEUqD)**.  

## 🚀 Example Usage

> [!IMPORTANT]  
> For the commands to work, it is necessary to have the **'Use External Apps'** permission enabled in the current channel. Otherwise, the messages will be private and will only be seen by the user itself. 

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

## 🔧 Installation  

1. **Clone the repository:**  
   ```sh
   gh repo clone jacklebeignet/goku
   cd goku
   ```

2. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Add your bot token:**
   
   Open src/TOKEN.txt and paste your Discord bot token inside.

4. **Run the bot:**
   ```sh
   python bot.py
   ```
