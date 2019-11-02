import java.util.Arrays;

class KMP_String_Match {
  void KMPSearch(String sub, String text){
    int N = text.length();
    int M = sub.length();

    int lps[] = new int[M];
    int j = 0;

    CreateLPSArray(sub, M, lps);
    
    int i = 0;
    while (i < N){
      if (sub.charAt(j) == text.charAt(i)){
        i++;
        j++;
      }
      if (j == M){
        System.out.println("Found Pattern at index " + (i-j));
        j = lps[j-1];
      }
      else if (i < N && sub.charAt(j) != text.charAt(i)){
        if (j != 0){
          j = lps[j-1];
        }
        else{
          i++;
        }
      }
    }
  }

  void CreateLPSArray(String sub, int M, int lps[]){
    int len = 0;
    int i = 1;
    lps[0] = 0;

    while(i < M){
      if (sub.charAt(i) == sub.charAt(len)){
        len++;
        lps[i] = len;
        i++;
      }
      else{
        if(len != 0){
          len = lps[len-1];
        }
        else{
          lps[i] = len;
          i++;
        }
      }
    }
  }

  public static void main(String args[]) {
    String sub = "AAC";
    String text = "AAAAAAC";
    new KMP_String_Match().KMPSearch(sub, text);
  }

}