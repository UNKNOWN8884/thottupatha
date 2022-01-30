# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Rename-Bot-0")
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1287407305))
    CAPTION = "Rename Bot by @{}\n\nMade by @KDramasFlix"
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", "./downloads")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    ONE_PROCESS_ONLY = bool(os.environ.get("ONE_PROCESS_ONLY", False))
    START_TEXT = """
Hɪ Bʀᴏ/ Sɪs Hᴏᴡ Aʀᴇ Yᴏᴜ?

♥️MY Nᴀᴍᴇ Is :[Mᴋ Rᴇɴᴀᴍᴇʀ](https://t.me/Renamermk_bot)

♂️ I Rᴇɴᴀᴍᴇ Yᴏᴜʀ Fɪʟᴇs Wɪᴛʜ Mʏ Mᴀxɪᴍᴜᴍ Sᴘᴇᴇᴅ

♂️ Gɪᴠᴇ /help Fᴏʀ Mᴏʀᴇ Iɴғᴏ

♥️Mᴀᴅᴇ Bʏ:@CRACKERON
    """
    HELP_TEXT = """**Fᴏʟʟᴏᴡ Tʜᴇsᴇ Sᴛᴇᴘs Tᴏ Uɴᴅᴇʀsᴛᴀɴᴅ Mᴇ🦋**
 
**➠ Cᴏɴғɪɢᴜʀᴇ Mʏ Sᴇᴛᴛɪɴɢs Bᴇғᴏʀᴇ Usɪɴɢ Mᴇ🧬
➠ Sᴇɴᴅ A Pʜᴏᴛᴏ Tᴏ Sᴇᴛ As Tʜᴇ Fɪʟᴇ Pʜᴏᴛᴏ🧬
➠ Sᴇɴᴅ Aɴʏ Fɪʟᴇ Oʀ Vɪᴅᴇᴏ Tᴏ Rᴇɴᴀᴍᴇ🧬
➠ Aɴᴅ Sᴇɴᴅ Wʜᴀᴛ Fɪʟᴇ Nᴀᴍᴇ Yᴏᴜ Wᴀɴᴛ Tᴏ Sᴇᴛ🧬
      Eɴᴊᴏʏ Eɴᴊᴀᴍɪ🐗

📝 Rᴇɴᴀᴍᴇ Cᴏᴍᴍᴀɴᴅs 📝
- /start - Tᴏ Aᴡᴀᴋᴇ Mᴇ😇
- /help - Tᴏ Yᴏᴜ Kɴᴏᴡ Hᴏᴡ Tᴏ Usᴇ Mᴇ
- /about - Aʙᴏᴜᴛ Mᴇ🤭
- /settings - Sᴇᴛᴛɪɴɢs 👀
- /show_thumb & /del_thumb -Fᴏʀ Tʜᴜᴍʙᴀɴɪʟ

© Mᴀᴅᴇ Bʏ♥️ :@CRACKERON **
"""
    ABOUT_TEXT = """ 
╭───[🔅@Renamermk_bot🔅]──⍟
│
├🤖**Mʏ Nᴀᴍᴇ:** [Rᴇɴᴀᴍᴇʀ Mᴋ](https://t.me/renamermk_bot)

│
├📡**Hᴏsᴛɪɴɢ Oɴ:** Tᴇʟᴇɢʀᴀᴍ, Pʟᴜs

├👨‍💻**Developer:** [A Cʀᴀᴄᴋᴇʀ](https://t.me/CRACKERON) 

├👥**Bᴏᴛ Sᴜᴘᴘᴏʀᴛ :** [Sᴜᴘᴘᴏʀᴛ](https://t.me/Mksupport1)
│
   Tʜᴀɴᴋs Tᴏ Bʀᴏ/ Sɪs Usɪɴɢ ᴍᴇ♥️
│
╰──────[ ♥️ ]───────────⍟
    """
    PROGRESS = """\n
╭───[** Pʀᴏɢʀᴇss 🕐 **]───⍟
│
├📁 Sɪᴢᴇ : {2}
│
├✅ Dᴏɴᴇ : {1}
│
├🚀 Pᴇʀᴄᴇɴᴛᴀɢᴇ : {0}%
│
├⚡ Sᴘᴇᴇᴅ  : {6}/s
│
├⏱️ Tɪᴍᴇ : {5}
╰─────────────────⍟"""
