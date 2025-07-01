import asyncio import os from datetime import datetime, timedelta from typing import Union

from pyrogram import Client from pyrogram.types import InlineKeyboardMarkup from pytgcalls import PyTgCalls from pytgcalls.exceptions import ( AlreadyJoinedError, NoActiveGroupCall, TelegramServerError, ) from pytgcalls.types import Update from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped from pytgcalls.types.input_stream.quality import HighQualityAudio, MediumQualityVideo from pytgcalls.types.stream import StreamAudioEnded

import config from SONALI import LOGGER, YouTube, app from SONALI.misc import db from SONALI.utils.database import ( add_active_chat, add_active_video_chat, get_lang, get_loop, group_assistant, is_autoend, music_on, remove_active_chat, remove_active_video_chat, set_loop, ) from SONALI.utils.exceptions import AssistantErr from SONALI.utils.formatters import check_duration, seconds_to_min, speed_converter from SONALI.utils.inline.play import stream_markup, telegram_markup from SONALI.utils.stream.autoclear import auto_clean from SONALI.utils.thumbnails import get_thumb from strings import get_string

class Call: def init(self): self.userbot1 = Client("RAUSHANAss1", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.STRING1)) self.one = PyTgCalls(self.userbot1)

self.userbot2 = Client("RAUSHANAss2", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.STRING2))
    self.two = PyTgCalls(self.userbot2)

    self.userbot3 = Client("RAUSHANXAss3", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.STRING3))
    self.three = PyTgCalls(self.userbot3)

    self.userbot4 = Client("RAUSHANXAss4", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.STRING4))
    self.four = PyTgCalls(self.userbot4)

    self.userbot5 = Client("RAUSHANAss5", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.STRING5))
    self.five = PyTgCalls(self.userbot5)

async def stop_stream(self, chat_id: int):
    assistant = await group_assistant(self, chat_id)
    try:
        await assistant.leave_group_call(chat_id)
    except:
        pass

async def skip_stream(self, chat_id: int, link: str, video: Union[bool, str] = None):
    assistant = await group_assistant(self, chat_id)
    stream = AudioVideoPiped(link, audio_parameters=HighQualityAudio(), video_parameters=MediumQualityVideo()) if video else AudioPiped(link, audio_parameters=HighQualityAudio())
    await assistant.change_stream(chat_id, stream)

async def join_call(self, chat_id: int, link, video: Union[bool, str] = None):
    assistant = await group_assistant(self, chat_id)
    language = await get_lang(chat_id)
    _ = get_string(language)
    stream = AudioVideoPiped(link, audio_parameters=HighQualityAudio(), video_parameters=MediumQualityVideo()) if video else AudioPiped(link, audio_parameters=HighQualityAudio())
    try:
        await assistant.join_group_call(chat_id, stream)
    except NoActiveGroupCall:
        raise AssistantErr(_["call_8"])
    except AlreadyJoinedError:
        raise AssistantErr(_["call_9"])
    except TelegramServerError:
        raise AssistantErr(_["call_10"])
    await add_active_chat(chat_id)
    await music_on(chat_id)
    if video:
        await add_active_video_chat(chat_id)

async def start(self):
    LOGGER(__name__).info("Starting PyTgCalls Client...")
    if config.STRING1:
        await self.one.start()
    if config.STRING2:
        await self.two.start()
    if config.STRING3:
        await self.three.start()
    if config.STRING4:
        await self.four.start()
    if config.STRING5:
        await self.five.start()

RAUSHAN = Call()

