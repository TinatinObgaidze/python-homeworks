using System;
using System.Collections.Generic;
// Tika Loves Nika
namespace nikasdavalebulidavaleba

{
    class Program
    {

        public static void Main(string[] args)
        {
            Random rand = new Random();

            Console.WriteLine("Generating 10 random numbers:");
            List<int> rndList = new List<int>();
            for (int num = 1; num <= 10; num++)
            {
                int randnum = rand.Next(0, 100);
                rndList.Add(randnum);
                Console.WriteLine("number " +num + " of list =  "+ randnum);
            }
            List<int> listOfEvenNums = new List<int>();
            List<int> listOfOddNums = new List<int>();
            foreach (int ele in rndList)
            {
                if (ele % 2 == 0)
                {
                    listOfEvenNums.Add(ele);
               
                }
                else
                {
                    listOfOddNums.Add(ele);
                }
            }   
            foreach (int i in listOfEvenNums)
            {
                Console.WriteLine("Even numbers of list of even numbers are:    "+ i);

            }

            foreach (int i in listOfOddNums)
            {
                Console.WriteLine("Odd numbers of list of odd numbers are:      " + i);

            }

        }


    }
}
