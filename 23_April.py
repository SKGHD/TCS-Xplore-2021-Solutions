
class Player:
    def __init__(self,playerName,playerCountry,playerAge,noOfMatches,noOfRuns,noOfWickets):
        self.playerName = playerName
        self.playerCountry = playerCountry
        self.playerAge = playerAge
        self.noOfMatches = noOfMatches
        self.noOfRuns = noOfRuns
        self.noOfWickets = noOfWickets


class Team:
   
    def getMinRuns(self,playerList):
        self.playerList = playerList
        minRuns = self.playerList[0].noOfRuns
        minRunsPlayer = self.playerList[0]
        for player in self.playerList:
            
            if player.noOfRuns<minRuns:
                minRuns = player.noOfRuns
                minRunsPlayer = player
        return player        
        
    def getMaxWickets(self,playerList):
        self.playerList = playerList
        maxWickets = 0
        for player in self.playerList:
            
            if player.noOfWickets>maxWickets:
                maxWickets = player.noOfWickets
                maxWicketsPlayer = player
                
        return player        

if __name__ == '__main__':
    noOfPlayer = int(input("Enter Number of players:"))
    playerList = []
    for i in range(noOfPlayer):
        playerName = input("Enter Player name")
        playerCountry = input("Enter Player country")
        playerAge = input("Enter Player age")
        noOfMatches = int(input("Enter matches"))
        noOfRuns = int(input("Enter Runs"))
        noOfWickets = int(input("Enter Wickets"))
        
        playerList.append(Player(playerName,playerCountry,playerAge,noOfMatches,noOfRuns,noOfWickets))
        
        
    obj = Team()
    minRPlayer = obj.getMinRuns(playerList)
    maxWPlayer = obj.getMaxWickets(playerList)
    
    print(minRPlayer.playerName,minRPlayer.noOfRuns,minRPlayer.playerCountry,sep="\n")
    
    print(maxWPlayer.playerName,maxWPlayer.noOfWickets,maxWPlayer.playerCountry,sep="\n")