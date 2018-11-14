package week01.dataandvar;

/**
 * 演示流程控制
 */
public class ProcessControl {

    public static void main(String[] args) {
        for (int i = 1; i <= 9; i++) {
            for (int j = 1; j <= 9; j++) {
                if (j <= i) {
                    System.out.printf("%d*%d =%2d ", i, j, i * j);
                }
            }
            System.out.println();
        }
        System.out.println();

        for (int i = 1; i <= 9; i++) {
            for (int j = 1; j <= 9; j++) {
                if (j < i) {
                    System.out.print("        ");
                } else {
                    System.out.printf("%d*%d =%2d ", i, j, i * j);
                }
            }
            System.out.println();
        }
    }
}
