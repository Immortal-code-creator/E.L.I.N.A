# 🤖 E.L.I.N.A – Python-Based Personal AI Assistant

E.L.I.N.A (Enhanced Logical Intelligent Network Assistant) is a Python-based personal AI assistant designed to increase productivity, automate daily tasks, and reduce manual work.
It operates via command-line input and uses text-to-speech to interact with the user.

The assistant can greet users based on system time, play random music or movies, fetch weather reports, open websites and applications, launch games, and read out the latest news.

## 📖 DESCRIPTION

E.L.I.N.A is a lightweight, beginner-friendly AI assistant built entirely in Python.
Since no microphone was available, the assistant works through typed commands instead of voice recognition, making it simple and reliable.

It uses pyttsx3 for offline text-to-speech and integrates multiple APIs for real-time data such as weather and news.

## ✨ FEATURES

🔊 Text-to-Speech interaction using pyttsx3

🕒 Time-based greetings (Good Morning / Afternoon / Evening / Night)

🎵 Plays random music from local directory

🎬 Plays random movies from local directory

🌦 Real-time weather report for any location

📰 Reads latest 5 news headlines

🌐 Opens popular websites (Google, YouTube, GitHub, ChatGPT, etc.)

🎮 Launches games (if installed locally)

💻 Opens applications like VS Code

📚 Wikipedia search and summary

🧠 Command-line based interaction

## 🗂 SUPPORTED COMMANDS
### 🕰 Utility

- Time

- Date

- Weather report

### 🌐 Websites

-Google

-YouTube

-GitHub

-ChatGPT

-LeetCode

-Gmail

-Discord

-StackOverflow

-Reddit

-LinkedIn

-Twitter (X)

-Instagram

-Facebook

-Amazon

-Flipkart

-Netflix

-Prime Video

-Hotstar

-Canva

-WhatsApp

-Telegram
(and more)

### 🎮 Entertainment

-Play music

-Play movie

-Open Cuphead (if installed)

-Open Elden Ring (if installed)

### 📰 Information

-Latest news (Top 5)

-Wikipedia summaries

### 🧠 CONCEPTS USED

-Text-to-Speech (TTS)

-REST APIs

-API integration (News & Weather)

-Python modules and packages

-File handling

-OS-level application launching

-Conditional statements & loops

-Exception handling

-Command-line input handling

## 🛠 DEPENDENCIES

-Python 3.10 or later

-Windows OS (required for pyttsx3 SAPI5)

## 📦 MODULES USED

-pyttsx3

-datetime

-wikipedia

-webbrowser

-os

-random

-requests

## 📥 INSTALL DEPENDENCIES
-pip install pyttsx3 wikipedia requests

## 🔑 APIS USED
🌦 OpenWeatherMap API

-Used for real-time weather reports

-Requires API key

📰 NewsData.io API

-Used for fetching latest news

-Requires API key

⚠️ Replace API keys with your own keys before production use

## 🔑 Generate API_KEYS
- Go to openweather.org and create API_KEY and put it in place of "write API_KEY" in W-report() function
- Go to newsdata.io and create API_KEY and put it in place of "write API_KEY" in news() function

## ⚙️ HOW THE ASSISTANT WORKS

-User runs the program

-E.L.I.N.A greets the user using text-to-speech

-User enters commands via keyboard

-Assistant processes the command

-Corresponding function is executed

-Output is spoken aloud and/or displayed

## ▶️ EXECUTING THE PROGRAM
python elina.py

## ❓ TROUBLESHOOTING

-If the assistant does not work correctly:

-Ensure you are on Windows OS

-Check Python version:
    -python --version


-Verify all required modules are installed

-Check internet connection for weather, news and wikipedia

-Ensure file paths for music, movies, games, and apps are correct

-Verify API keys are valid

## 👨‍💻 AUTHOR

Aeshan Chowdhury
### GitHub: https://github.com/Immortal-code-creator
