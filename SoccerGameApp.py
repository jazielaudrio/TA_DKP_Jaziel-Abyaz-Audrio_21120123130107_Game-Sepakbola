import customtkinter as ctk
from GameModes import GameMode

class SoccerGameApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Soccer Game")
        self.geometry("600x400")
        
        self.history = []
        self.playerName = ""
        
        self.createWidgets()
    
    def createWidgets(self):
        self.frame = ctk.CTkFrame(self, fg_color="#2B2B2B", border_color="#2FA572", border_width=2)
        self.frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        self.titleLabel = ctk.CTkLabel(master=self.frame, text="Soccer Game", font=("Helvetica", 24))
        self.titleLabel.pack(pady=20)
        
        self.initialLabel = ctk.CTkLabel(master=self.frame, text="Press Enter to Start Game", font=("Helvetica", 16))
        self.initialLabel.pack(pady=20)
        
        self.bind('<Return>', self.startGameEntry)

    def startGameEntry(self, event=None):
        self.clearFrame(self.frame)
        
        self.label = ctk.CTkLabel(master=self.frame, text="Masukkan Nama Anda:", font=("Helvetica", 16))
        self.label.pack(pady=10)
        
        self.entry = ctk.CTkEntry(master=self.frame, placeholder_text="Nama")
        self.entry.pack(pady=10)
        
        self.submitBtn = ctk.CTkButton(master=self.frame, text="Submit", command=self.submitName)
        self.submitBtn.pack(pady=20)
    
    def submitName(self):
        self.playerName = self.entry.get()
        if self.playerName:
            self.resultLabel = ctk.CTkLabel(master=self.frame, text=f"Selamat Datang, {self.playerName}!", font=("Helvetica", 16))
            self.resultLabel.pack(pady=10)
            self.showMenu()
        else:
            self.resultLabel = ctk.CTkLabel(master=self.frame, text="Nama tidak boleh kosong!", font=("Helvetica", 16))
            self.resultLabel.pack(pady=10)
    
    def showMenu(self):
        self.clearFrame(self.frame)
        
        self.menuLabel = ctk.CTkLabel(master=self.frame, text="Pilih Mode:", font=("Helvetica", 16))
        self.menuLabel.pack(pady=10)
        
        self.shooterBtn = ctk.CTkButton(master=self.frame, text="Shooter", command=self.shooterMode)
        self.shooterBtn.pack(pady=10)
        
        self.keeperBtn = ctk.CTkButton(master=self.frame, text="Keeper", command=self.keeperMode)
        self.keeperBtn.pack(pady=10)
        
        self.historyBtn = ctk.CTkButton(master=self.frame, text="Tampilkan History", command=self.showHistory)
        self.historyBtn.pack(pady=10)
    
    def shooterMode(self):
        self.chooseDifficulty("shooter")
    
    def keeperMode(self):
        self.chooseDifficulty("keeper")
    
    def chooseDifficulty(self, mode):
        self.clearFrame(self.frame)
        
        self.difficultyLabel = ctk.CTkLabel(master=self.frame, text="Pilih Tingkat Kesulitan:", font=("Helvetica", 16))
        self.difficultyLabel.pack(pady=10)
        
        self.easyBtn = ctk.CTkButton(master=self.frame, text="Mudah", command=lambda: self.startGame(mode, "easy"))
        self.easyBtn.pack(pady=10)
        
        self.mediumBtn = ctk.CTkButton(master=self.frame, text="Sedang", command=lambda: self.startGame(mode, "medium"))
        self.mediumBtn.pack(pady=10)
        
        self.hardBtn = ctk.CTkButton(master=self.frame, text="Sulit", command=lambda: self.startGame(mode, "hard"))
        self.hardBtn.pack(pady=10)
    
    def startGame(self, mode, difficulty):
        self.clearFrame(self.frame)
        self.gameMode = GameMode(self, mode, self.playerName, difficulty)
        self.gameMode.startGame()
    
    def showHistory(self):
        self.clearFrame(self.frame)
        historyText = "\n".join(self.history) if self.history else "Belum ada history."
        self.historyLabel = ctk.CTkLabel(master=self.frame, text=historyText, font=("Helvetica", 16))
        self.historyLabel.pack(pady=10)
        self.backBtn = ctk.CTkButton(master=self.frame, text="Kembali", command=self.showMenu)
        self.backBtn.pack(pady=20)
    
    def clearFrame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
    
    def addToHistory(self, result):
        self.history.append(result)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("green")
    
    app = SoccerGameApp()
    app.mainloop()
