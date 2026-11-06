# aMAZEing
<div align="center">

![](https://amaze.cc.cd/assets/logo.webp)

[get the latest release at amaze.cc.cd](https://amaze.cc.cd/)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?style=for-the-badge&logo=sdl&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-UI-orange?style=for-the-badge)
![MySQL](https://img.shields.io/badge/MySQL-Database-lightblue?style=for-the-badge&logo=mysql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

*A modern desktop maze puzzle experience combining retro grid-based navigation with a robust cloud-backed user profile & progression system.*

</div>

---

## Features

* **Interactive Desktop GUI:** Modern, sleek control panels and menus powered by **CustomTkinter**, paired with smooth game loops rendered via **Pygame**.
* **Cloud User Authentication:** Secure user sign-up and login utilizing **bcrypt** password hashing backed by a remote **MySQL** database.
* **Progress & Save Management:** Persistent player statistics, leaderboards, and custom binary save-file serialization.
* **Dynamic Maze Generation:** Engaging grid layouts designed to test your navigation and speed.

---

## Tech Stack

* **Language:** Python 3.10+
* **Frontend / UI:** Pygame, CustomTkinter
* **Database & Security:** MySQL, `bcrypt`
* **Data Handling:** Binary file I/O for quick local game state persistence

---

## Getting Started

### Prerequisites

Make sure you have Python installed on your system along with pip.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/caseharmony/Maze-Game.git
   cd Maze-Game
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Database Credentials:**
   Set up your connection string or environment variables for your Aiven Cloud MySQL instance in your configuration file.

4. **Run the application:**
   ```bash
   python gui.py
   ```

---


## Contributing

Contributions, feature requests, and bug reports are welcome! Feel free to open an issue or submit a pull request.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.
