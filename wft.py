import subject
import simulation

# Run simulation

test = subject.subject(105, 183, '21/10/2000')
print(test)

for x in range(1,3653):
    interval = simulation.clock.advance()
    test.Update(interval, 2000)
print(test)


# If we pass each objects update() method a time delta, then in order to know the current date 
# it will have to track it internally

# If we query the time/date externally, then we must calculate the time delta for each update