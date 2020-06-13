# Implementation of binary search trees using lists
import matplotlib.pyplot as plt
import numpy as np
import math 
def insert(T,newItem): # Insert newItem to BST T
    if T == None:  # T is empty
        T = [newItem,None,None]
    else:
        if newItem< T[0]:
            T[1] = insert(T[1],newItem) # Insert newItem in left subtree
        else:
            T[2] = insert(T[2],newItem) # Insert newItem in right subtree
    return T

def inOrder(T):
    if T!=None:
        inOrder(T[1])
        print(T[0],end=' ')
        inOrder(T[2])
    
def size(T):
    if T is None: #check for is the binary tree is empty 
        return 0
    if T[1] is None and T[2] is None: #base case where there is no deeper list to go into 
        return 1
    
    if T[1] is not None and T[2] is None: #recursive call for when there is a left list to go to, but no right list
        return size(T[1]) +1 # the +1 ensures that the data stored in the current node is counted 
    
    if T[1] is None and T[2] is not None: #recursive call for when there is a right list to go to, but no left list 
        return size(T[2]) +1
    
    if T[1] is not None and T[2] is not None:  #recursive call for when there is a right list and a right list to go to
        return size(T[1]) + size(T[2]) + 1

    
def minimum(T):
    if T is None: 
        return math.inf
    iter = T
    while(iter[1] is not None): 
        iter = iter[1]
    return iter[0]
    
def maximum(T):
    if T is None: 
        return math.inf
    iter = T
    while(iter[2] is not None): 
        iter = iter[2]
    return iter[0]
    
def height(T):
    if T is None: #check for if the list is empty
        return -1
    if T is None:
        return 0
    if T[1] is None and T[2] is None: #base case where there is no deeper list to go into 
        return 0
    leftHeight = height(T[1]) +1 #recursive call for the left tree
    rightHeight = height(T[2]) +1 #recursive call for the right tree
    
    return max(leftHeight, rightHeight) #returns only the higher value, that way the largest depth(the height) is returned

def inTree(T,i):
    if T is None: #if there's nothing in the tree then the item can't be in the tree
        return False
    if T[0] == i: #the item does exist in the tree
        return True 
    leftTree = inTree(T[1], i) #recursive call for the left half of the tree
    rightTree = inTree(T[2], i) #recursive call for the right half of the tree
    if leftTree or rightTree: 
        return True
    return False

def printByLevel(T):
    if T is not None:
        print(T[0])
        if T[1] is not None and T[2] is not None:
            printTheLevel(T[1], T[2])
            
        if T[1] is not None and T[2] is None: 
            printTheLevel(T[1], None)
            
        if T[1] is None and T[2] is not None:
            printTheLevel(None, T[2])
            
        if T[1] is None and T[2] is None:
            printTheLevel(None, None)
        

def printTheLevel(left = None, right = None):
    if left is not None:
        print(left[0], end = ' ')
    if right is not None:
        print(right[0])
        
    if left is not None and right is not None:
        
        if left[1] is not None and left[2] is not None: 
            printTheLevel(left[1])
            printTheLevel(left[2])
            
        if left[1] is not None and left[2] is None:
            printTheLevel(left[1])
            
        if left[1] is None and left[2] is not None:
            printTheLevel(left[2])
     
    if right is not None:
        if right[1] is not None and right[2] is None:
            printTheLevel(right[1])
        if right[1] is None and right[2] is not None:
            printTheLevel(None, right[2])
        if right[1] is not None and right[2] is not None:
            printTheLevel(right[1], right[2])


def tree2List(T): 
    
    if T is not None:
        if T[1] is None and T[2] is None:
            return [T[0]]
        
        if T[1] is not None and T[2] is None: 
            return tree2List(T[1]) + [T[0]]
        
        if T[1] is None and T[2] is not None:
            return [T[0]] + tree2List(T[2])
        
        if T[1] is not None and T[2] is not None:
            return tree2List(T[1])+ [T[0]]+ tree2List(T[2])
    
def leaves(T):
    if T is not None:
        if T[1] is None and T[2] is None: #base case where you reach a leaf
            if T[0] is not None:
                return [T[0]]
        if T[1] is not None and T[2] is not None:
            return leaves(T[1]) +  leaves(T[2]) #recursive call for the left tree
        if T[1] is None and T[2] is not None: 
            return leaves(T[2])
        if T[1] is not None and T[2] is None:
            return leaves(T[1])
    return -math.inf
            
def itemsAtDepthD(T,d):
    if T is not None:
        if d == 0:
            return [T[0]]
        if d > 0:
            if T[1] is not None and T[2] is not None:
                return itemsAtDepthD(T[1], d-1) + itemsAtDepthD(T[2], d-1)
            if T[1] is None and T[2] is not None: 
                return itemsAtDepthD(T[2], d-1)
            if T[1] is not None and T[2] is None:
                return itemsAtDepthD(T[1], d-1) 
            if T[1] is None and T[2] is None:
                return []
    return -1

    
def depthOfK(T,k):
    if T is not None:
        if T[0] == k:
            return 0
        
        if k < T[0]:
            if T[1] is not None:
                leftCall = depthOfK(T[1], k)
                if leftCall == -1:
                    return -1
                else:
                    return leftCall+1
                
        if k > T[0]:
            if T[2] is not None:
                rightCall = depthOfK(T[2],k)
                if rightCall == -1:
                    return -1
                else:
                    return rightCall+1
        if T[1] is None and T[2] is None:
            return -1
    else: 
        return -math.inf
def draw(T):
    print('TBD')
if __name__ == "__main__":
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1, 20, 13]             
    T = None
    for a in A:
        print('Inserting',a)
        T = insert(T,a)   
        print(T)    
    inOrder(T)
    

    testList = []
    secondTestTree = None 
    for a in testList:
        print('Inserting',a)
        secondTestTree = insert(secondTestTree,a)   
        print(secondTestTree)
        
    testList = [1] 
    thirdTestTree = None
    for a in testList:
        print('Inserting',a)
        thirdTestTree = insert(thirdTestTree,a)   
        print(thirdTestTree)
    
    
    testList = [2, 0] 
    fourthTestTree = None
    for a in testList:
        print('Inserting',a)
        fourthTestTree = insert(fourthTestTree,a)   
        print(fourthTestTree)
    
    testList = [2, 0, 5, 6] 
    fifthTestTree = None
    for a in testList:
        print('Inserting',a)
        fifthTestTree = insert(fifthTestTree,a)   
        print(fifthTestTree)
        
    testList = [2, 0, 5, 4, 6, 7] 
    sixthTestTree = None
    for a in testList:
        print('Inserting',a)
        sixthTestTree = insert(sixthTestTree,a)   
        print(sixthTestTree)
        
    testList = [2, 0, 5, 1, 4, 6,3, 7] 
    seventhTestTree = None
    for a in testList:
        print('Inserting',a)
        seventhTestTree = insert(seventhTestTree,a)   
        print(seventhTestTree)
        
    print('')
    print('')
    print('')
    print('/////////size(T) Tests//////////////////////')
    print(size(T)) #14
    print(size(secondTestTree)) #0
    print(size(thirdTestTree)) #1
    print(size(fourthTestTree)) #1
    print(size(fifthTestTree)) #1
    print(size(sixthTestTree)) #1
    print(size(seventhTestTree)) #1
    
    print('/////////minimum(T) Tests//////////////////////')
    print(minimum(T)) #1
    print(minimum(secondTestTree)) #-inf
    print(minimum(thirdTestTree)) #1
    print(minimum(fourthTestTree)) #0
    print(minimum(fifthTestTree)) #0
    print(minimum(sixthTestTree)) #0
    print(minimum(seventhTestTree)) #0

    print('/////////maximum(T) Tests//////////////////////')
    print(maximum(T)) #20
    print(maximum(secondTestTree)) #inf
    print(maximum(thirdTestTree)) #1
    print(maximum(fourthTestTree)) #2
    print(maximum(fifthTestTree)) #6
    print(maximum(sixthTestTree)) #7
    print(maximum(seventhTestTree)) #7
    
    print('/////////height(T) Tests//////////////////////')
    print(height(T)) #4
    print(height(secondTestTree)) #-1
    print(height(thirdTestTree)) #0
    print(height(fourthTestTree)) #1
    print(height(fifthTestTree)) #2
    print(height(sixthTestTree)) #3
    print(height(seventhTestTree)) #3
    
    print('/////////inTree(T) Tests//////////////////////')
    print(inTree(T, 1)) #True
    print(inTree(secondTestTree, 30)) #False
    print(inTree(thirdTestTree, 30)) #False
    print(inTree(fourthTestTree, 2)) #True
    print(inTree(fifthTestTree, 2)) #True
    print(inTree(sixthTestTree, 1000)) #False
    print(inTree(seventhTestTree, 7)) #True
    
    print('/////////printByLevel(T) Tests//////////////////////')
    printByLevel(T)
    print()
    print('//////////////secondTestTree/////////////////')
    printByLevel(secondTestTree)
    print('')
    print('//////////////thirdTestTree/////////////////')
    printByLevel(thirdTestTree)
    print('')
    print('////////////fourthTestTree///////////////////')
    printByLevel(fourthTestTree)
    print('')
    print('////////////fifthTestTree///////////////////')
    printByLevel(fifthTestTree)
    print('')
    print('/////////////sixthTestTree//////////////////')
    printByLevel(sixthTestTree)
    print('')
    print('/////////////seventhTestTree//////////////////')
    printByLevel(seventhTestTree) 
    
    print('/////////tree2List(T) Tests//////////////////////')
    print(tree2List(T))
    print(tree2List(secondTestTree))
    print(tree2List(thirdTestTree))
    print(tree2List(fourthTestTree))
    print(tree2List(fifthTestTree))
    print(tree2List(sixthTestTree))
    print(tree2List(seventhTestTree)) 
    
    print('/////////leaves(T) Tests//////////////////////')
    print(leaves(T))
    print('//////////////secondTestTree/////////////////')
    print(leaves(secondTestTree))
    print('//////////////thirdTestTree/////////////////')
    print(leaves(thirdTestTree))
    print('//////////////fourthTestTree/////////////////')
    print(leaves(fourthTestTree))
    print('//////////////fifthTestTree/////////////////')
    print(leaves(fifthTestTree))
    print('//////////////sixthTestTree/////////////////')
    print(leaves(sixthTestTree))
    print('//////////////seventhTestTree/////////////////')
    print(leaves(seventhTestTree))
    
    print('/////////itemsAtDepthD(T,d) Tests//////////////////////')
    print(itemsAtDepthD(T, 3))
    print('//////////////secondTestTree/////////////////')
    print(itemsAtDepthD(secondTestTree, 0))
    print('//////////////thirdTestTree/////////////////')
    print(itemsAtDepthD(thirdTestTree, 0))
    print('//////////////fourthTestTree/////////////////')
    print(itemsAtDepthD(fourthTestTree, 1))
    print('//////////////fifthTestTree/////////////////')
    print(itemsAtDepthD(fifthTestTree, 1))
    print('//////////////sixthTestTree/////////////////')
    print(itemsAtDepthD(sixthTestTree, 2))
    print('//////////////seventhTestTree/////////////////')
    print(itemsAtDepthD(seventhTestTree, 2))
    print()
    print()
    
    print('/////////depthofK(T,d) Tests//////////////////////')
    print(depthOfK(T, 20))
    print('//////////////secondTestTree/////////////////')
    print(depthOfK(secondTestTree, 0))
    print('//////////////thirdTestTree/////////////////')
    print(depthOfK(thirdTestTree, 1000))
    print('//////////////fourthTestTree/////////////////')
    print(depthOfK(fourthTestTree, 0))
    print('//////////////fifthTestTree/////////////////')
    print(depthOfK(fifthTestTree, 5))
    print('//////////////sixthTestTree/////////////////')
    print(depthOfK(sixthTestTree, 0))
    print('//////////////seventhTestTree/////////////////')
    print(depthOfK(seventhTestTree, 5))
    