package com.may;

public class Trees<T extends Comparable<T>> {
	
	private Node<T> root;
	
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
	

	public static void main(String[] args) {
		Trees<Integer> tree = new Trees<>();
		Integer[] nums = {10,5,2,1,3,15,12,13,17};
		 tree.insert(nums);
		 tree.root = tree.removeHalfNode(tree.root);
		 System.out.println(tree.root);
	}
	
	
	
	public Node<T> removeHalfNode(Node<T> root) {
		if(root!=null){
			root.left = removeHalfNode(root.left);
			root.right = removeHalfNode(root.right);
			if(root.left == null ^ root.right == null) {
				if(root.left!=null) {
					return root.left;
				}
				else {
					return root.right;
				}
			}else {
				return root;
			}
		}else {
			return null;
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
	
	
	
	public void insert(T[] num) {
		for(T i:num) {
	     if(root== null) {
	    	 root = new Node<T>(i);
	     }else {
	    	 Node<T> temp = root;
	    	 Node<T> parent = null;
	    	 while(temp!=null) {
	    		 parent = temp;
	    		 if(temp.value.compareTo(i)<0) {
	    			 temp = temp.right;
	    		 }else {
	    			 temp = temp.left;
	    		 }
	    	 }
	    	 Node<T> newNode = new Node<T>(i);
	    	 if(parent.value.compareTo(i)<0) {
	    		 parent.right = newNode;
	    	 }else {
	    		 parent.left = newNode;
	    	 }
	     }
		}
	}
	
	
}
