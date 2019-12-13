public class Elevator_Maintenance {

    public static String[] solution(String[] inputArray) {
        String[] converted = new String[inputArray.length];
        for (int i = 0; i < inputArray.length; i++) {
            if (inputArray[i].charAt(1) == '.') {
                converted[i] = inputArray[i].substring(0, 1);
            } else {
                if (inputArray[i].charAt(2) == '.') {
                    converted[i] = inputArray[i].substring(0, 2);
                } else {
                    if (inputArray[i].charAt(3) == '.') {
                        converted[i] = inputArray[i].substring(0, 3);
                    }
                }
            }
        }
        return converted;
    }
}
