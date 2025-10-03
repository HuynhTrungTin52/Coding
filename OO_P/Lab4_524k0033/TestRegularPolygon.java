package Lab4_524k0033;
public class TestRegularPolygon {
    public static void main(String[] args) {
        RegularPolygon rp1 = new RegularPolygon();
        RegularPolygon rp2 = new RegularPolygon("q1", 4, 1.5);
        RegularPolygon rp3 = new RegularPolygon("pentagon", 5);
        RegularPolygon rp4 = new RegularPolygon(rp2);

        System.out.println("rp1: " + rp1);
        System.out.println("rp2: " + rp2);
        System.out.println("rp3: " + rp3);
        System.out.println("rp4: " + rp4);

        System.out.println("rp1 name: " + rp1.getName());
        System.out.println("rp2 edge amount: " + rp2.getEdgeAmount());
        System.out.println("rp3 edge length: " + rp3.getEdgeLength());

        rp1.setName("default");
        rp2.setEdgeAmount(6);
        rp3.setEdgeLength(2.0);

        System.out.println("rp1 updated: " + rp1);
        System.out.println("rp2 updated: " + rp2);
        System.out.println("rp3 updated: " + rp3);

        System.out.println("rp2 perimeter: " + rp2.getPerimeter());
        System.out.println("rp3 area: " + rp3.getArea());

        RegularPolygon rp5 = new RegularPolygon("bigPolygon", 7, 1);
        System.out.println("rp5: " + rp5);
        System.out.println("rp5 area: " + rp5.getArea());
    }
}
