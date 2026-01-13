def makefile(maze,playermoves,time):
    file=maze+"|||"+playermoves+"||||"+time
    return file
def breakfile(file):
    return map(file.split("||||"))
#[workingimage,mazelist,unsolvedimage,solvedimage]