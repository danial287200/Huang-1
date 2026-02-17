import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Huang's Guardian - A Gift for You",
    page_icon="🐱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to ensure the component is truly full-screen
st.markdown("""
<style>
    /* Reset Streamlit's default padding and margins */
    .stApp > header { display: none; }
    .main .block-container { 
        padding: 0 !important; 
        margin: 0 !important; 
        max-width: 100% !important;
    }
    /* Ensure the iframe fills the entire viewport */
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
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            background-color: var(--aged-parchment);
            font-family: 'Ma Shan Zheng', cursive;
        }

        .background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: url('https://images.unsplash.com/photo-1528164344705-47542687000d?auto=format&fit=crop&w=1920&q=80') no-repeat center center;
            background-size: cover;
            z-index: -1;
            filter: brightness(0.9) saturate(1.2);
        }

        .overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle, transparent 60%, rgba(0,0,0,0.2));
            pointer-events: none;
        }

        .border-frame {
            position: fixed;
            top: 2vw;
            left: 2vw;
            right: 2vw;
            bottom: 2vw;
            border: 3px solid var(--royal-gold);
            box-shadow: 0 0 15px var(--royal-gold), inset 0 0 10px var(--royal-gold);
            border-image: url('https://i.imgur.com/6fP6mN2.png') 30 round;
            border-image-slice: 30;
            border-image-width: 15px;
            pointer-events: none;
            z-index: 100;
        }

        .pet-container {
            position: absolute;
            bottom: 15vh;
            left: 50%;
            transform: translateX(-50%);
            text-align: center;
            cursor: pointer;
            -webkit-tap-highlight-color: transparent; /* For mobile tap feedback */
        }

        .pet-sprite {
            width: 40vw;
            max-width: 200px;
            height: 40vw;
            max-height: 200px;
            object-fit: cover;
            border-radius: 50%;
            border: 4px solid var(--royal-gold);
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
            animation: float 4s ease-in-out infinite;
            transition: transform 0.2s;
        }

        .pet-sprite:active {
            transform: scale(0.95);
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-15px); }
        }

        .speech-bubble {
            position: absolute;
            top: -8vh;
            left: 50%;
            transform: translateX(-50%) scale(0);
            background: rgba(255, 255, 255, 0.9);
            padding: 1.5vh 3vh;
            border-radius: 20px;
            border: 2px solid var(--imperial-red);
            font-family: 'Zhi Mang Xing', cursive;
            font-size: 4vh;
            color: var(--imperial-red);
            white-space: nowrap;
            z-index: 10;
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .ui-container {
            position: fixed;
            bottom: 5vh;
            width: 100%;
            display: flex;
            justify-content: center;
            gap: 5vw;
            z-index: 101;
        }

        .btn {
            background: var(--imperial-red);
            color: var(--royal-gold);
            border: 2px solid var(--royal-gold);
            padding: 1.5vh 4vw;
            font-size: 3vh;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 4px 8px rgba(0,0,0,0.4);
            transition: all 0.2s;
            font-family: 'Ma Shan Zheng', cursive;
            -webkit-tap-highlight-color: transparent;
        }

        .btn:active {
            background: #a00000;
            transform: translateY(2px);
            box-shadow: 0 2px 4px rgba(0,0,0,0.4);
        }

        .btn-subtitle {
            display: block;
            font-size: 1.5vh;
            opacity: 0.8;
            font-family: sans-serif;
        }

        .title-container {
            position: fixed;
            top: 5vh;
            width: 100%;
            text-align: center;
            color: var(--royal-gold);
            text-shadow: 3px 3px 6px rgba(139, 0, 0, 0.7);
            z-index: 101;
        }

        .title-main {
            font-family: 'Zhi Mang Xing', cursive;
            font-size: 8vh;
            margin: 0;
        }

        .title-sub {
            font-size: 2.5vh;
            letter-spacing: 2px;
        }

        .petal {
            position: absolute;
            background-color: #ffb7c5;
            border-radius: 150% 0 150% 0;
            animation: fall linear infinite;
            z-index: 1;
            pointer-events: none;
        }

        @keyframes fall {
            0% { transform: translate(0, -10vh) rotate(0deg); opacity: 1; }
            100% { transform: translate(10vw, 110vh) rotate(360deg); opacity: 0; }
        }
    </style>
</head>
<body>
    <div class="background"></div>
    <div class="overlay"></div>
    <div class="border-frame"></div>

    <div class="title-container">
        <h1 class="title-main">Huang 的守护者</h1>
        <div class="title-sub">Huang's Guardian</div>
    </div>

    <div class="pet-container" ontouchstart="meow(event)" onclick="meow(event)">
        <div id="speech" class="speech-bubble">喵!</div>
        <img src="https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=500&q=80" alt="Calico Cat" class="pet-sprite">
    </div>

    <div class="ui-container">
        <button class="btn" ontouchstart="feed(event)" onclick="feed(event)">
            喂食
            <span class="btn-subtitle">Feed</span>
        </button>
        <button class="btn" ontouchstart="playMessage(event)" onclick="playMessage(event)">
            听听我想对你说
            <span class="btn-subtitle">A Message for Huang</span>
        </button>
    </div>

    <audio id="meow-sound" src="https://www.myinstants.com/media/sounds/kawaii-meow.mp3" preload="auto"></audio>
    <audio id="voice-message" src="https://www.myinstants.com/media/sounds/kawaii-meow.mp3" preload="auto"></audio> <!-- Placeholder -->

    <script>
        // Prevent double-triggering on mobile
        let lastTouchTime = 0;
        function isFastClick(event) {
            const time = new Date().getTime();
            if (event.type === 'click' && time - lastTouchTime < 500) {
                return true;
            }
            if (event.type === 'touchstart') {
                lastTouchTime = time;
            }
            return false;
        }

        function showSpeech(text, duration) {
            const speech = document.getElementById('speech');
            speech.innerText = text;
            speech.style.transform = 'translateX(-50%) scale(1)';
            setTimeout(() => {
                speech.style.transform = 'translateX(-50%) scale(0)';
            }, duration);
        }

        function meow(event) {
            if (isFastClick(event)) return;
            const sound = document.getElementById('meow-sound');
            sound.currentTime = 0;
            sound.play().catch(e => console.log("Audio play failed:", e));
            showSpeech("喵! (Meow!)", 1500);
        }

        function feed(event) {
            if (isFastClick(event)) return;
            confetti({
                particleCount: 150,
                spread: 90,
                origin: { y: 0.6 },
                colors: ['#ff4757', '#ff6b81', '#ffa502', '#ffc048']
            });
            showSpeech("好香啊! (Yummy!)", 2000);
        }

        function playMessage(event) {
            if (isFastClick(event)) return;
            const voice = document.getElementById('voice-message');
            voice.currentTime = 0;
            voice.play().catch(e => console.log("Audio play failed:", e));
            showSpeech("我爱你, Huang! ❤️", 3000);
        }

        function createPetal() {
            const petal = document.createElement('div');
            petal.className = 'petal';
            petal.style.left = Math.random() * 100 + 'vw';
            petal.style.width = (Math.random() * 1 + 1) + 'vw';
            petal.style.height = petal.style.width;
            petal.style.opacity = Math.random() * 0.7 + 0.3;
            petal.style.animationDuration = (Math.random() * 3 + 4) + 's';
            petal.style.animationDelay = (Math.random() * 2) + 's';
            
            document.body.appendChild(petal);
            
            setTimeout(() => {
                petal.remove();
            }, 7000);
        }

        // Initial setup
        document.addEventListener('DOMContentLoaded', () => {
            for (let i = 0; i < 20; i++) {
                createPetal();
            }
            setInterval(createPetal, 500);
        });
    </script>
</body>
</html>
"""

components.html(html_content, height=3000, scrolling=False)
