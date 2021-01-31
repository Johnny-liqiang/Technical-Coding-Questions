#Use a hashtable and traverse from max_value to 0

from collections import Counter

def findProfit(numSuppliers: int, inventory: List[int], order: int) -> int:
    
    d = Counter()
    # add the profit to the hashtable, where the key value as inventory - > count of that inventory value. inventory[i] stands for the inventory count 
    for i in range(numSuppliers):
        d[inventory[i]] += 1
    
    # currentmaxInventoryProfit
    # Now instead of subtracting one by one I can find the the value till the maximum value can be used
    cur = max(d)
    profit = 0
    
    while order > 0 and cur > 0:
        freq = d[cur]  # the frequency, iterate until the orders fulfilled

        if order >= freq:
            order -= freq
            profit += cur * freq
        elif order < freq:
            profit += order * cur
            break
            
        cur -= 1
        d[cur] += freq
    
    return profit
    
#timecomplexity O(n) # considering a max() function of the highest key of hashmap, maybe o(nlogn)
#spacecomplexity O(n)
  
  
  
  
    
    
 '''
   public static int maxProfit(int[] invetory, int order) {
            Integer[] b = new Integer[invetory.length];
            for (int i = 0; i < invetory.length; i++) {
                    b = invetory;
            }
            Arrays.sort(b, (o1,o2) -> o2-o1);
            Integer[] a = new Integer[invetory.length+1];
            for (int i = 0; i < invetory.length; i++) {
                    a = b;
            }
            a[invetory.length] = 0;
            int supIdx = 1;
            int maxPro = 0;
            while(order >= 0 && supIdx < a.length) {
                    while(supIdx < a.length && a[supIdx-1] == a[supIdx]) {
                            supIdx++;
                    }//move the pointer to the second largest number in the array and then we will know how many suppliers who have the largest inventory
                    if(a[supIdx-1] == 0) break;
                    int supMulti = supIdx;
                    int diff = a[supIdx-1] - a[supIdx];
                    int localCountToOrder = diff * supMulti;
                    localCountToOrder = Math.min(order, localCountToOrder);
                    order -= localCountToOrder;
                    int localPro = a[supIdx-1];
                    while(localCountToOrder > 0 && localPro >= a[supIdx]) {
                            int curCountToTake = Math.min(supMulti, localCountToOrder);
                            maxPro += localPro * curCountToTake;
                            localPro--;
                            localCountToOrder -= curCountToTake;
                    }
                    supIdx++;
            }
            return maxPro;
    }
 
 '''
