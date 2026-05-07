
class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer, Integer> counts = new HashMap<>();
        int left = 0, maxFruits = 0;

        for (int right = 0; right < fruits.length; right++) {
            // Add current fruit to the basket
            counts.put(fruits[right], counts.getOrDefault(fruits[right], 0) + 1);

            // If we have more than 2 types, shrink the window from the left
            while (counts.size() > 2) {
                counts.put(fruits[left], counts.get(fruits[left]) - 1);
                if (counts.get(fruits[left]) == 0) {
                    counts.remove(fruits[left]);
                }
                left++;
            }

            // Calculate the current window size
            maxFruits = Math.max(maxFruits, right - left + 1);
        }

        return maxFruits;
    }
}
