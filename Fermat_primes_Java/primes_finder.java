import java.math.*;

class primes_finder
{
  public static void main(String args[])
  {
    boolean flag=false;
    BigInteger testable_number, remainder, i, i_max;
    BigInteger ZERO = new BigInteger("0");
    BigInteger ONE = new BigInteger("1");
    BigInteger TWO=new BigInteger("2");
    BigInteger ABSOLUTE_MIN=new BigInteger("3");
    BigInteger MIN=new BigInteger("3");
    testable_number=MIN;
    int test;

    while (true)
    {
      i=ABSOLUTE_MIN;
      i_max = testable_number.divide(TWO);
      i_max =i_max.add(ONE);
      test=i.compareTo(i_max);
      while (test==-1)
      {
        remainder=testable_number.remainder(i);
        test=remainder.compareTo(ZERO);
        if (test==0)
        {
          flag=true;
          i=i_max;
        }
        i=i.add(ONE);
        test=i.compareTo(i_max);
      }
      if (!flag)
      {
        System.out.println(testable_number +",");
      }
      testable_number=testable_number.add(TWO);
    }
  }
}
