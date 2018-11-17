package week01.extendAndInterface;

public final class ProductManager extends Manager {
    public int getSalary(int pyTrade) {
        return super.getSalary() + pyTrade;
    }
}
