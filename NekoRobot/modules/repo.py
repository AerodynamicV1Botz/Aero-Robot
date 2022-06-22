"""
MIT License
Copyright (C) 2017-2019, Paul Larsen
Copyright (C) 2022 Awesome-Prince
Copyright (c) 2022, Koyūki • Network, <https://github.com/Awesome-Prince/NekoRobot-3>
This file is part of @NekoXRobot (Telegram Bot)
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the Software), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from telethon import events, Button, custom
import re, os
from NekoRobot.events import register
from NekoRobot import telethn as tbot
from NekoRobot import telethn as tgbot
PHOTO = "https://telegra.ph//file/930b78ad0d3629f7047ec.jpg"
@register(pattern=("/repo"))
async def awake(event):
  NEKO = """
         We Are So Happy To Announce That We Have Public Our NekoRobot Repo. ✨🥀
➖➖➖➖➖➖➖➖➖➖➖➖➖
「@AeroXRobot」
➖➖➖➖➖➖➖➖➖➖➖➖➖
Here is the Repo Deploy your Own NekoRobot.
⚜️Repo ➛ https://github.com/AerodynamicV1Botz/Aero-Robot.git
➖➖➖➖➖➖➖➖➖➖➖➖➖
🔰 Thanks for your support 
It's Fully stable Repo so you can deploy and make own Bot.
──────────────────
Powered By:- @AerodynamicV1_OFFICIAL
"""
  
  BUTTON = [[Button.url("📢 Repository", "https://github.com/AerodynamicV1Botz/Aero-Robot"), Button.url("💻 Collaborators", "https://telegra.ph//file/2a8e42a346478715b197f.jpg")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=NEKO,  buttons=BUTTON)
