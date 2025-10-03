package Lab4_524k0033;
public class RegularPolygon {
    private String name;
    private int edgeAmount;
    private double edgeLength;

    public RegularPolygon() {
        this.name = "";
        this.edgeAmount = 3;
        this.edgeLength = 1;
    }

    public RegularPolygon(String name, int edgeAmount, double edgeLength) {
        this.name = name;
        this.edgeAmount = edgeAmount;
        this.edgeLength = edgeLength;
    }

    public RegularPolygon(String name, int edgeAmount) {
        this.name = name;
        this.edgeAmount = edgeAmount;
        this.edgeLength = 1;
    }

    public RegularPolygon(RegularPolygon polygon) {
        this.name = polygon.name;
        this.edgeAmount = polygon.edgeAmount;
        this.edgeLength = polygon.edgeLength;
    }

    public String getName() {
        return name;
    }

    public int getEdgeAmount() {
        return edgeAmount;
    }

    public double getEdgeLength() {
        return edgeLength;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setEdgeAmount(int num) {
        this.edgeAmount = num;
    }

    public void setEdgeLength(double length) {
        this.edgeLength = length;
    }

    public String getPolygon() {
        if (edgeAmount == 3) {
            return "Triangle";
        } else if (edgeAmount == 4) {
            return "Quadrangle";
        } else if (edgeAmount == 5) {
            return "Pentagon";
        } else if (edgeAmount == 6) {
            return "Hexagon";
        } else {
            return "Polygon has the number of edges greater than 6";
        }
    }

    public double getPerimeter() {
        return edgeLength * edgeAmount;
    }

    public double getArea() {
        double area;
        if (edgeAmount == 3) {
            area = edgeLength * edgeLength * 0.433;
        } else if (edgeAmount == 4) {
            area = edgeLength * edgeLength * 1;
        } else if (edgeAmount == 5) {
            area = edgeLength * edgeLength * 1.72;
        } else if (edgeAmount == 6) {
            area = edgeLength * edgeLength * 2.595;
        } else {
            area = -1;
        }
        return area;
    }

    @Override
    public String toString() {
        return name + " - " + getPolygon() + " - " + getArea();
    }
}
