package TaskTwo;

import java.util.concurrent.CountDownLatch;
import java.util.stream.IntStream;

public class TestWorkers {
    private static Integer var = 0;

    public static void main(String[] args) {

        final CountDownLatch counter = new CountDownLatch(2);
        final Runnable runnable = () -> {
//            for (int i = 0; i < 1000; i++) {
//                var++;
//                System.out.println(var);
//            }
            IntStream.range(0,10).forEach(value -> var++);
//            IntStream.range(0,1000).forEach(value -> var++);
            counter.countDown();
        };

        Thread thread1 = new Thread(runnable);
        Thread thread2 = new Thread(runnable);

        thread1.start();
        thread2.start();

        try {
            counter.await();
            System.out.println(var);
        } catch (InterruptedException ignored) {
        }
    }
}