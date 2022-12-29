class Solution {
    public int[] getOrder(int[][] tasks) {
        
        for(int i = 0; i < tasks.length; i++){
            int[] a = new int[3];
            a[0] = tasks[i][0];
            a[1] = tasks[i][1];
            a[2] = i;
            tasks[i] = a;
        }

        Arrays.sort(tasks, new customComparator(0));
        PriorityQueue<int[]> pq = new PriorityQueue<>(new customComparator(1));

        int[] ans = new int[tasks.length];

        int currentTime = tasks[0][0];
        int ans_i = 0, tasks_i = 0;

        while(ans_i < ans.length){
            while(tasks_i < tasks.length && tasks[tasks_i][0] <= currentTime){
                pq.offer(tasks[tasks_i++]);
            }

            if(pq.isEmpty()){
                currentTime = tasks[tasks_i][0];
                pq.offer(tasks[tasks_i++]);
            }
            int[] curr = pq.poll();
            ans[ans_i++] = curr[2];
            currentTime += curr[1];
        }
        return ans;
    }

    class customComparator implements Comparator<int[]>{

        int startIdx;

        public customComparator(int idx){
            startIdx = idx;
        }

        public int compare(int[] A, int[] B){
            for(int i = startIdx; i < 3; i++){
                if(A[i] != B[i]){
                    return A[i] - B[i];
                }
            }
            return 0;
        }
    }

}