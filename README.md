# Tile Map Game Framework

This project is a framework for creating a spite-based tilemap adventure game. All code was written in Python 2.7 using the Pygame library.

## Main Classes
### GameController
Provides an interface for managing which map in the world is currently active and for moving the player to the appropriate map zones

### Tile
Models a single square tile on the game map background. Tiles are the base layer and can either be passable or impassable

### ExitTile
A tile which causes the player to transition to a different map in the world

### GameMap
Models the game map as a 2D collection of tiles

### Player
Stores player image, position, and equipment information
