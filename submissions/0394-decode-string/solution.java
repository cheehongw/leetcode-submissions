class Solution {
    public String decodeString(String s) {
        if (!s.contains("[")) return s;
        
        System.out.println(s);
        int firstK = getFirstK(s);
        int encodedEndPointer = getEncodedEndPointer(s);
        String beforeKString = beforeK(s);
        String encodedString = getEncodedString(s, encodedEndPointer);
        String undecodedString = getUnencodedString(s, encodedEndPointer);
        
        StringBuffer sb = new StringBuffer();
        sb.append(beforeKString);
        
        while (firstK != 0) {
            sb.append(encodedString);
            firstK--;
        }
        
        sb.append(undecodedString);
        
        return decodeString(sb.toString());
        
    }
    
    public int getFirstK(String s) {
        int i = 0, j = 0;
        while (!Character.isDigit(s.charAt(i))) i++;
        j = i;
        while (Character.isDigit(s.charAt(j))) j++;
        
        int k = Integer.valueOf(s.substring(i, j));
        return k;
    }
    
    public String beforeK(String s) {
        int i = 0;
        while (!Character.isDigit(s.charAt(i))) i++;
        return s.substring(0, i);
    }
    
    public int getEncodedEndPointer(String s) {
        //System.out.println(s);
        String[] splits = s.split("\\[", 2);
        //System.out.println(Arrays.toString(splits));
        String embeddedString = splits[1];
        int counter = 1;
        int pointer = 0;
        
        while (counter != 0) {
            char c = embeddedString.charAt(pointer);
            if (c == '[') {
                counter += 1;
            } else if (c == ']') {
                counter -= 1;
            }
            pointer++;
        }
        
        return pointer;
    }
    
    public String getEncodedString(String s, int encodeEndPointer) {
        String[] splits = s.split("\\[", 2);
        String embeddedString = splits[1];
        return embeddedString.substring(0, encodeEndPointer - 1);
        
    }
    
    public String getUnencodedString(String s, int encodeEndPointer) {
        String[] splits = s.split("\\[", 2);
        String embeddedString = splits[1];
        return embeddedString.substring(encodeEndPointer, embeddedString.length());
        
    }
}
