# enemy_data.py
ENEMY_SPAWN_DATA = [
  {
    #1
    "weak": 15,
    "medium": 0,
    "strong": 0,
    "elite": 0
  },
  {
    #2
    "weak": 30,
    "medium": 0,
    "strong": 0,
    "elite": 0
  },
  {
    #3
    "weak": 20,
    "medium": 5,
    "strong": 0,
    "elite": 0
  },
  {
    #4
    "weak": 30,
    "medium": 15,
    "strong": 0,
    "elite": 0
  },
  {
    #5
    "weak": 5,
    "medium": 20,
    "strong": 0,
    "elite": 0
  },
  {
    #6
    "weak": 15,
    "medium": 15,
    "strong": 4,
    "elite": 0
  },
  {
    #7
    "weak": 20,
    "medium": 25,
    "strong": 5,
    "elite": 0
  },
  {
    #8
    "weak": 10,
    "medium": 20,
    "strong": 15,
    "elite": 0
  },
  {
    #9
    "weak": 15,
    "medium": 10,
    "strong": 5,
    "elite": 0
  },
  {
    #10
    "weak": 0,
    "medium": 100,
    "strong": 0,
    "elite": 0
  },
  {
    #11
    "weak": 5,
    "medium": 10,
    "strong": 12,
    "elite": 2
  },
  {
    #12
    "weak": 0,
    "medium": 15,
    "strong": 10,
    "elite": 5
  },
  {
    #13
    "weak": 20,
    "medium": 0,
    "strong": 25,
    "elite": 10
  },
  {
    #14
    "weak": 15,
    "medium": 15,
    "strong": 15,
    "elite": 15
  },
  {
    #15
    "weak": 25,
    "medium": 25,
    "strong": 25,
    "elite": 25
  }
]

ENEMY_DATA = {
    "weak": {
    "health": 100,
    "speed": 2,
    "damage": 5,
    "attack_cooldown": 1000 # Contoh: serang setiap 1 detik
  },
    "medium": {
    "health": 150,
    "speed": 3,
    "damage": 8,
    "attack_cooldown": 1200 # Contoh: serang setiap 1.2 detik
  },
    "strong": {
    "health": 200,
    "speed": 4,
    "damage": 10,
    "attack_cooldown": 1500 # Contoh: serang setiap 1.5 detik
  },
    "elite": {
    "health": 300,
    "speed": 6,
    "damage": 15,
    "attack_cooldown": 800 # Contoh: serang setiap 0.8 detik
  }
}