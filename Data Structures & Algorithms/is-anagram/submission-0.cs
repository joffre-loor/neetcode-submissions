public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length != t.Length) return false;

        int[] store = new int[26];

        for(int i = 0; i < s.Length; i++){
            store[t[i] - 'a']++;
            store[s[i] - 'a']--;
        }
        foreach(int x in store) if (x != 0) return false;
        
        return true;
    }
}
