import sys
import time

class pstate:
	board = []
	f_score = 0
	g_score = 0
	came_from = None

	def __init__(self, b):
		self.board = b

	def print_state(self):
		print self.board

	def heurstic(self, goal): #number * number of moves requred
		h = 0
		for i in range(len(goal)):
			if goal[i]!=self.board[i]:
				h = h + 1
		return h
	def isLegal(self,dir):
		#direction of blank tile move
		#0 = up, 1 = right, 2 = down, 3 = left
		blank = -1
		for i in range(0,len(self.board)):
			if self.board[i]==0:
				blank = i
				break
		if dir == 0:
			if blank<3:
				return False
			else:
				return True
		elif dir == 2:
			if blank>5:
				return False
			else:
				return True
		elif dir == 1:
			if (blank+1)%3==0:
				return False
			else:
				return True
		elif dir == 3:
			if (blank%3)==0:
				return False
			else:
				return True

	def switch(self, dir):
		if(self.isLegal(dir)):
			#temp is the tile being moved. Is the REAL cost
			blank = -1
			for i in range(0,len(self.board)):
				if self.board[i]==0:
					blank = i
					break
			new_board = self.board[:]
			if dir==0:
				temp = new_board[blank-3]
				new_board[blank-3]=new_board[blank]
				new_board[blank]=temp
			if dir==1:
				temp = new_board[blank+1]
				new_board[blank+1]=new_board[blank]
				new_board[blank]=temp
			if dir==2:
				temp = new_board[blank+3]
				new_board[blank+3]=new_board[blank]
				new_board[blank]=temp
			if dir==3:
				temp = new_board[blank-1]
				new_board[blank-1]=new_board[blank]
				new_board[blank]=temp
			return new_board, temp
		else:
			return None, None

def backtrack(current):
	trace = []

	print "Solution: The shortest path cost = " + str(current.g_score)
	print ""
	print "Sequence:"
	while 1:
		if current.came_from == None:
			trace.append(current.board)
			break
		else:
			trace.append(current.board)
			current = current.came_from
	trace.reverse()
	
	for b in trace:
		toString(b)
		print "---------"

		

def toString(l):
	print l[:3]
	print l[3:6]
	print l[6:9]


def A_star(start, goal):
	closed = []
	opened = []

	t = pstate(start)
	t.g_score=0
	t.f_score=t.g_score+t.heurstic(goal)

	opened.append(t)
	j = 0
	while opened:
		#time.sleep(1)
		min_f_score = 1000000
		current_index = -1

		for i in range(len(opened)):
			#print "Opened[" + str(i) + "] : f_score=" + str(opened[i].f_score)
			#toString(opened[i].board)

			if opened[i].f_score < min_f_score:
				current_index = i
				current = opened[i]
				min_f_score = opened[i].f_score
		#print "min f_score at " + str(current_index) + " is " + str(min_f_score)

		if current.board == goal:
			return backtrack(current)

		closed.append(current.board)
		#print "Closed: " + str(len(closed))
		opened.pop(current_index)
		#print "Opened: " + str(len(opened))
		#print "Current Heurstic: " + str(current.heurstic(goal))
		#print toString(current.board)
		if current.heurstic(goal)==1:
			time.sleep(3)


		neighbors = []
		cost = []
		for i in range(0,4):
			n, c = current.switch(i)
			if n != None:
				neighbors.append(n)
				cost.append(c)


		for k in range(len(neighbors)):
			if neighbors[k] in closed:
				continue
			tentative_g_score = current.g_score + cost[k] # Real Cost

			opened_index = -1
			for i in range(len(opened)):
				if opened[i].board==neighbors[k]:
					opened_index=i

			if (opened_index==-1) or (opened[opened_index].g_score<tentative_g_score):
				temp = pstate(neighbors[k])
				temp.came_from = current
				temp.g_score = tentative_g_score
				temp.f_score = temp.g_score + temp.heurstic(goal)
				if opened_index == -1:
					opened.append(temp)
	return False








		



if __name__=="__main__":
	goal = [1,2,3,8,0,4,7,6,5]

	f = open(sys.argv[1], 'r')
	i=0
	b =[]
	for line in f:
		elements = line.strip().split()
		for e in elements:
			b.append(int(e))
	temp = pstate(b)

	A_star(b, goal)







