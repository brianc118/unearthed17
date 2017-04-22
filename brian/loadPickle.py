import pickle

trips = pickle.load( open( "trip.pickle", "rb" ) )

print(len(trips[2617].values()))