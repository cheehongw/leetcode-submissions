class Solution {
    
    List<Character> openBrackets = Arrays.asList(new Character[]{'(', '{', '['});
    List<Character> closeBrackets = Arrays.asList(new Character[]{')', '}', ']'});
    
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if (openBrackets.contains(c)) {
                stack.push(c);
            } else { //close brackets
                
                if (stack.isEmpty()) return false;
                
                int index = closeBrackets.indexOf(c);
                Character expectedChar = openBrackets.get(index);
                Character actualChar = stack.pop();
                
                if (!actualChar.equals(expectedChar)) return false;
            }
            
        }
        
        return stack.size() == 0;
    }
}
