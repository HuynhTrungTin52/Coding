package Lab3_524k0033;

public class rectangle {
	private float width=1;
	private float length=1;

	public rectangle(){
		width=1;
		length=1;
	}

	public rectangle(float width, float length){
		this.width=width;
		this.length=length;
	}

	public float getWidth(){
		return width;
	}
	public float getlength(){
		return length;
	}
	public float getArea(){
		return width*length;
	}

	public float getPerimeter(){
		return 2*(width+length);
	}
	public float setWidth(float width){
		return this.width=width;
	}

	public float setLength(float length){
		return this.length=length;
	}

	@Override
	public String toString(){
		return "Rectangle[width: "+width+", length: "+length+"]";
	}
}
