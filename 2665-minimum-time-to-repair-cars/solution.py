class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def isValidTime(time):
            cars_done = 0
            for rank, workers in ranks.items():
                # rank * cars ** 2 = time, cars ** 2 = time / rank, cars = sqrt(time / rank)
                cars_done += workers * floor(sqrt(time / rank)) # each worker w/ same rank does same num cars
            return cars_done >= cars # true / false if current time can process enough cars

        ranks = Counter(ranks) # turn ranks into counter for faster isValidTime() check
        
        # min time is 0, max time is if all workers take the most time
        left, right = 0, max(ranks) * ceil(cars / len(ranks)) ** 2
        while left < right: # binary search for minimum possible time
            mid = (left + right) // 2

            if isValidTime(mid):
                right = mid # valid time, move right down
            else:
                left = mid + 1 # invalid time, move left up

        return left # left = right = min possible time. left - 1 is first invalid time
