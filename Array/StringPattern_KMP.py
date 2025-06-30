def patternSearch(text,pat):
    n=len(text)
    m = len(pat)
    i=0    
    for i in range(n-m+1):
       j=0 
       while j<m and text[i+j] == pat[j]:
           j +=1

       if(j==m):
           print (f'pattern found at index {i}')


if __name__ == '__main__':
    # Example 1
    text1 = "AABAACAADAABAABA"
    pattern1 = "AABA"
    print("Example 1:")
    patternSearch(text1, pattern1)
    
    # Example 2
    text2 = "agd"
    pattern2 = "g"
    print("\nExample 2:")
    patternSearch(text2, pattern2)