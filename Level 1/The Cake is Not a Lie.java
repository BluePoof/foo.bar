public class The_Cake_is_Not_a_Lie {

    public static int solution(String chain) {
        int strLen = chain.length();
        int subsLen = 0;
        int j;
        int currLen = strLen;
        String subChain;
        boolean validate;
        for (int i = 1; i <= currLen; i++) {
            subChain = chain.substring(0, i);
            validate = true;
            j = 0;
            while (validate == true && j <= currLen - subChain.length()) {
                if (subChain.equals(chain.substring(j, j + subChain.length()))) {
                    validate = true;
                } else {
                    validate = false;
                }
                j = j + subChain.length();
                if (j == currLen && validate == true) {
                    subsLen = subChain.length();
                    validate = false;
                    i = currLen;
                }
            }
        }
        return strLen / subsLen;
    }
}