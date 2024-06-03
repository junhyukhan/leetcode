https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

The problem gives two arrays where they are merged into array1 in-place.  
array1's length is equal to the length of both arrays combined.  
The empty space of array1 is filled with 0's.

1. One way is to just add the elements of array2 to the end of array1, then sort array1.  
   - This has a time complexity of O(nlogn), although that depends on the language used.
3. The better way is using the two-pointer approach.  
   - Have three indices, all starting at the end of each array (m, n, m+n) - 1.
   - This has a time complexity of O(m + n).  
   - By going backwards, the 0's are filled first, and we do not need to keep a temporary variable when replacing a value of array1 in-place.
