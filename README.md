# 🐍 Classic Snake Game (Python Turtle)

A smooth and visually appealing **Snake Game** built using Python's built-in `turtle` graphics library.
Lightweight, beginner-friendly, and runs perfectly even on low-end systems like Intel UHD graphics.

---

## 🎮 Features

* 🐍 Classic Snake gameplay
* 🎯 Random food spawning with grid alignment
* 📈 Real-time score & high score tracking
* 💥 Collision detection (walls & self)
* 🔄 Automatic game reset on collision
* ⚡ Smooth performance with optimized frame delay
* 🎨 Clean and modern color theme

---

## 🖥️ Preview

```
Snake moves around the screen, eats food, grows longer,
and the game resets if it hits the wall or itself.
Try to beat your high score!
```

---

## 🎯 Controls

| Key            | Action     |
| -------------- | ---------- |
| ⬆️ Up Arrow    | Move Up    |
| ⬇️ Down Arrow  | Move Down  |
| ⬅️ Left Arrow  | Move Left  |
| ➡️ Right Arrow | Move Right |

---

## 🚀 Getting Started

### ✅ Prerequisites

* Python 3.x installed
* No external libraries required (uses built-in modules)

### ▶️ Run the Game

```bash
python snake_game.py
```

---

## 🛠️ Technologies Used

* 🐍 Python
* 🖌️ Turtle Graphics
* ⏱️ Time module
* 🎲 Random module

---

## ⚙️ Game Configuration

You can easily customize the game from the settings section:

```python
WIDTH, HEIGHT = 600, 600
DELAY = 0.1
SEGMENT_SIZE = 20
```

* **DELAY ↓** = Faster game
* **DELAY ↑** = Slower game

---

## 🎨 Color Theme

| Element    | Color Code |
| ---------- | ---------- |
| Background | #1a1a2e    |
| Snake Head | #e94560    |
| Snake Body | #0f3460    |
| Food       | #f5c542    |
| Text       | #ffffff    |

---

## 🧠 Game Logic Overview

* Snake moves continuously in the current direction
* Eating food:

  * Increases score
  * Adds a new segment
  * Spawns food at a new position
* Collision:

  * Wall or self → Game resets
  * High score is preserved

---

## 🔄 Future Improvements

* 🎵 Sound effects
* 🧩 Difficulty levels
* 💾 Save high score permanently
* 🎮 Pause/Resume feature
* 🖥️ Fullscreen mode

---

## 🤝 Contributing

Feel free to fork this repo and improve the game!
Pull requests are welcome.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## ⭐ Support

If you like this project, don't forget to **star ⭐ the repo**!

---

## 👨‍💻 Author

Made with ❤️ by **Divyansh Mourya**
