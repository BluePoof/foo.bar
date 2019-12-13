public class Ion_Flux_Relabeling {
    public static int parent(int h, int n) {
        int treesize = (int) Math.pow(2, h) - 1;
        if (n == treesize) {
            return -1;
        }
        int before = 0;
        do {
            if (treesize == 0) {
                break;
            }
            treesize >>>= 1;
            int left = before + treesize;
            int right = left + treesize;
            int parent = right + 1;
            if (left == n || right == n) {
                return parent;
            }
            if (n > left) {
                before = left;
            }
        } while (true);
        return 0;
    }

    public static int[] solution(int h, int[] q) {
        int answer[] = new int[q.length];
        for (int i = 0; i < q.length; i++) {
            answer[i] = parent(h, q[i]);
        }
        return answer;
    }
}
