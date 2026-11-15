public class Solution {
    public int[] TopKFrequent(int[] nums, int k){
        Dictionary<int,int> dic = new Dictionary<int,int>();
        List<int>[] frequent = new List<int>[nums.Length+1];
        for (int i = 0; i < frequent.Length; i++) {
            frequent[i] = new List<int>();
        }
        foreach(int x in nums){
            if(!dic.ContainsKey(x)){
                dic[x] = 1;
            }else{
                dic[x]++;
            }                           
        }
        foreach(var num in dic){
            frequent[num.Value].Add(num.Key);
        }
        int[] ret = new int[k];
        int index = 0;
        for(int i = frequent.Length - 1; i > 0 && index < k; i--){
            foreach(int n in frequent[i]){
                ret[index++] = n;
                if(index == k){
                    return ret;
                }
            }
        }
        return ret;
    }
}
