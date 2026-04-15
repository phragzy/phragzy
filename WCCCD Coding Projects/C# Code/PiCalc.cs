namespace FinalProject
{
    class PiCalculator
    {
        static void Main()
        {
            PiCalc();
        }
        static void PiCalc()
        {
            Console.WriteLine("Please enter a Positive Number:");
            int userInput = Convert.ToInt32(Console.ReadLine());
            double x = 0;
            int y = 1;
                if (userInput > 0)
                {
                    int count;
                    for (count = 1; count < userInput; count += 2)
                    {
                        x = x + y * (1.0 /count);
                        y = y * (-1);
                    }
                }
                else
                {
                    Console.WriteLine("Error, please enter a positive number.");
                }
                double Pi = x * 4;
            Console.WriteLine(Pi);
        }
    }
}