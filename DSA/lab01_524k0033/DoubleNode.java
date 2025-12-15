package lab01_524k0033;

public class DoubleNode {

    private Double data;
    private DoubleNode next;

    public DoubleNode() {
        data = null;
        next = null;
    }

    public DoubleNode(Double data) {
        this(data, null);
    }

    public DoubleNode(Double data, DoubleNode next) {
        this.data = data;
        this.next = next;
    }

    public DoubleNode getNext() {
        return next;
    }

    public Double getData() {
        return data;
    }

    public Double setData(Double f) {
        Double delData = this.data;
        this.data = f;
        return delData;
    }

    public void setNext(DoubleNode n) {
        next = n;
    }

}
