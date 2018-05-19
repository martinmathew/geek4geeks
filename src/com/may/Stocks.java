package com.may;

import java.util.ArrayList;



public class Stocks {

	
	public static void main(String[] args) {
		int[] sts = {100,10, 180, 260, 310, 40, 535, 695};
		int[] bs = stocks(sts);
		System.out.println(bs);
	}
	
	
	public static int[] stocks(int[] arr) {
	    int[] bs = new int[arr.length];
	    int count = 0;
		int start = 0;
		bs[count]=start;
		for(int i=0;i<arr.length;i++) {
			if(i == arr.length-1||arr[i] > arr[i+1]) {
				
				if(i != start) {
					
					bs[++count]=i;
				}
				
				if(i < arr.length-1) {
					start=i+1;
				bs[++count]=start;
				}
				
			}
			
			
		}
		return bs;
	}
	
	
	
}
