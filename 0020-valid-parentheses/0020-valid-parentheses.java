class Solution {
    public boolean isValid(String s) {
         Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            // If it's an opening bracket, push the expected closing bracket
            if (c == '(') {
                stack.push(')');
            } else if (c == '{') {
                stack.push('}');
            } else if (c == '[') {
                stack.push(']');
            } 
            // If it's a closing bracket, check if it matches the stack top
            else {
                if (stack.isEmpty() || stack.pop() != c) {
                    return false;
                }
            }
        }

        // If the stack is empty, all brackets were matched
        return stack.isEmpty();
    }
}