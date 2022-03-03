"""
Wordle solver
"""
import pygame
import numpy as np

class WordleGrid:
    """
    Draw the wordle
    """
    WORDS = [
        "about", "above", "abuse", "actor", "acute", "admit",
        "adopt", "adult", "after", "again", "agent", "agree",
        "ahead", "alarm", "album", "alert", "alike", "alive",
        "allow", "alone", "along", "alter", "among", "anger",
        "Angle", "angry", "apart", "apple", "apply", "arena",
        "argue", "arise", "array", "aside", "asset", "audio",
        "audit", "avoid", "award", "aware", "badly", "baker",
        "bases", "basic", "basis", "beach", "began", "begin",
        "begun", "being", "below", "bench", "billy", "birth",
        "black", "blame", "blind", "block", "blood", "board",
        "boost", "booth", "bound", "brain", "brand", "bread",
        "break", "breed", "brief", "bring", "broad", "broke",
        "brown", "build", "built", "buyer", "cable", "calif",
        "carry", "catch", "cause", "chain", "chair", "chart",
        "chase", "cheap", "check", "chest", "chief", "child",
        "china", "chose", "civil", "claim", "class", "clean",
        "clear", "click", "clock", "close", "coach", "coast",
        "could", "count", "court", "cover", "craft", "crash",
        "cream", "crime", "cross", "crowd", "crown", "curve",
        "cycle", "daily", "dance", "dated", "dealt", "death",
        "debut", "delay", "depth", "doing", "doubt", "dozen",
        "draft", "drama", "drawn", "dream", "dress", "drill",
        "drink", "drive", "drove", "dying", "eager", "early",
        "earth", "eight", "elite", "empty", "enemy", "enjoy",
        "enter", "entry", "equal", "error", "event", "every",
        "exact", "exist", "extra", "faith", "false", "fault",
        "fiber", "field", "fifth", "fifty", "fight", "final",
        "first", "fixed", "flash", "fleet", "floor", "fluid",
        "focus", "force", "forth", "forty", "forum", "found",
        "frame", "frank", "fraud", "fresh", "front", "fruit",
        "fully", "funny", "giant", "given", "glass", "globe",
        "going", "grace", "grade", "grand", "grant", "grass",
        "great", "green", "gross", "group", "grown", "guard",
        "guess", "guest", "guide", "happy", "harry", "heart",
        "heavy", "hence", "henry", "horse", "hotel", "house",
        "human", "ideal", "image", "index", "inner", "input",
        "issue", "japan", "jimmy", "joint", "jones", "judge",
        "known", "label", "large", "laser", "later", "laugh",
        "layer", "learn", "lease", "least", "leave", "legal",
        "level", "lewis", "light", "limit", "links", "lives",
        "local", "logic", "loose", "lower", "lucky", "lunch",
        "lying", "magic", "major", "maker", "march", "maria",
        "match", "maybe", "mayor", "meant", "media", "metal",
        "might", "minor", "minus", "mixed", "model", "money",
        "month", "moral", "motor", "mount", "mouse", "mouth",
        "movie", "music", "needs", "never", "newly", "night",
        "noise", "north", "noted", "novel", "nurse", "occur",
        "ocean", "offer", "often", "order", "other", "ought",
        "paint", "panel", "paper", "party", "peace", "peter",
        "phase", "phone", "photo", "piece", "pilot", "pitch",
        "place", "plain", "plane", "plant", "plate", "point",
        "pound", "power", "press", "price", "pride", "prime",
        "print", "prior", "prize", "proof", "proud", "prove",
        "queen", "quick", "quiet", "quite", "radio", "raise",
        "range", "rapid", "ratio", "reach", "ready", "refer",
        "right", "rival", "river", "robin", "roger", "roman",
        "rough", "round", "route", "royal", "rural", "scale",
        "scene", "scope", "score", "sense", "serve", "seven",
        "shall", "shape", "share", "sharp", "sheet", "shelf",
        "shell", "shift", "shirt", "shock", "shoot", "short",
        "shown", "sight", "since", "sixth", "sixty", "sized",
        "skill", "sleep", "slide", "small", "smart", "smile",
        "smith", "smoke", "solid", "solve", "sorry", "sound",
        "south", "space", "spare", "speak", "speed", "spend",
        "spent", "split", "spoke", "sport", "staff", "stage",
        "stake", "stand", "start", "state", "steam", "steel",
        "stick", "still", "stock", "stone", "stood", "store",
        "storm", "story", "strip", "stuck", "study", "stuff",
        "style", "sugar", "suite", "super", "sweet", "table",
        "taken", "taste", "taxes", "teach", "teeth", "terry",
        "texas", "thank", "theft", "their", "theme", "there",
        "these", "thick", "thing", "think", "third", "those",
        "three", "threw", "throw", "tight", "times", "tired",
        "title", "today", "topic", "total", "touch", "tough",
        "tower", "track", "trade", "train", "treat", "trend",
        "trial", "tried", "tries", "truck", "truly", "trust",
        "truth", "twice", "under", "undue", "union", "unity",
        "until", "upper", "upset", "urban", "usage", "usual",
        "valid", "value", "video", "virus", "visit", "vital",
        "voice", "waste", "watch", "water", "wheel", "where",
        "which", "while", "white", "whole", "whose", "woman",
        "women", "world", "worry", "worse", "worst", "worth",
        "would", "wound", "write", "wrong", "wrote", "yield",
        "young", "youth"
    ]


    #initialize the worlde
    #@param self
    #@param word: the correct word we are trying to solve
    #@param grid_dimensions: the dimensions of the wordle grid
    def __init__(self, word:str, grid_dimensions: tuple):
        #Create a matrix of values to put in the grid
        #Each value contains a "lette",a boolean to indicate if the letter is in the word
        #And a boolean to indicate if the letter is in the word and in the correct position
        self.matrix = np.zeros((grid_dimensions[0], grid_dimensions[1]), dtype=tuple)
        for i in range(grid_dimensions[0]):
            for j in range(grid_dimensions[1]):
                self.matrix[i][j] = (None, False, False)

        self.correct_word = np.zeros(len(word), dtype=str)
        for i, letter in enumerate(word):
            self.correct_word[i] = letter

        self.guesses = 0


    def enter_guess(self, guess):
        """
        Enter a guess for the wordle
        @param: self
        @param: guess: the guess to enter
        @return: True if the guess is "correct",False if it is incorrect
        """

        #Enter the guess into the matrix
        #If the word is in the word list, add it to the matrix

        #If the word is in the word list, add it to the matrix
        guess_str = ""
        for letter in guess:
            guess_str.join(letter)

        if guess_str not in self.WORDS:
            return False, False

        #Check if each letter is in the correct word
        for i, letter in enumerate(guess):
            self.matrix[self.guesses][i] = (letter, False, False)
            for j, correct_letter in enumerate(self.correct_word):
                if letter == correct_letter:
                    self.matrix[self.guesses][i] = (letter, True, False)
                    if i == j:
                        self.matrix[self.guesses][j] = (letter, True, True)           

        self.guesses += 1
        #Check if the guess is correct
        if guess == self.correct_word:
            return True, True
        return True, False



class GameScreen():
    """
    The game screen
    """
    def __init__(self, screen, font):
        """
        Initialize the game screen
        @param self
        @param screen: the pygame screen
        @param width: the width of the screen
        @param height: the height of the screen
        @param font: the font to use
        """
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.font = font
        self.background_color = "black"
        self.screen.fill(self.background_color)
        self.grid_width = width * 0.8
        self.grid_height = height * 0.8
        #Grid should have a border of 10% of the screen
        self.grid_start = (0.1*self.width, 0.1*self.height)

    def draw(self, grid, current_guess_letters):
        """
        Draw the game screen
        Draw the grid as a grid of letters in squares
        If the letter is in the word, draw it orange
        If the letter is in the word, and in the correct position, draw it green
        If the letter is not in the word, draw it grey
        @param self
        @param grid: the grid to draw
        """

        orange = (255, 165, 0)
        green = (0, 255, 0)
        grey = (128, 128, 128)

        #Draw a black bacground
        self.screen.fill(self.background_color)

        #Draw a title "Wordle"
        title_font = pygame.font.Font("freesansbold.ttf", 64)
        title_text = title_font.render("Wordle", True, "white")
        title_text_rect = title_text.get_rect()
        title_text_rect.center = (self.width // 2, 40)
        self.screen.blit(title_text, title_text_rect)

        #Add current guess to the grid
        for i, letter in enumerate(current_guess_letters):
            grid.matrix[grid.guesses][i] = (letter, False, False)

        #Draw a bunch of boxes with correct colours
        for i, row in enumerate(grid.matrix):
            for j, cell in enumerate(row):
                if cell[1]:
                    if cell[2]:
                        self.screen.fill(green, \
                            rect=[self.grid_start[0]+j*self.grid_width/len(grid.matrix), \
                                self.grid_start[1]+i*self.grid_height/len(grid.matrix[i]), \
                                self.grid_width/len(grid.matrix), \
                                self.grid_height/len(grid.matrix[i])])
                    else:
                        self.screen.fill(orange, \
                            rect=[self.grid_start[0]+j*self.grid_width/len(grid.matrix), \
                                self.grid_start[1]+i*self.grid_height/len(grid.matrix[i]), \
                                self.grid_width/len(grid.matrix), \
                                self.grid_height/len(grid.matrix[i])])
                else:
                    self.screen.fill(grey, \
                        rect=[self.grid_start[0]+j*self.grid_width/len(grid.matrix), \
                            self.grid_start[1]+i*self.grid_height/len(grid.matrix[i]), \
                            self.grid_width/len(grid.matrix), \
                            self.grid_height/len(grid.matrix[i])])

        #Populate the grid with the letters cenetered in the rectangles
        #Use 60 size font
        font = pygame.font.Font("freesansbold.ttf", 60)
        for i, row in enumerate(grid.matrix):
            for j, cell in enumerate(grid.matrix[i]):
                if cell[0] is not None:
                    self.screen.blit(
                        font.render(grid.matrix[i][j][0], True, "white"), \
                        (self.grid_start[0]+j*self.grid_width/len(grid.matrix)+\
                            self.grid_width/len(grid.matrix)/2-30, \
                        self.grid_start[1]+i*self.grid_height/len(grid.matrix)+\
                            self.grid_height/len(grid.matrix)/2-30))
                else:
                    self.screen.blit(font.render("_", True, "white"), \
                        (self.grid_start[0]+j*self.grid_width/len(grid.matrix)+\
                            self.grid_width/len(grid.matrix)/2-30, \
                        self.grid_start[1]+i*self.grid_height/len(grid.matrix)+\
                            self.grid_height/len(grid.matrix)/2-30))
        #Flip the screen
        pygame.display.flip()


def handle_guess(screen, guess, grid, game_screen, font):
    """
    Handle the guess when it is entered
    @description: Check if the guess is correct. If it is correct, return True.
    If it is incorrect, clear the screen and redraw the grid, then return False
    @param screen: the pygame screen
    @param guess: the guess to handle
    @param grid: the grid to handle the guess
    @param game_screen: the game screen to draw
    @param font: the font to use
    @return: True if the guess is correct, False otherwise
    """
    print(guess, grid.correct_word)
    if len(guess) == len(grid.correct_word):
        is_word, correct_guess = grid.enter_guess(guess)
        if correct_guess:
            return True
        if not is_word:
            guess = []
            #Replace the last letter with
            for i in range(len(grid.matrix[1])):
                grid.matrix[grid.guesses][i] = ("_", False, False)
            game_screen.draw(grid, guess)
            #Display message that the guess is not a word
            screen.blit(font.render("Not a word", True, (255, 0, 0)), (0, 0))
            pygame.display.flip()
            pygame.time.delay(1000)
        else:
            #Display message that the guess is not correct
            print("Not correct")
            screen.blit(font.render("Not correct", True, (255, 0, 0)), (0, 0))
            pygame.display.flip()
            pygame.time.delay(1000)
            guess = []
    else:
        print("Word must be 5 letters")
        screen.blit(font.render("Word must be 5 letters", \
            True, (255, 0, 0)), (0, 0))
        pygame.display.flip()
        pygame.time.delay(1000)
        guess = []
    return False

def handle_keydown(event, screen, grid, game_screen, guess, font):
    """
    @description:
        - Handle key presses
        - If the key is a letter, add it to the guess
        - If the key is backspace, remove the last letter from the guess
        - If the key is enter, check if the guess is correct
    @param event: the pygame event
    @param screen: the pygame screen
    @param grid: the wordle grid
    @param game_screen: the game screen
    @param guess: the current guess
    @param font: the font to use
    @return: True if the game should end, False if the game should continue
    """
    #If the user presses a key, check if it is a letter
    #If it is a letter, add it to the word
    if event.key == pygame.K_BACKSPACE:
        #Replace the last letter with _
        if len(guess) != 0:
            guess.pop()
        for i in range(len(grid.matrix[1])):
            grid.matrix[grid.guesses][i] = ("_", False, False)
        game_screen.draw(grid, guess)
    elif event.key == pygame.K_RETURN:
        return handle_guess(screen, guess, grid, game_screen, font)
    elif event.key == pygame.K_ESCAPE:
        return True
    #If the key is a letter, add it to the word
    elif event.key >= pygame.K_a and event.key <= pygame.K_z:
        if len(guess) != len(grid.correct_word):
            guess.append(chr(event.key))
            #Draw the game screen
            game_screen.draw(grid, guess)
    return False


def main():
    """
    @description:
        - Initialize the pygame screen
        - Initialize the grid
        - Initialize the game screen
        - Initialize the font
        - Initialize the guess
        - Initialize the game loop
        - Handle the key presses
        - If the game loop is over, end the game
    """
    #Initialize the pygame screen
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Wordle")

    #Initialize the font
    font = pygame.font.Font("freesansbold.ttf", 60)

    #Initialize the game screen
    game_screen = GameScreen(screen, font)

    #Initialize the grid
    grid = WordleGrid("water", (5,5))

    #Initialize the game loop
    game_over = False

    #Check for events
    guess = []
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                game_over = handle_keydown(event, screen, grid, game_screen, guess, font)
        #Draw the game screen
        game_screen.draw(grid, guess)

if __name__ == "__main__":
    main()
