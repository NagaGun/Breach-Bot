#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts start of Cybersecurity
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since Facebook Data Breach in 2019")


#Introduces Breach
print("Would you like to learn about the Facebook data breach in 2019?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains Breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organizations response, (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("Hackers exploited a vulnerability in a now-defunct Facebook function that allowed users to find each other by phone number, revealing the phone numbers, email addresses, names, and locations of 530 million people.")
  
  elif topic.lower() == "b":
    print("Facebook resolved the issue and paid $5 million for failing to protect user privacy, yet they did not notify any individual whose information got stolen.")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to CIA Triad, (b) my reaction, (c) my advice, (d) none")
  topic = input()

  if topic.lower() == "a":
    print("The breach compromised the confidentiality of 530 million people's information.")

  elif topic.lower() == "b":
    print("I disagree with the organization's response because they should've let the exposed users know that their accounts were breached so that they could’ve taken steps to try and secure their accounts from future breaches.")

  elif topic.lower() == "c":
     print("My advice would be to always keep a two-step verification for any important accounts and to create strong passwords.")

  elif topic.lower() == "d":
     break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

  input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")