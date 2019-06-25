#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()

    print(args.file)


# In[48]:


def formatregex(regex):
    result=''
    allOperators =['|', '?', '+', '*']
    binaryOperators = ['|']
    i=0;
    for c1 in regex:   
        if i + 1 < len(regex):
            c2 = regex[i + 1]

            result += c1

            if (c1!='(' and c2!=')' and c2 not in allOperators and c1 not in binaryOperators):
                result += '.'
        i+=1

    result += regex[len(regex) - 1]

    return result;


# In[49]:





# In[34]:


precedence = {'(': 1, '|': 2, '.': 3,'?':4, '*':4, '+':4, '^':5 }
def getprecedence(c):
    if(c in precedence):
        return precedence[c]
    else:
        return 6


# In[44]:



def infixToPostfix(regex):
    postfix = ''

    stack = []

    formattedRegex = formatregex(regex);

    for c in formattedRegex:
        if c == '(':
            stack.append(c);
        elif c == ')':

            while (stack[len(stack)-1] != '('): 

                postfix += stack.pop()
            stack.pop();
        else:
            while (len(stack) > 0):
                peekedChar = stack.pop()
                stack.append(peekedChar)
                peekedCharPrecedence = getprecedence(peekedChar)
                currentCharPrecedence=getprecedence(c)

                if (peekedCharPrecedence >= currentCharPrecedence):

                    postfix += stack.pop()

                else:
                    break;

            stack.append(c)
    while (len(stack) > 0):
        postfix += stack.pop()
    return postfix;


# In[45]:





# In[144]:


def Union(lst1, lst2): 
    final_list = list(set(lst1) | set(lst2)) 
    return final_list 
class State:
    def __init__(self, name):
        self.epsilon = [] # epsilon-closure
        self.transitions = {} # char : state
        self.name = name
        self.is_end = False
    
class NFA:
    def __init__(self, start, end,):
        self.state_set=[]
        self.alphabet=[]
        self.start = start
        self.end = end # start and end states
        end.is_end = True
        self.transitions=[]
        
    def addstate(self, state, state_set): # add state + recursively add epsilon transitions
        if state in state_set:
            return
        state_set.add(state)
        for eps in state.epsilon:
            self.addstate(eps, state_set)
    
class Handler:
    def __init__(self):
        self.state_count = 0

    def create_state(self):
        self.state_count += 1
        return State('q' + str(self.state_count))
    
    def handle_char(self, t, nfa_stack):
        s0 = self.create_state()
        s1 = self.create_state()
        s0.transitions[t] = s1
        nfa = NFA(s0, s1)
        if t not in nfa.alphabet:
            nfa.alphabet.append(t)
        nfa.state_set.append(s0)
        nfa.state_set.append(s1)
        nfa.transitions.append((s0,t,s1))
        nfa_stack.append(nfa)
    
    def handle_concat(self, t, nfa_stack):
        n2 = nfa_stack.pop()
        n1 = nfa_stack.pop()
        nfa = NFA(n1.start, n2.end)
        nfa.alphabet=Union(n1.alphabet,n2.alphabet)
        
 
       
        n1.end.epsilon.append(n2.start)
        nfa.state_set=Union(n1.state_set,n2.state_set)
        nfa.state_set.remove(n1.end)
        nfa.transitions=Union(n1.transitions,n2.transitions) 
        newtransitions=[]
        for t in nfa.transitions:
            
            if(t[2]==n1.end):
                r=(t[0],t[1],n2.start)
                t=r
             
            newtransitions.append(t)
        nfa.transitions=newtransitions
        nfa_stack.append(nfa)
    
    def handle_alt(self, t, nfa_stack):
        n2 = nfa_stack.pop()
        n1 = nfa_stack.pop()
        s0 = self.create_state()
        s0.epsilon = [n1.start, n2.start]
        s3 = self.create_state()
        n1.end.epsilon.append(s3)       
        n2.end.epsilon.append(s3)
        n1.end.is_end = False
        n2.end.is_end = False
        nfa = NFA(s0, s3)
        nfa.alphabet=Union(n1.alphabet,n2.alphabet)
        if ' ' not in nfa.alphabet:
            nfa.alphabet.append(' ')
        nfa.state_set=Union(n1.state_set,n2.state_set)
        nfa.state_set.extend([s0,s3])        
        nfa.transitions=Union(n1.transitions,n2.transitions)  
        nfa.transitions.extend([(s0,' ',n1.start),(s0,' ',n2.start),(n1.end,' ',s3),(n2.end,' ',s3)])                    
        nfa_stack.append(nfa)
    
    def handle_rep(self, t, nfa_stack):
        n1 = nfa_stack.pop()
        s0 = self.create_state()
        s1 = self.create_state()
        s0.epsilon = [n1.start]
        if t == '*':
            s0.epsilon.append(s1)
        n1.end.epsilon.extend([s1, n1.start])
        n1.end.is_end = False
        nfa = NFA(s0, s1)
        nfa.alphabet=n1.alphabet
        nfa.transitions=n1.transitions      
        nfa.state_set=n1.state_set       
        if ' ' not in nfa.alphabet:
            nfa.alphabet.append(' ')
        if t == '*':
            nfa.transitions.append((s0,' ',s1))
        nfa.transitions.extend([(n1.end,' ',s1),(n1.end,' ',n1.start),(s0,' ',n1.start)])
        nfa.state_set.extend([s0,s1])        
        
        nfa_stack.append(nfa)
        
    def handle_qmark(self, t, nfa_stack):        
        n1 = nfa_stack.pop()
        n1.start.epsilon.append(n1.end)
        if ' ' not in nfa.alphabet:
            n1.alphabet.append(' ')
        n1.transitions.append((n1.start,' ',n1.end))
        nfa_stack.append(n1)

      
regex=' (s|ε t)*'
regex=regex.replace(" ",'')
regex=regex.replace("?",'|ε')
regex=regex.replace('ε',' ')
postfix=infixToPostfix(regex)
print(postfix)
allOperators =['|', '?', '+', '*','.']
handler = Handler()
nfa_stack=[]
for c in postfix:
    
    if c not in allOperators:
        handler.handle_char(c,nfa_stack)

    elif c=='|':
        handler.handle_alt(c,nfa_stack)
    elif c=='.':
        handler.handle_concat(c,nfa_stack)
    else:
        handler.handle_rep(c,nfa_stack)

result = nfa_stack.pop()
resultString='';
for s in result.state_set:
    resultString+=s.name+','
resultString=resultString[:len(resultString)-1]
resultString+='\n'
for a in result.alphabet:
    resultString+=a+','
resultString=resultString[:len(resultString)-1]
resultString+='\n'
resultString+=result.start.name
resultString+='\n'
resultString+=result.end.name
resultString+='\n'
for t in result.transitions:
    resultString+="("+str(t[0].name)+','+str(t[1])+', '+str(t[2].name)+')'+','
resultString=resultString[:len(resultString)-1]

text_file = open("task_2_result.txt", "w")
text_file.write(resultString)
text_file.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




