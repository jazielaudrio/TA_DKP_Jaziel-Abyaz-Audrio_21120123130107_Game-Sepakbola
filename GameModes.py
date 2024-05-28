import customtkinter as ctk
import random

class GameMode:
    def __init__(self, app, mode, playerName, difficulty):
        self.app = app
        self.mode = mode
        self.playerName = playerName
        self.difficulty = difficulty
        self.trials = 0
        self.playerScore = 0
        self.botScore = 0
        self.trialResults = []
        self.options = ["kiri", "tengah", "kanan"]
    
    def startGame(self):
        self.nextTrial()
    
    def nextTrial(self):
        self.app.clearFrame(self.app.frame)
        self.trials += 1
        if self.trials <= 5:
            self.trialLabel = ctk.CTkLabel(master=self.app.frame, text=f"Percobaan {self.trials}")
            self.trialLabel.pack(pady=10)
            
            self.actionFrame = ctk.CTkFrame(master=self.app.frame)
            self.actionFrame.pack(pady=10)
            
            for option in self.options:
                btn = ctk.CTkButton(master=self.actionFrame, text=f"Tendang {option}" if self.mode == "shooter" else f"Tangkap {option}", 
                                    command=lambda o=option: self.processChoice(o))
                btn.pack(side="left", padx=5)
        else:
            if self.playerScore > self.botScore:
                winner = self.playerName
                winnerScore = self.playerScore
                loserScore = self.botScore
            else:
                winner = "Keeper" if self.mode == "shooter" else "Shooter"
                winnerScore = self.botScore
                loserScore = self.playerScore
            self.endGame(winner, winnerScore, loserScore)
    
    def processChoice(self, playerChoice):
        botChoice = self.getBotChoice()
        result = ""
        
        if self.mode == "shooter":
            result = f"{self.playerName} menendang ke {playerChoice}, Bot Keeper mencoba menangkap ke {botChoice}"
            if playerChoice != botChoice:
                result += "\nGoal!"
                self.playerScore += 1
            else:
                result += "\nTertangkap!"
                self.botScore += 1
        else:
            result = f"{self.playerName} mencoba menangkap ke {playerChoice}, Bot Shooter menendang ke {botChoice}"
            if playerChoice == botChoice:
                result += "\nTertangkap!"
                self.playerScore += 1
            else:
                result += "\nGoal!"
                self.botScore += 1
        
        self.trialResults.append(f"Percobaan {self.trials}: {result}")
        self.showResult(result)
    
    def getBotChoice(self):
        if self.difficulty == "easy":
            # Bot has a lower chance of guessing correctly
            if random.random() < 0.3:
                return random.choice(self.options)
            else:
                return self.options[(self.options.index(random.choice(self.options)) + 1) % 3]
        elif self.difficulty == "medium":
            # Bot has a medium chance of guessing correctly
            if random.random() < 0.5:
                return random.choice(self.options)
            else:
                return self.options[(self.options.index(random.choice(self.options)) + 1) % 3]
        else:
            # Bot has a higher chance of guessing correctly
            if random.random() < 0.7:
                return random.choice(self.options)
            else:
                return self.options[(self.options.index(random.choice(self.options)) + 1) % 3]
    
    def showResult(self, result):
        self.app.clearFrame(self.app.frame)
        
        resultLabel = ctk.CTkLabel(master=self.app.frame, text=result)
        resultLabel.pack(pady=20)
        
        nextBtn = ctk.CTkButton(master=self.app.frame, text="Next", command=self.nextTrial)
        nextBtn.pack(pady=20)
    
    def endGame(self, winner, winnerScore, loserScore):
        self.app.clearFrame(self.app.frame)
        endLabel = ctk.CTkLabel(master=self.app.frame, text="PERMAINAN SELESAI", font=("Helvetica", 20, "bold"))
        endLabel.pack(pady=20)

        resultLabel = ctk.CTkLabel(master=self.app.frame, text=f"{winner} MENANG\nSKOR\n{winnerScore}-{loserScore}", font=("Helvetica", 16))
        resultLabel.pack(pady=20)

        backBtn = ctk.CTkButton(master=self.app.frame, text="Kembali", command=self.app.showMenu)
        backBtn.pack(pady=20)

        # Add to history
        gameResult = f"PERMAINAN SELESAI\n\n{winner} MENANG\nSKOR\n{winnerScore}-{loserScore}"
        self.app.addToHistory(gameResult)
