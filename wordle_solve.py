#Wordle solver
import pygame

class wordle_grid:
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
        self.matrix = []
        for i in range(grid_dimensions[0]):
            self.matrix.append([])
            for j in range(grid_dimensions[1]):
                self.matrix[i].append((None, False, False))

        self.correct_word = []
        for letter in word:
            self.correct_word.append(letter)
        
        self.guesses = 0

    #Enter a guess for the wordle
    #@param self
    #@param guess: the guess to enter
    #@return: True if the guess is "correct",False if it is incorrect
    def enter_guess(self, guess):
        #Enter the guess into the matrix
        #If the word is in the word list, add it to the matrix

        #If the word is in the word list, add it to the matrix
        guess_str = ""
        for letter in guess:
            guess_str += letter

        if not guess_str in self.WORDS:
            return False, False


        #Check if each letter is in the correct word
        for i in range(len(guess)):
            for j in range(len(guess)):
                if guess[i] == self.correct_word[j]:
                    self.matrix[self.guesses][i] = (guess[i], True, False)
                    if i == j:
                        self.matrix[self.guesses][j] = (guess[i], True, True)
                    break
                else:
                    self.matrix[self.guesses][i] = (guess[i], False, False)

        self.guesses += 1
        #Check if the guess is correct
        if guess == self.correct_word:
            return True, True
        else:
            return True, False



class game_screen():
    #initialize the game screen
    #@param self
    #@param screen: the pygame screen
    #@param width: the width of the screen
    #@param height: the height of the screen
    #@param font: the font to use
    #@param font_size: the size of the font
    #@param font_color: the color of the font
    #@param background_color: the color of the background
    def __init__(self, screen, width, height, font, font_size, font_color, background_color):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.background_color = background_color
        self.screen.fill(self.background_color)
    
    #Draw the game screen
    #@param self
    #@param grid: the grid to draw
    def draw(self, grid, current_guess_letters):
        #Draw the grid as a grid of letters in squares
        #If the letter is in the word, draw it orange
        #If the letter is in the word, and in the correct position, draw it green
        #If the letter is not in the word, draw it grey


        orange = (255, 165, 0)
        green = (0, 255, 0)
        grey = (128, 128, 128)

        #Draw a black bacground
        self.screen.fill(self.background_color)

        #Draw a title "Wordle"
        title_font = pygame.font.Font("freesansbold.ttf", 64)
        title_text = title_font.render("Wordle", True, self.font_color)
        title_text_rect = title_text.get_rect()
        title_text_rect.center = (self.width // 2, 40)
        self.screen.blit(title_text, title_text_rect)

        self.grid_width = 0.80*self.width
        self.grid_height = 0.80*self.height

        #Grid should have a border of 10% of the screen
        self.grid_start = (0.1*self.width, 0.1*self.height)

        #Add current guess to the grid
        for i in range(len(current_guess_letters)):
            grid.matrix[grid.guesses][i] = (current_guess_letters[i], False, False)

        #Draw a bunch of boxes with correct colours
        for i in range(len(grid.matrix)):
            for j in range(len(grid.matrix[i])):
                if grid.matrix[i][j][1]:
                    if grid.matrix[i][j][2]:
                        self.screen.fill(green, rect=[self.grid_start[0]+j*self.grid_width/len(grid.matrix), self.grid_start[1]+i*self.grid_height/len(grid.matrix[i]), self.grid_width/len(grid.matrix), self.grid_height/len(grid.matrix[i])])
                    else:
                        self.screen.fill(orange, rect=[self.grid_start[0]+j*self.grid_width/len(grid.matrix), self.grid_start[1]+i*self.grid_height/len(grid.matrix[i]), self.grid_width/len(grid.matrix), self.grid_height/len(grid.matrix[i])])
                else:
                    self.screen.fill(grey, rect=[self.grid_start[0]+j*self.grid_width/len(grid.matrix), self.grid_start[1]+i*self.grid_height/len(grid.matrix[i]), self.grid_width/len(grid.matrix), self.grid_height/len(grid.matrix[i])])
        
        #Populate the grid with the letters cenetered in the rectangles
        #Use 60 size font 
        font = pygame.font.Font("freesansbold.ttf", 60)
        for i in range(len(grid.matrix)):
            for j in range(len(grid.matrix[i])):
                if grid.matrix[i][j][0] != None:
                    self.screen.blit(font.render(grid.matrix[i][j][0], True, self.font_color), (self.grid_start[0]+j*self.grid_width/len(grid.matrix)+self.grid_width/len(grid.matrix)/2-30, self.grid_start[1]+i*self.grid_height/len(grid.matrix)+self.grid_height/len(grid.matrix)/2-30))
                else:
                    self.screen.blit(font.render("_", True, self.font_color), (self.grid_start[0]+j*self.grid_width/len(grid.matrix)+self.grid_width/len(grid.matrix)/2-30, self.grid_start[1]+i*self.grid_height/len(grid.matrix)+self.grid_height/len(grid.matrix)/2-30))

        
        #Flip the screen
        pygame.display.flip()



if __name__ == "__main__":
    #Initialize the pygame screen
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Wordle")

    #Initialize the font
    font = pygame.font.Font("freesansbold.ttf", 32)

    #Initialize the game screen
    game_screen = game_screen(screen, 800, 800, font, 32, (255, 255, 255), (0, 0, 0))

    #Initialize the grid
    grid = wordle_grid("water", (5,5))

    #Initialize the game loop
    game_over = False

    #Check for events
    guess = []
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                #If the user presses a key, check if it is a letter
                #If it is a letter, add it to the word
                if event.key == pygame.K_BACKSPACE:
                    #Replace the last letter with _
                    guess.pop()
                    for i in range(len(grid.matrix[1])):
                        grid.matrix[grid.guesses][i] = ("_", False, False)
                    game_screen.draw(grid, guess)
                elif event.key == pygame.K_RETURN:
                    print(guess, grid.correct_word)
                    if len(guess) == len(grid.correct_word):
                        print("was here")
                        is_word, correct_guess = grid.enter_guess(guess)
                        if correct_guess:
                            game_over = True
                            break
                        if not is_word:
                            guess = []
                            #Replace the last letter with _]
                            for i in range(len(grid.matrix[1])):
                                grid.matrix[grid.guesses][i] = ("_", False, False)

                            game_screen.draw(grid, guess)
                            #Diesplay message that the guess is not a word
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
                        screen.blit(font.render("Word must be 5 letters", True, (255, 0, 0)), (0, 0))
                        pygame.display.flip()
                        pygame.time.delay(1000)
                        guess = []
                elif event.key == pygame.K_ESCAPE:
                    game_over = True
                #If the key is a letter, add it to the word
                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    if len(guess) == len(grid.correct_word):
                        continue
                    guess.append(chr(event.key))
                    #Draw the game screen
                    game_screen.draw(grid, guess)

                    

            
        #Draw the game screen
        game_screen.draw(grid, guess)



            



        
            




