package com.may;

public class Trees<T> {
	
	
	 class  Node<T>{
		
		private T value;
		private Node<T> left;
		private Node<T> right;
		
		public Node(T t) {
			this.value = t;
		}

		public T getValue() {
			return value;
		}

		public void setValue(T value) {
			this.value = value;
		}

		public Node<T> getLeft() {
			return left;
		}

		public void setLeft(Node<T> left) {
			this.left = left;
		}

		public Node<T> getRight() {
			return right;
		}

		public void setRight(Node<T> right) {
			this.right = right;
		}
		
		
	}
	

	
	
	public  Node<T>  mirror(Node<T> root) {
		if(root!=null) {
		 root.setLeft(mirror(root.right));
		 root.setRight(mirror(root.left));
		 return root;
		}
		else {
			return null;
		}
	}
	
	
	
	public 
	
	
}
