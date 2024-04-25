from logic import *

rain = Symbol("rain")  # It's raining
hagrid = Symbol("hagrid") # Harry is visiting Hagrid
dumbledore = Symbol("dumbledore") # Harry is visiting dumbledor

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(model_check(knowledge, rain))
