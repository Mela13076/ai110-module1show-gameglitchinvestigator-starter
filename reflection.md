# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

1. When entering a guess (50) and the secret is 52 it told me to go lower, and when i guessed 54 it told me to guess higher
2. when picking easy it says the range is 1-20 and attepsts 6 but this doesn't change the blue card
3. when switching difficulty it should do a new game but attempts chagne unless you hit new game.
4. hard range is 1-50 but normal range is 1-100
5. when a new game starts the red message is still on the bottom and history still shows the old one. (developer only)
--- 


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion you accepted and why.
- Give one example of an AI suggestion you changed or rejected and why.

1. I used Copilot ask and agent mode. 
2. One example of AI suggestion I accepted was moving game logic fully into the logic_utils.py file. It did a great job at picking out any logic, even small and moving it to a different file. 
2. One example of an AI suggestion I rejected was it trying to rewrite a whole function, the change wasn't needed when only one line was the problem. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

1. Once I would fix a bug or Copilot fixed a bug I would run the app again and test if the game fix was implemented or not. 
2. Yes, AI created a text file I can use to test out the logic utils to make sure the functions are working correctly. 
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

1. I perfer ask mode and not agent mode so I can understand the issues and attempt to fix on my own. 
2. I would use only agent mode. 
3. This made me realize that using AI isn't always correct when solving fixes. 
