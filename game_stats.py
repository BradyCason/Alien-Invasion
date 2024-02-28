class GameStats():
    """Track statistics for Alien Invasion"""
    
    def __init__(self, settings):
        """Initialize statistics"""
        self.settings = settings
        self.reset_stats()
        
        #start Alien Invasion in an inactive state.
        self.game_active = False
        
        #High score should never be reset
        self.high_score = 0
        
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit -1
        self.score = 0
        self.level = 1
