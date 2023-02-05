import math

RES = WIDTH, HEIGHT = 1600, 900  # Screen Size
# RES = WIDTH, HEIGHT = 1920, 1080
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 0  # Frame Rate

PLAYER_POS = 1.5, 5  # mini_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004  # Player speed
PLAYER_ROT_SPEED = 0.002  # Rotation speed
PLAYER_SIZE_SCALE = 60  # Player scale
PLAYER_MAX_HEALTH = 100  # Player Health

MOUSE_SENSITIVITY = 0.0007  # sensitivity
MOUSE_MAX_REL = 40  # maximum relative movement
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

FLOOR_COLOUR = (30, 30, 30)

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2
