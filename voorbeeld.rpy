d "do you like horror games?"
menu:
      "Yes.":
              d "Nice I like them too."
              d "Are traps gay?"
              menu:
                     "Obviously.":
                             a "Hahah yeah, I just thought I'd ask a trick question!"
                             return
                     "Not if it's a feminine penis!":
                             a "..........right, well, I've gotta go, uhhh, bye."
                             return

       "No":
              d "Why don't you like horror games?"
              menu:
                    "Because I'm a big bitch":
                            d "I don't like bitches. Bye."
                            return
                    "Because the stories are usually stupid.":
                            d "Yeah I guess you're right."
                            return

#This is an example of a branching decision tree. However, this method (which is used in the video) is only good for questions right before the end of the game. What if you want to continue after the choice? If you simply remove the "return" then you will start reading the next line, which is NOT what we want.

#The solution is to have more jumps and labels. Here is another way to explore the same decision tree I made above.

d "do you like horror games?"
menu:
      "Yes.":
              d "Nice I like them too."
             # (if you create a variable to keep track of answers to questions, this line here is where you would set that. A boolean value likesHorror might be set here, like "$ likesHorror = true". We will use this later)
              jump question2
     "No I don't like horror games":
             ($ likesHorror = false)
             d "why not?"
             menu:
                   "Because I'm a big bitch":
                            d "I don't like bitches. Bye!"
                            return #(this return is here for an IMMEDIATE GAME OVER, if someone makes a terrible decision which ends the game, this is what you'd do.)
                  "Because the stories are usually stupid.":
                            d "Yeah I guess that's true."
                            jump question2





label question2:
d "are traps gay?"
menu:
       "Obviously.":
               d "Hahah yeah, I just thought I'd ask a trick question!"
               $ trapsAreGay = true
               jump continue
       "Not if it's a feminine penis!":
               d "Interesting. I'll remember that...."
               $ trapsAreGay = false
               jump continue
label continue:
#(the game continues on from here, and we can make our variables relevant in the future with "if" statements. example:)
if trapsAreGay == true:
     d "I wonder who actually believes traps aren't gay."
