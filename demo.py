import pygame
import random
import sys
import time

pygame.init()

# --- Screen setup ---
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplication Game")

# --- Fonts and Colors ---
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 32)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# --- Clock setup ---
clock = pygame.time.Clock()
TIMER_LIMIT = 60

def draw_center_text(text, font, color, y_offset=0):
    rendered = font.render(text, True, color)
    screen.blit(rendered, (WIDTH//2 - rendered.get_width()//2, HEIGHT//2 - rendered.get_height()//2 + y_offset))

def play_game():
    # Generate new question
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    correct_answer = str(num1 * num2)
    user_input = ""
    tries = 0
    message = ""
    message_color = WHITE
    start_time = time.time()
    game_over = False

    while True:
        screen.fill(BLACK)
        elapsed_time = int(time.time() - start_time)
        remaining_time = max(0, TIMER_LIMIT - elapsed_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_input == correct_answer:
                        message = "🎉 Correct!"
                        message_color = GREEN
                        game_over = True
                    else:
                        tries += 1
                        if tries == 2:
                            message = f"❌ Wrong! Answer: {correct_answer}"
                            message_color = RED
                            game_over = True
                        else:
                            message = "❌ Try Again"
                            message_color = RED
                        user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.unicode.isdigit():
                    user_input += event.unicode

        if not game_over and remaining_time == 0:
            message = f"⏰ Time's up! Answer: {correct_answer}"
            message_color = RED
            game_over = True

        # Display question, input, timer, and message
        question_text = font.render(f"What is {num1} × {num2}?", True, WHITE)
        screen.blit(question_text, (WIDTH // 2 - question_text.get_width() // 2, 50))

        input_text = font.render(user_input, True, WHITE)
        screen.blit(input_text, (WIDTH // 2 - input_text.get_width() // 2, 150))

        timer_text = small_font.render(f"Time Left: {remaining_time}s", True, WHITE)
        screen.blit(timer_text, (20, 20))

        message_text = small_font.render(message, True, message_color)
        screen.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, 250))

        pygame.display.flip()
        clock.tick(30)

        # Once game ends, show play again prompt
        if game_over:
            pygame.time.delay(1500)  # Wait 1.5 sec before showing prompt
            return ask_play_again()

def ask_play_again():
    while True:
        screen.fill(BLACK)
        draw_center_text("Do you want to play again? (Y/N)", small_font, WHITE)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    return False

# --- Main loop ---
while True:
    play_more = play_game()
    if not play_more:
        break

pygame.quit()
sys.exit()