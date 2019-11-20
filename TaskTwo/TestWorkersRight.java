package TaskTwo;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.stream.IntStream;

public class TestWorkersRight {
    private static Integer var = 0;

    public static void main(String[] args) {


        Lock lock = new ReentrantLock();
        final CountDownLatch counter = new CountDownLatch(2);

        final Runnable runnable = () -> {
            lock.lock();
            IntStream.range(0, 10).forEach(value -> var++);
            counter.countDown();
            lock.unlock();
        };

        Thread thread1 = new Thread(runnable);
        Thread thread2 = new Thread(runnable);

        thread1.start();
        thread2.start();

        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        try {
            counter.await();
            System.out.println(var);
        } catch (InterruptedException ignored) {
        }
    }
}