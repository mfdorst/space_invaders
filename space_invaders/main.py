from time import sleep, time
import pygame as pg

HEIGHT = 600
WIDTH = 800


def main():
    pg.init()

    screen = pg.display.set_mode((WIDTH, HEIGHT))

    player_img = pg.image.load('assets/spaceship.png')
    player_img = pg.transform.scale(player_img, (32, 32))

    PLAYER_START = 32
    PLAYER_END = WIDTH - 64
    player_pos = PLAYER_START

    TARGET_FRAME_DURATION = 1 / 60
    last_frame_time = time()

    while True:
        # Clear the screen
        screen.fill((0, 0, 0))
        # Draw the player
        screen.blit(player_img, (player_pos, HEIGHT - 64))
        # Display the updated frame
        pg.display.update()

        # Update the player position (move from left to right, then reset)
        player_pos += 2
        if player_pos > PLAYER_END:
            player_pos = PLAYER_START

        # Check for QUIT event
        if pg.event.peek(eventtype=pg.QUIT):
            break

        # Calculate the time since the previous frame
        delta_time = time() - last_frame_time
        # Calculate the desired wait time to achieve the desired frame rate
        wait_time = TARGET_FRAME_DURATION - delta_time
        # Wait for the next frame to achieve the target FPS
        if wait_time > 0:
            sleep(wait_time)
        else:
            print(f'FRAME DELAY: {-wait_time}s')
        last_frame_time = time()
