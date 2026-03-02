// Last updated: 02/03/2026, 13:58:47
public class Solution {
    private Solution[] child;
    private int ct;

    public Solution() {
        child = new Solution[26];
        ct = 0;
    }

    public int[] sumPrefixScores(String[] words) {
        for (String s : words) {
            insert(s);
        }
        int[] res = new int[words.length];
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            res[i] = countPre(word);
        }
        return res;
    }

    private void insert(String word) {
        Solution cur = this;
        for (int i = 0; i < word.length(); i++) {
            int id = word.charAt(i) - 'a';
            if (cur.child[id] == null) {
                cur.child[id] = new Solution();
            }
            cur.child[id].ct++;
            cur = cur.child[id];
        }
    }

    private int countPre(String word) {
        Solution cur = this;
        int localCt = 0;
        for (int i = 0; i < word.length(); i++) {
            int id = word.charAt(i) - 'a';
            if (cur.child[id] == null) {
                return localCt;
            }
            localCt += cur.ct;
            cur = cur.child[id];
        }
        localCt += cur.ct;
        return localCt;
    }
}