import pprint

#import os
'''
def ensure_pythonhashseed(seed=0):
    current_seed = os.environ.get("PYTHONHASHSEED")

    seed = str(seed)
    if current_seed is None or current_seed != seed:
        print(f'Setting PYTHONHASHSEED="{seed}"')
        os.environ["PYTHONHASHSEED"] = seed
        # restart the current process
        os.execl(sys.executable, sys.executable, *sys.argv)
'''
class Hashtable:
    def __init__(self, elements):
        self.bucket_size = len(elements)
        self.buckets = [None] * self.bucket_size
        self._assign_buckets(elements)

    def custom_hash(self, key): 
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            hash_value = (hash_value * ord(i) % self.bucket_size)

        return hash_value

    def _assign_buckets(self, elements):
        for key, value in elements:
            hashed_key = self.custom_hash(key)
            
            while self.buckets[hashed_key] is not None:
                self.buckets[hashed_key] = list(self.buckets[hashed_key])
                hashed_key = (hashed_key + 1) % self.bucket_size
            self.buckets[hashed_key] = list((key, value))
            
        

    def get_value(self, input_key):
        hashed_key = self.custom_hash(input_key)
        trys = 0 
        while self.buckets[hashed_key] is not None:
            key,value = self.buckets[hashed_key]
            if key == input_key:
                return value
            hashed_key = (hashed_key + 1) % self.bucket_size
            trys+=1
            if trys >= self.bucket_size:
                return 'Not found on the database'

    def __str__(self):

        return pprint.pformat(self.buckets) # here pformat is used to return a printable representation of the object

if __name__ == "__main__":

    capitals = [
        ('France', 'Paris'),
        ('United States', 'Washington D.C.'),
        ('Italy', 'Rome'),
        ('Canada', 'Ottawa'),
        ('Brazil', 'Brasilia'),
    ]
    hashtable = Hashtable(capitals)
    # print(hashtable)

    print(f"The capital of Italy is {hashtable.get_value('Italy')}")
    print(f"The capital of France is {hashtable.get_value('France')}")
    print(f"The capital of United States is {hashtable.get_value('United States')}")
    print(f"The capital of Canada is {hashtable.get_value('Canada')}")
    print(f"The capital of Brazil is {hashtable.get_value('Brazil')}")
    print(f"The capital of Chile is {hashtable.get_value('Chile')}")