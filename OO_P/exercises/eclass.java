package exercises;

import java.awt.Point;
import java.text.DecimalFormat;
import java.util.Random;
public class eclass {
	public static void setPoints(Point points[])
	{
		Random seed = new Random();
		for (int i = 0; i < 10; i++) {
            points[i] = new Point(seed.nextInt(10) + 1, seed.nextInt(10) + 1);
        }
	}
	public static double findMin(Point points[])
	{
		double minDistance = Double.MAX_VALUE;
        for (int i = 0; i < 10; i++) {
            for (var j = i + 1; j < 10; j++) { 
                double distance = points[i].distance(points[j]); 

                if (distance < minDistance) {
                    minDistance = distance;
                    
                }
            }
        }
		return minDistance;
	}

	public static void printPoints(double minDistance,Point p1, Point p2)
	{
		
		DecimalFormat df = new DecimalFormat("0.##");
        System.out.println("Minimum distance: " + df.format(minDistance));
        System.out.println("Between points: (" + df.format(p1.x) + ", " + df.format(p1.y) + ") and (" + df.format(p2.x) + ", " + df.format(p2.y) + ")");

	}
	public static void main(String[] args) {

		
		Point[] points = new Point[10]; 
		setPoints(points);
        
		double minDistance=findMin(points);
		Point p1=null;
		Point p2=null;
		for (int i = 0; i < points.length; i++) {
            for (int j = i + 1; j < points.length; j++) {
                if (points[i].distance(points[j]) == minDistance) {
                    p1 = points[i];
                    p2 = points[j];
                    break; 
                }
            }
            if(p1 != null) break; 
		}
		printPoints(minDistance,p1,p2);
	}
}
