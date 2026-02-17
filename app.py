import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="Huang's Guardian - A Gift for You",
    page_icon="🐱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# كود CSS لإخفاء عناصر Streamlit الزائدة
st.markdown("""
<style>
    .stApp > header { display: none; }
    .main .block-container { 
        padding: 0 !important; 
        margin: 0 !important; 
        max-width: 100% !important;
    }
    iframe {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# محتوى الـ HTML
html_content = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Huang's Guardian</title>
    <link href="https://fonts.googleapis.com/css2?family=Zhi+Mang+Xing&family=Ma+Shan+Zheng&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        :root {
            --imperial-red: #8b0000;
            --royal-gold: #ffd700;
            --aged-parchment: #f5e6d3;
        }
        body, html {
            margin: 0; padding: 0;
            width: 100%; height: 100%;
            overflow: hidden;
            background-color: var(--aged-parchment);
            font-family: 'Ma Shan Zheng', cursive;
        }
        .background {
            position: fixed; top: 0; left: 0;
            width: 100%; height: 100%;
            background: url('https://images.unsplash.com/photo-1528164344705-47542687000d?auto=format&fit=crop&w=1920&q=80') no-repeat center center;
            background-size: cover;
            z-index: -1;
            filter: brightness(0.9) saturate(1.2);
        }
        .border-frame {
            position: fixed; top: 2vw; left: 2vw; right: 2vw; bottom: 2vw;
            border: 3px solid var(--royal-gold);
            box-shadow: 0 0 15px var(--royal-gold);
            pointer-events: none; z-index: 100;
        }
        .pet-container {
            position: absolute; bottom: 20vh; left: 50%;
            transform: translateX(-50%); text-align: center;
            cursor: pointer; -webkit-tap-highlight-color: transparent;
        }
        .pet-sprite {
            width: 45vw; max-width: 220px;
            height: 45vw; max-height: 220px;
            object-fit: cover; border-radius: 50%;
            border: 4px solid var(--royal-gold);
            animation: float 4s ease-in-out infinite;
        }
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }
        .speech-bubble {
            position: absolute; top: -10vh; left: 50%;
            transform: translateX(-50%) scale(0);
            background: rgba(255, 255, 255, 0.95);
            padding: 1.5vh 3vh; border-radius: 20px;
            border: 2px solid var(--imperial-red);
            font-family: 'Zhi Mang Xing', cursive;
            font-size: 3.5vh; color: var(--imperial-red);
            white-space: nowrap; transition: transform 0.3s;
        }
        .ui-container {
            position: fixed; bottom: 5vh;
            width: 100%; display: flex;
            justify-content: center; gap: 4vw; z-index: 101;
        }
        .btn {
            background: var(--imperial-red); color: var(--royal-gold);
            border: 2px solid var(--royal-gold); padding: 1.2vh 4vw;
            font-size: 2.5vh; border-radius: 10px;
            cursor: pointer; font-family: 'Ma Shan Zheng', cursive;
        }
        .title-container {
            position: fixed; top: 6vh; width: 100%;
            text-align: center; color: var(--royal-gold);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5); z-index: 101;
        }
        .petal {
            position: absolute; background-color: #ffb7c5;
            border-radius: 150% 0 150% 0;
            animation: fall linear infinite; pointer-events: none;
        }
        @keyframes fall {
            0% { transform: translate(0, -10vh) rotate(0deg); opacity: 1; }
            100% { transform: translate(10vw, 110vh) rotate(360deg); opacity: 0; }
        }
    </style>
</head>
<body>
    <div class="background"></div>
    <div class="border-frame"></div>
    <div class="title-container">
        <h1 style="font-family: 'Zhi Mang Xing'; font-size: 7vh; margin:0;">Huang 的守护者</h1>
        <div style="font-size: 2vh;">Huang's Eternal Guardian</div>
    </div>
    <div class="pet-container" onclick="playVoice()">
        <div id="speech" class="speech-bubble">喵!</div>
        <img src="https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=500&q=80" class="pet-sprite">
    </div>
    <div class="ui-container">
        <button class="btn" onclick="feed()">喂食 (Feed)</button>
        <button class="btn" onclick="playVoice()">听听我想对你说 (Listen)</button>
    </div>
    <audio id="main-audio" src="https://raw.githubusercontent.com/danial287200/Huang-1/main/cat%20voice.mp3" preload="auto"></audio>
    <script>
        function showSpeech(text, duration) {
            const speech = document.getElementById('speech');
            speech.innerText = text;
            speech.style.transform = 'translateX(-50%) scale(1)';
            setTimeout(() => {
                speech.style.transform = 'translateX(-50%) scale(0)';
            }, duration);
        }
        function playVoice() {
            const audio = document.getElementById('main-audio');
            audio.currentTime = 0;
            audio.play().catch(e => console.log("Audio Error:", e));
            showSpeech("我爱你, Huang! ❤️", 3000);
        }
        function feed() {
            confetti({
                particleCount: 100,
                spread: 70,
                origin: { y: 0.7 }
            });
            showSpeech("好香啊! (Yummy!)", 2000);
        }
        function createPetal() {
            const petal = document.createElement('div');
            petal.className = 'petal';
            petal.style.left = Math.random() * 100 + 'vw';
            petal.style.width = (Math.random() * 1 + 1) + 'vw';
            petal.style.height = petal.style.width;
            petal.style.animationDuration = (Math.random() * 3 + 4) + 's';
            document.body.appendChild(petal);
            setTimeout(() => petal.remove(), 7000);
        }
        setInterval(createPetal, 500);
    </script>
</body>
</html>
"""

# عرض المكون
components.html(html_content, height=1200, scrolling=False)
