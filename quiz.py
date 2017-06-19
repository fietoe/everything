print("Kiana's Quiz of Random Stuff I Just Kind of Know for Some Reason")
total_score = 0
q1 = int(input("1. If My Chemical Romance got back together (with bob) and played a show with Panic! At The Disco and Fall Out Boy how many people would be playing on stage (not including tour band)?"))
if q1 == 10:
   total_score = total_score + 1
   print("correct")
else:
   print("incorrect")
print()

print("2. What are the names of all the members in Motionless in White?")
print("a. Spencer Charnas, Justin DeBlieck, Justin Morrow, Conor Sullivan")
print("b. Chris Cerulli, Josh Balz, Ryan Sitkowski, Ricky Olson, Devin Sola, and Vinny Mauro")
print("c. Andy Biersack, Ashley Purdy, \"Jinxx\", Jake Pitts, and Christian Coma")
print("d. Ben Bruce, James Cassells, Danny Worsnop, and Sam Bettley")
q2 = input("Answer:")
if q2.lower () == "b":
   total_score = total_score + 1
   print("correct")
else:
   print("incorrect")
print()

print("3. What Bring Me The Horizon song has the lyrics \"I can't drown my demons they know how to swim?\"")
print("a. Drown \nb. Deathbeds \nc. Throne \nd. Can You Feel My Heart")
q3 = input("Answer:")
if q3.lower () == "d":
   total_score = total_score + 1
   print("correct")
else:
   print("incorrect")
print()

print("4. What year did Fall Out Boy get together?")
print("a. 2001 \nb. 2003 \nc. 2009 \nd. 2013")
q4 = input("Answer:")
if q4.lower () == "a":
   total_score = total_score + 1
   print("correct")
else:
   print("incorrect")
print()

print("5. Who is currently Asking Alexandria's lead singer?")
print("a. Ben Bruce \nb. Danny Wosnop \nc. Denis Stoff \nd. Cameron Liddell")
q5 = input("Answer:")
if q5.lower () == "b":
   total_score = total_score + 1
   print("correct")
else:
   print("incorrect")
print()

percent = total_score / 5 * 100
print("You got", percent, "percent")
if percent <= 50:
   print("Wow, you're dumb")