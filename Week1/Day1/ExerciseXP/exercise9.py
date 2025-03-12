#Exercise 9 : Tall enough to ride a roller coaster

"""Instructions
Write code that will ask the user for their height in centimeters.
If they are over 145cm print a message that states they are tall enough to ride.
If they are not tall enough print a message that says they need to grow some more to ride."""


Height = int(input("Enter your height : "))
if Height > 145:
    print("You are tall enough to ride a roller coster.")
else:
    print("You still have to grow a little to be able to go up")

    