![Logo](animated_logo.gif)

# 🎬 Lanflix · 局域网本地视频播放器

**Lanflix** is a lightweight **local video player** made for **older smart TVs** like LG Netcast. It plays your `.mp4` files directly from your PC using your **home network** (Wi-Fi or LAN), through the TV's browser. No internet or extra installation needed.

💡 100% offline · No accounts · No external access · Pure HTML5 + LAN only


## 🚀 Features

* 📁 Automatically plays any `.mp4` file placed in the `localMovies/` folder
* 🖥️ Simple interface controllable with your TV's keyboard or mouse
* 🔄 Works on old browsers (uses `XMLHttpRequest`, no `fetch`, no ES6)
* 🌐 If internet is available, streams public domain movies from Archive.org
* 🔒 Your files never leave your local network


## 📦 Project Structure

```
Lanflix/
├── index.html        # Main UI
├── server.py         # Local web server
└── localMovies/      # Folder for your movie files (.mp4)
```


## 🧑‍💻 How to Use Lanflix

1. 📥 Clone or download the repository:

   ```bash
   git clone https://github.com/dfralan/lanflix.git
   cd lanflix
   ```

2. 🎞️ Copy your `.mp4` movie files into the `localMovies/` folder.

3. ▶️ Start the local server:

   ```bash
   python3 server.py
   ```

   Output should look like:

   ```
   📡 Server running at:
      👉 Local:      http://localhost:8080
      👉 On your LAN: http://192.168.1.100:8080
   ```

4. 📺 On your smart TV browser (Netcast or other), go to:

   ```
   http://192.168.1.100:8080
   ```

5. 🍿 Pick a movie and enjoy fullscreen playback!



## 🌐 Optional: Public Domain Movies

If your network has internet access, Lanflix can also show a few hand-picked **classic public domain films** from [Archive.org](https://archive.org), including:

* *Night of the Living Dead* (1968)
* *Plan 9 from Outer Space* (1959)
* *Sherlock Holmes* (1922)

## 📋 Requirements

* Python 3.x
* A browser that supports HTML5 video (.mp4) — even on old TVs
* All devices must be connected to the **same local network**



## 🛠️ Technical Details

* `server.py` uses Python’s built-in `http.server` and auto-detects your local IP
* `index.html` is 100% flat: no frameworks, no modern JS
* Your files are never shared online — only inside your LAN



## 📄 License

MIT License



![Logo](logo.svg)

## ✨ Built with love by cinephiles who won’t throw away their TV