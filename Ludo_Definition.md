## Ludo Definition

After researching different interpretations of Ludo, I propose my own definition of its rules, divided into two categories:

* **Strict Ludo Rule Set**: a foundational rule set that defines what most *common* Ludo games share.
* **Loose Ludo Rule Set**: a minimal rule set containing only the essential elements required for a game to still be considered Ludo.

This project will initially follow the **Strict Ludo Rule Set**, and will gradually relax constraints until it reaches the **Loose Ludo** definition.

The rules presented here are **arbitrary and opinion-based**. Different interpretations are valid, and others may disagree on what should be considered “Strict Ludo”.

Each Rule is supposed to only contain one fundamental information about the game

---

## Strict Ludo

### Core Definition

1. Ludo is a **turn-based board game**.
2. It is played by **2 to 4 players**.
3. Each player is assigned a **unique color**.
4. The game is played on a **cyclical board**.
5. The game uses **markers** that match each player’s color.
6. Each player has **exactly 4 markers**.
7. A player may only move **markers they own**.
8. All markers are **provided by the game**.
9. Each marker progresses through **four phases**: **Start**, **Path**, **End Path**, and **Finish**.
10. Each player has their own **Start**, **End Path**, and **Finish**, associated with their color.
11. Only a player’s own markers may use their **Start**, **End Path**, and **Finish**.
12. A player **wins** by placing **all of their markers** on their **Finish**.

---

### Turn Structure & Dice

13. The game is played using **one or two standard six-sided dice**, fairness assumed.
14. Turn order is determined by **rolling the dice** before the game begins.
15. The player with the **highest roll** goes first.
16. Ties for highest roll are resolved by **rerolling among tied players** until the tie is broken.
17. On their turn, a player **rolls the dice** and performs the resulting move(s).
18. If a player has **no valid moves**, their turn ends immediately.
19. The game ends immediately when a player wins; **ties are not possible**.

---

### Board & Setup

20. The **Path** is a circular track shared by all players.
21. At the start of the game, all markers are placed on their respective **Start**.
22. Markers **cannot move while on the Start**.
23. To remove a marker from the Start, a player must **roll a 6**.
24. When a marker leaves the Start, it is placed on the tile immediately following the player’s Start on the Path, called the **entry tile**.
25. Entry tiles and End Paths are **equally spaced** around the Path.

---

### Movement Rules

26. Markers move **clockwise** along the Path.
27. Movement distance is **equal to the dice roll**.
28. A player may choose **any marker** to move, provided the move is valid.
29. Markers on the Path may pass over other markers without interaction.
30. When a player rolls a number **other than 6**, they must move a marker already on the Path.
31. If all markers are on the Start and the player rolls a 6, they must remove a marker from the Start.
32. If all markers are on the Start and the player does not roll a 6, their turn ends.
33. Movement rules are **consistent across the Path**; all Path tiles behave identically.

---

### Protection & Capture

34. Two or more markers of the **same player** may occupy the same tile.
35. If a marker lands on a tile occupied by one or more **opponent markers**, **all opponent markers on that tile are captured** and returned to their respective Starts.
36. Markers on their own **entry tile** are **Protected**.
37. Protected markers **cannot be captured**.
38. Protected markers may move normally; once they leave the entry tile, they lose protection.

---

### End Path & Finish

39. A marker may only enter its **End Path** from the tile immediately preceding it.
40. A marker may only enter its **Finish** from the last tile of its End Path.
41. The End Path and Finish are **exclusive** to each player.
42. Markers **cannot be captured** while on the End Path or Finish.
43. A marker may only move into the Finish if the **dice roll is exact**.
44. Markers on the End Path may not pass over other markers. If any tile of the movement is blocked, the move is invalid.
45. The End Path consists of **4 or 5 tiles**, chosen uniformly for all players.
46. The Finish consists of **a single tile**.

---

### Two-Dice Rules

47. When using two dice, **each die is resolved separately**.
48. The player may **choose the order** in which dice are resolved.
49. If only one die can be legally played, the player must play it.
50. If neither die can be legally played, the player’s turn ends.
51. The player may apply **both dice to a single marker**, provided the total movement is valid.

---

### Board Geometry

52. The Path contains **(End Path size × 2 + 3) × 4 tiles**.
53. The board may optionally include **four extra Path tiles at the corners**, used only to ensure orthogonal connectivity; these tiles follow standard Path rules.