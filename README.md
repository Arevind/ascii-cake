# 🎂 ascii-cake 🎂  
_A birthday CLI app that mixes ASCII art, fireworks, music, and pure chaos_  
```
   ____       .-'''-.     _______  .-./`) .-./`)             _______      ____    .--.   .--.      .-''-.   
 .'  __ `.   / _     \   /   __  \ \ .-.')\ .-.')           /   __  \   .'  __ `. |  | _/  /     .'_ _   \  
/   '  \  \ (`' )/`--'  | ,_/  \__)/ `-' \/ `-' \          | ,_/  \__) /   '  \  \| (`' ) /     / ( ` )   ' 
|___|  /  |(_ o _).   ,-./  )       `-'`"` `-'`"`        ,-./  )       |___|  /  ||(_ ()_)     . (_ o _)  | 
   _.-`   | (_,_). '. \  '_ '`)     .---.  .---.         \  '_ '`)        _.-`   || (_,_)   __ |  (_,_)___| 
.'   _    |.---.  \  : > (_)  )  __ |   |  |   |          > (_)  )  __ .'   _    ||  |\ \  |  |'  \   .---. 
|  _( )_  |\    `-'  |(  .  .-'_/  )|   |  |   |         (  .  .-'_/  )|  _( )_  ||  | \ `'   / \  `-'    / 
\ (_ o _) / \       /  `-'`-'     / |   |  |   |          `-'`-'     / \ (_ o _) /|  |  \    /   \       /  
 '.(_,_).'   `-...-'     `._____.'  '---'  '---'            `._____.'   '.(_,_).' `--'   `'-'     `'-..-'   
                                                                                                            
```
---

## ✨ What is this?  

`ascii-cake` is a **birthday celebration in your terminal**.  
Think: 🎆 ASCII fireworks, 🎵 background music, 💌 scrolling letters, 🎭 fake "hacker" verifications, and a lot of fun styling via [Rich](https://github.com/Textualize/rich).  

If you want to surprise someone nerdy (or yourself 😅), just run this script and let the magic unfold.  

---

## 🎇 Features  

- **Fake scripts + verification quiz** 🕵️ – You need to "hack" your way in.  
- **Fireworks animation** 🎆 – Terminal-based explosions in full color.  
- **ASCII cake & visuals** 🍰 – Because birthdays need art.  
- **Background music** 🎵 – Plays via `pygame` if available, otherwise simulates sound.  
- **Scrolling birthday letter** 💌 – Slowly reveals a personal message.  
- **Finale celebration screen** 🎉 – Emojis, confetti vibes, and a warm goodbye.  

---

## 🛠️ Requirements  

- Python **3.7+**  
- Libraries:  
  - [`rich`](https://github.com/Textualize/rich) → colorful CLI magic ✨  
  - [`pygame`](https://www.pygame.org/) (optional, for music playback 🎵)  

## ▶️ Usage

1. Clone the repo:
```bash
git clone https://github.com/Arevind/ascii-cake.git
cd ascii-cake
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the script:
```bash
python fireworks.py
```

4. Sit back and enjoy 🎂

5. (Optional) To convert this into an executable(Windows):
```bash
pip install pyinstaller
pyinstaller --onefile fireworks.py
```
The `.exe` will be available inside the dist/ folder. 

⚠️ Pro tip: Keep your volume on for the full experience.

## 🔐 A Sneak Peek
1.
<img width="1621" height="908" alt="Screenshot 2025-09-18 165558" src="https://github.com/user-attachments/assets/827ba9b1-74eb-4c31-b5d2-ec11860d6949" />
2.
<img width="1639" height="904" alt="Screenshot 2025-09-18 165853" src="https://github.com/user-attachments/assets/adafdd24-5847-4091-b846-e01b62dc0e83" />
3.
<img width="1573" height="880" alt="Screenshot 2025-09-18 165934" src="https://github.com/user-attachments/assets/634adda1-0999-49c1-bd08-bb5f52f15f82" />

```python
📂 Project Structure
ascii-cake/
│
├── fireworks.py      # Main script
├── fireworks.spec 
├── music.mp3         # (Optional) bundled birthday track
├── requirements.txt
└── README.md         # You're reading it 🎉
```
## 🎵 Music
- Included music by [pianocafe_Kumi](https://pixabay.com/users/pianocafe_kumi-35185506/)
   
- Default file name: `music.mp3`

- If not found, the app switches to simulation mode 🎶 (fake notes in the console).

- You can drop in any `.mp3` you like.(just name it to music)

## 🎁 Why did I build this?

Because sometimes a git repo can be a gift.
This is a small, chaotic, terminal-based way of saying:

"Happy Birthday, you beautiful nerd." 💖

## 🚀 Future Add-ons (if I ever stop celebrating)

-  Text-to-Speech birthday wishes

-  Customizable quizzes

-  Extra ASCII animations (balloons, cake candles, etc.)

##  Author

Built with too much coffee ☕ and a questionable sense of humor by Arevind Mohan.

## 🎉 Final Words

Run it, share it, fork it.
Make someone’s day better with a little terminal confetti.

🎂  🎈  🎁  ✨  🌟  💖  🎊  🥳


