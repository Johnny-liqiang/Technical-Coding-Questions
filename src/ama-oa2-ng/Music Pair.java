import java.util.*;
class Solution {
    public static int numPairsDivisibleBy60(int[] times){
        // WRITE YOUR BRILLIANT CODE HERE
        Map<Integer, Integer> map = new HashMap<>();
        int res = 0;
        for(int n : times) {
            n = n%60;
            if(map.containsKey(60 - n == 60 ? 0 : 60 - n))
                res += map.get(60 - n == 60 ? 0 : 60 - n);
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        return res;
                
    }
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int[] times = Arrays.stream(scanner.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        scanner.close();
        System.out.println(numPairsDivisibleBy60(times));
    }
}
