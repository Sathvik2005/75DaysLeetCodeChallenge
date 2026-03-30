class MyQueue {
     Stack<Integer> s1; // Input stack
     Stack<Integer> s2; // Output stack

    public MyQueue() {
        s1 = new Stack<>();
        s2 = new Stack<>();
    }
    
    public void push(int x) {
        s1.push(x);
    }
    
    public int pop() {
        move();
        return s2.pop();
    }
    
    public int peek() {
        move();
        return s2.peek();
    }
    
    public boolean empty() {
        return s1.isEmpty() && s2.isEmpty();
    }

    private void move() {
        // Only move elements if the output stack is empty
        if (s2.isEmpty()) {
            while (!s1.isEmpty()) {
                s2.push(s1.pop());
            }
        }
    }
}
