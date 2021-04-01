n = int(input())
grid = []
for i in range(n):
    grid.append(input().split())
    

def cure(i,j,k):
    if i<0 or j<0 or i>n-1 or j>n-1 or grid[i][j] == '0':
        return
    
    if i>0 and int(grid[i-1][j]) <= int(k):  #top
        cure(i-1,j,k)
        grid[i-1][j] = '0'
        
    if i>0 and j<n-1 and int(grid[i-1][j+1]) <= int(k):   #top-right
        cure(i-1,j+1,k)
        grid[i-1][j+1] = '0'
        
    if j<n-1 and int(grid[i][j+1]) <= int(k):    #right
        cure(i,j+1,k)
        grid[i][j+1] = '0'
        
    if i<n-1 and j<n-1 and int(grid[i+1][j+1]) <= int(k):   #bottom-right
        cure(i+1,j+1,k)
        grid[i+1][j+1] = '0'
        
    if i<n-1 and int(grid[i+1][j]) <= int(k):    #bottom
        grid[i+1][j] = '0'
        cure(i+1,j,k)
        
    if i<n-1 and j>0 and int(grid[i+1][j-1]) <= int(k):     #bottom-left
        grid[i+1][j-1] = '0'
        cure(i+1,j-1,k)
        
    if j>0 and int(grid[i][j-1]) <= int(k):   #left
        grid[i][j-1] = '0'
        cure(i,j-1,k)
        
    if i>0 and j>0 and int(grid[i-1][j-1]) <= int(k):    #top-left
        cure(i-1,j-1,k)
        grid[i-1][j-1] = '0'
        
       
            
antidote = [0,0,0,0]

for k in range(5,1,-1):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == str(k):
                antidote[int(k)-2] += 1
                k = str(k)
                cure(i,j,k)
                grid[i][j] = '0'
                
                
for i in antidote:
    print(i, end=" ")
