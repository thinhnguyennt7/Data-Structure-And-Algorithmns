public class Solve {
	
	//Driver 
	public static void main(String[] args) {
		Solve m = new Solve();
		int arr[][] = {{1,0,1},{0,1,0},{1,0,1}}; // Sample
		System.out.println(m.solveMatrix(arr));
	}

	public boolean solveMatrix(int[][] arr) {
		if (arr.length == 0 || arr[0].length == 0) {
			return false;
		}

		// Check Col
		boolean colFlag = true;
		for (int i = 0; i < arr.length; i++) {
			colFlag = true;
			for (int j = 0; j < arr[0].length; j++) {
				if (arr[j][i] == 0) {
					colFlag = false;
					break;
				}
			}
			if (colFlag) {
				break;
			}
		}

		// Check row
		boolean rowFlag = true;
		for (int row = 0; row < arr.length; row++) {
			rowFlag = true;
			for (int col = 0; col < arr[0].length && rowFlag; col++) {
				if (arr[row][col] == 0) {
					rowFlag = false;
					break;
				}
			}
			if (rowFlag) {
				break;
			}
		}

		//Check diagonal
		int row = 0;
		boolean diagonalFlag = true;
		for (row = 0; row < arr.length; row++) {
			diagonalFlag = true;
			if (arr[row][row] == 0){
				diagonalFlag = false;
				break;
			}
		}

		if (colFlag || rowFlag || diagonalFlag) {
			return true;
		} else {
			return false;
		}
	}
}