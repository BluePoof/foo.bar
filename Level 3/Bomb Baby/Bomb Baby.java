import java.math.BigInteger;

public class Bomb_Baby {
    public static final int one = 1;

    public static String solution(String x, String y) {
        BigInteger w = new BigInteger(x);
        BigInteger z = new BigInteger(y);
        BigInteger counter = BigInteger.ZERO;
        if (w.equals(BigInteger.ONE) && z.equals(BigInteger.ONE)) {
            return String.valueOf(0);
        } else {
            while (true) {
                if (checker(w, z)) {
                    if (w.compareTo(z) == one) {
                        if (w.compareTo((z.multiply(BigInteger.valueOf(100)))) == one) {
                            counter = counter.add(w.divide(z));
                            w = w.subtract((w.divide(z).multiply(z)));
                        } else {
                            w = w.subtract(z);
                            counter = counter.add(BigInteger.ONE);
                        }
                    }
                    if (z.compareTo(w) == one) {
                        if (z.compareTo((w.multiply(BigInteger.valueOf(100)))) == one) {
                            counter = counter.add(z.divide(w));
                            z = z.subtract((z.divide(w).multiply(w)));
                        } else {
                            z = z.subtract(w);
                            counter = counter.add(BigInteger.ONE);
                        }
                    }
                    if (w.equals(BigInteger.ONE) && z.equals(BigInteger.ONE)) {
                        return String.valueOf(counter);
                    }
                } else {
                    return "impossible";
                }
            }
        }
    }

    public static boolean checker(BigInteger x, BigInteger y) {
        return (!x.equals(BigInteger.ZERO) && !y.equals(BigInteger.ZERO)) && (BigInteger.ONE.compareTo(x) != one && BigInteger.ONE.compareTo(y) != one) && (!x.equals(y) || x.equals(BigInteger.ONE) && y.equals(BigInteger.ONE));
    }
}
